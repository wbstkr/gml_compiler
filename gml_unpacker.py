import os

OUTLINE_FILENAME = "scriptlist"


def read_file(filename):
    with open(filename) as file:
        contents = list(map(str.rstrip, file.readlines()))
    return contents


def write_file(filename, string_list):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as file:
        file.write("\n".join(string_list))


def unpack_gml(filename, dir):
    global OUTLINE_FILENAME
    with open(filename) as file:
        scripts = "".join(file.readlines()).split("#define ")
    scripts = list(map(lambda x: x.strip().split("\n"), scripts[1:]))
    for script_contents in scripts:
        script_file = os.path.join(dir, f"{script_contents[0]}.gml")
        write_file(os.path.normcase(script_file), script_contents[1:])
    outline_contents = [element[0] for element in scripts]
    outline_file = os.path.join(dir, f"{OUTLINE_FILENAME}.txt")
    write_file(os.path.normpath(outline_file), outline_contents)


def pack_gml(dir, file):
    global OUTLINE_FILENAME
    outline_file = os.path.join(dir, f"{OUTLINE_FILENAME}.txt")
    gml_file = []
    for script_name in read_file(os.path.normpath(outline_file)):
        script_file = os.path.join(dir, f"{script_name}.gml")
        contents = read_file(os.path.normpath(script_file))
        contents.insert(0, f"#define {script_name}")
        contents.append("\n")
        gml_file.extend(contents)
    write_file(file, gml_file)
