from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import content_router
from utils.config import settings

# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description=settings.API_DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(content_router)

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Social Media Content Generation API",
        "version": settings.API_VERSION,
        "docs": "/docs",
        "platforms": "Any social platform (Instagram, LinkedIn, Pinterest, YouTube, TikTok, etc.)",
        "features": [
            "AI-powered captions",
            "Platform-aware hashtags",
            "Content idea brainstorming",
            "Video titles, descriptions & tags for any platform"
        ]
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "api_version": settings.API_VERSION
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)