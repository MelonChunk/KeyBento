from pydantic import BaseSettings


class Settings(BaseSettings):

    SECRET_KEY: str = "0093c877c19ce8d77da13dbda7f77c94a75ef89c6459e126dbf9709d5af870cd"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15  # 60*24*70

    class Config:
        case_sensitive = True


class ProdSettings(Settings):
    environment: str = "PRODUCTION"


class DebugSettings(Settings):
    environment: str = "DEBUG"
