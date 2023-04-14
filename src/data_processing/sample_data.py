from datetime import datetime
import re
from numpy.random import choice
import pandas as pd
from common import paths
from models import User, Property, Availability, CityInterest


first_word = r"^([\w\-]+)"
last_word = r"([\w\-]+)$"

survey_yes_no_columns = ["Have you exchanged your home before?"]
survey_columns = [
    "Free travel",
    "More authentic travel",
    "Ecologically sustainable",
    "Working from abroad for longer periods",
    "I enjoy hosting others",
    "Experience a new way to travel",
    "Be part of share economies",
    "Other",
]

month_columns = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

city_columns = ["Paris", "London", "Berlin", "New York", "Tokyo", "San Francisco"]

other_target_columns = ["Sea", "Mountains", "Countryside", "Lake", "City"]


def load_user_data():
    user_data = pd.read_csv(paths.sample_data_path, dtype={"Your number?": "string"})
    return clean_userdata(user_data)


def clean_userdata(user_data):
    return user_data.rename(
        columns={
            "Hi future traveller! What's your name and last name? ": "username",
            "Your number?": "phone_number",
            "And what's your email address": "email",
            "Start Date (UTC)": "join_date",
            "Where do you live? ": "location",
        }
    ).assign(user_id=lambda x: x.username.rank().astype("int"))


def get_user_info(user_data):
    return (
        user_data[["user_id", "username", "email", "phone_number", "join_date"]]
        .assign(name_tuples=lambda x: x.username.str.split(" "))
        .assign(first_name=lambda x: x.name_tuples.apply(lambda y: y[0]))
        .assign(
            last_name=lambda x: x.name_tuples.apply(
                lambda y: y[1] if len(y) == 2 else ""
            )
        )
        .assign(join_date=lambda x: pd.to_datetime(x.join_date))
        .drop(columns=["name_tuples"])
    )


def extract_property_info(user_data):
    return user_data[["user_id", "location"]].assign(
        city=lambda x: x.location.apply(lambda x: re.search(first_word, x).group(1)),
        country=lambda x: x.location.apply(lambda x: re.search(last_word, x).group(1)),
    )[["user_id", "city", "country"]]


def extract_availabilities(user_data):
    return (
        user_data[["user_id"] + month_columns]
        .melt(id_vars="user_id", var_name="month", value_name="available")
        .assign(available=lambda x: ~x.available.isnull())
    )


def extract_city_interests(user_data):
    return (
        user_data[["user_id"] + city_columns]
        .melt(id_vars="user_id", var_name="city", value_name="interested")
        .assign(interested=lambda x: ~x.interested.isnull())
    )


def load_users(db):
    user_data = load_user_data()
    user_info = get_user_info(user_data)
    property_info = extract_property_info(user_data)
    availabilities = extract_availabilities(user_data)
    city_interests = extract_city_interests(user_data)

    for i, row in user_info.iterrows():
        user = User(
            username=row.username,
            first_name=row.first_name,
            last_name=row.last_name,
            email=row.email,
            last_seen=datetime.now(),
        )
        property = Property(
            type="Flat",
            description="",
            city=property_info.loc[i, "city"],
            country=property_info.loc[i, "country"],
            address="",
        )
        user_availabilities = availabilities.query(f"user_id == {row.user_id}")
        user_city_interests = city_interests.query(f"user_id == {row.user_id}")
        user.availabilities = [
            Availability(month=k.month, available=k.available)
            for _, k in user_availabilities.iterrows()
        ]
        user.city_interests = [
            CityInterest(city=k.city, interested=k.interested)
            for _, k in user_city_interests.iterrows()
        ]
        property.owner = user
        db.add(user)
        db.add(property)
        db.commit()


def suggest_hosts(user, db, num_suggestions=3):

    user_available_months = [av.month for av in user.availabilities if av.available]
    potential_hosts = (
        db.query(User)
        .join(Availability)
        .filter(Availability.month.in_(user_available_months))
        .filter(Availability.available)
        .filter(User.id != user.id)
        .all()
    )
    if len(potential_hosts) < num_suggestions:
        potential_hosts = (
            db.query(User).filter(User.id != user.id).limit(num_suggestions).all()
        )

    interested_cities = {ci.city for ci in user.city_interests if ci.interested}
    hosts_in_city = [
        host
        for host in potential_hosts
        if len(interested_cities.intersection({prop.city for prop in host.properties}))
        > 0
    ]
    suggestions = hosts_in_city[:num_suggestions]

    if len(suggestions) < num_suggestions:
        num_missing_hosts = num_suggestions - len(suggestions)
        suggestions += list(choice(potential_hosts, num_missing_hosts, replace=False))

    return suggestions


def generate_full_suggestions(db):
    users = db.query(User).all()
    summaries = []
    for user in users:
        suggestions = suggest_hosts(user, db, 3)
        summaries.append(
            {
                "user_name": user.username,
                "suggestion1": suggestions[0].username,
                "suggestion2": suggestions[1].username,
                "suggestion3": suggestions[2].username,
            }
        )
    return pd.DataFrame(summaries)


def generate_suggestion_file(db):
    suggestions = generate_full_suggestions(db)
    suggestions.to_csv(paths.data_path / "suggestions.csv", index=False)


if __name__ == "__main__":
    from api.core.db import mock_db_session

    db = next(mock_db_session())
    load_users(db)
    generate_suggestion_file(db)
