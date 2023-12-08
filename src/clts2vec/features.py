binary_features = ['cons', 'syl', 'son', 'cont', 'delrel', 'lat', 'nas', 'voi', 'sg', 'cg', 'pharyngeal', 'laryngeal',
                   'cor', 'dorsal', 'lab', 'hi', 'lo', 'back', 'round', 'velaric', 'long', 'ant', 'distr', 'strid']

clts_feature_hierarchy = {
    'type': 0,
    'manner': 1,
    'place': 2,
    'phonation': 2
}

max_hierarchy_level = max(clts_feature_hierarchy.values()) + 1

clts_features = {
    'type': {
        'consonant': {
            'cons': 1, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'aspiration': {
        'aspirated': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 1, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'sibilancy': {
        'sibilant': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'creakiness': {
        'creaky': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 1,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'release': {
        'unreleased': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'with-lateral-release': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'with-mid-central-vowel-release': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'with-nasal-release': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'ejection': {
        'ejective': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 1,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'place': {
        'alveolar': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 1, 'distr': 0, 'strid': 0
        },
        'alveolo-palatal': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'bilabial': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'dental': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'epiglottal': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'glottal': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'labial': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'linguolabial': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'labio-palatal': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'labio-velar': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 1,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'labio-dental': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'palatal': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'palatal-velar': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'pharyngeal': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 1, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'post-alveolar': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'retroflex': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'uvular': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'velar': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'pharyngealization': {
        'pharyngealized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 1, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'voicing': {
        'devoiced': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': -1, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'revoiced': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 1, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'nasalization': {
        'nasalized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'preceding': {
        'pre-aspirated': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 1, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'pre-glottalized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 1,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'pre-labialized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 1,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'pre-nasalized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'pre-palatalized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'labialization': {
        'labialized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 1,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'syllabicity': {
        'syllabic': {
            'cons': 0, 'syl': 1, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'palatalization': {
        'labio-palatalized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 1,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'palatalized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'phonation': {
        'voiced': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 1, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'voiceless': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': -1, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'duration': {
        'long': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 1, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'mid-long': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 1, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'stress': {
        'primary-stress': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'secondary-stress': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'laterality': {
        'lateral': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 1, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'velarization': {
        'velarized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'manner': {
        'affricate': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 1, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'approximant': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 1, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'click': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 1, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'fricative': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 1, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'implosive': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'nasal': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'nasal-click': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'stop': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'tap': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'trill': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 1, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'laminality': {
        'apical': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': -1, 'strid': 0
        },
        'laminal': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 1, 'strid': 0
        }
    },
    'articulation': {
        'strong': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'breathiness': {
        'breathy': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 1, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'glottalization': {
        'glottalized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 1,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'raising': {
        'lowered': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'raised': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    },
    'relative_articulation': {
        'centralized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'mid-centralized': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'advanced': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'retracted': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        }
    }
}

clts_feature_values = {
    'consonant': {
        'features': {
            'cons': 1, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'type'
    },
    'aspirated': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 1, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'aspiration'
    },
    'sibilant': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'sibilancy'
    },
    'creaky': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 1,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'creakiness'
    },
    'unreleased': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'release'
    },
    'with-lateral-release': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'release'
    },
    'with-mid-central-vowel-release': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'release'
    },
    'with-nasal-release': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'release'
    },
    'ejective': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 1,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'ejection'
    },
    'alveolar': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 1, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'alveolo-palatal': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'bilabial': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'dental': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'epiglottal': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'glottal': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'labial': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'linguolabial': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'labio-palatal': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'labio-velar': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 1,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'labio-dental': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'palatal': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'palatal-velar': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'pharyngeal': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 1, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'post-alveolar': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'retroflex': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'uvular': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'velar': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'place'
    },
    'pharyngealized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 1, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'pharyngealization'
    },
    'devoiced': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': -1, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'voicing'
    },
    'revoiced': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 1, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'voicing'
    },
    'nasalized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'nasalization'
    },
    'pre-aspirated': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 1, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'preceding'
    },
    'pre-glottalized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 1,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'preceding'
    },
    'pre-labialized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 1,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'preceding'
    },
    'pre-nasalized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'preceding'
    },
    'pre-palatalized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'preceding'
    },
    'labialized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 1,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'labialization'
    },
    'syllabic': {
        'features': {
            'cons': 0, 'syl': 1, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'syllabicity'
    },
    'labio-palatalized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 1,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'palatalization'
    },
    'palatalized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'palatalization'
    },
    'voiced': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 1, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'phonation'
    },
    'voiceless': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': -1, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'phonation'
    },
    'long': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 1, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'duration'
    },
    'mid-long': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 1, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'duration'
    },
    'primary-stress': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'stress'
    },
    'secondary-stress': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'stress'
    },
    'lateral': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 1, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'laterality'
    },
    'velarized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'velarization'
    },
    'affricate': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 1, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'approximant': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 1, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'click': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 1, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'fricative': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 1, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'implosive': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'nasal': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'nasal-click': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'stop': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'tap': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'trill': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 1, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'manner'
    },
    'apical': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': -1, 'strid': 0
        },
        'domain': 'laminality'
    },
    'laminal': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 1, 'strid': 0
        },
        'domain': 'laminality'
    },
    'strong': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'articulation'
    },
    'breathy': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 1, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'breathiness'
    },
    'glottalized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 1,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'glottalization'
    },
    'lowered': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'raising'
    },
    'raised': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'raising'
    },
    'centralized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'relative_articulation'
    },
    'mid-centralized': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'relative_articulation'
    },
    'advanced': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'relative_articulation'
    },
    'retracted': {
        'features': {
            'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
            'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
            'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
        },
        'domain': 'relative_articulation'
    }
}
