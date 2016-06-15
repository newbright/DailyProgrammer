import math
import struct
import subprocess

# .wav header constants
SAMPLE_RATE = 8000 # Hz
SAMPLE_SIZE = 8 # Bits, or 1 Byte
NUM_CHANNELS = 1 # Mono
WAVE_FORMAT_PCM = 0x001
HEADERS_SIZE = 44 - 8
FORMAT_SIZE = 16

# Other constants
NOTE_DURATION = 300 # ms
FREQUENCY = {
  'A' : 440.00,
  'B' : 493.88,
  'C' : 523.25,
  'D' : 587.33,
  'E' : 659.25,
  'F' : 698.46,
  'G' : 783.99,
  '_' : 0
}
NOTE_STRING = "ABCDEFG_GFEDCBA_" # Note names, where '_' is a rest

# Generates the appropriate header for a .wav file
def generate_header(data_size):
  return struct.pack(
    '4si4s4sihhiihh4si',
    b'RIFF',
    HEADERS_SIZE + data_size,
    b'WAVE',
    b'fmt ',
    FORMAT_SIZE,
    WAVE_FORMAT_PCM,
    NUM_CHANNELS,
    SAMPLE_RATE,
    int(SAMPLE_RATE * SAMPLE_SIZE * NUM_CHANNELS / 8),
    int(SAMPLE_SIZE * NUM_CHANNELS / 8),
    SAMPLE_SIZE,
    b'data',
    data_size
  )    

# Generate a sine wave of the note 'n' for duration of 'd' milliseconds.
def sine(n, d, s):
  samples = int(SAMPLE_RATE * ( d / 1000))
  for note in n:
    frequency = FREQUENCY[note]
    if frequency == 0:
      for t in range(int(samples)):
        yield 128
      continue

    wavelength = SAMPLE_RATE / frequency

    for i in range(int(samples)):
      # We must recast 's' to the actual time, in seconds
      realtime = (i / SAMPLE_RATE)
      if s == 'sine':
        # Find the point on the sine graph with the real time
        point = math.sin(2 * math.pi * realtime * frequency)
      elif s == 'square':
        point = math.copysign(1, math.sin(2 * math.pi * realtime * frequency))
      elif s == 'tri':
        point = ((realtime * frequency) - 2 * math.floor(((realtime * frequency) + 1) / 2)) * math.pow(-1, math.floor(((realtime * frequency) + 1) / 2))
      elif s == 'saw':
        point = 2 * ((realtime * frequency) - math.floor(realtime * frequency)) - 1
      # Because the above assumes amplitude = 1, we recast to an unsigned integer
      yield round((point * 127) + 127)


# Open the output file for our waveform
with open('wavesout.wav', 'wb') as fileout:
  data = bytes(sine(NOTE_STRING, NOTE_DURATION, 'sine')) + bytes(sine(NOTE_STRING, NOTE_DURATION, 'square')) + bytes(sine(NOTE_STRING, NOTE_DURATION, 'tri')) + bytes(sine(NOTE_STRING, NOTE_DURATION, 'saw'))
  headers = generate_header(len(data))
  fileout.write(headers)
  fileout.write(data)

fileout.close()
