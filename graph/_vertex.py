class Vertex:
    def __init__(self, key: str, value: int) -> None:
        self.key = key
        self.value = value

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vertex) and other.key == self.key

    def __hash__(self) -> int:
        return hash(self.key)

    def __repr__(self) -> str:
        return f"Vertex({self.key}: {self.value})"
