
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Load Gemini API key
load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.1-flash-lite"

chat = client.chats.create(model=MODEL)

print("JARVIS is online!")
print("Using:", MODEL)
print("Type 'exit' to quit.\n")

while True:
    command = input("You: ").strip()

    if command.lower() == "exit":
        print("JARVIS: Goodbye, sir.")
        break

    if not command:
        continue

    for attempt in range(3):
        try:
            response = chat.send_message(command)
            print("JARVIS:", response.text)
            break

        except errors.ServerError as error:
            if error.code not in (500, 503, 504):
                print("JARVIS: Server error:", error)
                break

            if attempt == 2:
                print("JARVIS: Gemini is still busy.")
                break

            delay = 2 ** (attempt + 1)
            print(f"Gemini is busy. Retrying in {delay}s...")
            time.sleep(delay)

        except errors.ClientError as error:
            print("JARVIS: API request failed:", error)
            break

        except Exception as error:
            print("JARVIS: Unexpected error:", error)
            break
