from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    name_exists = instance.get_by_name(path_file)
    if name_exists is None:
        file_list = txt_importer(path_file)
        dictionary = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_list),
            "linhas_do_arquivo": file_list,
        }
        instance.enqueue(dictionary)
        print(dictionary, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return
    file = instance.search(0)
    file = file["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
