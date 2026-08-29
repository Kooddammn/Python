import math_utils
from math_utils import square
from math_utils import add
from math_utils import subtract

#Task 1: Create a simple module (math_utils.py)
addResult = math_utils.add(4,7)
subtractResult = math_utils.subtract(7,2)
squareResult = math_utils.square(6)
print(addResult)
print(subtractResult)
print(squareResult)

print(square(4))
print(add(7,9))
print(subtract(5,2))

#Task 2: Create another module (string_utils.py)
import string_utils

print(string_utils.captilized_word("this is gen ai assignment 5-importing ,creating modules and packages"))
print(string_utils.reverse_string("this is gen ai assignment 5-importing ,creating modules and packages"))
print(string_utils.word_count("this is gen ai assignment 5-importing ,creating modules and packages"))



