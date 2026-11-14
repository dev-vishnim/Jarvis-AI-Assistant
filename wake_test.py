
import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel

print("Loading JARVIS wake-word detector...")

whisper = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

SAMPLE_RATE = 16000
DURATION = 3

print("Wake-word detector is ready!")
print("Say 'Hey Jarvis' to activate.")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )
        sd.wait()

        audio = np.squeeze(audio)

        segments, _ = whisper.transcribe(
            audio,
            language="en",
            beam_size=1,
            vad_filter=True,
            condition_on_previous_text=False
        )

        heard = " ".join(
            segment.text for segment in segments
        ).strip()

        if heard:
            print("Heard:", heard)

        if "jarvis" in heard.lower():
            print("\nJARVIS ACTIVATED!")
            print("Wake word detected successfully.\n")

except KeyboardInterrupt:
    print("\nWake-word test stopped.")
