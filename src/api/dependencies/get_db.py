import os
from api.core.db import TestingSessionLocal


def get_db():
    """
    Creates db session before each request and closes it afterwards.
    Feed into endpoints as argument db: Session = Depends(get_db)
    """
    if os.environ.get("ENV", "DEBUG") == "DEBUG":
        # Hack to get db controllable via ENV variable,
        # Having settings as a dependency breaks the db inexplicably
        db = TestingSessionLocal()
    else:
        db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
