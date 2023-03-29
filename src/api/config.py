from pydantic import BaseSettings


class Settings(BaseSettings):

    SECRET_KEY: str = "585a9ebe882df806e3ce9dd75c7d2317a997c8178d1f4818a27376603a0aea56"
    ACCESS_TOKEN_EXPIRE_MINUTES: str = 10080

    class Config:
        case_sensitive = True


class ProdSettings(Settings):
    environment: str = "PRODUCTION"


class DebugSettings(Settings):
    environment: str = "DEBUG"
