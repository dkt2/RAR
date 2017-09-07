""" script to automated recording sounds based on a schedule"""
import wave
import time
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
# RATE = 44100
RATE = 10000
# RECORD_SECONDS = 5
RECORD_SECONDS = 3600
WAVE_OUTPUT_FILENAME = ""
TIMEDATE = time.asctime(time.localtime(time.time()))
HOUR = time.localtime(time.time())[3]

PY_DRIVER = pyaudio.PyAudio()
STREAM = PY_DRIVER.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

for n in range(0, 24):
    WAVE_OUTPUT_FILENAME = "{}.wav".format(TIMEDATE)
    print("* recording cycle {}".format(n))
    print("* recording")
    FRAMES = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = STREAM.read(CHUNK)
        FRAMES.append(data)
    print("* done recording")
    print("* saving recording")
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(PY_DRIVER.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(FRAMES))
    wf.close()
    print("* done recording\n")

STREAM.stop_stream()
STREAM.close()
PY_DRIVER.terminate()
