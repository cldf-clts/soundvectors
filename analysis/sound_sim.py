import matplotlib.pyplot as plt
import numpy as np
from clts2vec.parse import parse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from seaborn import heatmap

# the 25 most common consonants and 20 most common vowels, according to phoible
core_consonants = ["p", "b", "m", "w", "f", "v", "t", "t̪", "d", "s", "z", "r", "ɾ", "l",
                   "n", "ʃ", "tʃ", "dʒ", "j", "ɲ", "k", "ɡ", "ŋ", "ʔ", "h"]
core_vowels = ["i", "iː", "ĩ", "ɪ", "e", "eː", "ɛ", "a", "aː", "ã",
               "ɨ", "ə", "u", "uː", "ũ", "ʊ", "o", "oː", "õ", "ɔ"]


def plot(func):
    def inner(*args):
        plt.cla()
        func(*args)
        plt.show()
    return inner


# preliminary test only on consonants
def chunk_parse(sounds):
    return [parse(s) for s in sounds]


@plot
def cos_similarity_heatmap(vectors, sounds):
    sim_matrix = cosine_similarity(vectors)
    heatmap(sim_matrix, xticklabels=sounds, yticklabels=sounds)


@plot
def plot_pca(vectors, sounds):
    pca = PCA(n_components=2)
    res = pca.fit_transform(vectors)
    plt.scatter(*np.swapaxes(res, 0, 1))
    for sound, coordinates in zip(sounds, res):
        plt.annotate(sound, coordinates)


@plot
def plot_tsne(vectors, sounds):
    tsne = TSNE(n_components=2, perplexity=5)
    res = tsne.fit_transform(np.array(vectors))
    plt.scatter(*np.swapaxes(res, 0, 1))
    for sound, coordinates in zip(sounds, res):
        plt.annotate(sound, coordinates)


if __name__ == "__main__":
    for sample in [core_vowels, core_consonants, core_vowels + core_consonants]:
        vecs = chunk_parse(sample)
        cos_similarity_heatmap(vecs, sample)
        plot_pca(vecs, sample)
        plot_tsne(vecs, sample)
