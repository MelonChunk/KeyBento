import tempfile
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base import Base


TEST_URL = "sqlite:///./test.db"

test_engine = sa.create_engine(TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
# Set up the database once
Base.metadata.drop_all(bind=test_engine)
Base.metadata.create_all(bind=test_engine)


def mock_db_session():
    """Used purely for unit testing"""
    path = tempfile.mkdtemp("mock")
    db_url = f"sqlite:///{path}/db.sqlite"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    yield scoped_session(sessionmaker(bind=engine))
    engine.dispose()
