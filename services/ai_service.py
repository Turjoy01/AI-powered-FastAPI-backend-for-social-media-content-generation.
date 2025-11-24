from openai import OpenAI
from typing import Optional
from utils.config import settings

class AIService:
    """Service for interacting with OpenAI API"""
    
    def __init__(self):
        """Initialize the AI service with API key"""
        self.client = None
        self.model = settings.OPENAI_MODEL
        self._initialized = False
    
    def _ensure_initialized(self):
        """Lazy initialization - only create client when needed"""
        if not self._initialized:
            if not settings.OPENAI_API_KEY:
                raise ValueError(
                    "OPENAI_API_KEY is not set. Please set it in your .env file or environment variables.\n"
                    "Get your API key from: https://platform.openai.com/api-keys"
                )
            self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
            self._initialized = True
    
    async def generate_content(
        self,
        prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Generate content using OpenAI API
        
        Args:
            prompt: The prompt to send to the AI
            temperature: Controls randomness (0.0 to 1.0)
            max_tokens: Maximum tokens in response
            
        Returns:
            Generated text content
            
        Raises:
            Exception: If API call fails
        """
        self._ensure_initialized()
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant specialized in creating engaging social media content."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature or settings.TEMPERATURE,
                max_tokens=max_tokens or settings.MAX_TOKENS,
            )
            
            if not response.choices or not response.choices[0].message.content:
                raise Exception("Empty response from AI service")
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            raise Exception(f"AI generation failed: {str(e)}")
    
    def validate_api_key(self) -> bool:
        """
        Validate that the API key is working
        
        Returns:
            True if API key is valid, False otherwise
        """
        try:
            self._ensure_initialized()
            # Try a simple generation to test the API key
            self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5
            )
            return True
        except Exception:
            return False

# Singleton instance
ai_service = AIService()
