from soundvectors import SoundVectors
from pyclts import CLTS

"""
A very simple example of how to work with this package.
"""

bipa = CLTS().bipa
sv = SoundVectors(ts=bipa)

# You can parse any valid IPA string to obtain a feature vector.
vec = sv.get_vec("t")
print(f"Parsed vector for [t]: \n{vec}\n\n")

# Instead of a string, you can also pass a CLTS Sound object.
t = bipa["t"]
vec2 = sv.get_vec(t)
print(f"Parsed vector for the CLTS Sound object derived from [t]: \n{vec}\n\n")

# The two obtained vectors are identical
print(f"Are the two obtained vectors identical?\n{vec == vec2}\n\n")

# Instead of a tuple, you can also retrieve the vector as a dictionary-like object (with the features as keys)
vec_obj = sv.get_vec("t", vectorize=False)
print(vec_obj)

# From such an object, you can cast to more readable feature strings or sets
vec_set = vec_obj.as_set()
print(f"Vector set for [t]: \n{vec_set}\n\n")
print(f"Vector string for [t]: \n{str(vec_obj)}\n\n")
