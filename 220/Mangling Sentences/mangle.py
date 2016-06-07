#------------------------------------------------------------
# Challenge #220: "Mangling Sentences"
# Difficulty: Easy
# June 22, 2015
# Brandon Newbright
#------------------------------------------------------------

def mangle(word):

	punctuation = ",.'-"

	# Creates a set of the indeces 'i' of the punctuation characters in the word
	punctuation_indeces = [(i, c) for i, c in enumerate(word) if c in punctuation]

	# Creates a set of the indeces 'i' of the capital characters in the word
	capital_indeces = [i for i, c in enumerate(word) if c.isupper()]

	for c in punctuation:
		word = word.replace(c, "")

	word = sorted(word.lower())

	for i, c in punctuation_indeces:
		word.insert(i, c)

	for i in range(len(word)):
		if i in capital_indeces:
			word[i] = word[i].upper()

	mangled = "".join(word)

	return mangled

def parse_sentence(sentence):
	parsed = []
	for word in sentence.split():
		parsed.append(mangle(word))

	print("Output : {}".format(" ".join(parsed)))

sentences = open('input.txt','r')

for line in sentences.readlines():
	print("Input : {}".format(line))
	parse_sentence(line)
	print()