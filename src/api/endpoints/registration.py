import re

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from api.dependencies import get_db
from schemas.user import CreateUserSchema
from models.user import User

router = APIRouter()

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def validdate_proposed_user(new_user: CreateUserSchema, db):
    field_report = {
        "username": None,
        "lastname": None,
        "firstname": None,
        "email": None,
        "password": None,
    }
    if len(db.query(User).filter(User.username == new_user.username).all()) > 0:
        field_report["username"] = "Username already exists"

    if not EMAIL_REGEX.match(new_user.email):
        field_report["email"] = "This is not a valid email"

    if (new_user.password == new_user.password.lower()) or (
        new_user.password == new_user.password.upper()
    ):
        field_report["password"] = "Password needs upper- and lowercase letters"

    if len(new_user.password) < 12:
        field_report["password"] = "Password needs at least 12 characters"

    if not re.search("[0-9]", new_user.password):
        field_report["password"] = "Password needs some numbers at least"

    if any(value is not None for _, value in field_report.items()):
        return False, field_report

    return True, field_report


@router.post("/register_user")
def register_user(new_user: CreateUserSchema, db=Depends(get_db)):
    is_valid, field_report = validdate_proposed_user(new_user, db=db)
    if is_valid:
        user = User.create(new_user)
        db.add(user)
        db.commit()
        return True
    return JSONResponse(
        status_code=420,
        content={
            "errors": {
                "firstname": field_report["firstname"],
                "lastname": field_report["lastname"],
                "username": field_report["username"],
                "email": field_report["email"],
                "password": field_report["password"],
            }
        },
    )
