from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.constants import BACKEND_DIR


class SqliteDatabaseSettings(BaseSettings):
    echo: bool = False
    pool_pre_ping: bool = True
    driver: str
    file_name: str
    dialect: str

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env", env_prefix="DATABASE_", extra="ignore"
    )

    @property
    def async_url(self) -> str:
        return f"{self.dialect}+{self.driver}:///{self.file_name}"


class Settings(BaseSettings):
    db: SqliteDatabaseSettings = SqliteDatabaseSettings()


settings = Settings()
