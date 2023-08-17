from fastapi import HTTPException, status

CredentialsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

UnauthorisedException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)

EmailAlreadyRegisteredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="This email address already registered its interest.",
    headers={"WWW-Authenticate": "Bearer"},
)
