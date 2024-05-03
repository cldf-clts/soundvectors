"""
soundvectors: Vectorize Speech Sounds in Phonetic Transcription.
"""
import enum
import typing
import warnings
import functools
import itertools
import collections
import dataclasses

try:  # pragma: no cover
    from pyclts import CLTS, TranscriptionSystem
except ImportError:  # pragma: no cover
    CLTS = typing.Any
    TranscriptionSystem = None

__version__ = "1.0.dev0"

COMPLEX_SOUNDS = {
    'diphthong': 'vowel',
    'cluster': 'consonant',
}


class Sound(typing.Protocol):  # Sound objects are expected to have a name attribute.
    name: str


class DomainHierarchyType(typing.Protocol):  # pragma: no cover
    @classmethod
    def primary_domains(cls) -> typing.Set:
        pass

    @classmethod
    def exclude_for_to_sound(cls) -> typing.Set:
        pass


@dataclasses.dataclass(frozen=True, order=True)  # Make instances immutable and orderable.
class FeatureBundle:
    """
    A bundle of ordered, binary features.
    """
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
    velaric: int = dataclasses.field(
        default=0, metadata={'dc:description': 'Mortensen et al. (2016)'})
    long: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    ant: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    distr: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    strid: int = dataclasses.field(default=0, metadata={'dc:description': ''})
    hitone: int = dataclasses.field(
        default=0, metadata={'dc:description': 'Mortensen et al. (2016)'})
    hireg: int = dataclasses.field(
        default=0, metadata={'dc:description': 'Mortensen et al. (2016)'})
    loreg: int = dataclasses.field(default=0, metadata={'dc:description': 'Supplements hireg'})
    rising: int = dataclasses.field(
        default=0, metadata={'dc:description': 'CLTS tone representation'})
    falling: int = dataclasses.field(
        default=0, metadata={'dc:description': 'CLTS tone representation'})
    contour: int = dataclasses.field(
        default=0, metadata={'dc:description': 'CLTS tone representation'})
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

    def updated(self, other, valid_values=(1, -1)):
        """
        """
        return dataclasses.replace(self, **other.as_dict(valid_values=valid_values))

    @classmethod
    def fields(cls):
        """
        Shortcut for `dataclasses.fields`.
        """
        return dataclasses.fields(cls)


class CLTSDomainHierarchy(enum.Enum):
    """
    CLTS feature domains ordered from least to most specific.
    """
    type = 1
    manner = 2
    height = 3
    roundedness = 4
    centrality = 5
    place = 6
    phonation = 7
    aspiration = 8
    creakiness = 9
    release = 10
    ejection = 11
    pharyngealization = 12
    voicing = 13
    nasalization = 14
    preceding = 15
    labialization = 16
    syllabicity = 17
    palatalization = 18
    duration = 19
    stress = 20
    airstream = 21
    velarization = 22
    laminality = 23
    articulation = 24
    breathiness = 25
    glottalization = 26
    raising = 27
    relative_articulation = 28
    rhotacization = 29
    friction = 30
    rounding = 31
    start = 32
    contour = 33
    to_roundedness = 34

    @classmethod
    def primary_domains(cls):
        return {i for i in itertools.takewhile(lambda i: i.value < 8, cls)}

    @classmethod
    def exclude_for_to_sound(cls):
        return {cls.raising, cls.relative_articulation, cls.rounding}


@functools.total_ordering
class HierarchicalFeature:
    """
    A HierarchicalFeature is a feature that can be ordered via its domain.
    """
    def __init__(self,
                 name: str,
                 domain: typing.Union[typing.Any, str],  # An enum.Enum member.
                 featurebundle: FeatureBundle):
        self.name = name
        self.domain = getattr(CLTSDomainHierarchy, domain) if isinstance(domain, str) else domain
        self.featurebundle = featurebundle

    def __eq__(self, other):  # pragma: no cover
        return self.domain == other.domain and self.name == other.name

    def __lt__(self, other):
        return (self.domain.value, self.name) < (other.domain.value, other.name)


clts_features = [
    HierarchicalFeature(
        "consonant", "type",
        FeatureBundle.from_positive_and_negative(
            ['cons'],
            ['syl', 'son', 'cont', 'delrel', 'lat', 'nas', 'voi', 'sg', 'cg', 'pharyngeal',
             'laryngeal', 'cor', 'dorsal', 'lab', 'hi', 'lo', 'back', 'front', 'round',
             'velaric', 'long'])),
    HierarchicalFeature(
        "vowel", "type",
        FeatureBundle.from_positive_and_negative(
            ["syl", "son", "cont", "voi"],
            ["cons", "lat", "nas", "sg", "cg", "pharyngeal", "laryngeal", "hi", "lo",
             "back", "front", "tense", "round", "velaric", "long"])),
    HierarchicalFeature(
        "tone", "type",
        FeatureBundle.from_positive_and_negative(
            [],
            ["hitone", "hireg", "loreg", "rising", "falling", "contour"])),
    HierarchicalFeature(
        "diphthong", "type",
        FeatureBundle.from_positive_and_negative(
            [],
            ["backshift", "frontshift", "opening", "closing", "centering", "longdistance",
             "secondrounded"])),
    HierarchicalFeature(
        "aspirated", "aspiration",
        FeatureBundle.from_positive_and_negative(["sg"], [])),
    HierarchicalFeature(
        "creaky", "creakiness",
        FeatureBundle.from_positive_and_negative(["cg"], [])),
    HierarchicalFeature(
        "unreleased", "release",
        FeatureBundle.from_positive_and_negative(
            [], [])),
    HierarchicalFeature(
        "with-lateral-release", "release",
        FeatureBundle.from_positive_and_negative(
            ["lat"], [])),
    HierarchicalFeature(
        "with-mid-central-vowel-release", "release",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "with-nasal-release", "release",
        FeatureBundle.from_positive_and_negative(["nas"], [])),
    HierarchicalFeature(
        "ejective", "ejection",
        FeatureBundle.from_positive_and_negative(["cg"], [])),
    HierarchicalFeature(
        "alveolar", "place",
        FeatureBundle.from_positive_and_negative(["cor", "ant", "front"], ["distr"])),
    HierarchicalFeature(
        "alveolo-palatal", "place",
        FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "distr", "front"], ["ant"])),
    HierarchicalFeature(
        "bilabial", "place",
        FeatureBundle.from_positive_and_negative(["lab", "front"], [])),
    HierarchicalFeature(
        "dental", "place",
        FeatureBundle.from_positive_and_negative(["cor", "ant", "distr", "front"], [])),
    HierarchicalFeature(
        "epiglottal", "place",
        FeatureBundle.from_positive_and_negative(["lo"], [])),
    HierarchicalFeature(
        "glottal", "place",
        FeatureBundle.from_positive_and_negative(["laryngeal", "lo"], [])),
    HierarchicalFeature(
        "labial", "place",
        FeatureBundle.from_positive_and_negative(["lab", "front"], [])),
    HierarchicalFeature(
        "linguolabial", "place",
        FeatureBundle.from_positive_and_negative(
            ["cor", "lab", "ant", "front"], ["distr"])),
    HierarchicalFeature(
        "labio-palatal", "place",
        FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "round", "distr", "front"], ["ant"])),
    HierarchicalFeature(
        "labio-velar", "place", FeatureBundle.from_positive_and_negative(
            ["dorsal", "hi", "back", "round", "front"], [])),
    HierarchicalFeature(
        "labio-dental", "place",
        FeatureBundle.from_positive_and_negative(["lab", "front"], [])),
    HierarchicalFeature(
        "palatal", "place",
        FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "distr"], ["ant"])),
    HierarchicalFeature(
        "palatal-velar", "place",
        FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "back", "distr"], ["ant"])),
    HierarchicalFeature(
        "pharyngeal", "place",
        FeatureBundle.from_positive_and_negative(["pharyngeal", "lo", "back"], [])),
    HierarchicalFeature(
        "post-alveolar", "place",
        FeatureBundle.from_positive_and_negative(
            ["cor", "distr", "front"], ["ant"])),
    HierarchicalFeature(
        "retroflex", "place",
        FeatureBundle.from_positive_and_negative(["cor"], ["ant", "distr"])),
    HierarchicalFeature(
        "uvular", "place",
        FeatureBundle.from_positive_and_negative(["dorsal", "lo", "back"], [])),
    HierarchicalFeature(
        "velar", "place",
        FeatureBundle.from_positive_and_negative(["dorsal", "hi", "back"], [])),
    HierarchicalFeature(
        "pharyngealized", "pharyngealization",
        FeatureBundle.from_positive_and_negative(["pharyngeal"], [])),
    HierarchicalFeature(
        "devoiced", "voicing",
        FeatureBundle.from_positive_and_negative([], ["voi"])),
    HierarchicalFeature(
        "revoiced", "voicing",
        FeatureBundle.from_positive_and_negative(["voi"], [])),
    HierarchicalFeature(
        "nasalized", "nasalization",
        FeatureBundle.from_positive_and_negative(["nas"], [])),
    HierarchicalFeature(
        "pre-aspirated", "preceding",
        FeatureBundle.from_positive_and_negative(["sg"], [])),
    HierarchicalFeature(
        "pre-breathy-aspirated", "preceding",
        FeatureBundle.from_positive_and_negative(["sg"], [])),
    HierarchicalFeature(
        "pre-glottalized", "preceding",
        FeatureBundle.from_positive_and_negative(["cg", "lo"], [])),
    HierarchicalFeature(
        "pre-labialized", "preceding",
        FeatureBundle.from_positive_and_negative(["dorsal", "hi", "round"], [])),
    HierarchicalFeature(
        "pre-nasalized", "preceding",
        FeatureBundle.from_positive_and_negative(["nas"], [])),
    HierarchicalFeature(
        "pre-palatalized", "preceding",
        FeatureBundle.from_positive_and_negative(["cor", "dorsal", "hi"], [])),
    HierarchicalFeature(
        "labialized", "labialization",
        FeatureBundle.from_positive_and_negative(
            ["dorsal", "hi", "back", "round"], [])),
    HierarchicalFeature(
        "syllabic", "syllabicity",
        FeatureBundle.from_positive_and_negative(["syl"], [])),
    HierarchicalFeature(
        "non-syllabic", "syllabicity",
        FeatureBundle.from_positive_and_negative([], ["syl"])),
    HierarchicalFeature(
        "labio-palatalized", "palatalization",
        FeatureBundle.from_positive_and_negative(
            ["cor", "dorsal", "hi", "round"], [])),
    HierarchicalFeature(
        "palatalized", "palatalization",
        FeatureBundle.from_positive_and_negative(["cor", "dorsal", "hi"], [])),
    HierarchicalFeature(
        "voiced", "phonation",
        FeatureBundle.from_positive_and_negative(["voi"], [])),
    HierarchicalFeature(
        "voiceless", "phonation",
        FeatureBundle.from_positive_and_negative([], ["voi"])),
    HierarchicalFeature(
        "long", "duration",
        FeatureBundle.from_positive_and_negative(["long"], [])),
    HierarchicalFeature(
        "mid-long", "duration",
        FeatureBundle.from_positive_and_negative(["long"], [])),
    HierarchicalFeature(
        "ultra-long", "duration",
        FeatureBundle.from_positive_and_negative(["long"], [])),
    HierarchicalFeature(
        "ultra-short", "duration",
        FeatureBundle.from_positive_and_negative([], ["long"])),
    HierarchicalFeature(
        "primary-stress", "stress",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "secondary-stress", "stress",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "lateral", "airstream",
        FeatureBundle.from_positive_and_negative(["cons", "lat"], [])),
    HierarchicalFeature(
        "sibilant", "airstream",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "velarized", "velarization",
        FeatureBundle.from_positive_and_negative(["dorsal", "hi", "back"], [])),
    HierarchicalFeature(
        "affricate", "manner",
        FeatureBundle.from_positive_and_negative(["delrel"], ["strid"])),
    HierarchicalFeature(
        "approximant", "manner",
        FeatureBundle.from_positive_and_negative(["son", "cont"], ["cons"])),
    HierarchicalFeature(
        "click", "manner",
        FeatureBundle.from_positive_and_negative(["velaric"], [])),
    HierarchicalFeature(
        "fricative", "manner",
        FeatureBundle.from_positive_and_negative(["cont"], ["strid"])),
    HierarchicalFeature(
        "implosive", "manner",
        FeatureBundle.from_positive_and_negative(["cg"], [])),
    HierarchicalFeature(
        "nasal", "manner",
        FeatureBundle.from_positive_and_negative(["son", "nas"], [])),
    HierarchicalFeature(
        "nasal-click", "manner",
        FeatureBundle.from_positive_and_negative(["nas", "velaric"], [])),
    HierarchicalFeature(
        "stop", "manner",
        FeatureBundle.from_positive_and_negative([], ["son", "cont"])),
    HierarchicalFeature(
        "tap", "manner",
        FeatureBundle.from_positive_and_negative(["son"], ["cont"])),
    HierarchicalFeature(
        "trill", "manner",
        FeatureBundle.from_positive_and_negative(["son", "cont"], [])),
    HierarchicalFeature(
        "apical", "laminality",
        FeatureBundle.from_positive_and_negative([], ["distr"])),
    HierarchicalFeature(
        "laminal", "laminality",
        FeatureBundle.from_positive_and_negative(["distr"], [])),
    HierarchicalFeature(
        "strong", "articulation",
        FeatureBundle.from_positive_and_negative(["tense"], [])),
    HierarchicalFeature(
        "breathy", "breathiness",
        FeatureBundle.from_positive_and_negative(["sg"], [])),
    HierarchicalFeature(
        "glottalized", "glottalization",
        FeatureBundle.from_positive_and_negative(["cg"], [])),
    HierarchicalFeature(
        "lowered", "raising",
        FeatureBundle.from_positive_and_negative(["lo"], [])),
    HierarchicalFeature(
        "raised", "raising",
        FeatureBundle.from_positive_and_negative(["hi"], [])),
    HierarchicalFeature(
        "centralized", "relative_articulation",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "mid-centralized", "relative_articulation",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "advanced", "relative_articulation",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "retracted", "relative_articulation",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "back", "centrality",
        FeatureBundle.from_positive_and_negative(["back"], [])),
    HierarchicalFeature(
        "central", "centrality",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "front", "centrality",
        FeatureBundle.from_positive_and_negative(["front"], [])),
    HierarchicalFeature(
        "near-back", "centrality",
        FeatureBundle.from_positive_and_negative(["back"], [])),
    HierarchicalFeature(
        "near-front", "centrality",
        FeatureBundle.from_positive_and_negative(["front"], [])),
    HierarchicalFeature(
        "rhotacized", "rhotacization",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "close", "height",
        FeatureBundle.from_positive_and_negative(["hi", "tense"], [])),
    HierarchicalFeature(
        "close-mid", "height",
        FeatureBundle.from_positive_and_negative(["tense"], [])),
    HierarchicalFeature(
        "mid", "height",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "near-close", "height",
        FeatureBundle.from_positive_and_negative(["hi"], [])),
    HierarchicalFeature(
        "near-open", "height",
        FeatureBundle.from_positive_and_negative(["lo"], [])),
    HierarchicalFeature(
        "open", "height",
        FeatureBundle.from_positive_and_negative(["lo", "tense"], [])),
    HierarchicalFeature(
        "open-mid", "height",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "with-friction", "friction",
        FeatureBundle.from_positive_and_negative([], ["son"])),
    HierarchicalFeature(
        "rounded", "roundedness",
        FeatureBundle.from_positive_and_negative(["round"], [])),
    HierarchicalFeature(
        "unrounded", "roundedness",
        FeatureBundle.from_positive_and_negative([], ["round"])),
    HierarchicalFeature(
        "less-rounded", "rounding",
        FeatureBundle.from_positive_and_negative(["round"], [])),
    HierarchicalFeature(
        "more-rounded", "rounding",
        FeatureBundle.from_positive_and_negative(["round"], [])),
    HierarchicalFeature(
        "from-high", "start",
        FeatureBundle.from_positive_and_negative(["hireg", "hitone"], [])),
    HierarchicalFeature(
        "from-low", "start",
        FeatureBundle.from_positive_and_negative(["loreg"], [])),
    HierarchicalFeature(
        "from-mid", "start",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "from-mid-high", "start",
        FeatureBundle.from_positive_and_negative(["hireg"], [])),
    HierarchicalFeature(
        "from-mid-low", "start",
        FeatureBundle.from_positive_and_negative(["loreg", "hitone"], [])),
    HierarchicalFeature(
        "contour", "contour",
        FeatureBundle.from_positive_and_negative(["contour"], [])),
    HierarchicalFeature(
        "falling", "contour",
        FeatureBundle.from_positive_and_negative(["falling"], [])),
    HierarchicalFeature(
        "rising", "contour",
        FeatureBundle.from_positive_and_negative(["rising"], [])),
    HierarchicalFeature(
        "flat", "contour",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "short", "contour",
        FeatureBundle.from_positive_and_negative([], [])),
    HierarchicalFeature(
        "to_rounded", "to_roundedness",
        FeatureBundle.from_positive_and_negative(["secondrounded"], [])),
    HierarchicalFeature(
        "to_unrounded", "to_roundedness",
        FeatureBundle.from_positive_and_negative([], ["secondrounded"])),
]
assert len(clts_features) == len({f.name for f in clts_features}), "Duplicate clts feature name"
clts_features = collections.OrderedDict((o.name, o) for o in sorted(clts_features))

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
    def __init__(
            self,
            ts: typing.Optional[typing.Union[
                TranscriptionSystem,  # A pyclts.TranscriptionSystem
                typing.Callable[[typing.List[str]], typing.List[str]]  # A soundclasses-like func
            ]] = None,
            feature_values: typing.Dict[str, HierarchicalFeature] = clts_features,
            feature_hierarchy: typing.Optional[DomainHierarchyType] = CLTSDomainHierarchy,
            joint_defs=joint_feature_definitions
    ):
        self.ts = ts
        self.feature_values = feature_values
        self.joint_defs = joint_defs
        self.feature_hierarchy = feature_hierarchy
        self.primary_domains = self.feature_hierarchy.primary_domains()

    def clts_compatibility(self, clts: CLTS) -> bool:
        """
        Check compatibility with a particular CLTS release
        """
        import json
        clts_features = json.loads(
            clts.transcriptionsystems_dir.joinpath('features.json').read_text(encoding='utf8'))
        for k, d in self.feature_values.items():
            if d.domain.name not in ['type', 'to_roundedness']:
                # Make sure, k appears as feature for the domain for at least one type in CLTS:
                for dd in clts_features.values():
                    if d.domain.name in dd and (k in dd[d.domain.name]):
                        break
                else:  # pragma: no cover
                    raise AssertionError('{}: {}'.format(d.domain.name, k))
        return True

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
            if isinstance(self.ts, TranscriptionSystem):
                sound_transcribed = self.ts[sound]
            else:
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
                base_vec = base_vec.updated(self.feature_values["diphthong"].featurebundle)
                # set up feature pairs for diphthong trajectory
                diphthong_features = (["from_" + f for f in sound.split()[:-1]] +  # noqa: W504
                                      ["to_" + f for f in sound_to_sound.split()[:-1]])

        features = [f for df in sound.split() for f in df.split("-and-")]

        primary_features, secondary_features = self._get_features(features)

        for feature, hf in primary_features:
            base_vec = base_vec.updated(hf.featurebundle)

        # diphthongs take their core vowel features from their first vowel,
        # diphthong-specific features are then applied afterwards
        if complex_sound == "diphthong":
            # apply joint diphthong features
            base_vec = self._apply_joint_feature_defs(diphthong_features, base_vec)
            # extract secondary features for second segment
            to_sound_features = [f for df in sound_to_sound.split() for f in df.split("-and-")]
            _, to_secondary_features = self._get_features(to_sound_features)
            for f, fv in to_secondary_features:
                if fv and fv.domain in self.feature_hierarchy.exclude_for_to_sound():
                    continue
                secondary_features.append((f, fv))
            # check if second part is rounded
            #
            # FIXME: That's an assumption based on the CLTS feature system!
            #
            if "to_rounded" in diphthong_features:
                base_vec = base_vec.updated(
                    self.feature_values["to_rounded"].featurebundle, valid_values={1})
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

        for feature, fv in secondary_features:
            base_vec = base_vec.updated(
                fv.featurebundle, valid_values={1} if complex_sound == 'diphthong' else {1, -1})
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

    def _get_features(self, featureset) -> typing.Tuple[typing.List, typing.List]:
        primary, secondary = [], []
        # Augment the featureset with matching HierarchicalFeatures if they are defined:
        featureset = [
            (feature, self.feature_values.get(feature))
            for feature in featureset if feature in self.feature_values]
        for feature, hf in sorted(featureset, key=lambda i: i[1]):
            (primary if hf.domain in self.primary_domains else secondary).append((feature, hf))

        return primary, secondary

    def _apply_joint_feature_defs(self, sound_features, base_vec):
        for features, bin_feature_vec in self.joint_defs.items():
            if set(features).issubset(set(sound_features)):
                base_vec = base_vec.updated(bin_feature_vec)
        return base_vec
