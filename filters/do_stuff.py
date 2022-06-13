from pandocfilters import toJSONFilter, Str
# from mhchem import mhchem


def caps(key, value, format, meta):
    if key == 'Str':
        return Str(value.upper())


if __name__ == "__main__":
    toJSONFilter(caps)
