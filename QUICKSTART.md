# Quick Start Guide

## ✅ Everything is Now Fixed!

The `.env` file has been created with your OpenAI API key, and the server is ready to run.

---

## How to Start the Server

### Option 1: Direct Command (Simple)
```powershell
uvicorn main:app --reload
```

### Option 2: Using the Startup Script
```powershell
.\start.ps1
```

Both options will work now because the `.env` file is properly configured!

---

## What Was Fixed

1. ✅ **Created `.env` file** with your OpenAI API key
2. ✅ **Modified AI service** to use lazy initialization (loads API key from .env automatically)
3. ✅ **Verified** the API key loads correctly
4. ✅ **Tested** the app imports successfully

---

## Access Your API

Once you run `uvicorn main:app --reload`, visit:

- **Interactive Docs**: http://127.0.0.1:8000/docs
- **API Root**: http://127.0.0.1:8000
- **Health Check**: http://127.0.0.1:8000/health

---

## Test an Endpoint

Open http://127.0.0.1:8000/docs and try:

1. Click on **POST /api/instagram/caption**
2. Click **"Try it out"**
3. Enter:
   ```json
   {
     "topic": "coffee",
     "tone": "casual",
     "length": "short"
   }
   ```
4. Click **"Execute"**
5. See your AI-generated caption! ☕

---

## Important Files

- **`.env`** - Contains your API key (gitignored, never commit this!)
- **`start.ps1`** - Startup script (also has API key)
- **`main.py`** - FastAPI application
- **`README.md`** - Full documentation

---

## You're All Set! 🚀

Just run: `uvicorn main:app --reload`
