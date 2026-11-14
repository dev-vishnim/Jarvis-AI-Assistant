
import subprocess

def speak(message):
    script = """
param([string]$message)

Add-Type -AssemblyName System.Speech

$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speaker.Rate = 0
$speaker.Speak($message)
$speaker.Dispose()
"""

    subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            "& { " + script + " }",
            message
        ],
        check=True
    )

speak("Hello sir. This is Jarvis.")
speak("I am testing my voice for the second time.")
speak("If you can hear this, my voice is working correctly.")
