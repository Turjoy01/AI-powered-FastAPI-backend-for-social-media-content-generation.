from fastapi import APIRouter, HTTPException

from models.schemas import (
    CaptionRequest,
    CaptionResponse,
    HashtagRequest,
    HashtagResponse,
    ContentIdeasRequest,
    ContentIdeasResponse,
    VideoTitleRequest,
    VideoTitleResponse,
    VideoDescriptionRequest,
    VideoDescriptionResponse,
    VideoTagsRequest,
    VideoTagsResponse,
)
from services.content_generator import content_generator

router = APIRouter(prefix="/api/content", tags=["Content"])


@router.post("/caption", response_model=CaptionResponse)
async def generate_caption(request: CaptionRequest):
    """Generate a caption for any social platform."""
    try:
        caption = await content_generator.generate_caption(
            platform=request.platform,
            topic=request.topic,
            tone=request.tone.value,
            length=request.length.value,
        )
        return CaptionResponse(caption=caption, platform=request.platform)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to generate caption: {exc}")


@router.post("/hashtags", response_model=HashtagResponse)
async def generate_hashtags(request: HashtagRequest):
    """Generate hashtags for any platform."""
    try:
        hashtags = await content_generator.generate_hashtags(
            platform=request.platform,
            topic=request.topic,
            count=request.count,
        )
        return HashtagResponse(hashtags=hashtags, count=len(hashtags), platform=request.platform)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to generate hashtags: {exc}")


@router.post("/content-ideas", response_model=ContentIdeasResponse)
async def generate_content_ideas(request: ContentIdeasRequest):
    """Generate content ideas tailored to the specified platform."""
    try:
        ideas = await content_generator.generate_content_ideas(
            platform=request.platform,
            niche=request.niche,
            count=request.count,
        )
        return ContentIdeasResponse(ideas=ideas, count=len(ideas), platform=request.platform)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to generate content ideas: {exc}")


@router.post("/video/title", response_model=VideoTitleResponse)
async def generate_video_title(request: VideoTitleRequest):
    """Generate a video title for any video-first platform."""
    try:
        title = await content_generator.generate_video_title(
            platform=request.platform,
            topic=request.topic,
            style=request.style,
        )
        return VideoTitleResponse(title=title, platform=request.platform)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to generate video title: {exc}")


@router.post("/video/description", response_model=VideoDescriptionResponse)
async def generate_video_description(request: VideoDescriptionRequest):
    """Generate a video description for any video-first platform."""
    try:
        description = await content_generator.generate_video_description(
            platform=request.platform,
            topic=request.topic,
            length=request.length.value,
        )
        return VideoDescriptionResponse(description=description, platform=request.platform)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to generate video description: {exc}")


@router.post("/video/tags", response_model=VideoTagsResponse)
async def generate_video_tags(request: VideoTagsRequest):
    """Generate video tags for any platform."""
    try:
        tags = await content_generator.generate_video_tags(
            platform=request.platform,
            topic=request.topic,
            count=request.count,
        )
        return VideoTagsResponse(tags=tags, count=len(tags), platform=request.platform)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to generate video tags: {exc}")

