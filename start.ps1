# Set OpenAI API Key
$env:OPENAI_API_KEY=""

# Start the FastAPI server
.venv\Scripts\uvicorn.exe main:app --reload
