from clts2vec.features import binary_features, clts_features, clts_feature_values


# whenever a feature is defined, all three central objects [binary_features, clts_features, clts_feature_values]
# must be updated accordingly

def delete_feature(feature):
    # delete from binary_features
    if feature in binary_features:
        binary_features.remove(feature)

    # delete from clts_features
    for value_dict in clts_features.values():
        for feature_dict in value_dict.values():
            if feature in feature_dict:
                feature_dict.pop(feature)

    # delete from clts_feature_values
    for value_dict in clts_feature_values.values():
        for feature_dict in value_dict.values():
            if feature in feature_dict:
                feature_dict.pop(feature)


def redefine_feature(clts_feature_value, features):
    """
    redefine the mapping from a given CLTS feature value to binary features.
    novel binary features will automatically be added to the feature inventory.
    :param clts_feature_value: the CLTS feature value to be modified
    :param features: the new binary feature definition
    """
    if clts_feature_value not in clts_feature_values:
        raise KeyError(f"'{clts_feature_value}' is not a valid CLTS feature value.")

    feature_domain = clts_feature_values[clts_feature_value]["domain"]
    old_feature_dict = clts_feature_values[clts_feature_value]["features"]

    for feature, value in features.items():
        old_feature_dict[feature] = value
        if feature not in binary_features:
            binary_features.append(feature)

    clts_feature_values[clts_feature_value]["features"] = old_feature_dict
    clts_features[feature_domain][clts_feature_value] = old_feature_dict
