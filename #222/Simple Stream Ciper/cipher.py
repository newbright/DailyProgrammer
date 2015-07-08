#------------------------------------------------------------
# Challenge #222: "Simple Stream Cipher"
# Difficulty: Intermediate
# July 8, 2015
# Brandon Newbright
#------------------------------------------------------------

# Generator to yield a sequence of pseudo-randomized numbers.
def lcg(x, a, c, m):
    while True:
        x = ((a * x) + c) % m
        yield x

# Uses 'Numerical Recipes' parameters for 'a' and 'c'; 'm' altered to adhere to utf-8 capabilities
def enc(msg, key):
    m = 2 ** 16
    a = 1664525
    c = 1013904223
    x = key
    enc_chars = []

    # Creates a new instance of the linear congruential generator. 
    cipher_stream = lcg(x, a, c, m)

    for ch in msg:
        enc_chars.append(chr(ord(ch) ^ next(cipher_stream)))

    return "".join(enc_chars)

# Because a new instance of the LCG will be made and will function identically to the one created in the encoding function, the decode "function" is identical in every way.
dec = enc


msg="Attack at dawn"
print("MESSAGE: ", msg)

enc_msg=enc(msg, 31337)
print("ENCODED: ", enc_msg)

dec_msg=dec(enc_msg, 31337)
print("DECODED: ", dec_msg)
