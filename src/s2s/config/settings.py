from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SETLISTFM_API_KEY: str = ''
    SPOTIFY_CLIENT_ID: str = ''
    SPOTIFY_CLIENT_SECRET: str = ''

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
