import matplotlib.pyplot as plt
from clts2vec.parse import parse
from sklearn.metrics.pairwise import cosine_similarity
from seaborn import heatmap

# the 25 most common consonants and vowels, according to phoible
core_consonants = ["p", "b", "m", "w", "f", "v", "t", "t̪", "d", "s", "z", "r", "ɾ", "l",
                   "n", "ʃ", "tʃ", "dʒ", "j", "ɲ", "k", "ɡ", "ŋ", "ʔ", "h"]
core_vowels = ["i", "iː", "ĩ", "ɪ", "e", "eː", "ɛ", "a", "aː", "ã",
               "ɨ", "ə", "u", "uː", "ũ", "ʊ", "o", "oː", "õ", "ɔ"]

# preliminary test only on consonants
sim_matrix = cosine_similarity([parse(s) for s in core_vowels])
heatmap(sim_matrix, xticklabels=core_vowels, yticklabels=core_vowels)
plt.show()

# TODO implement PCA plot
