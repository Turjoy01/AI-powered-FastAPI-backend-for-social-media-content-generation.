# Social Media Content Generation API

AI-powered FastAPI backend for generating social media content for any platform (Instagram, TikTok, LinkedIn, Pinterest, YouTube, etc.).

## Features

- 🤖 **AI-Powered Content Generation** using OpenAI GPT-4o-mini
- 🌐 **Platform Agnostic**: supports any social or video platform
- ✍️ **Captions & Ideas**: tone and length aware
- #️⃣ **Hashtags & Tags**: SEO-friendly for each platform
- 🎥 **Video Assets**: titles, descriptions, and tags for any video channel
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

All endpoints live under `/api/content` and accept a `platform` field so you can target anything from Instagram to Threads or future networks.

- `POST /api/content/caption` - Generate captions
- `POST /api/content/hashtags` - Generate platform-aware hashtags
- `POST /api/content/content-ideas` - Generate tailored content ideas
- `POST /api/content/video/title` - Generate video titles
- `POST /api/content/video/description` - Generate video descriptions
- `POST /api/content/video/tags` - Generate video tags/keywords

## Example Usage

### Generate LinkedIn Caption

```bash
curl -X POST "http://127.0.0.1:8000/api/content/caption" \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "LinkedIn",
    "topic": "morning coffee routine",
    "tone": "casual",
    "length": "medium"
  }'
```

### Generate TikTok Hashtags

```bash
curl -X POST "http://127.0.0.1:8000/api/content/hashtags" \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "TikTok",
    "topic": "fitness motivation",
    "count": 10
  }'
```

### Generate YouTube Title

```bash
curl -X POST "http://127.0.0.1:8000/api/content/video/title" \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "YouTube",
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
│   └── content.py         # Unified content endpoints
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

<img width="1168" height="916" alt="image" src="https://github.com/user-attachments/assets/89817137-871e-4c57-9f06-8a9f2f15c149" />

