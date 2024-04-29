"""
CLTS2Vec: Vectorize Speech Sounds in Phonetic Transcription.
"""
import warnings
from collections import OrderedDict

__version__ = "1.0.dev0"


binary_features = ["cons", "syl", "son", "cont", "delrel", "lat", "nas", "voi", "sg", "cg", "pharyngeal", "laryngeal",
    "cor", "dorsal", "lab", "hi", "lo", "back", "front", "tense", "round", "velaric", "long", "ant", "distr", "strid",
    "hitone", "hireg", "loreg", "rising", "falling", "contour", "backshift", "frontshift", "opening", "closing",
    "centering", "longdistance", "secondrounded", ]

clts_feature_hierarchy = {"type": 0, "manner": 1, "height": 1, "roundedness": 1, "centrality": 1, "place": 2,
    "phonation": 2, }

max_hierarchy_level = max(clts_feature_hierarchy.values()) + 1

clts_features = {"type": {
    "consonant": {"cons": 1, "syl": -1, "son": -1, "cont": -1, "delrel": -1, "lat": -1, "nas": -1, "voi": -1, "sg": -1,
        "cg": -1, "pharyngeal": -1, "laryngeal": -1, "cor": -1, "dorsal": -1, "lab": -1, "hi": -1, "lo": -1, "back": -1,
        "front": -1, "round": -1, "velaric": -1, "long": -1, "ant": 0, "distr": 0, "strid": 0, },
    "vowel": {"cons": -1, "syl": 1, "son": 1, "cont": 1, "delrel": 0, "lat": -1, "nas": -1, "voi": 1, "sg": -1,
        "cg": -1, "pharyngeal": -1, "laryngeal": -1, "cor": 0, "dorsal": 0, "lab": 0, "hi": -1, "lo": -1, "back": -1,
        "front": -1, "tense": -1, "round": -1, "velaric": -1, "long": -1, "ant": 0, "distr": 0, "strid": 0, },
    "tone": {"hitone": -1, "hireg": -1, "loreg": -1, "rising": -1, "falling": -1, "contour": -1, },
    "diphthong": {"backshift": -1, "frontshift": -1, "opening": -1, "closing": -1, "centering": -1, "longdistance": -1,
        "secondrounded": -1, }, }, "aspiration": {
    "aspirated": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 1, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "sibilancy": {
    "sibilant": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "creakiness": {
    "creaky": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 1,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "release": {
    "unreleased": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "with-lateral-release": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 1, "nas": 0, "voi": 0,
        "sg": 0, "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "with-mid-central-vowel-release": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0,
        "voi": 0, "sg": 0, "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0,
        "back": 0, "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "with-nasal-release": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 1, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "ejection": {
    "ejective": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 1,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "place": {
    "alveolar": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 1, "distr": -1, "strid": 0, "front": 1, },
    "alveolo-palatal": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": -1, "distr": 1, "strid": 0, "front": 1, },
    "bilabial": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 1, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, "front": 1, },
    "dental": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 1, "distr": 1, "strid": 0, "front": 1, },
    "epiglottal": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 1, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "glottal": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 1, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 1, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "labial": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 1, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, "front": 1, },
    "linguolabial": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 0, "lab": 1, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 1, "distr": -1, "strid": 0, "front": 1, },
    "labio-palatal": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 0,
        "round": 1, "velaric": 0, "long": 0, "ant": -1, "distr": 1, "strid": 0, "front": 1, },
    "labio-velar": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 1,
        "round": 1, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, "front": 1, },
    "labio-dental": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 1, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, "front": 1, },
    "palatal": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": -1, "distr": 1, "strid": 0, },
    "palatal-velar": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 1,
        "round": 0, "velaric": 0, "long": 0, "ant": -1, "distr": 1, "strid": 0, },
    "pharyngeal": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 1, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 1, "back": 1,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "post-alveolar": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": -1, "distr": 1, "strid": 0, "front": 1, },
    "retroflex": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": -1, "distr": -1, "strid": 0, },
    "uvular": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 1, "lab": 0, "hi": 0, "lo": 1, "back": 1, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "velar": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 1, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "pharyngealization": {
    "pharyngealized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 1, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "voicing": {
    "devoiced": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": -1, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "revoiced": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 1, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "nasalization": {
    "nasalized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 1, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "preceding": {
    "pre-aspirated": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 1,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "pre-breathy-aspirated": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0,
        "sg": 1, "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "pre-glottalized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 1, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 1, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "pre-labialized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 0,
        "round": 1, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "pre-nasalized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 1, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "pre-palatalized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "labialization": {
    "labialized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 1,
        "round": 1, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "syllabicity": {
    "syllabic": {"cons": 0, "syl": 1, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "non-syllabic": {"cons": 0, "syl": -1, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "palatalization": {
    "labio-palatalized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 0,
        "round": 1, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "palatalized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 1, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "phonation": {
    "voiced": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 1, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "voiceless": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": -1, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "duration": {
    "long": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 1, "ant": 0, "distr": 0, "strid": 0, },
    "mid-long": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 1, "ant": 0, "distr": 0, "strid": 0, },
    "ultra-long": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 1, "ant": 0, "distr": 0, "strid": 0, },
    "ultra-short": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": -1, "ant": 0, "distr": 0, "strid": 0, }, }, "stress": {
    "primary-stress": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "secondary-stress": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "laterality": {
    "lateral": {"cons": 1, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 1, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "velarization": {
    "velarized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 1, "lab": 0, "hi": 1, "lo": 0, "back": 1, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "manner": {
    "affricate": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 1, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": -1, },
    "approximant": {"cons": -1, "syl": 0, "son": 1, "cont": 1, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "click": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 1, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "fricative": {"cons": 0, "syl": 0, "son": 0, "cont": 1, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": -1, },
    "implosive": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 1,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "nasal": {"cons": 0, "syl": 0, "son": 1, "cont": 0, "delrel": 0, "lat": 0, "nas": 1, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "nasal-click": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 1, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 1, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "stop": {"cons": 0, "syl": 0, "son": -1, "cont": -1, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "tap": {"cons": 0, "syl": 0, "son": 1, "cont": -1, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "trill": {"cons": 0, "syl": 0, "son": 1, "cont": 1, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "laminality": {
    "apical": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": -1, "strid": 0, },
    "laminal": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 1, "strid": 0, }, }, "articulation": {
    "strong": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, "tense": 1, }}, "breathiness": {
    "breathy": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 1, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "glottalization": {
    "glottalized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 1, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }}, "raising": {
    "lowered": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 1, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "raised": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 1, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, }, "relative_articulation": {
    "centralized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "mid-centralized": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0,
        "cg": 0, "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0,
        "round": 0, "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "advanced": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, },
    "retracted": {"cons": 0, "syl": 0, "son": 0, "cont": 0, "delrel": 0, "lat": 0, "nas": 0, "voi": 0, "sg": 0, "cg": 0,
        "pharyngeal": 0, "laryngeal": 0, "cor": 0, "dorsal": 0, "lab": 0, "hi": 0, "lo": 0, "back": 0, "round": 0,
        "velaric": 0, "long": 0, "ant": 0, "distr": 0, "strid": 0, }, },
    "centrality": {"back": {"back": 1}, "central": {}, "front": {"front": 1}, "near-back": {"back": 1},
        "near-front": {"front": 1}, }, "rhotacization": {"rhotacized": {}},
    "height": {"close": {"hi": 1, "tense": 1}, "close-mid": {"tense": 1}, "mid": {}, "near-close": {"hi": 1},
        "near-open": {"lo": 1}, "open": {"lo": 1, "tense": 1}, "open-mid": {}, },
    "friction": {"with-friction": {"son": -1}}, "roundedness": {"rounded": {"round": 1}, "unrounded": {"round": -1}},
    "rounding": {"less-rounded": {"round": 1}, "more-rounded": {"round": 1}},
    "start": {"from-high": {"hireg": 1, "hitone": 1}, "from-low": {"loreg": 1}, "from-mid": {},
        "from-mid-high": {"hireg": 1}, "from-mid-low": {"loreg": 1, "hitone": 1}, },
    "contour": {"contour": {"contour": 1}, "falling": {"falling": 1}, "rising": {"rising": 1}, "flat": {},
        "short": {}, },
    "to_roundedness": {"to_rounded": {"secondrounded": 1}, "to_unrounded": {"secondrounded": -1}, }, }

clts_feature_values = {}

for domain, value_dict in clts_features.items():
    for value, feature_dict in value_dict.items():
        clts_feature_values[value] = {"features": feature_dict, "domain": domain}

joint_feature_definitions = {("glottal", "stop"): {"cg": 1}, ("affricate", "alveolar"): {"strid": 1},
    ("affricate", "labio-dental"): {"strid": 1}, ("affricate", "post-alveolar"): {"strid": 1},
    ("affricate", "uvular"): {"strid": 1}, ("fricative", "alveolar"): {"strid": 1},
    ("fricative", "labio-dental"): {"strid": 1}, ("fricative", "post-alveolar"): {"strid": 1},
    ("fricative", "uvular"): {"strid": 1}, ("contour", "from-high", "via-mid-high"): {"falling": 1},
    ("contour", "from-high", "via-mid"): {"falling": 1}, ("contour", "from-high", "via-mid-low"): {"falling": 1},
    ("contour", "from-high", "via-low"): {"falling": 1}, ("contour", "from-mid-high", "via-high"): {"rising": 1},
    ("contour", "from-mid-high", "via-mid"): {"falling": 1},
    ("contour", "from-mid-high", "via-mid-low"): {"falling": 1},
    ("contour", "from-mid-high", "via-low"): {"falling": 1}, ("contour", "from-mid", "via-high"): {"rising": 1},
    ("contour", "from-mid", "via-mid-high"): {"rising": 1}, ("contour", "from-mid", "via-mid-low"): {"falling": 1},
    ("contour", "from-mid", "via-low"): {"falling": 1}, ("contour", "from-mid-low", "via-high"): {"rising": 1},
    ("contour", "from-mid-low", "via-mid-high"): {"rising": 1}, ("contour", "from-mid-low", "via-mid"): {"rising": 1},
    ("contour", "from-mid-low", "via-low"): {"falling": 1}, ("contour", "from-low", "via-high"): {"rising": 1},
    ("contour", "from-low", "via-mid-high"): {"rising": 1}, ("contour", "from-low", "via-mid"): {"rising": 1},
    ("contour", "from-low", "via-mid-low"): {"rising": 1}, ("from_front", "to_near-front"): {"backshift": 1},
    ("from_near-front", "to_front"): {"frontshift": 1}, ("from_front", "to_central"): {"backshift": 1},
    ("from_central", "to_front"): {"frontshift": 1}, ("from_front", "to_near-back"): {"backshift": 1},
    ("from_near-back", "to_front"): {"frontshift": 1}, ("from_front", "to_back"): {"backshift": 1},
    ("from_back", "to_front"): {"frontshift": 1}, ("from_near-front", "to_central"): {"backshift": 1},
    ("from_central", "to_near-front"): {"frontshift": 1}, ("from_near-front", "to_near-back"): {"backshift": 1},
    ("from_near-back", "to_near-front"): {"frontshift": 1}, ("from_near-front", "to_back"): {"backshift": 1},
    ("from_back", "to_near-front"): {"frontshift": 1}, ("from_central", "to_near-back"): {"backshift": 1},
    ("from_near-back", "to_central"): {"frontshift": 1}, ("from_central", "to_back"): {"backshift": 1},
    ("from_back", "to_central"): {"frontshift": 1}, ("from_near-back", "to_back"): {"backshift": 1},
    ("from_back", "to_near-back"): {"frontshift": 1}, ("from_close", "to_close-mid"): {"opening": 1, "centering": 1},
    ("from_close-mid", "to_close"): {"closing": 1}, ("from_close", "to_mid"): {"opening": 1},
    ("from_mid", "to_close"): {"closing": 1}, ("from_close", "to_open-mid"): {"opening": 1},
    ("from_open-mid", "to_close"): {"closing": 1, "longdistance": 1},
    ("from_close", "to_near-open"): {"opening": 1, "centering": 1, "longdistance": 1},
    ("from_near-open", "to_close"): {"closing": 1, "longdistance": 1},
    ("from_close", "to_open"): {"opening": 1, "longdistance": 1},
    ("from_open", "to_close"): {"closing": 1, "longdistance": 1}, ("from_near-close", "to_mid"): {"opening": 1},
    ("from_mid", "to_near-close"): {"closing": 1, "centering": 1}, ("from_near-close", "to_open-mid"): {"opening": 1},
    ("from_open-mid", "to_near-close"): {"closing": 1, "centering": 1},
    ("from_near-close", "to_near-open"): {"opening": 1, "centering": 1},
    ("from_near-open", "to_near-close"): {"closing": 1, "centering": 1},
    ("from_near-close", "to_open"): {"opening": 1, "longdistance": 1},
    ("from_open", "to_near-close"): {"closing": 1, "centering": 1, "longdistance": 1},
    ("from_close-mid", "to_open-mid"): {"opening": 1}, ("from_open-mid", "to_close-mid"): {"closing": 1},
    ("from_close-mid", "to_near-open"): {"opening": 1, "centering": 1},
    ("from_near-open", "to_close-mid"): {"closing": 1},
    ("from_close-mid", "to_open"): {"opening": 1, "longdistance": 1}, ("from_open", "to_close-mid"): {"closing": 1},
    ("from_mid", "to_near-open"): {"opening": 1, "centering": 1}, ("from_near-open", "to_mid"): {"closing": 1},
    ("from_mid", "to_open"): {"opening": 1}, ("from_open", "to_mid"): {"closing": 1},
    ("from_open-mid", "to_open"): {"opening": 1}, ("from_open", "to_open-mid"): {"closing": 1, "centering": 1},
    ("from_close", "to_near-close"): {"centering": 1}, ("from_close-mid", "to_near-close"): {"centering": 1},
    ("from_open-mid", "to_near-open"): {"centering": 1}, ("from_open", "to_near-open"): {"centering": 1},
    ("to_mid", "to_central"): {"centering": 1}, ("to_close-mid", "to_central"): {"centering": 1},
    ("to_open-mid", "to_central"): {"centering": 1}, ("from_near-close", "to_close-mid"): {"centering": 1},
    ("from_near-open", "to_open-mid"): {"centering": 1}, }


def is_valid_sound(sound):
    """
    Check if sound corresponds to our expectations.

    @note: We expect a string à la "voiced bilabial stop consonant"
    """
    if isinstance(sound, str) and (sound.endswith(" consonant") or sound.endswith(" vowel") or
                                   sound.endswith(" tone") or sound.endswith(" diphthong") or
                                   sound.endswith(" cluster")):
        return True
    return False


class FeatureBundle(OrderedDict):

    def __init__(self, features):
        OrderedDict.__init__(OrderedDict())
        for f in features:
            self[f] = 0

    def __str__(self):
        return ",".join([
            {1: "+", -1: "-", 0: "0_"}[v] + k for k, v in self.items()])

    def as_vec(self):
        return tuple(self.values())

    def as_set(self):
        return frozenset({{1: "+", -1: "-"}[v] + k for k, v in self.items() if v})


class SoundVectors:
    """
    CLTS2Vec handles vectorization of sounds represented by features.

    Examples::
        >>> import soundvectors
        >>> c2v = soundvectors.SoundVectors()
        >>> c2v
    """

    feature_values = clts_feature_values
    binary_features = binary_features
    joint_defs = joint_feature_definitions
    feature_hierarchy = clts_feature_hierarchy
    ts = None

    def __init__(
            self,
            ts=None,
            feature_values=None,
            feature_hierarchy=None,
            binary_features=None,
            joint_defs=None
    ):

        self.ts = ts
        self.feature_values = feature_values or self.feature_values
        self.joint_defs = joint_defs or self.joint_defs
        self.feature_hierarchy = feature_hierarchy or self.feature_hierarchy
        self.binary_features = binary_features or self.binary_features

    def __call__(self, sounds, vectorize=True):
        vectors = []

        for sound in sounds:
            try:
                vectors.append(self.get_vec(sound, vectorize=vectorize))
            except ValueError:
                warnings.warn(f"Invalid sound encountered: [{sound}]. Returned feature vector is `None`")
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
            >>> print(vec["cont"]
            - 1
        """
        sound = self.validate(sound)
        base_vec = FeatureBundle(self.binary_features)  # {f: 0 for f in self.binary_features}

        # check if sound is diphthong or complex
        complex_sound = False
        if sound.endswith(" diphthong"):
            self._apply_feature("diphthong", base_vec)
            sound_to_sound = sound[sound.index(" to ") + 4: -10] + " vowel"
            sound = sound[5: sound.index(" to ")] + " vowel"
            # set up feature pairs for diphthong trajectory
            diphthong_features = (["from_" + f for f in sound.split()[:-1]] +
                                  ["to_" + f for f in sound_to_sound.split()[:-1]])
            complex_sound = "diphthong"

        elif sound.endswith(" cluster"):
            sound_to_sound = sound[sound.index(" to ") + 4: -8] + " consonant"
            sound = sound[5: sound.index(" to ")] + " consonant"
            complex_sound = "cluster"

        features = [f for df in sound.split() for f in df.split("-and-")]

        primary_features, secondary_features = self._get_features(features)

        for feature in primary_features:
            self._apply_feature(feature, base_vec)

        # diphthongs take their core vowel features from their first vowel,
        # diphthong-specific features are then applied afterwards
        if complex_sound == "diphthong":
            # apply joint diphthong features
            self._apply_joint_feature_defs(diphthong_features, base_vec)
            # check if second part is rounded
            if "to_rounded" in diphthong_features:
                self._apply_positive_features("to_rounded", base_vec)
            # check for duration
            if "long" in sound_to_sound or "short" in sound_to_sound:
                duration = [f for f in sound_to_sound.split() if ("long" in f
                                                                  or "short" in f)][0]
                self._apply_positive_features(duration, base_vec)
            # assign [+nas] if second part of the diphthong is nasalized
            if "nasalized" in sound_to_sound:
                self._apply_positive_features("nasalized", base_vec)
        elif complex_sound == "cluster":
            from_vec = self.get_vec(sound, vectorize=False)
            to_vec = self.get_vec(sound_to_sound, vectorize=False)
            for f in binary_features:
                if from_vec[f] == 1 or to_vec[f] == 1:
                    base_vec[f] = 1
                elif from_vec[f] == -1 or to_vec[f] == -1:
                    base_vec[f] = -1
                else:
                    base_vec[f] = 0

        self._apply_joint_feature_defs(features, base_vec)

        for feature in secondary_features:
            self._apply_feature(feature, base_vec)

        if not vectorize:
            return base_vec
        return base_vec.as_vec()

    def _get_features(self, featureset):
        primary_features, secondary_features = [], []
        for feature in featureset:
            if self.feature_values.get(
                    feature, {"domain": ""}
            )["domain"] in self.feature_hierarchy:
                primary_features.append(feature)
            else:
                secondary_features.append(feature)
        primary_features = sorted(
            primary_features,
            key=lambda x: self.feature_hierarchy.get(
                self.feature_values.get(
                    x, {"domain": ""})["domain"],
                max_hierarchy_level))

        return primary_features, secondary_features

    def _apply_feature(self, feature, base_vec):
        bin_feature_vec = self.feature_values.get(
            feature, {"features": {}})["features"]
        for k, v in bin_feature_vec.items():
            if v in [1, -1]:
                base_vec[k] = v

    def _apply_joint_feature_defs(self, sound_features, base_vec):
        for features, bin_feature_vec in self.joint_defs.items():
            if set(features).issubset(set(sound_features)):
                for k, v in bin_feature_vec.items():
                    if v in [1, -1]:
                        base_vec[k] = v

    def _apply_positive_features(self, feature, base_vec):
        bin_feature_vec = self.feature_values.get(
            feature, {"features": {}})["features"]
        for k, v in bin_feature_vec.items():
            if v == 1:
                base_vec[k] = v


