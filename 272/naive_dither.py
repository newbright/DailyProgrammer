from math import floor
import struct

def read_pbm(fname):
  with open(fname) as f:
    data = [s for s in f if not s.startswith('#')]
  magic_number = data.pop(0)
  dimensions = [int(d) for d in data.pop(0).split()]
  pixels = []
  max_value = int(data.pop(0))
  for y in range(dimensions[1]):
    rowlist = data.pop(0).rstrip().split()
    row = []
    for x in range(dimensions[0]):
      cell = []
      for b in range(3):
        cell.append(int(rowlist.pop(0)))
      row.append(cell)
    pixels.append(row)
  return(pixels)

def fs_dither(dim, img):
  # img as list of lists of tuples of byte(s)
  pixel = img
  for y, row in enumerate(pixel):
    print(y)
    for x, cell in enumerate(row):
      old = pixel[y][x]
      new = grayscale(old)
      pixel[y][x] = new
      if x < dim[0] - 1 and y < dim[1] - 1:
        for b in range(3):
          quant_error = old[b] - new[b]
          pixel[y][x+1][b] += floor(quant_error * 7/16)
          pixel[y+1][x-1][b] += floor(quant_error * 3/16)
          pixel[y+1][x][b] += floor(quant_error * 5/16)
          pixel[y+1][x+1][b] += floor(quant_error * 1/16)
    print(row)
  print(pixel)


def grayscale(pixel):
  # Uses GIMP 'Luminosity' algorithm: 0.21R + 0.72G + 0.07B
  r = floor(0.21*pixel[0])
  g = floor(0.72*pixel[1])
  b = floor(0.07*pixel[2])
  return [r,g,b]

fs_dither([4,4], read_pbm("test.ppm"))
