def get_positive_value(atom):
    return atom > 0


def get_rule_loop(rules, atoms):
    loop_rules = list()
    for rule in rules:

        if len(atoms.intersection(rule[0])) > 0 and len(atoms.intersection(rule[1])) > 0:
            # we use the observation that rule must contain two occurrences of atoms or more in rule to be part of loop.
            loop_rules.append(rule)
    return loop_rules


def get_rule_No_loop(rules, atoms):
    NoLoop_rules = list()
    for rule in rules:

        if len(atoms.intersection(rule[0])) > 0 and len(atoms.intersection(rule[1])) == 0:
            # we use the observation that rule must contain two occurrences of atoms or more in rule to be part of loop.
            NoLoop_rules.append(rule)
    return NoLoop_rules


def read_cfg(cfg_file):
    import json

    with open(cfg_file) as c:
        cfg = json.load(c)
    return cfg


def flatten_cfg(dd, filter=[], separator='.', prefix=''):
    if prefix.startswith(tuple(filter)):
        return {}

    if isinstance(dd, dict):
        return {prefix + separator + k if prefix else k: v
                for kk, vv in dd.items()
                for k, v in flatten_cfg(vv, filter, separator, kk).items()
                if not (prefix + separator + k).startswith(tuple(filter))
                }
    elif isinstance(dd, list):
        return {prefix: " ".join(dd)}
    else:
        return {prefix: dd}
