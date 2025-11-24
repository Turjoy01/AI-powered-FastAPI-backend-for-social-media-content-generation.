from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class ToneEnum(str, Enum):
    """Available tone options"""
    CASUAL = "casual"
    PROFESSIONAL = "professional"
    ENERGETIC = "energetic"
    FRIENDLY = "friendly"
    HUMOROUS = "humorous"
    INSPIRATIONAL = "inspirational"
    EDUCATIONAL = "educational"

class LengthEnum(str, Enum):
    """Available length options"""
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

class PlatformEnum(str, Enum):
    """Supported platforms"""
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    YOUTUBE = "youtube"

# Request Models
class CaptionRequest(BaseModel):
    """Request model for caption generation"""
    topic: str = Field(..., description="Topic or theme for the caption", min_length=1)
    tone: ToneEnum = Field(default=ToneEnum.CASUAL, description="Tone of the caption")
    length: LengthEnum = Field(default=LengthEnum.MEDIUM, description="Length of the caption")
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "morning coffee routine",
                "tone": "casual",
                "length": "medium"
            }
        }

class HashtagRequest(BaseModel):
    """Request model for hashtag generation"""
    topic: str = Field(..., description="Topic for hashtag generation", min_length=1)
    count: int = Field(default=10, ge=5, le=30, description="Number of hashtags to generate")
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "fitness motivation",
                "count": 10
            }
        }

class ContentIdeasRequest(BaseModel):
    """Request model for content ideas generation"""
    niche: str = Field(..., description="Niche or industry for content ideas", min_length=1)
    count: int = Field(default=5, ge=3, le=10, description="Number of ideas to generate")
    
    class Config:
        json_schema_extra = {
            "example": {
                "niche": "sustainable living",
                "count": 5
            }
        }

class YouTubeTitleRequest(BaseModel):
    """Request model for YouTube title generation"""
    topic: str = Field(..., description="Topic for the video title", min_length=1)
    style: str = Field(default="clickable", description="Style of the title (clickable, informative, educational, entertaining)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "how to start a podcast",
                "style": "clickable"
            }
        }

class YouTubeDescriptionRequest(BaseModel):
    """Request model for YouTube description generation"""
    topic: str = Field(..., description="Topic for the video description", min_length=1)
    length: LengthEnum = Field(default=LengthEnum.MEDIUM, description="Length of the description")
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "beginner's guide to photography",
                "length": "medium"
            }
        }

class YouTubeTagsRequest(BaseModel):
    """Request model for YouTube tags generation"""
    topic: str = Field(..., description="Topic for tag generation", min_length=1)
    count: int = Field(default=15, ge=5, le=30, description="Number of tags to generate")
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "cooking healthy meals",
                "count": 15
            }
        }

# Response Models
class CaptionResponse(BaseModel):
    """Response model for caption generation"""
    caption: str = Field(..., description="Generated caption")
    platform: PlatformEnum = Field(..., description="Platform the caption is for")
    
    class Config:
        json_schema_extra = {
            "example": {
                "caption": "Starting my day with the perfect cup of coffee ☕✨ There's something magical about that first sip! What's your go-to morning drink?",
                "platform": "instagram"
            }
        }

class HashtagResponse(BaseModel):
    """Response model for hashtag generation"""
    hashtags: List[str] = Field(..., description="List of generated hashtags")
    count: int = Field(..., description="Number of hashtags generated")
    platform: PlatformEnum = Field(..., description="Platform the hashtags are for")
    
    class Config:
        json_schema_extra = {
            "example": {
                "hashtags": ["#fitness", "#motivation", "#workout", "#gym"],
                "count": 4,
                "platform": "instagram"
            }
        }

class ContentIdeasResponse(BaseModel):
    """Response model for content ideas generation"""
    ideas: List[str] = Field(..., description="List of generated content ideas")
    count: int = Field(..., description="Number of ideas generated")
    platform: PlatformEnum = Field(..., description="Platform the ideas are for")
    
    class Config:
        json_schema_extra = {
            "example": {
                "ideas": [
                    "[Reel] - Zero Waste Kitchen: Show your plastic-free kitchen essentials",
                    "[Carousel] - 5 Easy Swaps: Sustainable alternatives for daily items"
                ],
                "count": 2,
                "platform": "instagram"
            }
        }

class YouTubeTitleResponse(BaseModel):
    """Response model for YouTube title generation"""
    title: str = Field(..., description="Generated YouTube title")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "How to Start a Podcast in 2024 | Complete Beginner's Guide"
            }
        }

class YouTubeDescriptionResponse(BaseModel):
    """Response model for YouTube description generation"""
    description: str = Field(..., description="Generated YouTube description")
    
    class Config:
        json_schema_extra = {
            "example": {
                "description": "Learn everything you need to know about starting a podcast..."
            }
        }

class YouTubeTagsResponse(BaseModel):
    """Response model for YouTube tags generation"""
    tags: List[str] = Field(..., description="List of generated tags")
    count: int = Field(..., description="Number of tags generated")
    
    class Config:
        json_schema_extra = {
            "example": {
                "tags": ["podcast", "how to start a podcast", "podcasting tips"],
                "count": 3
            }
        }

class ErrorResponse(BaseModel):
    """Error response model"""
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")
    
    class Config:
        json_schema_extra = {
            "example": {
                "error": "Invalid API key",
                "detail": "Please check your GEMINI_API_KEY environment variable"
            }
        }
