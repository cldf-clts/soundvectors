"""
soundvectors: Vectorize Speech Sounds in Phonetic Transcription.
"""
import typing
import warnings
import dataclasses

__version__ = "1.0.dev0"

COMPLEX_SOUNDS = {
    'diphthong': 'vowel',
    'cluster': 'consonant',
}


class Sound(typing.Protocol):  # Sound objects are expected to have a name attribute.
    name: str


@dataclasses.dataclass(frozen=True, order=True)  # Make instances immutable and orderable.
class FeatureBundle:
    cons: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    syl: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    son: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    cont: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    delrel: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    lat: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    nas: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    voi: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    sg: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    cg: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    pharyngeal: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    laryngeal: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    cor: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    dorsal: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    lab: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    hi: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    lo: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    back: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    front: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    tense: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    round: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    velaric: int = dataclasses.field(default=0, metadata={'dc:description': 'Mortensen et al. (2016)'})
    long: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    ant: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    distr: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    strid: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    hitone: int = dataclasses.field(default=0, metadata={'dc:description': 'Mortensen et al. (2016)'})
    hireg: int = dataclasses.field(default=0, metadata={'dc:description': 'Mortensen et al. (2016)'})
    loreg: int = dataclasses.field(default=0, metadata={'dc:description': 'Supplements hireg'})
    rising: int = dataclasses.field(default=0, metadata={'dc:description': 'CLTS tone representation'})
    falling: int = dataclasses.field(default=0, metadata={'dc:description': 'CLTS tone representation'})
    contour: int = dataclasses.field(default=0, metadata={'dc:description': 'CLTS tone representation'})
    backshift: int = dataclasses.field(default=0, metadata={'dc:description': 'Rubehn 2022'})
    frontshift: int = dataclasses.field(default=0, metadata={'dc:description': 'Rubehn 2022'})
    opening: int = dataclasses.field(default=0, metadata={'dc:description': 'Rubehn 2022'})
    closing: int = dataclasses.field(default=0, metadata={'dc:description': 'Rubehn 2022'})
    centering: int = dataclasses.field(default=0, metadata={'dc:description': 'Rubehn 2022'})
    longdistance: int = dataclasses.field(default=0, metadata={'dc:description': 'Rubehn 2022'})
    secondrounded: int = dataclasses.field(default=0, metadata={'dc:description': 'Rubehn 2022'})

    def __post_init__(self):
        assert all(v in {0, 1, -1} for v in dataclasses.astuple(self))

    @classmethod
    def from_positive_and_negative(cls, pos: list, neg: list):
        """
        Factory method to allow for transparent instantiation.
        """
        assert not set(pos).intersection(neg)
        return cls(**{k: 1 if k in pos else -1 for k in pos + neg})

    def as_vector(self) -> typing.Tuple[int]:
        return dataclasses.astuple(self)

    def as_dict(self,
                valid_values: typing.Optional[typing.Union[typing.Container, typing.Iterable]]
                = None) -> typing.Dict[str, int]:
        """
        Returns a `dict` keyed with the fields of the FeatureBundle, filtered to values in
        `valid_values`.
        """
        return {
            k: v for k, v in dataclasses.asdict(self).items()
            if valid_values is None or (v in valid_values)}

    def as_set(self) -> frozenset:
        """
        The set of applicable features and their values.
        """
        return frozenset(
            {'{}{}'.format('+' if v > 0 else '-', k) for k, v in self.as_dict({1, -1}).items()})

    def __str__(self):
        return ','.join(
            '{}{}'.format('+' if v > 0 else ('-' if v < 0 else '0_'), k)
            for k, v in self.as_dict().items())

    def replace(self, **changes):
        """
        Shortcut for `dataclasses.replace`.
        """
        return dataclasses.replace(self, **changes)

    @classmethod
    def fields(cls):
        """
        Shortcut for `dataclasses.fields`.
        """
        return dataclasses.fields(cls)


clts_feature_hierarchy = [  # CLTS feature domains ordered from least to most specific.
    "type",
    "manner",
    "height",
    "roundedness",
    "centrality",
    "place",
    "phonation",
]

clts_features = {
    "type": {
        "consonant": FeatureBundle.from_positive_and_negative(
            ['cons'],
            ['syl', 'son', 'cont', 'delrel', 'lat', 'nas', 'voi', 'sg', 'cg', 'pharyngeal',
             'laryngeal', 'cor', 'dorsal', 'lab', 'hi', 'lo', 'back', 'front', 'round',
             'velaric', 'long']),
        "vowel": FeatureBundle.from_positive_and_negative(
            ["syl", "son", "cont", "voi"],
            ["cons", "lat", "nas", "sg", "cg", "pharyngeal", "laryngeal", "hi", "lo",
             "back", "front", "tense", "round", "velaric", "long"]),
        "tone": FeatureBundle.from_positive_and_negative(
            [],
            ["hitone", "hireg", "loreg", "rising", "falling", "contour"]),
        "diphthong": FeatureBundle.from_positive_and_negative(
            [],
            ["backshift", "frontshift", "opening", "closing", "centering", "longdistance",
             "secondrounded"]),
    },
    "aspiration": {
        "aspirated": FeatureBundle.from_positive_and_negative(
            ["sg"], []),
    },
    "creakiness": {
        "creaky": FeatureBundle.from_positive_and_negative(
            ["cg"], []),
    },
    "release": {
        "unreleased": FeatureBundle.from_positive_and_negative(
            [], []),
        "with-lateral-release": FeatureBundle.from_positive_and_negative(
            ["lat"], []),
        "with-mid-central-vowel-release":
            FeatureBundle.from_positive_and_negative([], []),
        "with-nasal-release": FeatureBundle.from_positive_and_negative(
            ["nas"], []),
    },
    "ejection": {
        "ejective": FeatureBundle.from_positive_and_negative(["cg"], []),
    },
    "place": {
        "alveolar": FeatureBundle.from_positive_and_negative(["cor", "ant", "front"], ["distr"]),
        "alveolo-palatal": FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "distr", "front"], ["ant"]),
        "bilabial": FeatureBundle.from_positive_and_negative(["lab", "front"], []),
        "dental": FeatureBundle.from_positive_and_negative(["cor", "ant", "distr", "front"], []),
        "epiglottal": FeatureBundle.from_positive_and_negative(["lo"], []),
        "glottal": FeatureBundle.from_positive_and_negative(["laryngeal", "lo"], []),
        "labial": FeatureBundle.from_positive_and_negative(["lab", "front"], []),
        "linguolabial": FeatureBundle.from_positive_and_negative(
            ["cor", "lab", "ant", "front"], ["distr"]),
        "labio-palatal": FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "round", "distr", "front"], ["ant"]),
        "labio-velar": FeatureBundle.from_positive_and_negative(
            ["dorsal", "hi", "back", "round", "front"], []),
        "labio-dental": FeatureBundle.from_positive_and_negative(["lab", "front"], []),
        "palatal": FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "distr"], ["ant"]),
        "palatal-velar": FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "back", "distr"], ["ant"]),
        "pharyngeal": FeatureBundle.from_positive_and_negative(["pharyngeal", "lo", "back"], []),
        "post-alveolar": FeatureBundle.from_positive_and_negative(
            ["cor", "distr", "front"], ["ant"]),
        "retroflex": FeatureBundle.from_positive_and_negative(["cor"], ["ant", "distr"]),
        "uvular": FeatureBundle.from_positive_and_negative(["dorsal", "lo", "back"], []),
        "velar": FeatureBundle.from_positive_and_negative(["dorsal", "hi", "back"], []),
    },
    "pharyngealization": {
        "pharyngealized": FeatureBundle.from_positive_and_negative(["pharyngeal"], []),
    },
    "voicing": {
        "devoiced": FeatureBundle.from_positive_and_negative([], ["voi"]),
        "revoiced": FeatureBundle.from_positive_and_negative(["voi"], []),
    },
    "nasalization": {
        "nasalized": FeatureBundle.from_positive_and_negative(["nas"], []),
    },
    "preceding": {
        "pre-aspirated": FeatureBundle.from_positive_and_negative(["sg"], []),
        "pre-breathy-aspirated": FeatureBundle.from_positive_and_negative(["sg"], []),
        "pre-glottalized": FeatureBundle.from_positive_and_negative(["cg", "lo"], []),
        "pre-labialized": FeatureBundle.from_positive_and_negative(["dorsal", "hi", "round"], []),
        "pre-nasalized": FeatureBundle.from_positive_and_negative(["nas"], []),
        "pre-palatalized": FeatureBundle.from_positive_and_negative(["cor", "dorsal", "hi"], []),
    },
    "labialization": {
        "labialized": FeatureBundle.from_positive_and_negative(
            ["dorsal", "hi", "back", "round"], []),
    },
    "syllabicity": {
        "syllabic": FeatureBundle.from_positive_and_negative(["syl"], []),
        "non-syllabic": FeatureBundle.from_positive_and_negative([], ["syl"]),
    },
    "palatalization": {
        "labio-palatalized": FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "round"], []),
        "palatalized": FeatureBundle.from_positive_and_negative(["cor", "dorsal", "hi"], []),
    },
    "phonation": {
        "voiced": FeatureBundle.from_positive_and_negative(["voi"], []),
        "voiceless": FeatureBundle.from_positive_and_negative([], ["voi"]),
    },
    "duration": {
        "long": FeatureBundle.from_positive_and_negative(["long"], []),
        "mid-long": FeatureBundle.from_positive_and_negative(["long"], []),
        "ultra-long": FeatureBundle.from_positive_and_negative(["long"], []),
        "ultra-short": FeatureBundle.from_positive_and_negative([], ["long"]),
    },
    "stress": {
        "primary-stress": FeatureBundle.from_positive_and_negative([], []),
        "secondary-stress": FeatureBundle.from_positive_and_negative([], []),
    },
    "airstream": {
        "lateral": FeatureBundle.from_positive_and_negative(["cons", "lat"], []),
        "sibilant": FeatureBundle.from_positive_and_negative([], []),
    },
    "velarization": {
        "velarized": FeatureBundle.from_positive_and_negative(["dorsal", "hi", "back"], []),
    },
    "manner": {
        "affricate": FeatureBundle.from_positive_and_negative(["delrel"], ["strid"]),
        "approximant": FeatureBundle.from_positive_and_negative(["son", "cont"], ["cons"]),
        "click": FeatureBundle.from_positive_and_negative(["velaric"], []),
        "fricative": FeatureBundle.from_positive_and_negative(["cont"], ["strid"]),
        "implosive": FeatureBundle.from_positive_and_negative(["cg"], []),
        "nasal": FeatureBundle.from_positive_and_negative(["son", "nas"], []),
        "nasal-click": FeatureBundle.from_positive_and_negative(["nas", "velaric"], []),
        "stop": FeatureBundle.from_positive_and_negative([], ["son", "cont"]),
        "tap": FeatureBundle.from_positive_and_negative(["son"], ["cont"]),
        "trill": FeatureBundle.from_positive_and_negative(["son", "cont"], []),
    },
    "laminality": {
        "apical": FeatureBundle.from_positive_and_negative([], ["distr"]),
        "laminal": FeatureBundle.from_positive_and_negative(["distr"], []),
    },
    "articulation": {
        "strong": FeatureBundle.from_positive_and_negative(["tense"], []),
    },
    "breathiness": {
        "breathy": FeatureBundle.from_positive_and_negative(["sg"], []),
    },
    "glottalization": {
        "glottalized": FeatureBundle.from_positive_and_negative(["cg"], []),
    },
    "raising": {
        "lowered": FeatureBundle.from_positive_and_negative(["lo"], []),
        "raised": FeatureBundle.from_positive_and_negative(["hi"], []),
    },
    "relative_articulation": {
        "centralized": FeatureBundle.from_positive_and_negative([], []),
        "mid-centralized": FeatureBundle.from_positive_and_negative([], []),
        "advanced": FeatureBundle.from_positive_and_negative([], []),
        "retracted": FeatureBundle.from_positive_and_negative([], []),
    },
    "centrality": {
        "back": FeatureBundle.from_positive_and_negative(["back"], []),
        "central": FeatureBundle.from_positive_and_negative([], []),
        "front": FeatureBundle.from_positive_and_negative(["front"], []),
        "near-back": FeatureBundle.from_positive_and_negative(["back"], []),
        "near-front": FeatureBundle.from_positive_and_negative(["front"], []),
    },
    "rhotacization": {
        "rhotacized": FeatureBundle.from_positive_and_negative([], []),
    },
    "height": {
        "close": FeatureBundle.from_positive_and_negative(["hi", "tense"], []),
        "close-mid": FeatureBundle.from_positive_and_negative(["tense"], []),
        "mid": FeatureBundle.from_positive_and_negative([], []),
        "near-close": FeatureBundle.from_positive_and_negative(["hi"], []),
        "near-open": FeatureBundle.from_positive_and_negative(["lo"], []),
        "open": FeatureBundle.from_positive_and_negative(["lo", "tense"], []),
        "open-mid": FeatureBundle.from_positive_and_negative([], []),
    },
    "friction": {
        "with-friction": FeatureBundle.from_positive_and_negative([], ["son"]),
    },
    "roundedness": {
        "rounded": FeatureBundle.from_positive_and_negative(["round"], []),
        "unrounded": FeatureBundle.from_positive_and_negative([], ["round"]),
    },
    "rounding": {
        "less-rounded": FeatureBundle.from_positive_and_negative(["round"], []),
        "more-rounded": FeatureBundle.from_positive_and_negative(["round"], []),
    },
    "start": {
        "from-high": FeatureBundle.from_positive_and_negative(["hireg", "hitone"], []),
        "from-low": FeatureBundle.from_positive_and_negative(["loreg"], []),
        "from-mid": FeatureBundle.from_positive_and_negative([], []),
        "from-mid-high": FeatureBundle.from_positive_and_negative(["hireg"], []),
        "from-mid-low": FeatureBundle.from_positive_and_negative(["loreg", "hitone"], []),
    },
    "contour": {
        "contour": FeatureBundle.from_positive_and_negative(["contour"], []),
        "falling": FeatureBundle.from_positive_and_negative(["falling"], []),
        "rising": FeatureBundle.from_positive_and_negative(["rising"], []),
        "flat": FeatureBundle.from_positive_and_negative([], []),
        "short": FeatureBundle.from_positive_and_negative([], []),
    },
    "to_roundedness": {
        "to_rounded": FeatureBundle.from_positive_and_negative(["secondrounded"], []),
        "to_unrounded": FeatureBundle.from_positive_and_negative([], ["secondrounded"]),
    }
}

clts_feature_values = {}

for domain, value_dict in clts_features.items():
    for value, feature_dict in value_dict.items():
        clts_feature_values[value] = {"features": feature_dict, "domain": domain}

joint_feature_definitions = {
    ("glottal", "stop"): FeatureBundle(cg=1),
    ("affricate", "alveolar"): FeatureBundle(strid=1),
    ("affricate", "labio-dental"): FeatureBundle(strid=1),
    ("affricate", "post-alveolar"): FeatureBundle(strid=1),
    ("affricate", "uvular"): FeatureBundle(strid=1),
    ("fricative", "alveolar"): FeatureBundle(strid=1),
    ("fricative", "labio-dental"): FeatureBundle(strid=1),
    ("fricative", "post-alveolar"): FeatureBundle(strid=1),
    ("fricative", "uvular"): FeatureBundle(strid=1),
    ("contour", "from-high", "via-mid-high"): FeatureBundle(falling=1),
    ("contour", "from-high", "via-mid"): FeatureBundle(falling=1),
    ("contour", "from-high", "via-mid-low"): FeatureBundle(falling=1),
    ("contour", "from-high", "via-low"): FeatureBundle(falling=1),
    ("contour", "from-mid-high", "via-high"): FeatureBundle(rising=1),
    ("contour", "from-mid-high", "via-mid"): FeatureBundle(falling=1),
    ("contour", "from-mid-high", "via-mid-low"): FeatureBundle(falling=1),
    ("contour", "from-mid-high", "via-low"): FeatureBundle(falling=1),
    ("contour", "from-mid", "via-high"): FeatureBundle(rising=1),
    ("contour", "from-mid", "via-mid-high"): FeatureBundle(rising=1),
    ("contour", "from-mid", "via-mid-low"): FeatureBundle(falling=1),
    ("contour", "from-mid", "via-low"): FeatureBundle(falling=1),
    ("contour", "from-mid-low", "via-high"): FeatureBundle(rising=1),
    ("contour", "from-mid-low", "via-mid-high"): FeatureBundle(rising=1),
    ("contour", "from-mid-low", "via-mid"): FeatureBundle(rising=1),
    ("contour", "from-mid-low", "via-low"): FeatureBundle(falling=1),
    ("contour", "from-low", "via-high"): FeatureBundle(rising=1),
    ("contour", "from-low", "via-mid-high"): FeatureBundle(rising=1),
    ("contour", "from-low", "via-mid"): FeatureBundle(rising=1),
    ("contour", "from-low", "via-mid-low"): FeatureBundle(rising=1),
    ("from_front", "to_near-front"): FeatureBundle(backshift=1),
    ("from_near-front", "to_front"): FeatureBundle(frontshift=1),
    ("from_front", "to_central"): FeatureBundle(backshift=1),
    ("from_central", "to_front"): FeatureBundle(frontshift=1),
    ("from_front", "to_near-back"): FeatureBundle(backshift=1),
    ("from_near-back", "to_front"): FeatureBundle(frontshift=1),
    ("from_front", "to_back"): FeatureBundle(backshift=1),
    ("from_back", "to_front"): FeatureBundle(frontshift=1),
    ("from_near-front", "to_central"): FeatureBundle(backshift=1),
    ("from_central", "to_near-front"): FeatureBundle(frontshift=1),
    ("from_near-front", "to_near-back"): FeatureBundle(backshift=1),
    ("from_near-back", "to_near-front"): FeatureBundle(frontshift=1),
    ("from_near-front", "to_back"): FeatureBundle(backshift=1),
    ("from_back", "to_near-front"): FeatureBundle(frontshift=1),
    ("from_central", "to_near-back"): FeatureBundle(backshift=1),
    ("from_near-back", "to_central"): FeatureBundle(frontshift=1),
    ("from_central", "to_back"): FeatureBundle(backshift=1),
    ("from_back", "to_central"): FeatureBundle(frontshift=1),
    ("from_near-back", "to_back"): FeatureBundle(backshift=1),
    ("from_back", "to_near-back"): FeatureBundle(frontshift=1),
    ("from_close", "to_close-mid"): FeatureBundle(opening=1, centering=1),
    ("from_close-mid", "to_close"): FeatureBundle(closing=1),
    ("from_close", "to_mid"): FeatureBundle(opening=1),
    ("from_mid", "to_close"): FeatureBundle(closing=1),
    ("from_close", "to_open-mid"): FeatureBundle(opening=1),
    ("from_open-mid", "to_close"): FeatureBundle(closing=1, longdistance=1),
    ("from_close", "to_near-open"): FeatureBundle(opening=1, centering=1, longdistance=1),
    ("from_near-open", "to_close"): FeatureBundle(closing=1, longdistance=1),
    ("from_close", "to_open"): FeatureBundle(opening=1, longdistance=1),
    ("from_open", "to_close"): FeatureBundle(closing=1, longdistance=1),
    ("from_near-close", "to_mid"): FeatureBundle(opening=1),
    ("from_mid", "to_near-close"): FeatureBundle(closing=1, centering=1),
    ("from_near-close", "to_open-mid"): FeatureBundle(opening=1),
    ("from_open-mid", "to_near-close"): FeatureBundle(closing=1, centering=1),
    ("from_near-close", "to_near-open"): FeatureBundle(opening=1, centering=1),
    ("from_near-open", "to_near-close"): FeatureBundle(closing=1, centering=1),
    ("from_near-close", "to_open"): FeatureBundle(opening=1, longdistance=1),
    ("from_open", "to_near-close"): FeatureBundle(closing=1, centering=1, longdistance=1),
    ("from_close-mid", "to_open-mid"): FeatureBundle(opening=1),
    ("from_open-mid", "to_close-mid"): FeatureBundle(closing=1),
    ("from_close-mid", "to_near-open"): FeatureBundle(opening=1, centering=1),
    ("from_near-open", "to_close-mid"): FeatureBundle(closing=1),
    ("from_close-mid", "to_open"): FeatureBundle(opening=1, longdistance=1),
    ("from_open", "to_close-mid"): FeatureBundle(closing=1),
    ("from_mid", "to_near-open"): FeatureBundle(opening=1, centering=1),
    ("from_near-open", "to_mid"): FeatureBundle(closing=1),
    ("from_mid", "to_open"): FeatureBundle(opening=1),
    ("from_open", "to_mid"): FeatureBundle(closing=1),
    ("from_open-mid", "to_open"): FeatureBundle(opening=1),
    ("from_open", "to_open-mid"): FeatureBundle(closing=1, centering=1),
    ("from_close", "to_near-close"): FeatureBundle(centering=1),
    ("from_close-mid", "to_near-close"): FeatureBundle(centering=1),
    ("from_open-mid", "to_near-open"): FeatureBundle(centering=1),
    ("from_open", "to_near-open"): FeatureBundle(centering=1),
    ("to_mid", "to_central"): FeatureBundle(centering=1),
    ("to_close-mid", "to_central"): FeatureBundle(centering=1),
    ("to_open-mid", "to_central"): FeatureBundle(centering=1),
    ("from_near-close", "to_close-mid"): FeatureBundle(centering=1),
    ("from_near-open", "to_open-mid"): FeatureBundle(centering=1),
}


def is_valid_sound(sound: typing.Any) -> bool:
    """
    Check if sound corresponds to our expectations.

    @note: We expect a string à la "voiced bilabial stop consonant"
    """
    return bool(sound and  # noqa: W504
                isinstance(sound, str) and  # noqa: W504
                sound.split()[-1] in {'consonant', 'vowel', 'tone', 'diphthong', 'cluster'})


class SoundVectors:
    """
    Handles vectorization of sounds represented by features.

    Examples::
        >>> import soundvectors
        >>> c2v = soundvectors.SoundVectors()
        >>> c2v
    """

    feature_values = clts_feature_values
    joint_defs = joint_feature_definitions
    feature_hierarchy = clts_feature_hierarchy
    ts = None

    def __init__(
            self,
            ts=None,
            feature_values=None,
            feature_hierarchy=None,
            joint_defs=None
    ):

        self.ts = ts
        self.feature_values = feature_values or self.feature_values
        self.joint_defs = joint_defs or self.joint_defs
        self.feature_hierarchy = feature_hierarchy or self.feature_hierarchy

    def clts_compatibility(self, clts):
        """
        Check compatibility with a particular CLTS release
        """
        import json
        clts_features = json.loads(
            clts.transcriptionsystems_dir.joinpath('features.json').read_text(encoding='utf8'))
        for k, d in self.feature_values.items():
            if d['domain'] not in ['type', 'to_roundedness']:
                # Make sure, k appears as feature for the domain for at least one type in CLTS:
                for dd in clts_features.values():
                    if d['domain'] in dd and (k in dd[d['domain']]):
                        break
                else:
                    raise AssertionError('{}: {}'.format(d['domain'], k))

    def __call__(self, sounds, vectorize=True):
        vectors = []

        for sound in sounds:
            try:
                vectors.append(self.get_vec(sound, vectorize=vectorize))
            except ValueError:
                warnings.warn(
                    f"Invalid sound encountered: [{sound}]. Returned feature vector is `None`")
                vectors.append(None)

        return vectors

    def validate(self, sound):
        """
        Try to retrieve the sound name from CLTS or `linse`.
        """
        if is_valid_sound(sound):
            return sound
        if sound and hasattr(sound, "name"):
            if is_valid_sound(sound.name):
                return sound.name
        elif sound and self.ts:
            sound_transcribed = self.ts([sound])[0]
            if is_valid_sound(sound_transcribed):
                return sound_transcribed
            if hasattr(sound_transcribed, "name"):
                if is_valid_sound(sound_transcribed.name):
                    return sound_transcribed.name
        raise ValueError("Invalid sound encountered.")

    def __getitem__(self, sound: typing.Union[str, Sound]) -> FeatureBundle:
        sound = self.validate(sound)
        base_vec = FeatureBundle()

        # check if sound is complex
        complex_sound = sound.split()[-1] if sound.split()[-1] in COMPLEX_SOUNDS else False
        if complex_sound:
            from_sound, complex, to_sound = sound.partition(' to ')
            assert complex
            sound_to_sound = to_sound.replace(complex_sound, COMPLEX_SOUNDS[complex_sound])
            sound = '{} {}'.format(from_sound, COMPLEX_SOUNDS[complex_sound])

            if complex_sound == "diphthong":
                base_vec = self._apply_feature("diphthong", base_vec)
                # set up feature pairs for diphthong trajectory
                diphthong_features = (["from_" + f for f in sound.split()[:-1]] +  # noqa: W504
                                      ["to_" + f for f in sound_to_sound.split()[:-1]])

        features = [f for df in sound.split() for f in df.split("-and-")]

        primary_features, secondary_features = self._get_features(features)

        for feature in primary_features:
            base_vec = self._apply_feature(feature, base_vec)

        # diphthongs take their core vowel features from their first vowel,
        # diphthong-specific features are then applied afterwards
        if complex_sound == "diphthong":
            # apply joint diphthong features
            base_vec = self._apply_joint_feature_defs(diphthong_features, base_vec)
            # extract secondary features for second segment
            to_sound_features = [f for df in sound_to_sound.split() for f in df.split("-and-")]
            _, to_secondary_features = self._get_features(to_sound_features)
            for f in to_secondary_features:
                if (self.feature_values.get(f, {"domain": ""})["domain"] not in
                        ["raising", "relative_articulation", "rounding"]):
                    secondary_features.append(f)
            # check if second part is rounded
            if "to_rounded" in diphthong_features:
                base_vec = self._apply_feature("to_rounded", base_vec, valid={1})
        elif complex_sound == "cluster":
            from_vec = self.get_vec(sound, vectorize=False)
            to_vec = self.get_vec(sound_to_sound, vectorize=False)
            kw = {}
            for f in FeatureBundle.fields():
                if from_vec[f.name] == 1 or to_vec[f.name] == 1:  # 1 trumps -1.
                    kw[f.name] = 1
                elif from_vec[f.name] == -1 or to_vec[f.name] == -1:  # -1 trumps 0.
                    kw[f.name] = -1
            base_vec = FeatureBundle(**kw)

        base_vec = self._apply_joint_feature_defs(features, base_vec)

        for feature in secondary_features:
            if complex_sound == "diphthong":
                base_vec = self._apply_feature(feature, base_vec, valid={1})
            else:
                base_vec = self._apply_feature(feature, base_vec)
        return base_vec

    def get_vec(self, sound, vectorize=True):
        """
        Retrieve the vector for a given sound.

        @param sound: A sound represented by a feature string. If a
            transcription system has been supplied, it can also be a
            sound in IPA notation.
        @param vectorize: Return a binary vector if set to True.
        @returns: vector (dictionary of feature values or tuple of values)

        Examples::

            >>> from soundvectors import SoundVectors
            >>> sv = SoundVectors()
            >>> vec = sv.get_vec("t", vectorize=False)
            >>> print(vec["cont"])
            - 1
        """
        base_vec = self[sound]
        return base_vec.as_vector() if vectorize else base_vec.as_dict()

    def _get_hierarchy_level(self, domain):
        if domain in self.feature_hierarchy:
            return self.feature_hierarchy.index(domain)
        return len(self.feature_hierarchy)

    def _get_features(self, featureset):
        primary_features, secondary_features = [], []
        for feature in featureset:
            if self.feature_values.get(feature, {"domain": ""})["domain"] in self.feature_hierarchy:
                primary_features.append(feature)
            else:
                secondary_features.append(feature)
        primary_features = sorted(
            primary_features,
            key=lambda x: self._get_hierarchy_level(
                self.feature_values.get(x, {"domain": ""})["domain"]))

        return primary_features, secondary_features

    def _apply_feature(self, feature, base_vec, valid=(1, -1)):
        bin_feature_vec = self.feature_values.get(
            feature, {"features": FeatureBundle()})["features"]
        return base_vec.replace(**bin_feature_vec.as_dict(valid_values=valid))

    def _apply_joint_feature_defs(self, sound_features, base_vec):
        for features, bin_feature_vec in self.joint_defs.items():
            if set(features).issubset(set(sound_features)):
                base_vec = base_vec.replace(**bin_feature_vec.as_dict(valid_values={1, -1}))
        return base_vec
