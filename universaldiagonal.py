"""universal uquation for the diagonals in the pascal's triangle
"""

import math

diagonal = input("What diagonal do you want to see?")
term = input("What term do you want to see?")

product= term
for i in range (term, term + (diagonal - 2)+1):
	product = (math.factorial(term + diagonal-2)/ (math.factorial(diagonal-1)*math.factorial(term-1)))
print product