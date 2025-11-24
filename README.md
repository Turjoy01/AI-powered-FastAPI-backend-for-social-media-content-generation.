# Social Media Content Generation API

AI-powered FastAPI backend for generating social media content for Instagram, TikTok, and YouTube.

## Features

- 🤖 **AI-Powered Content Generation** using OpenAI GPT-4o-mini
- 📸 **Instagram**: Captions, Hashtags, Content Ideas
- 🎵 **TikTok**: Captions, Hashtags, Content Ideas
- 🎥 **YouTube**: Titles, Descriptions, Tags, Content Ideas
- 🚀 **Fast & Scalable** with FastAPI
- 📚 **Interactive API Documentation** with Swagger UI

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and add your Gemini API key:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

Get your OpenAI API key from: https://platform.openai.com/api-keys

### 3. Run the Server

**Option 1: Using the startup script (recommended)**
```bash
.\start.ps1
```

**Option 2: Manual start**
```bash
# Set API key first
$env:OPENAI_API_KEY="your_api_key_here"
# Then start server
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpoints

### Instagram
- `POST /api/instagram/caption` - Generate Instagram captions
- `POST /api/instagram/hashtags` - Generate Instagram hashtags
- `POST /api/instagram/content-ideas` - Generate Instagram content ideas

### TikTok
- `POST /api/tiktok/caption` - Generate TikTok captions
- `POST /api/tiktok/hashtags` - Generate TikTok hashtags
- `POST /api/tiktok/content-ideas` - Generate TikTok content ideas

### YouTube
- `POST /api/youtube/title` - Generate YouTube titles
- `POST /api/youtube/description` - Generate YouTube descriptions
- `POST /api/youtube/tags` - Generate YouTube tags
- `POST /api/youtube/content-ideas` - Generate YouTube content ideas

## Example Usage

### Generate Instagram Caption

```bash
curl -X POST "http://127.0.0.1:8000/api/instagram/caption" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "morning coffee routine",
    "tone": "casual",
    "length": "medium"
  }'
```

### Generate TikTok Hashtags

```bash
curl -X POST "http://127.0.0.1:8000/api/tiktok/hashtags" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "fitness motivation",
    "count": 10
  }'
```

### Generate YouTube Title

```bash
curl -X POST "http://127.0.0.1:8000/api/youtube/title" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "how to start a podcast",
    "style": "clickable"
  }'
```

## Project Structure

```
.
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── models/
│   ├── __init__.py
│   └── schemas.py         # Pydantic models
├── routes/
│   ├── __init__.py
│   ├── instagram.py       # Instagram endpoints
│   ├── tiktok.py          # TikTok endpoints
│   └── youtube.py         # YouTube endpoints
├── services/
│   ├── __init__.py
│   ├── ai_service.py      # Gemini API integration
│   └── content_generator.py  # Content generation logic
└── utils/
    ├── __init__.py
    ├── config.py          # Configuration management
    └── prompts.py         # AI prompt templates
```

## Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **OpenAI GPT-4o-mini** - AI model for content generation
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## License

MIT
