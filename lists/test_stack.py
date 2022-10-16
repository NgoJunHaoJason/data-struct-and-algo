from .stack import Stack


def test_create_stack():
    stack = Stack()
    assert str(stack) == "Stack()"


def test_push_on_stack():
    stack = Stack()

    stack.push(2)
    stack.push(3)
    stack.push(5)

    assert str(stack) == "Stack(2, 3, 5)"


def test_pop_off_stack():
    stack = Stack()

    stack.push(2)
    stack.push(3)
    stack.push(5)

    value = stack.pop()

    assert str(stack) == "Stack(2, 3)"
    assert value == 5
