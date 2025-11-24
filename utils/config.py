import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings and configuration"""
    
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # API Configuration
    API_TITLE: str = "Social Media Content Generation API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = """
    AI-powered content generation API for social media platforms.
    
    Supports:
    - Instagram (captions, hashtags, content ideas)
    - TikTok (captions, hashtags, content ideas)
    - YouTube (titles, descriptions, tags, content ideas)
    """
    
    # CORS Settings
    CORS_ORIGINS: list = ["*"]
    
    # AI Model Settings
    OPENAI_MODEL: str = "gpt-4o-mini"
    MAX_TOKENS: int = 2048
    TEMPERATURE: float = 0.7
    
    def validate(self):
        """Validate required settings"""
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        return True

settings = Settings()
