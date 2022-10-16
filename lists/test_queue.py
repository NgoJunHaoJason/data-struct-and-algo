from .queue import Queue


def test_create_queue():
    queue = Queue()
    assert str(queue) == "Queue()"


def test_enqueue():
    queue = Queue()

    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)

    assert str(queue) == "Queue(2, 3, 5)"


def test_pop_off_queue():
    queue = Queue()

    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)

    value = queue.dequeue()

    assert str(queue) == "Queue(3, 5)"
    assert value == 2
