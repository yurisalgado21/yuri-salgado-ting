import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido")
    try:
        with open(path_file, "r") as file:
            result_list = []
            content = file.read()
            content = content.split("\n")
            for line in content:
                result_list.append(line)
        return result_list
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
