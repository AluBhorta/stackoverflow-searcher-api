
def get_dict_hash(d):
    return hash(frozenset(d.items()))
