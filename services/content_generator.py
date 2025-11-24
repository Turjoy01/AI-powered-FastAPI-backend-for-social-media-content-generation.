from typing import List
from services.ai_service import ai_service
from utils.prompts import InstagramPrompts, TikTokPrompts, YouTubePrompts

class ContentGenerator:
    """Service for generating social media content"""
    
    def __init__(self):
        self.ai_service = ai_service
    
    # Instagram Methods
    async def generate_instagram_caption(
        self,
        topic: str,
        tone: str = "casual",
        length: str = "medium"
    ) -> str:
        """Generate Instagram caption"""
        prompt = InstagramPrompts.caption(topic, tone, length)
        return await self.ai_service.generate_content(prompt)
    
    async def generate_instagram_hashtags(
        self,
        topic: str,
        count: int = 10
    ) -> List[str]:
        """Generate Instagram hashtags"""
        prompt = InstagramPrompts.hashtags(topic, count)
        response = await self.ai_service.generate_content(prompt)
        
        # Parse hashtags from response
        hashtags = [
            line.strip() 
            for line in response.split('\n') 
            if line.strip() and line.strip().startswith('#')
        ]
        return hashtags[:count]
    
    async def generate_instagram_content_ideas(
        self,
        niche: str,
        count: int = 5
    ) -> List[str]:
        """Generate Instagram content ideas"""
        prompt = InstagramPrompts.content_ideas(niche, count)
        response = await self.ai_service.generate_content(prompt)
        
        # Parse ideas from response
        ideas = [
            line.strip() 
            for line in response.split('\n') 
            if line.strip() and line.strip()[0].isalnum()
        ]
        return ideas[:count]
    
    # TikTok Methods
    async def generate_tiktok_caption(
        self,
        topic: str,
        tone: str = "energetic",
        length: str = "short"
    ) -> str:
        """Generate TikTok caption"""
        prompt = TikTokPrompts.caption(topic, tone, length)
        return await self.ai_service.generate_content(prompt)
    
    async def generate_tiktok_hashtags(
        self,
        topic: str,
        count: int = 8
    ) -> List[str]:
        """Generate TikTok hashtags"""
        prompt = TikTokPrompts.hashtags(topic, count)
        response = await self.ai_service.generate_content(prompt)
        
        # Parse hashtags from response
        hashtags = [
            line.strip() 
            for line in response.split('\n') 
            if line.strip() and line.strip().startswith('#')
        ]
        return hashtags[:count]
    
    async def generate_tiktok_content_ideas(
        self,
        niche: str,
        count: int = 5
    ) -> List[str]:
        """Generate TikTok content ideas"""
        prompt = TikTokPrompts.content_ideas(niche, count)
        response = await self.ai_service.generate_content(prompt)
        
        # Parse ideas from response
        ideas = [
            line.strip() 
            for line in response.split('\n') 
            if line.strip() and line.strip()[0].isalnum()
        ]
        return ideas[:count]
    
    # YouTube Methods
    async def generate_youtube_title(
        self,
        topic: str,
        style: str = "clickable"
    ) -> str:
        """Generate YouTube title"""
        prompt = YouTubePrompts.title(topic, style)
        return await self.ai_service.generate_content(prompt)
    
    async def generate_youtube_description(
        self,
        topic: str,
        length: str = "medium"
    ) -> str:
        """Generate YouTube description"""
        prompt = YouTubePrompts.description(topic, length)
        return await self.ai_service.generate_content(prompt)
    
    async def generate_youtube_tags(
        self,
        topic: str,
        count: int = 15
    ) -> List[str]:
        """Generate YouTube tags"""
        prompt = YouTubePrompts.tags(topic, count)
        response = await self.ai_service.generate_content(prompt)
        
        # Parse tags from response
        tags = [
            line.strip().replace('#', '') 
            for line in response.split('\n') 
            if line.strip()
        ]
        return tags[:count]
    
    async def generate_youtube_content_ideas(
        self,
        niche: str,
        count: int = 5
    ) -> List[str]:
        """Generate YouTube content ideas"""
        prompt = YouTubePrompts.content_ideas(niche, count)
        response = await self.ai_service.generate_content(prompt)
        
        # Parse ideas from response
        ideas = [
            line.strip() 
            for line in response.split('\n') 
            if line.strip() and line.strip()[0].isalnum()
        ]
        return ideas[:count]

# Singleton instance
content_generator = ContentGenerator()
