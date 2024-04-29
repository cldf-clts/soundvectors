# SoundVectors

This lightweight Python package provides a robust tool for translating sounds into phonological feature vectors. It is described in detail in our study "A Generative System for Translating Sounds to Phonological Feature Vectors". If you use the package, we ask you kindly to cite this paper.

> Rubehn, Arne, Jessica Nieder, and Johann-Mattis List (2024): A Generative System for Translating Sounds to Phonological Feature Vectors. +++

## Installation

You can install the `soundvectors` package via `pip`.

```
pip install soundvectors
```

### Requirements for running the evaluation

If you wish to reproduce the evaluation from our paper, you require some additional dependencies that are not required by the core package. To install them, clone this repository and run:

```
$ pip install -e .[dev]
```

You also need to download the evaluation data from Lexibank. For this, `cd` into the `eval` directory and run:

```bash
soundvectors$ cd eval  # cd into eval directory
eval$ make download
```

This will clone the [`lexibank-analysed`](https://github.com/lexibank/lexibank-analysed) dataset into the `eval` directory.

After running the evaluation scripts, you can clear the data from your disk by running the command:

```bash
eval$ make clear
```

## Usage

The core of this package is the `SoundVectors` class, which translates valid IPA symbols to their corresponding feature vectors.
The recommended usage of `SoundVectors` is passing a callable transcription system via the keyword argument `ts`:

```python
>>> from soundvectors import SoundVectors
>>> from pyclts import CLTS
>>> bipa = CLTS().bipa
>>> sv = SoundVectors(ts=bipa)
>>> sv.get_vec("t")
(1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0)
```

Alternatively, the `get_vec` function can be called passing a `Sound` object (derived from `pyclts`), or a string describing the sound according to IPA conventions. The resulting vectors are the same:

```python
>>> sv.get_vec("voiceless alveolar stop consonant") == sv.get_vec("t") == sv.get_vec(bipa["t"])
True
```

Instead of obtaining a vector directly, the function can also return a dictionary-like `FeatureBundle` object. This object extends `OrderedDict` and offers some convenience methods for improving the readability of the generated feature vector:

```python
>>> feature_bundle = sv.get_vec("t", vectorize=False)  # set vectorize=False to return an object
>>> feature_bundle["cons"]  # feature values can be retrieved by indexing
1

>>> feature_bundle.as_set()  # represent feature bundle as set of non-zero feature strings
frozenset({'-son', '-distr', '-cont', '-lab', '-lo', '-long', '+front', '-laryngeal', '-syl', '-delrel', '-voi', '-round', '+cons', '-velaric', '-dorsal', '-back', '-nas', '-pharyngeal', '+ant', '+cor', '-cg', '-sg', '-lat', '-hi'})

>>> str(feature_bundle)  # string representation
'+cons,-syl,-son,-cont,-delrel,-lat,-nas,-voi,-sg,-cg,-pharyngeal,-laryngeal,+cor,-dorsal,-lab,-hi,-lo,-back,+front,0_tense,-round,-velaric,-long,+ant,-distr,0_strid,0_hitone,0_hireg,0_loreg,0_rising,0_falling,0_contour,0_backshift,0_frontshift,0_opening,0_closing,0_centering,0_longdistance,0_secondrounded'

>>> feature_bundle.as_vec()  # raw vector representation (equal to the return value with vectorize=True)
(1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0)
```

Finally, you can `__call__` the `SoundVectors` object to process a `Collection` of sounds:

```python
>> > sv(["s", "v"])
[(1, -1, -1, ..., 0),
 (1, -1, -1, ..., 0)]
```


## Evaluation

The `eval` directory provides the code that was used for the Evaluation section in the paper. If you wish to reproduce our results reported in the paper, make sure that you have installed the dependencies and downloaded the data (see above). Then, you can simply run all evaluation scripts - with each file corresponding to a subsection of the paper with the same name:

```bash
$ cd eval
$ python vector_similarities.py  # 4.1 & 4.2
$ python equivalence_classes.py  # 4.3
$ python distinctiveness.py  # 4.4
$ python concordanceline.py  # 4.4
```
