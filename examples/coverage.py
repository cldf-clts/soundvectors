from cltoolkit import Wordlist
from pyclts import CLTS
from pycldf import Dataset
from pathlib import Path
from clts2vec.parse import parse
from collections import defaultdict
from tabulate import tabulate

data_dir = Path(__file__).parent.parent / "resources" / "eval" / "lexibank-analysed"
metadata_file = data_dir / "cldf" / "wordlist-metadata.json"

vec_to_sound_per_language = {}
sound_inventory_sizes = {}

wl = Wordlist([Dataset.from_metadata(metadata_file)], ts=CLTS().bipa)

for language in wl.languages:
    language_name = language.id
    sound_inventory = language.sound_inventory.sounds
    sound_inventory_sizes[language_name] = len(sound_inventory)

    vec_to_sounds = defaultdict(list)

    for sound in sound_inventory:
        sound_vec = parse(sound.obj)
        vec_to_sounds[sound_vec].append(sound.grapheme)

    vec_to_sound_per_language[language_name] = vec_to_sounds

equivalence_classes_to_langs = defaultdict(list)

for lang, vec_to_sounds in vec_to_sound_per_language.items():
    for sounds in vec_to_sounds.values():
        if len(sounds) > 1:
            equivalence_classes_to_langs[frozenset(sounds)].append(lang)

duplets_per_lang = {}
langs_per_duplet_num = defaultdict(list)

for lang, size in sound_inventory_sizes.items():
    vec_to_sounds = vec_to_sound_per_language[lang]
    num_duplets = size - len(vec_to_sounds)
    duplets_per_lang[lang] = num_duplets
    langs_per_duplet_num[num_duplets].append(lang)

table = []
num_duplets = 0

for i in range(5):
    num_duplets += len(langs_per_duplet_num.get(i, []))
    table.append([i, num_duplets])

print(langs_per_duplet_num)
print(f"Number of languages with at most <n> confused sounds (from {len(sound_inventory_sizes)} in total):")
print(tabulate(table))

table = []

"""
for lang, vec_to_sounds in vec_to_sound_per_language.items():
    for sounds in vec_to_sounds.values():
        if len(sounds) > 1:
            table.append([lang, " ".join(sounds)])
"""

for eq_class, langs in equivalence_classes_to_langs.items():
    table.append([" ".join(sorted(list(eq_class))), ", ".join(sorted(langs))])

table = sorted(table, key=lambda x: x[0])

print("Sounds with the same feature representation:")
print(tabulate(table))
