from typing import List, Generic, Optional, TypeVar

from . import cstruct

T = TypeVar('T')
def _is_prefix(xs: List[T], ys: List[T]) -> bool:
    if len(xs) > len(ys):
        return False
    return ys[:len(xs)] == xs

Cmd = TypeVar('Cmd')
class Sequence(cstruct.CStruct['Sequence[Cmd]', Cmd]):
    def __init__(self, xs=None):
        self.xs = xs or []

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Sequence):
            return False
        return self.xs == other.xs

    def __str__(self) -> str:
        return str(self.xs)

    def __repr__(self) -> str:
        return str(self)

    def append(self, cmd: Cmd) -> 'Sequence[Cmd]':
        return Sequence(self.xs + [cmd])

    def leq(self, other: 'Sequence[Cmd]') -> Optional[bool]:
        if _is_prefix(self.xs, other.xs):
            return True
        if _is_prefix(other.xs, self.xs):
            return False
        return None

    def glb(self, other: 'Sequence[Cmd]') -> 'Sequence[Cmd]':
        for i in range(max(len(self.xs), len(other.xs)), 0, -1):
            if (self.xs[:i] == other.xs[:i]):
                return Sequence(self.xs[:i])
        return Sequence([])

    def compatible(self, other: 'Sequence[Cmd]') -> bool:
        return _is_prefix(self.xs, other.xs) or _is_prefix(other.xs, self.xs)

    def lub(self, other: 'Sequence[Cmd]') -> Optional['Sequence[Cmd]']:
        if not self.compatible(other):
            return None

        return self if len(self.xs) >= len(other.xs) else other

    def contains(self, cmd: Cmd) -> bool:
        return cmd in self.xs
