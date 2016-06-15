import math
import struct
import subprocess

# .wav header constants
SAMPLE_RATE = 8000 # Hz
SAMPLE_SIZE = 8 # Bits, or 1 Byte
NUM_CHANNELS = 1 # Mono
WAVE_FORMAT_PCM = 0x001
HEADERS_SIZE = 44 - 8 # Bytes
FORMAT_SIZE = 16 # Bits

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
} # Hz
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

# Generate a waveform 'w' of the notes in string 'n', each for a duration of 'd' milliseconds.
def generate_waveform(w, n, d):
  # Number of samples taken per note
  samples = int(SAMPLE_RATE * ( d / 1000))

  # Loop through the note-string and process each note
  for note in n:

    frequency = FREQUENCY[note]

    # Handle rests
    if frequency == 0:
      for t in range(int(samples)):
        yield 128
      continue

    # Get the wavelength of a note in samples
    wavelength = SAMPLE_RATE / frequency

    # Process each sample, using the wavelength to convert each back into time
    for t in range(int(samples)):
      if w == 'sine':
        point = math.sin(2 * math.pi * (t / wavelength))
      elif w == 'square':
        point = math.copysign(1, math.sin(2 * math.pi * (t / wavelength)))
      elif w == 'tri':
        point = ((t / wavelength) - 2 * math.floor(((t / wavelength) + 1) / 2)) * math.pow(-1, math.floor(((t / wavelength) + 1) / 2))
      elif w == 'saw':
        point = 2 * ((t / wavelength) - math.floor(t / wavelength)) - 1
      # Because the above assumes amplitude = 1, we recast to an unsigned integer
      yield round((point * 127) + 127)


# Open the output file for our waveform
with open('wavesout.wav', 'wb') as fileout:
  # Write one of each waveform shape to our output
  data = bytes(generate_waveform('sine', NOTE_STRING, NOTE_DURATION)) 
  data += bytes(generate_waveform('square', NOTE_STRING, NOTE_DURATION))
  data += bytes(generate_waveform('tri', NOTE_STRING, NOTE_DURATION))
  data += bytes(generate_waveform('saw', NOTE_STRING, NOTE_DURATION))

  headers = generate_header(len(data))
  fileout.write(headers)
  fileout.write(data)

fileout.close()
