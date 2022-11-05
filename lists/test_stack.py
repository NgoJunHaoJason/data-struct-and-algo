from ._stack import Stack


def test_create_stack() -> None:
    stack = Stack()
    assert str(stack) == "Stack()"


def test_push_on_stack() -> None:
    stack = Stack()

    stack.push("A")
    stack.push("B")
    stack.push("C")

    assert str(stack) == "Stack(A, B, C)"


def test_pop_off_stack() -> None:
    stack = Stack()

    stack.push("A")
    stack.push("B")
    stack.push("C")

    value = stack.pop()

    assert str(stack) == "Stack(A, B)"
    assert value == "C"
