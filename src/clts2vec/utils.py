from clts2vec.features import binary_features


def vec_to_feature_set(vector):
    feature_set = set()

    for i, value in enumerate(vector):
        feature_name = binary_features[i]
        if value == 1:
            feature_set.add(f"+{feature_name}")
        elif value == -1:
            feature_set.add(f"-{feature_name}")

    return frozenset(feature_set)


def vec_to_str(vector):
    named_features = []
    for value, name in zip(vector, binary_features):
        if value == 1:
            named_features.append("+" + name)
        elif value == -1:
            named_features.append("-" + name)
        else:
            named_features.append("0_" + name)

    return ",".join(named_features)


def __format_dict_str(d, var_name=None):
    output = ""

    if var_name:
        output += f"{var_name} = "

    indent_lvl = 0
    dict_str = str(d)

    last_char = ""
    while dict_str:
        c = dict_str[0]
        dict_str = dict_str[1:]

        if c == "{":
            indent_lvl += 1
            output += c
            output += "\n"
            output += indent_lvl * "\t"
        elif c == "}":
            indent_lvl -= 1
            output += "\n"
            output += indent_lvl * "\t"
            output += c
        elif c == ",":
            output += c
            if last_char == "}":
                output += "\n"
                output += indent_lvl * "\t"
        else:
            if not (c == " " and (output.endswith("\t") or output.endswith("\n"))):
                output += c
                if dict_str.startswith("'pharyngeal':") or dict_str.startswith("'velaric':"):
                    output += "\n"
                    output += indent_lvl * "\t"
        last_char = c

    return output
