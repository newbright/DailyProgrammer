from math import sin, pi

# Given a sample rate 's', generate a sine wave of frequency 'f'
# for 'd' milliseconds.
def sine(f, s, d):
  wave = []
  samples = int(s / d)
  for t in range(samples):
    # We must recast 't' to the actual time, in seconds
    point = sin(2 * pi * (t / s))
    # Because the above assumes amplitude = 1, we recast to an unsigned integer
    wave.append(str((point * 127) + 127))
  return wave

# Sample rate, in Hz
s = 8000
# Note duration, in ms
d = 300
# Note string; A, B, C, D, E, F, G = notes & _ = rest
n = "ABCDEFG_GFEDCBA"

# We assign each note its respecive frequency in a dictionary
fdict = {
  'A' : 440.00,
  'B' : 493.88,
  'C' : 523.25,
  'D' : 587.33,
  'E' : 659.25,
  'F' : 698.46,
  'G' : 783.99,
  '_' : 0
}

# Open the output file for our waveform
fileout = open('wavesout.txt', 'w+')

for c in n:
  fileout.write('\n'.join(sine(fdict[c], s, d)))

fileout.close()
