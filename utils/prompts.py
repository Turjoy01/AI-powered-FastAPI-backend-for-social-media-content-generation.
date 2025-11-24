"""
AI prompt templates for social media content generation
"""

class InstagramPrompts:
    """Prompt templates for Instagram content"""
    
    @staticmethod
    def caption(topic: str, tone: str = "casual", length: str = "medium") -> str:
        return f"""Generate an engaging Instagram caption about: {topic}

Requirements:
- Tone: {tone}
- Length: {length} (short: 1-2 sentences, medium: 3-5 sentences, long: 6-10 sentences)
- Include emojis where appropriate
- Make it engaging and authentic
- Add a call-to-action if relevant

Generate only the caption text, no additional explanation."""

    @staticmethod
    def hashtags(topic: str, count: int = 10) -> str:
        return f"""Generate {count} relevant Instagram hashtags for: {topic}

Requirements:
- Mix of popular and niche hashtags
- Relevant to the topic
- Include trending hashtags if applicable
- Format: #hashtag (one per line)

Generate only the hashtags, no additional explanation."""

    @staticmethod
    def content_ideas(niche: str, count: int = 5) -> str:
        return f"""Generate {count} creative Instagram content ideas for the niche: {niche}

Requirements:
- Diverse content types (posts, reels, stories, carousels)
- Engaging and trendy
- Actionable and specific
- Include brief description for each idea

Format each idea as:
[Content Type] - [Idea Title]: [Brief Description]"""


class TikTokPrompts:
    """Prompt templates for TikTok content"""
    
    @staticmethod
    def caption(topic: str, tone: str = "energetic", length: str = "short") -> str:
        return f"""Generate a catchy TikTok caption about: {topic}

Requirements:
- Tone: {tone}
- Length: {length} (short: 1-2 sentences, medium: 2-4 sentences)
- Use trending language and slang
- Include emojis
- Make it attention-grabbing
- Keep it concise and punchy

Generate only the caption text, no additional explanation."""

    @staticmethod
    def hashtags(topic: str, count: int = 8) -> str:
        return f"""Generate {count} trending TikTok hashtags for: {topic}

Requirements:
- Include viral and trending hashtags
- Mix of broad and specific hashtags
- Relevant to the topic
- Format: #hashtag (one per line)

Generate only the hashtags, no additional explanation."""

    @staticmethod
    def content_ideas(niche: str, count: int = 5) -> str:
        return f"""Generate {count} viral TikTok video ideas for the niche: {niche}

Requirements:
- Trending formats and challenges
- Engaging hooks
- Specific and actionable
- Include brief description and hook for each idea

Format each idea as:
[Video Type] - [Hook]: [Brief Description]"""


class YouTubePrompts:
    """Prompt templates for YouTube content"""
    
    @staticmethod
    def title(topic: str, style: str = "clickable") -> str:
        return f"""Generate a compelling YouTube video title about: {topic}

Requirements:
- Style: {style} (clickable, informative, educational, entertaining)
- 60-70 characters optimal
- Include keywords for SEO
- Attention-grabbing but not clickbait
- Clear and descriptive

Generate only the title, no additional explanation."""

    @staticmethod
    def description(topic: str, length: str = "medium") -> str:
        return f"""Generate a YouTube video description about: {topic}

Requirements:
- Length: {length} (short: 2-3 sentences, medium: 1 paragraph, long: 2-3 paragraphs)
- Include relevant keywords
- Add timestamps placeholder if needed
- Include call-to-action (subscribe, like, comment)
- SEO-optimized

Generate only the description text, no additional explanation."""

    @staticmethod
    def tags(topic: str, count: int = 15) -> str:
        return f"""Generate {count} relevant YouTube tags/keywords for: {topic}

Requirements:
- Mix of broad and specific keywords
- SEO-optimized
- Relevant to the topic
- Include long-tail keywords
- Format: one tag per line (no # symbol)

Generate only the tags, no additional explanation."""

    @staticmethod
    def content_ideas(niche: str, count: int = 5) -> str:
        return f"""Generate {count} YouTube video ideas for the niche: {niche}

Requirements:
- Diverse video formats (tutorials, vlogs, reviews, lists, etc.)
- SEO-friendly topics
- Engaging and valuable to viewers
- Include brief description and target audience for each idea

Format each idea as:
[Video Format] - [Title]: [Brief Description] | Target: [Audience]"""
