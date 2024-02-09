import librosa as lr
import numpy as np

from keras.layers import Dense, LSTM, Activation
from keras.models import Sequential
from keras.optimizers import Adam

SR = 16000  # Sampling Rate
LENGTH = 16  # Amount of blocks for 1 walkthrough
OVERLAP = 8  # Step between samples in amount of blocks
FFT = 1024  # Length of block (64ms)


# List of all records
voices = [("man11.wav", True),
          ("man12.wav", True),
          ("man13.wav", True),
          ("man14.wav", True),
          ("man21.wav", False),
          ("man22.wav", False),
          ("man23.wav", False),
          ("man24.wav", False),
          ("man31.wav", False),
          ("man32.wav", False),
          ("man33.wav", False),
          # ("man34.wav", False),
          # ("man41.wav", False),
          # ("man42.wav", False),
          # ("man43.wav", False),
          # ("man44.wav", False),
          # ("man51.wav", False),
          # ("man52.wav", False),
          # ("man53.wav", False),
          # ("man54.wav", False),
          # ("man61.wav", False),
          # ("man62.wav", False),
          # ("man63.wav", False),
          # ("man64.wav", False),
          # ("man71.wav", False),
          # ("man72.wav", False),
          # ("man73.wav", False),
          # ("man74.wav", False),
          ("woman11.wav", False),
          ("woman12.wav", False),
          ("woman13.wav", False),
          ("woman14.wav", False),
          ("woman21.wav", False),
          ("woman22.wav", False),
          ("woman23.wav", False),
          ("woman24.wav", False),
          ("woman31.wav", False),
          ("woman32.wav", False),
          ("woman33.wav", False),
          ("woman34.wav", False),
          # ("woman41.wav", False),
          # ("woman42.wav", False),
          # ("woman43.wav", False),
          # ("woman44.wav", False),
          # ("woman51.wav", False),
          # ("woman52.wav", False),
          # ("woman53.wav", False),
          # ("woman54.wav", False),
          # ("woman61.wav", False),
          # ("woman62.wav", False),
          # ("woman63.wav", False),
          # ("woman64.wav", False)
          ]


def process_audio(a_name, a_path):
    f_a_path = a_path + a_name
    audio, _ = lr.load(f_a_path, sr=SR)  # upload track into memory

    # exporting coefficients
    afs = lr.feature.mfcc(audio,  # from track
                          sr=SR,  # sampling rate 16kHz
                          n_mfcc=34,  # exporting 34 parameters
                          n_fft=2048)  # using 125ms blocks
    # Summarize all the coefficients in time
    # Drop the first two coefficients 'cos they cannot be heard
    afss = np.sum(afs[2:], axis=-1)

    # Normalize 'em
    afss = afss / np.max(np.abs(afss))

    return afss


def confidence(x, y):
    return np.sum((x - y) ** 2)  # Euclidean distance
    # Less is better


audio_path = "raw_data_wav/"

# Upload several audio track
# woman21 = process_audio("woman21.wav", audio_path)
# woman22 = process_audio("woman22.wav", audio_path)
# woman11 = process_audio("woman11.wav", audio_path)
# woman12 = process_audio("woman12.wav", audio_path)
# man11 = process_audio("man12.wav", audio_path)
# savv1 = process_audio("savvat_gt.wav", "savvat_audio/")
man = process_audio("man63.wav", audio_path)
george = process_audio("george3.wav", audio_path)
george5 = process_audio("george5.wav", "savvat_audio/")
natali = process_audio("natali.wav", "savvat_audio/")

# Compare coefficients on nearness
# print('same', confidence(woman11, woman12))
# print('same', confidence(woman21, woman22))
# print('diff', confidence(woman11, woman21))
# print('diff', confidence(woman11, woman22))
# print('diff', confidence(woman12, woman21))
# print('diff', confidence(woman12, woman22))
print('same:', confidence(george, george5))
print('diff:', confidence(george5, natali))
