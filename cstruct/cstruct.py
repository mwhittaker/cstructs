from typing import Any, List, Generic, Optional, TypeVar

C = TypeVar('C')
Cmd = TypeVar('Cmd')

class CStruct(Generic[C, Cmd]):
    """A command-structure set, as defined in [1].

    A command-structure set, or c-struct, is an algebraic structure that
    consists of

      - a set of commands Cmd,
      - a set of c-structs CStruct,
      - a distinguished bottom element bot in CStruct, and
      - an append operator +: CStruct x Cmd -> CStruct.

    A couple of things to note:

      - We extend the + operator to sequences of commands in the obvious way: v
        + [C1, C2, ..., Cn] = ((v + C1) + C2) + ... + Cn.
      - We say v <= w if there exists a sequence of commands sigma such that w
        = v + sigma.
      - Let Str(P) be the set of c-structs that can be formed from sequences of
        commands formed from P.
      - Say c-structs v and w are compatible if they have an upper bound.
      - We say that a c-struct v contains a command C if v is constructible
        from some set of commands containing C.

    A c-struct must satisfy the following axioms:

        1. CStruct = {bot + sigma | sigma in Seq(Cmd)}
        2. <= is a partial order.
        3. For any set P of commands and any c-structs u, v, and w in Str(P):
            - the glb of v and w exists and is in Str(P).
            - the v and w are compatible, then the lub of v and w exists and is
              in Str(P).
            - If {u, v, w} is compatible, then u and (v lub w) are compatible.
        4. For any command C and compatible c-structs v and w, if v and w both
           contain C, then the glb also contains C.

    [1]: https://scholar.google.com/scholar?cluster=16508749535628900004
    """
    def append(self, cmd: Cmd) -> C:
        raise NotImplementedError()

    def leq(self, other: C) -> Optional[bool]:
        raise NotImplementedError()

    def glb(self, other: C) -> C:
        raise NotImplementedError()

    def compatible(self, other: C) -> bool:
        raise NotImplementedError()

    def lub(self, other: C) -> Optional[C]:
        raise NotImplementedError()

    def contains(self, cmd: Cmd) -> bool:
        raise NotImplementedError()

    def append_all(self, cmds: List[Cmd]) -> C:
        # This confuses mypy, so we go with Any.
        cstruct: Any = self
        for cmd in cmds:
            cstruct = cstruct.append(cmd)
        return cstruct
