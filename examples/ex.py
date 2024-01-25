from clts2vec.parse import parse, PATH_TO_CLTS
from clts2vec.utils import vec_to_str
from pyclts import CLTS

"""
A very simple example of how to work with this package.
"""

# You can parse any valid IPA string to obtain a feature vector.
vec = parse("t")
print(f"Parsed vector for [t]: \n{vec}\n\n")

# Instead of a string, you can also pass a CLTS Sound object.
bipa = CLTS(PATH_TO_CLTS).bipa
t = bipa["t"]
vec2 = parse(t)
print(f"Parsed vector for the CLTS Sound object derived from [t]: \n{vec}\n\n")

# The two obtained vectors are identical
print(f"Are the two obtained vectors identical?\n{vec == vec2}\n\n")

# To make the vector more readable, you can use the vec_to_str convenience method.
vec_str = vec_to_str(vec)
print(f"Vector string for [t]: \n{vec_str}\n\n")
