from typing import List
from services.ai_service import ai_service
from utils.prompts import GlobalPrompts


class ContentGenerator:
    """Service for generating social media content on any platform."""
    
    def __init__(self):
        self.ai_service = ai_service
    
    async def generate_caption(
        self,
        platform: str,
        topic: str,
        tone: str = "casual",
        length: str = "medium"
    ) -> str:
        """Generate a caption tailored to the requested platform."""
        prompt = GlobalPrompts.caption(platform, topic, tone, length)
        return await self.ai_service.generate_content(prompt)
    
    async def generate_hashtags(
        self,
        platform: str,
        topic: str,
        count: int = 10
    ) -> List[str]:
        """Generate hashtags aligned with the platform's culture."""
        prompt = GlobalPrompts.hashtags(platform, topic, count)
        response = await self.ai_service.generate_content(prompt)
        
        hashtags = [
            line.strip()
            for line in response.split("\n")
            if line.strip()
        ]
        # Ensure hashtags include # when the AI omitted it
        normalized = []
        for tag in hashtags:
            raw = tag.replace(" ", "")
            if not raw:
                continue
            normalized.append(raw if raw.startswith("#") else f"#{raw.lstrip('#')}")
        return normalized[:count]
    
    async def generate_content_ideas(
        self,
        platform: str,
        niche: str,
        count: int = 5
    ) -> List[str]:
        """Generate platform-aware content ideas."""
        prompt = GlobalPrompts.content_ideas(platform, niche, count)
        response = await self.ai_service.generate_content(prompt)
        
        ideas = [
            line.strip()
            for line in response.split("\n")
            if line.strip()
        ]
        return ideas[:count]
    
    async def generate_video_title(
        self,
        platform: str,
        topic: str,
        style: str = "clickable"
    ) -> str:
        """Generate a video title optimised for the specified platform."""
        prompt = GlobalPrompts.video_title(platform, topic, style)
        return await self.ai_service.generate_content(prompt)
    
    async def generate_video_description(
        self,
        platform: str,
        topic: str,
        length: str = "medium"
    ) -> str:
        """Generate a video description optimised for the specified platform."""
        prompt = GlobalPrompts.video_description(platform, topic, length)
        return await self.ai_service.generate_content(prompt)
    
    async def generate_video_tags(
        self,
        platform: str,
        topic: str,
        count: int = 15
    ) -> List[str]:
        """Generate SEO-friendly video tags for any platform."""
        prompt = GlobalPrompts.video_tags(platform, topic, count)
        response = await self.ai_service.generate_content(prompt)
        
        tags = [
            line.strip().replace("#", "")
            for line in response.split("\n")
            if line.strip()
        ]
        return tags[:count]


# Singleton instance
content_generator = ContentGenerator()
