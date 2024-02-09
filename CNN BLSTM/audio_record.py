import pyaudio
import wave


def voice_recorder(output_filename, seconds_of_audio):
    """Record a voice of target within PyAudio interface with device(7) - USB MICRO"""

    chunk = 2024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2  # Stereo
    fs = 44100  # Record at 44100 samples per second

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    input_device_index=7,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds_of_audio)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    print('stream stopped')
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    return None


"""Example of using voice_recorder function"""
# file_sec_duration = 7
# filename = "target2check.wav"
# voice_recorder("target.wav", 7)
