from piper import PiperVoice
import wave
import io
import sounddevice as sd
import numpy as np

MODEL_PATH = r"C:\piper_models\hi_IN-pratham-medium.onnx"

print("Loading model...")
voice = PiperVoice.load(MODEL_PATH)

def speak(text):
    print("Speaking:", text)

    # Create in-memory WAV
    mem_wav = io.BytesIO()

    # Piper writes directly into a wave file object
    with wave.open(mem_wav, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    # Move to beginning of buffer
    mem_wav.seek(0)

    # Read WAV data
    with wave.open(mem_wav, 'rb') as wav:
        sample_rate = wav.getframerate()
        frames = wav.readframes(wav.getnframes())

    # Convert to numpy array
    audio = np.frombuffer(frames, dtype=np.int16)

    # Play immediately
    sd.play(audio, samplerate=sample_rate)
    sd.wait()

# Test
speak("मैं हिमांशु नाम के एक लड़के को जानता हूँ              जय श्री राम")
