import math
import numpy as np
import shutil
import sounddevice as sd

g,l,h = 1000000,100,2000
dur   = 13

try:
    columns, _ = shutil.get_terminal_size()
except:
    columns = 80

# uncomment and get the loopback device id
# it tends not to change, so :shrug:
# print(sd.query_devices())

sr = sd.query_devices(8, 'input')['default_samplerate']
df = (h-l)/(columns-1)
fs = math.ceil(sr/df)
lb = math.floor(l/df)

def callback(indata, frames, time, status):
    if any(indata):
        mag = np.abs(np.fft.rfft(indata[:,0], n=fs))[lb:lb+columns]
        mag *= g/fs
        print(*mag, sep=' ', end='\n')

with sd.InputStream(device=8, channels=1, callback=callback,
                    blocksize=int(sr * dur / 1000),
                    samplerate=sr):
    while True:
        try:
            pass
        except KeyboardInterrupt:
            aweijf
