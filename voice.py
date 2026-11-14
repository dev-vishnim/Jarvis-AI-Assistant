
import os
import numpy as np
import sounddevice as sd
import subprocess

from pathlib import Path
from dotenv import load_dotenv
from google import genai
from faster_whisper import WhisperModel

# Load Gemini API key
load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key is missing!")

# Initialize Gemini
client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.1-flash-lite"
)

# Initialize local speech recognition
print("Loading speech recognition...")
whisper = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)




def speak(message):
    print("JARVIS:", message)

    script = """
Add-Type -AssemblyName System.Speech

$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speaker.Rate = 0

$text = [Console]::In.ReadToEnd()
$speaker.Speak($text)

$speaker.Dispose()
"""

    subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            script
        ],
        input=message,
        text=True,
        check=True
    )


def listen():
    sample_rate = 16000
    duration = 6

    print("\nListening for 6 seconds...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    audio = np.squeeze(audio)

    segments, info = whisper.transcribe(
        audio,
        beam_size=5,
        language="en"
    )

    command = " ".join(
        segment.text for segment in segments
    ).strip()

    print("YOU:", command)
    return command

def ask_gemini(command):
    response = chat.send_message(command)
    return response.text or "I couldn't generate a response."

speak("Jarvis voice system is online.")

while True:
    try:
        input("\nPress Enter to speak...")

        command = listen()

        if not command:
            speak("I didn't hear anything.")
            continue

        if command.lower() in [
            "exit", "goodbye", "stop jarvis"
        ]:
            speak("Goodbye, sir.")
            break

        response = ask_gemini(command)
        speak(response)

    except KeyboardInterrupt:
        print("\nJARVIS stopped.")
        break

    except Exception as error:
        print("Error:", error)
        speak("Something went wrong.")
