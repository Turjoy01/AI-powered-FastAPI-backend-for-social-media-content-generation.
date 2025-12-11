"""
AI prompt templates for platform-agnostic social media content generation.
"""


def _platform_label(platform: str) -> str:
    """Normalize the platform label for prompts."""
    return platform.strip() or "the target platform"


class GlobalPrompts:
    """Prompt templates that adapt to any social platform."""
    
    @staticmethod
    def caption(platform: str, topic: str, tone: str = "casual", length: str = "medium") -> str:
        normalized_platform = _platform_label(platform)
        return f"""Generate an engaging caption for {normalized_platform} about: {topic}

Requirements:
- Platform-specific nuances for {normalized_platform}
- Tone: {tone}
- Length: {length} (short: 1-2 sentences, medium: 3-5 sentences, long: 6-10 sentences)
- Use formatting, emojis, or mentions that fit {normalized_platform}
- Add a call-to-action that suits {normalized_platform} culture

Respond with the caption only."""
    
    @staticmethod
    def hashtags(platform: str, topic: str, count: int = 10) -> str:
        normalized_platform = _platform_label(platform)
        return f"""Generate {count} relevant hashtags for {normalized_platform} about: {topic}

Requirements:
- Include a mix of broad and niche tags suitable for {normalized_platform}
- Reflect current trends and community language
- Format: one hashtag per line (include # if the platform uses it)

Respond with hashtags only."""
    
    @staticmethod
    def content_ideas(platform: str, niche: str, count: int = 5) -> str:
        normalized_platform = _platform_label(platform)
        return f"""Generate {count} creative content ideas for {normalized_platform} in the niche: {niche}

Requirements:
- Mix of popular and emerging content formats for {normalized_platform}
- Provide a short description for each idea
- Highlight hooks, calls-to-action, or storytelling angles that resonate on {normalized_platform}

Format:
[Format] - [Idea Title]: [Brief Description]"""
    
    @staticmethod
    def video_title(platform: str, topic: str, style: str = "clickable") -> str:
        normalized_platform = _platform_label(platform)
        return f"""Generate a compelling {normalized_platform} video title about: {topic}

Requirements:
- Style: {style} (clickable, informative, educational, entertaining, inspirational, etc.)
- Optimize for search and click-through on {normalized_platform}
- Keep under 70 characters when possible
- Avoid clickbait wording

Respond with the title only."""
    
    @staticmethod
    def video_description(platform: str, topic: str, length: str = "medium") -> str:
        normalized_platform = _platform_label(platform)
        return f"""Write a {length} {normalized_platform} video description about: {topic}

Requirements:
- Include a strong hook in the first sentence
- Add relevant keywords and optional timestamps
- Close with a call-to-action that fits {normalized_platform}
- Keep formatting clean and readable

Respond with the description only."""
    
    @staticmethod
    def video_tags(platform: str, topic: str, count: int = 15) -> str:
        normalized_platform = _platform_label(platform)
        return f"""Generate {count} SEO-friendly tags/keywords for a {normalized_platform} video about: {topic}

Requirements:
- Mix of short-tail and long-tail keywords
- Reflect search intent on {normalized_platform}
- Format: one tag per line (no # symbol unless common on the platform)

Respond with tags only."""