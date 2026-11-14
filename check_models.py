
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).resolve().parent / ".env")

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

print("Available models:\n")

for model in client.models.list():
    if "flash" in model.name.lower():
        print(model.name)
