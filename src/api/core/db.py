import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from models.base import Base

TEST_URL = "sqlite:///./test.db"

test_engine = sa.create_engine(TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
# Set up the database once
Base.metadata.drop_all(bind=test_engine)
Base.metadata.create_all(bind=test_engine)
