from pandocfilters import toJSONFilter, Str, Math, RawInline, Para
import requests
# from mhchem import mhchem
# import re

# with open("filters/log.txt", "w") as f:
#     f.write("")
#     f.close()


def handlePu(s):
    res = requests.get(
        "https://mhchem-api.vercel.app/parseTex?tex=" + s)
    result = res.text
    if not result:
        log("Could not parse mhchem formula " + s + "\n")
        return "\\text{Could not parse}"
    return result


def caps(key, value, format, meta):
    log(key)
    log(str((value)))
    if key == "RawInline":
        if (format == "latex" or format == "tex") and ("\\pu{") in value[1]:
            result = handlePu(value[1])
            if result:
                return Math({'t': 'InlineMath'}, result)
    if key == "Math":
        if (format == "latex" or format == "tex") and ("\\pu{") in value[1]:
            result = handlePu(value[1])
            log(result)
            if result:
                return Math(value[0], result)
    # if key == "Math":
    #     print(value)
    #     m = re.search('\\\\pu{.*}', value)

    #     text = value.replace("(\\pu%b{})", handlePu)
    # if key == 'Str':
    #     return Str(value.upper())


def log(data):
    # write to file
    # with open("filters/log.txt", "a+") as f:
    #     f.write(data)
    #     f.write("\n")
    #     f.close()
    pass


if __name__ == "__main__":
    toJSONFilter(caps)
