import librosa as lr
import numpy as np
import os
import re
from glob import glob

from keras.layers import Dense, LSTM, Activation
from keras.models import Sequential
from keras.optimizers import Adam


def filter_audio(audio):
    """filter every audio file in raw data in several parameters"""

    # Calculate voice energy for every 123 ms block
    apower = lr.amplitude_to_db(np.abs(lr.stft(audio, n_fft=2048)), ref=np.max)

    # Summarize energy of every rate, normalize
    apsums = np.sum(apower, axis=0) ** 2
    apsums -= np.min(apsums)
    apsums /= np.max(apsums)

    # Smooth the graph for saving short spaces and pauses, remove sharpness
    apsums = np.convolve(apsums, np.ones((9,)), 'same')
    # Normalize again
    apsums -= np.min(apsums)
    apsums /= np.max(apsums)

    # Set noise limit to 35% over voice
    apsums = np.array(apsums > 0.35, dtype=bool)

    # Extend the blocks every on 125ms
    # before separated samples (2048 at block)
    apsums = np.repeat(apsums, np.ceil(len(audio) / len(apsums)))[:len(audio)]

    return audio[apsums]


def prepare_audio(a_name, target=False):
    """audio tokenizer for further neuron model using"""
    samprate = 16000  # Sampling Rate
    length = 16  # Amount of blocks for 1 walkthrough
    overlap = 8  # Step between samples in amount of blocks
    fft = 1024  # Length of block (64ms)

    # Upload and preparing data sets
    # audio_path = "raw_data_wav/"
    # full_a_name = audio_path + a_name
    print('loading %s' % a_name)
    audio, _ = lr.load(a_name, sr=samprate)
    audio = filter_audio(audio)  # Removing silence and spaces between words
    data = lr.stft(audio, n_fft=fft).swapaxes(0, 1)  # Export spectrogram
    samples = []

    for i in range(0, len(data) - length, overlap):
        samples.append(np.abs(data[i:i + length]))  # Create training sample

    results_shape = (len(samples), 1)
    results = np.ones(results_shape) if target else np.zeros(results_shape)

    return np.array(samples), results


def create_model(list_of_voices, path_of_mod, num_of_epoch=15):
    """prepare raw data of input list, create, train and save the model"""

    # Unite all training samples
    X, Y = prepare_audio(*list_of_voices[0])
    for voice in list_of_voices[1:]:
        dx, dy = prepare_audio(*voice)
        X = np.concatenate((X, dx), axis=0)
        Y = np.concatenate((Y, dy), axis=0)
        del dx, dy

    # Shake all blocks randomly
    perm = np.random.permutation(len(X))
    X = X[perm]
    Y = Y[perm]

    # Create model
    model = Sequential()
    model.add(LSTM(128, return_sequences=True, input_shape=X.shape[1:]))
    model.add(LSTM(64))
    model.add(Dense(64))
    model.add(Activation('tanh'))
    model.add(Dense(16))
    model.add(Activation('sigmoid'))
    model.add(Dense(1))
    model.add(Activation('hard_sigmoid'))

    # Compile and train model
    model.compile(Adam(lr=0.005), loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, Y, epochs=num_of_epoch, batch_size=32, validation_split=0.2)  # epochs=15 is preferred
    print(model.evaluate(X, Y))
    model.save(path_of_mod + 'model.hdf5')

    return None


def find_wavs(directory, pattern='**/*.wav'):
    """Recursively finds all files matching the pattern"""
    return glob(os.path.join(directory, pattern), recursive=True)


def wav_reader(directory):
    """Find all wav files in directory and compose it in list of tuples with 'True' mark at target"""
    wav_list = find_wavs(directory)
    res_list = []

    for wav in wav_list:
        temp_list = [wav]

        if re.match(r'.*target1.*\.wav$', wav):
            temp_list.append(True)
        else:
            temp_list.append(False)

        res_list.append(tuple(temp_list))

    return res_list


# voices = wav_reader('raw_data_wav/')
# create_model(voices, 'model/_')
