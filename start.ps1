# Set OpenAI API Key
$env:OPENAI_API_KEY="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"

# Start the FastAPI server
.venv\Scripts\uvicorn.exe main:app --reload
