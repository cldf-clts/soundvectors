binary_features = ['cons', 'syl', 'son', 'cont', 'delrel', 'lat', 'nas', 'voi', 'sg', 'cg', 'pharyngeal', 'laryngeal',
                   'cor', 'dorsal', 'lab', 'hi', 'lo', 'back', 'front', 'tense', 'round', 'velaric', 'long', 'ant', 'distr', 'strid',
				   'hitone', 'hireg', 'loreg', 'rising', 'falling', 'contour']

clts_feature_hierarchy = {
	'type': 0,
	'manner': 1,
	'height': 1,
	'roundedness': 1,
	'centrality': 1,
	'place': 2,
	'phonation': 2
}

max_hierarchy_level = max(clts_feature_hierarchy.values()) + 1

clts_features = {
	'type': {
		'consonant': {
			'cons': 1, 'syl': -1, 'son': -1, 'cont': -1, 'delrel': -1, 'lat': -1, 'nas': -1, 'voi': -1, 'sg': -1, 'cg': -1, 
			'pharyngeal': -1, 'laryngeal': -1, 'cor': -1, 'dorsal': -1, 'lab': -1, 'hi': -1, 'lo': -1, 'back': -1, 'round': -1, 
			'velaric': -1, 'long': -1, 'ant': 0, 'distr': 0, 'strid': 0
		}, 'vowel': {
			'cons': -1, 'syl': 1, 'son': 1, 'cont': 1, 'delrel': 0, 'lat': -1, 'nas': -1, 'voi': 1, 'sg': -1, 'cg': -1,
			'pharyngeal': -1, 'laryngeal': -1, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': -1, 'lo': -1, 'back': -1, 'front': -1,
			'tense': -1, 'round': -1, 'velaric': -1, 'long': -1, 'ant': 0, 'distr': 0, 'strid': 0
		}, 'tone': {
			'hitone': -1, 'hireg': -1, 'loreg': -1, 'rising': -1, 'falling': -1, 'contour': -1
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
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 1, 'distr': -1, 'strid': 0
		},
		'alveolo-palatal': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': -1, 'distr': 1, 'strid': 0
		},
		'bilabial': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'dental': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 1, 'distr': 1, 'strid': 0
		},
		'epiglottal': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'glottal': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 1, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'labial': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'linguolabial': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 1, 'distr': -1, 'strid': 0
		},
		'labio-palatal': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 1, 
			'velaric': 0, 'long': 0, 'ant': -1, 'distr': 1, 'strid': 0
		},
		'labio-velar': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 1, 'round': 1, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'labio-dental': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 1, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'palatal': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': -1, 'distr': 1, 'strid': 0
		},
		'palatal-velar': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 1, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': -1, 'distr': 1, 'strid': 0
		},
		'pharyngeal': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 1, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 1, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'post-alveolar': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': -1, 'distr': 1, 'strid': 0
		},
		'retroflex': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 1, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': -1, 'distr': -1, 'strid': 0
		},
		'uvular': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 1, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'velar': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 1, 'round': 0, 
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
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 1, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'pre-labialized': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 1, 
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
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 1, 'round': 1, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		}
	},
	'syllabicity': {
		'syllabic': {
			'cons': 0, 'syl': 1, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'non-syllabic': {
			'cons': 0, 'syl': -1, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		}
	},
	'palatalization': {
		'labio-palatalized': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 1, 
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
		},
		'ultra-long': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
			'velaric': 0, 'long': 1, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'ultra-short': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0,
			'velaric': 0, 'long': -1, 'ant': 0, 'distr': 0, 'strid': 0
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
			'cons': 1, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 1, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		}
	},
	'velarization': {
		'velarized': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 1, 'lab': 0, 'hi': 1, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		}
	},
	'manner': {
		'affricate': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 1, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': -1
		},
		'approximant': {
			'cons': -1, 'syl': 0, 'son': 1, 'cont': 1, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0,
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
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': -1
		},
		'implosive': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'nasal': {
			'cons': 0, 'syl': 0, 'son': 1, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 0, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
		},
		'nasal-click': {
			'cons': 0, 'syl': 0, 'son': 0, 'cont': 0, 'delrel': 0, 'lat': 0, 'nas': 1, 'voi': 0, 'sg': 0, 'cg': 0, 
			'pharyngeal': 0, 'laryngeal': 0, 'cor': 0, 'dorsal': 0, 'lab': 0, 'hi': 0, 'lo': 0, 'back': 0, 'round': 0, 
			'velaric': 1, 'long': 0, 'ant': 0, 'distr': 0, 'strid': 0
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
			'cons': 0, 'syl': 0, 'son': 1, 'cont': 1, 'delrel': 0, 'lat': 0, 'nas': 0, 'voi': 0, 'sg': 0, 'cg': 0, 
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
	},
	'centrality': {
		'back': {
			'back': 1
		},
		'central': {},
		'front': {
			'front': 1
		},
		'near-back': {
			'back': 1
		},
		'near-front': {
			'front': 1
		}
	},
	'rhotacization': {
		'rhotacized': {}
	},
	'height': {
		'close': {
			'hi': 1, 'tense': 1
		},
		'close-mid': {
			'tense': 1
		},
		'mid': {},
		'near-close': {
			'hi': 1
		},
		'near-open': {
			'lo': 1
		},
		'open': {
			'lo': 1, 'tense': 1
		},
		'open-mid': {}
	},
	'friction': {
		'with-friction': {}
	},
	'roundedness': {
		'rounded': {
			'round': 1
		},
		'unrounded': {
			'round': -1
		}
	},
	'start': {
		'from-high': {
			'hireg': 1, 'hitone': 1
		},
		'from-low': {
			'loreg': 1
		},
		'from-mid': {},
		'from-mid-high': {
			'hireg': 1
		},
		'from-mid-low': {
			'loreg': 1, 'hitone': 1
		}
	},
	'contour': {
		'contour': {
			'contour': 1
		},
		'falling': {
			'falling': 1
		},
		'rising': {
			'rising': 1
		},
		'flat': {},
		'short': {}
	}
}

clts_feature_values = {}

for domain, value_dict in clts_features.items():
	for value, feature_dict in value_dict.items():
		clts_feature_values[value] = {'features': feature_dict, 'domain': domain}

joint_feature_definitions = {
	('glottal', 'stop'): {
		'cg': 1
	},
	('affricate', 'alveolar'): {
		'strid': 1
	},
	('affricate', 'labio-dental'): {
		'strid': 1
	},
	('affricate', 'post-alveolar'): {
		'strid': 1
	},
	('affricate', 'uvular'): {
		'strid': 1
	},
	('fricative', 'alveolar'): {
		'strid': 1
	},
	('fricative', 'labio-dental'): {
		'strid': 1
	},
	('fricative', 'post-alveolar'): {
		'strid': 1
	},
	('fricative', 'uvular'): {
		'strid': 1
	},
	('contour', 'from-high', 'via-mid-high'): {
		'falling': 1
	},
	('contour', 'from-high', 'via-mid'): {
		'falling': 1
	},
	('contour', 'from-high', 'via-mid-low'): {
		'falling': 1
	},
	('contour', 'from-high', 'via-low'): {
		'falling': 1
	},
	('contour', 'from-mid-high', 'via-high'): {
		'rising': 1
	},
	('contour', 'from-mid-high', 'via-mid'): {
		'falling': 1
	},
	('contour', 'from-mid-high', 'via-mid-low'): {
		'falling': 1
	},
	('contour', 'from-mid-high', 'via-low'): {
		'falling': 1
	},
	('contour', 'from-mid', 'via-high'): {
		'rising': 1
	},
	('contour', 'from-mid', 'via-mid-high'): {
		'rising': 1
	},
	('contour', 'from-mid', 'via-mid-low'): {
		'falling': 1
	},
	('contour', 'from-mid', 'via-low'): {
		'falling': 1
	},
	('contour', 'from-mid-low', 'via-high'): {
		'rising': 1
	},
	('contour', 'from-mid-low', 'via-mid-high'): {
		'rising': 1
	},
	('contour', 'from-mid-low', 'via-mid'): {
		'rising': 1
	},
	('contour', 'from-mid-low', 'via-low'): {
		'falling': 1
	},
	('contour', 'from-low', 'via-high'): {
		'rising': 1
	},
	('contour', 'from-low', 'via-mid-high'): {
		'rising': 1
	},
	('contour', 'from-low', 'via-mid'): {
		'rising': 1
	},
	('contour', 'from-low', 'via-mid-low'): {
		'rising': 1
	}
}
