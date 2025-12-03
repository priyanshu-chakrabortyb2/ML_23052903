import soundfile as sf

audio, sample_rate = sf.read("123440/260-123440-0000.flac")
print("Sample Rate:", sample_rate)
print("Audio Length:", len(audio))