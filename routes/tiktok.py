from fastapi import APIRouter, HTTPException
from models.schemas import (
    CaptionRequest,
    CaptionResponse,
    HashtagRequest,
    HashtagResponse,
    ContentIdeasRequest,
    ContentIdeasResponse,
    PlatformEnum
)
from services.content_generator import content_generator

router = APIRouter(prefix="/api/tiktok", tags=["TikTok"])

@router.post("/caption", response_model=CaptionResponse)
async def generate_caption(request: CaptionRequest):
    """
    Generate a TikTok caption
    
    - **topic**: The topic or theme for the caption
    - **tone**: The tone of the caption (energetic, casual, humorous, etc.)
    - **length**: The length of the caption (short, medium)
    """
    try:
        caption = await content_generator.generate_tiktok_caption(
            topic=request.topic,
            tone=request.tone.value,
            length=request.length.value
        )
        
        return CaptionResponse(
            caption=caption,
            platform=PlatformEnum.TIKTOK
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate caption: {str(e)}")

@router.post("/hashtags", response_model=HashtagResponse)
async def generate_hashtags(request: HashtagRequest):
    """
    Generate TikTok hashtags
    
    - **topic**: The topic for hashtag generation
    - **count**: Number of hashtags to generate (5-30)
    """
    try:
        hashtags = await content_generator.generate_tiktok_hashtags(
            topic=request.topic,
            count=request.count
        )
        
        return HashtagResponse(
            hashtags=hashtags,
            count=len(hashtags),
            platform=PlatformEnum.TIKTOK
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate hashtags: {str(e)}")

@router.post("/content-ideas", response_model=ContentIdeasResponse)
async def generate_content_ideas(request: ContentIdeasRequest):
    """
    Generate TikTok content ideas
    
    - **niche**: The niche or industry for content ideas
    - **count**: Number of ideas to generate (3-10)
    """
    try:
        ideas = await content_generator.generate_tiktok_content_ideas(
            niche=request.niche,
            count=request.count
        )
        
        return ContentIdeasResponse(
            ideas=ideas,
            count=len(ideas),
            platform=PlatformEnum.TIKTOK
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate content ideas: {str(e)}")
