# pylint: skip-file
# flake8: noqa

import pytest

from api.endpoints.registration import validdate_proposed_user
from api.core.db import mock_db_session

from models.user import User
from schemas.user import CreateUserSchema


@pytest.fixture(scope="function")
def db():
    db = mock_db_session()
    db = next(db)
    user = User(username="hans")
    db.add(user)
    return db


good_user = CreateUserSchema(
    username="hans2",
    password="ThePassword123",
    first_name="Hans",
    last_name="Olo",
    email="hansolo@gmail.com",
)


def test_good_user_is_validated(db):
    validation_result, report = validdate_proposed_user(good_user, db=db)
    assert validation_result
    for key, value in report.items():
        assert not value


def test_no_two_users_of_same_name(db):
    user = good_user
    user.username = "hans"  # Name already in db
    validation_result, report = validdate_proposed_user(user, db)
    assert not validation_result
    assert report["username"] == "Username already exists"


def test_invalid_email(db):
    user = good_user
    user.email = "email"
    validation_result, report = validdate_proposed_user(user, db)
    assert not validation_result
    assert report["email"] == "This is not a valid email"


def test_password_needs_upper_and_lower_letters(db):
    user = good_user
    user.password = "passwordpassword123"
    validation_result, report = validdate_proposed_user(user, db)
    assert not validation_result
    assert report["password"] == "Password needs upper- and lowercase letters"

    user = good_user
    user.password = "PASSWORDPASSWORD123"
    validation_result, report = validdate_proposed_user(user, db)
    assert not validation_result
    assert report["password"] == "Password needs upper- and lowercase letters"


def test_short_password_gets_flagged(db):
    user = good_user
    user.password = "pass123"
    validation_result, report = validdate_proposed_user(user, db)
    assert not validation_result
    assert report["password"] == "Password needs at least 12 characters"


def test_password_needs_numbers(db):
    user = good_user
    user.password = "passwordpassword"
    validation_result, report = validdate_proposed_user(user, db)
    assert not validation_result
    assert report["password"] == "Password needs some numbers at least"
