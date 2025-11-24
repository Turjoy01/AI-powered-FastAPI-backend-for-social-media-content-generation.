from fastapi import APIRouter, HTTPException
from models.schemas import (
    YouTubeTitleRequest,
    YouTubeTitleResponse,
    YouTubeDescriptionRequest,
    YouTubeDescriptionResponse,
    YouTubeTagsRequest,
    YouTubeTagsResponse,
    ContentIdeasRequest,
    ContentIdeasResponse,
    PlatformEnum
)
from services.content_generator import content_generator

router = APIRouter(prefix="/api/youtube", tags=["YouTube"])

@router.post("/title", response_model=YouTubeTitleResponse)
async def generate_title(request: YouTubeTitleRequest):
    """
    Generate a YouTube video title
    
    - **topic**: The topic for the video title
    - **style**: The style of the title (clickable, informative, educational, entertaining)
    """
    try:
        title = await content_generator.generate_youtube_title(
            topic=request.topic,
            style=request.style
        )
        
        return YouTubeTitleResponse(title=title)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate title: {str(e)}")

@router.post("/description", response_model=YouTubeDescriptionResponse)
async def generate_description(request: YouTubeDescriptionRequest):
    """
    Generate a YouTube video description
    
    - **topic**: The topic for the video description
    - **length**: The length of the description (short, medium, long)
    """
    try:
        description = await content_generator.generate_youtube_description(
            topic=request.topic,
            length=request.length.value
        )
        
        return YouTubeDescriptionResponse(description=description)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate description: {str(e)}")

@router.post("/tags", response_model=YouTubeTagsResponse)
async def generate_tags(request: YouTubeTagsRequest):
    """
    Generate YouTube video tags
    
    - **topic**: The topic for tag generation
    - **count**: Number of tags to generate (5-30)
    """
    try:
        tags = await content_generator.generate_youtube_tags(
            topic=request.topic,
            count=request.count
        )
        
        return YouTubeTagsResponse(
            tags=tags,
            count=len(tags)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate tags: {str(e)}")

@router.post("/content-ideas", response_model=ContentIdeasResponse)
async def generate_content_ideas(request: ContentIdeasRequest):
    """
    Generate YouTube content ideas
    
    - **niche**: The niche or industry for content ideas
    - **count**: Number of ideas to generate (3-10)
    """
    try:
        ideas = await content_generator.generate_youtube_content_ideas(
            niche=request.niche,
            count=request.count
        )
        
        return ContentIdeasResponse(
            ideas=ideas,
            count=len(ideas),
            platform=PlatformEnum.YOUTUBE
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate content ideas: {str(e)}")
