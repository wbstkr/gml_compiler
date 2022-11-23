import os

DIRECTORY = 'scripts'
OUTLINE = 'script_list'
CHARM = open('player.txt').readline()[1:-2]


def read_file(filename):
    with open(filename) as file:
        contents = list(map(str.rstrip, file.readlines()))
    return contents


def write_file(filename, string_list):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        file.write('\n'.join(string_list))


def compile_gml(filename, outline_file):
    gml_file = []
    for script_name in read_file(outline_file):
        contents = read_file(DIRECTORY + '/' + script_name + '.gml')
        contents.insert(0, '#define ' + script_name)
        contents.append('\n')
        gml_file.extend(contents)
    write_file(filename, gml_file)


def decompile_gml(filename):
    with open(filename) as file:
        contents = ''.join(file.readlines()).split('#define ')
    contents = list(map(lambda x: x.strip().split('\n'), contents[1:]))
    for content in contents:
        write_file(DIRECTORY + '/' + content[0] + '.gml', content[1:])
    outline = [element[0] for element in contents]
    write_file(DIRECTORY + '/' + OUTLINE + '.txt', outline)


if __name__ == "__main__":
    user_input = input('(D)ecompile / (C)ompile / (Q)uit ? ').lower()[0]
    if user_input == 'd':
        decompile_gml(CHARM + '.gml')
    elif user_input == 'c':
        compile_gml('./' + CHARM + '.gml', DIRECTORY + '/' + OUTLINE + '.txt')
