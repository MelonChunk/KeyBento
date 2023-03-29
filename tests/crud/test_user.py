# pylint: skip-file
import pytest

from models import User

from api.core.db import mock_db_session


@pytest.fixture(scope="function")
def empty_db():
    db = mock_db_session()
    return next(db)


def test_user_can_be_generated(empty_db):
    assert len(empty_db.query(User).all()) == 0
    new_user = User(first_name="Melon", last_name="Chunk")
    empty_db.add(new_user)
    empty_db.commit()
    assert len(empty_db.query(User).all()) == 1
