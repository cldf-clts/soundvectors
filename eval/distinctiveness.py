from cltoolkit import Wordlist
from pyclts import CLTS
from pycldf import Dataset
from pathlib import Path
from soundvectors import SoundVectors
from collections import defaultdict
from tabulate import tabulate

DATA = "lexibank-analysed"

metadata_fn = "wordlist-metadata.json" if DATA == "lexibank-analysed" else "cldf-metadata.json"

data_dir = Path(__file__).parent / DATA
metadata_file = data_dir / "cldf" / metadata_fn

vec_to_sound_per_language = {}
sound_inventory_sizes = {}

bipa = CLTS().bipa
wl = Wordlist([Dataset.from_metadata(metadata_file)], ts=bipa)
sv = SoundVectors(ts=bipa)

err = set()

for language in wl.languages:
    language_name = language.id
    sound_inventory = language.sound_inventory.sounds
    errors_per_lang = 0  # number of sounds that can not be encoded, should only be '+' in this setting

    vec_to_sounds = defaultdict(list)

    for sound in sound_inventory:
        # normalize string representation of sound via CLTS
        try:
            sound_vec = sv.get_vec(sound.obj)
            if hasattr(sound.obj, "s"):
                vec_to_sounds[sound_vec].append(sound.obj.s)
            else:
                vec_to_sounds[sound_vec].append(sound.grapheme)
        except ValueError:
            errors_per_lang += 1

    sound_inventory_sizes[language_name] = len(sound_inventory) - errors_per_lang
    vec_to_sound_per_language[language_name] = vec_to_sounds

print(f"Invalid sounds: {err}")

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

for i in range(10):
    num_duplets += len(langs_per_duplet_num.get(i, []))
    table.append([i, num_duplets, f"{(num_duplets / len(vec_to_sound_per_language)):.3f}"])

print(f"Number of languages with at most <n> confused sounds (from {len(sound_inventory_sizes)} in total):")
print(tabulate(table))

table = []

for eq_class, langs in equivalence_classes_to_langs.items():
    table.append([" ".join(sorted(list(eq_class))), ", ".join(sorted(langs))])

table = sorted(table, key=lambda x: x[0])

print("Sounds with the same feature representation:")
print(tabulate(table))
