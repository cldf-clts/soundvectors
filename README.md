# SoundVectors

This lightweight Python package provides a robust tool for translating sounds into phonological feature vectors. It is described in detail in our study "A Generative System for Translating Sounds to Phonological Feature Vectors". If you use the package, we ask you kindly to cite this paper.

> Rubehn, Arne, Jessica Nieder, and Johann-Mattis List (2024): A Generative System for Translating Sounds to Phonological Feature Vectors. +++

## Installation

You can install clts2vec via `pip`.

```
pip install clts2vec
```

### Requirements for running the evaluation

If you wish to reproduce the evaluation from our paper, you require some additional dependencies that are not required by the core package. To install them, run:

```
$ pip install -e .[dev]
```

You also need to download the evaluation data from Lexibank. For this, simply run:

```
clts2vec$ make download
```

This will clone the [`lexibank-analysed`](https://github.com/lexibank/lexibank-analysed) dataset into the `eval` directory.

After running the evaluation scripts, you can clear the data from your disk by running the command:

```
clts2vec$ make clear
```

## Usage

The core of this package is the `parse` function, which translates a valid IPA symbol to its corresponding feature vector:

```python
>> > from soundvectors.parse import parse
>> > parse("t")
(1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0)
```

A more readable string representation of the feature vector can be obtained with the `vec_to_str` function:

```python
>> > from soundvectors.parse import parse
>> > from soundvectors.utils import vec_to_str
>> > vec_to_str(parse("t"))
'+cons,-syl,-son,-cont,-delrel,-lat,-nas,-voi,-sg,-cg,-pharyngeal,-laryngeal,+cor,-dorsal,-lab,-hi,-lo,-back,0_front,0_tense,-round,-velaric,-long,+ant,-distr,0_strid,0_hitone,0_hireg,0_loreg,0_rising,0_falling,0_contour,0_backshift,0_frontshift,0_opening,0_closing,0_centering,0_longdistance,0_secondrounded'
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
