JARVIS — CLASSIFIED FACE / UI UPDATE
====================================

1. Back up your current Jarvis folder.
2. Extract this package into your existing Jarvis project folder.
3. Replace jarvis.py and merge the assets folder.
4. KEEP your existing .env file (GEMINI_API_KEY), music_library.json,
   and opera_jarvis_profile folder.
5. Install dependencies if needed:
     py -m pip install -r requirements-jarvis-ui.txt
6. Start JARVIS:
     py jarvis.py
   or double-click run_jarvis.bat.

Face artwork:
- The supplied geometric face is used as the central avatar projection.
- The mouth and eye overlays animate with JARVIS UI states.
- The Freepik attribution is retained in the UI caption/footer and in
  assets/FACE_ASSET_CREDIT.txt. Confirm your asset license before sharing
  or distributing the application.

Notes:
- This update keeps the existing Gemini, Whisper, voice, browser, music,
  and desktop automation code intact.
- Lip movement is a state-driven visual animation, not phoneme-perfect
  viseme synchronization. It moves while the Windows TTS process speaks.
