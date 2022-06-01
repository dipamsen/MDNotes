from pandocfilters import toJSONFilter, Null


def behead(key, value, format, meta):
    if key == "Header" and value[0] == 1 and "title" not in meta:
        meta["title"] = {"t": "MetaInlines", "c": value[2]}
        return Null()


if __name__ == "__main__":
    toJSONFilter(behead)