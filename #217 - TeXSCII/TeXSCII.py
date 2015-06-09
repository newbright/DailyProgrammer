#------------------------------------------------------------
# Challenge #217: "TeXSCII"
# Difficulty: Practical Exercise
# June 5, 2015
# Brandon Newbright
#------------------------------------------------------------


import re

expr_tokens = ['+', '-', '*', '/', '=', '(', ')']
latex_tokens = ['\\', '_', '^', 'sqrt', 'root', 'sub', 'sup', 'pi']

class Node:
	def __init__(self, value = None, children = []):
        self.value = value
        self.children = children

    def evaluate

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


def parse_to_expr(self, token_list):
	

	return Expr()

def tokenize(self, string):
	return re.split("([({+-/\\\*_^=})\n])", string)	


# symbols = [r'\frac', r'\root', r'\sqrt', r'\pi', r'_', r'^']

i = open("input.txt")
for line in i:
	parse_to_expr(tokenize(line))

