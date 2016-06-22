from PIL import Image

def fs_dither(fname):
  img = Image.open(fname).convert('L')
  pixel = img.load()
  w, h = img.size

  for y in range(h):
    for x in range(w):
      old = pixel[x, y]
      new = 0 if old < 127 else 255
      pixel[x, y] = new
      quant_error = old - new
      if x < w-1:
        pixel[x+1, y] += quant_error * 7 // 16
      if x > 0 and y < h-1:
        pixel[x-1, y+1] += quant_error * 3 // 16
      if y < h-1:
        pixel[x, y+1] += quant_error * 5 // 16
      if x < w-1 and y < h-1:
        pixel[x+1, y+1] += quant_error * 1 // 16
  img.save("output.png")
  img.show()

fs_dither("filein.png")
