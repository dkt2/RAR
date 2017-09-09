""" script to automated recording sounds based on a schedule"""
import wave
import time
import os
import pyaudio

PY_DRIVER = pyaudio.PyAudio()
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
# RATE = 44100
RATE = 10000
RECORD_SECONDS = 5
# RECORD_SECONDS = 60 # 1 min
# RECORD_SECONDS = 3600 # 1 hour
STREAM = PY_DRIVER.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

def get_curr_time():
    """ get current time formatted """
    return time.asctime(time.localtime(time.time()))

def get_curr_hour():
    """ get current hour """
    return time.localtime(time.time())[3]

def record():
    """ main recording routine """
    print("* RECORDING START")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = STREAM.read(CHUNK)
        frames.append(data)
    print("* RECORDING STOP")
    return frames

def save_recording(frames, filename):
    """ main recording saver routine """
    print("* RECORDING SAVING...")
    wave_form = wave.open("../recordings/{}".format(filename), 'wb')
    wave_form.setnchannels(CHANNELS)
    wave_form.setsampwidth(PY_DRIVER.get_sample_size(FORMAT))
    wave_form.setframerate(RATE)
    wave_form.writeframes(b''.join(frames))
    wave_form.close()
    print("* RECORDING SAVED")

def main():
    """ main """
    os.chdir(os.path.dirname(__file__))
    counter = 0
    loop = True
    while loop:
        filename = "{}.wav".format(get_curr_time())
        print()
        print("*** RECORDING CYCLE {} ***".format(counter))
        save_recording(record(), filename)
        print("*** RECORDING CYCLE {} ***".format(counter))
        counter += 1
    STREAM.stop_stream()
    STREAM.close()
    PY_DRIVER.terminate()

if __name__ == '__main__':
    main()
