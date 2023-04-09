# pylint: skip-file
# flake8: noqa

from schemas.destinations import CreateProperty
from models.properties import Property
from models.user import User
import pytest

from api.core.db import mock_db_session


@pytest.fixture(scope="function")
def db():
    db = mock_db_session()
    user = User(username="melonchunk")
    db = next(db)
    db.add(user)
    db.commit()
    return db


def test_property_creation(db):
    assert len(db.query(Property).all()) == 0
    new_property = CreateProperty(
        city="Munich",
        country="Germany",
        type="Flat",
        description="A nice little flat in the city center",
        address="Sendlinger Tor\n 81231 Munich\n Germany",
    )
    property = Property.create(new_property)
    user = db.query(User).first()
    property.owner = user

    db.add(property)
    db.commit()

    assert len(db.query(Property).all()) == 1

    property_retrieved = db.query(Property).first()
    assert property.owner == user
    assert property.city == "Munich"
    assert property.country == "Germany"
    assert property.type == "Flat"
    assert property.address == "Sendlinger Tor\n 81231 Munich\n Germany"
    assert property.description == "A nice little flat in the city center"
