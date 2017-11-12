""" script to automated recording sounds based on a schedule"""
import wave
import time
import os
import pyaudio

DIR = "./recordings" # directory relative to record.py
RECORD_SECONDS = 60 # 1 min
# RECORD_SECONDS = 3600 # 1 hour

PY_DRIVER = pyaudio.PyAudio()
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
# RATE = 44100
RATE = 10000
STREAM = PY_DRIVER.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

def current_hour():
    """ get current time """
    return time.localtime(time.time())[3]

def time_blocks():
    """ returns an array of array containing user specified beginning and end time """
    return_me = None
    with open('./times.txt') as file:
        for line in file:
            return_me = [li.split('-') for li in line.split(',')]
    return return_me

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
    wave_form = wave.open("{}/{}".format(DIR, filename), 'wb')
    wave_form.setnchannels(CHANNELS)
    wave_form.setsampwidth(PY_DRIVER.get_sample_size(FORMAT))
    wave_form.setframerate(RATE)
    wave_form.writeframes(b''.join(frames))
    wave_form.close()
    print("* RECORDING SAVED")

def main():
    """ main """
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    cycle = 1
    begin_time = None
    end_time = None
    for duration in time_blocks():
        begin_time = duration[0]
        end_time = duration[1]

        while int(begin_time) <= int(current_hour()) and int(current_hour()) <= int(end_time):
            filename = "{}.wav".format(time.asctime())
            print()
            print("*** RECORDING CYCLE {} ***".format(cycle))
            save_recording(record(), filename)
            print("*** RECORDING CYCLE {} ***".format(cycle))
            cycle += 1
    STREAM.stop_stream()
    STREAM.close()
    PY_DRIVER.terminate()

if __name__ == '__main__':
    main()
