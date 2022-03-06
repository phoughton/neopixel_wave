import machine
from ws2812 import WS2812
import random
import time

ws = WS2812(machine.Pin(0),8)

frame_gap = 1/20
max_intensity=255

gamma = [
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
    1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
    2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
    5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
   10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
   17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
   25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
   37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
   51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
   69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
   90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
  115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
  144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
  177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
  215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255]


def light(light_values):
    index=0
    for intensity in light_values:
        ws[index] = [gamma[intensity], gamma[0], gamma[0]]
        index += 1
    ws.write()

def waveform(size):
    background=[0 for c in range(size+1)]
    wave_pattern=[]
    
    half_way = int(size/2)+1
    for proportion in range(0, half_way+1):
        prop = proportion/half_way
        wave_pattern.append(int(prop*max_intensity))
    
    return background + wave_pattern + list(reversed(wave_pattern)) + background

size = 8
wave = waveform(size)

print(wave)
while True:
    for index in range(len(wave)):
        time.sleep(frame_gap)
        light(wave[index:index+size])
    
    for index in range(len(wave)-size, 0 , -1):
        time.sleep(frame_gap)
        light(wave[index:index+size])                  

    
