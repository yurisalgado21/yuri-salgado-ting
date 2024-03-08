"""from ting_file_management.file_process import process
from ting_file_management.queue import Queue
"""


def exists_word(word, instance):
    result_list = []
    for i in range(len(instance.queue)):
        search = instance.search(i)
        ocorrencias = [
            {"linha": idc + 1}
            for idc, line in enumerate(search["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]
        if ocorrencias:
            result_list.append(
                {
                    "palavra": word,
                    "arquivo": search["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )
        else:
            result_list = []

    return result_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


"""project = Queue()
process("statics/nome_pedro.txt", project)
word = exists_word("pedro", project)
print(word)
"""
