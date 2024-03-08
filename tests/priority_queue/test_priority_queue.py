from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    assert priority_queue.is_priority({"qtd_linhas": 4}) is True
    assert priority_queue.is_priority({"qtd_linhas": 9}) is False
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(-1)
    priority_queue.enqueue({"qtd_linhas": 9})
    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 2})
    assert len(priority_queue) == 3
    assert priority_queue.dequeue() == {"qtd_linhas": 4}
    assert priority_queue.search(0) == {"qtd_linhas": 2}
