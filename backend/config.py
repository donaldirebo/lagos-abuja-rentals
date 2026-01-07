cat > backend/app/core/config.py << 'EOF'
"""
Application Configuration
Uses pydantic-settings to load from environment variables
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    Falls back to defaults for local development.
    """
    
    # Application
    PROJECT_NAME: str = "Lagos-Abuja Rentals API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    POSTGRES_USER: str = "rental_user"
    POSTGRES_PASSWORD: str = "rental_password"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "rentals_db"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS (Cross-Origin Resource Sharing)
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]
    
    @property
    def DATABASE_URL(self) -> str:
        """Construct database URL from components"""
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


# Create global settings instance
settings = Settings()
EOF
```

**Understanding This Code:**

1. **BaseSettings:** Automatically loads from environment variables
2. **Defaults:** Development values (we'll override in production)
3. **DATABASE_URL:** Constructs PostgreSQL connection string
4. **@property:** Computed value (not stored, calculated on demand)
5. **env_file=".env":** Loads from `.env` file if it exists

**DevOps Insight:**
```
Local Dev: Use defaults (fast, no setup)
Staging: Use .env file (shared secrets)
Production: Use AWS Secrets Manager (secure)
