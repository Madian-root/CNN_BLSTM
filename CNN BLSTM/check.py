import librosa as lr
import numpy as np

from keras.models import load_model

SR = 16000  # Sampling Rate
LENGTH = 16  # Amount of blocks for 1 walkthrough
OVERLAP = 8  # Step between samples in amount of blocks
FFT = 1024  # Length of block (64ms)


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
    apsums = np.array(apsums > 0.1, dtype=bool)
    # Extend the blocks every on 125ms
    # before separated samples (2048 at block)
    apsums = np.repeat(apsums, np.ceil(len(audio) / len(apsums)))[:len(audio)]
    # print(apsums)

    return audio[apsums]


def prepare_audio(a_name):
    """audio tokenizer for further neuron model using"""

    # Upload and preparing data sets
    print('loading %s' % a_name)
    audio, _ = lr.load(a_name, sr=SR)
    audio = filter_audio(audio)  # Removing silence and spaces between words
    data = lr.stft(audio, n_fft=FFT).swapaxes(0, 1)  # Export spectrogram
    samples = []

    for i in range(0, len(data) - LENGTH, OVERLAP):
        samples.append(np.abs(data[i:i + LENGTH]))  # Create training sample

    return np.array(samples)


def check_access(target_path, mod_path):
    """check access status of target with pre-trained model"""
    # load model
    model = load_model(mod_path + 'model.hdf5')

    # tokenize target audio
    new_audio = prepare_audio(target_path)

    # use model to predict
    prediction = model.predict(new_audio)
    val_sum = 0
    for val in prediction:
        val_sum += val[0]
    # print(prediction)  # array of similarity in weight of neural network
    print('%.3f' % (100 * (val_sum / len(prediction))) + '%')  # percent of target similarity to owner
    if (val_sum / len(prediction)) * 100 > 85.0:
        print('access is allowed')
        return True
    else:
        print('access is denied')
        return False


# target_to_check = 'audio_to_check/vlad.wav'
# check_access(target_to_check, 'model/')
