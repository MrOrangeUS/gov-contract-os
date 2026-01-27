from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    supabase_url: str | None = None
    supabase_service_role_key: str | None = None

    redis_url: str = "redis://localhost:6379/0"
    jobs_api_key: str | None = None

    sam_api_key: str | None = None

    google_application_credentials_json: str | None = None
    gdrive_root_folder_id: str | None = None

    app_env: str = "local"


settings = Settings()
