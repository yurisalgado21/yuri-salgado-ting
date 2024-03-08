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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
