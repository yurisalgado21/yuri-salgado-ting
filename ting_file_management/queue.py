from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def search(self, index):
        if (
            isinstance(index, int)
            and index >= 0
            and index <= len(self.queue) - 1
        ):
            return self.queue[index]
        raise IndexError("Índice Inválido ou Inexistente")

    def get_by_name(self, name):
        for i in self.queue:
            if i["nome_do_arquivo"] == name:
                return i
        return None
