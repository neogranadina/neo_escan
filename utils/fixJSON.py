import json

def fixJSON(path2JSON):
    with open(path2JSON, "r") as fp:
        readlines = fp.readlines()

    # delete all \x00 characters

    readlines = [line.replace("\x00", "") for line in readlines]

    # join all lines

    readlines = "".join(readlines)

    # convert to json

    readlines = json.loads(readlines)

    # save new json file

    with open(path2JSON, "w") as fp:
        json.dump(readlines, fp, indent=4, ensure_ascii=False)
