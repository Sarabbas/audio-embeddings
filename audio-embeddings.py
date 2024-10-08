import openl3
import numpy as np
import soundfile as sf


audio_path= './Ses01F_impro01.wav'

audio,sr= sf.read(audio_path)
embedding, timestamps = openl3.get_audio_embedding(audio, sr)
print(embedding)