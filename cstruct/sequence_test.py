import unittest

from . import sequence

class SequenceTest(unittest.TestCase):
    def test_append(self) -> None:
        xs = sequence.Sequence[int]().append(1).append(2).append(3)
        self.assertEqual(xs, sequence.Sequence[int]([1, 2, 3]))

    def test_append_all(self) -> None:
        xs = sequence.Sequence[int]().append_all([1, 2, 3])
        self.assertEqual(xs, sequence.Sequence[int]([1, 2, 3]))

    def test_leq(self) -> None:
        x1 = sequence.Sequence[int]([1])
        x12 = sequence.Sequence[int]([1, 2])
        x2 = sequence.Sequence[int]([2])

        self.assertEqual(x1.leq(x1), True)
        self.assertEqual(x1.leq(x12), True)
        self.assertEqual(x12.leq(x1), False)
        self.assertEqual(x2.leq(x12), None)

    def test_glb(self) -> None:
        xs = sequence.Sequence[int]([1, 2, 4, 5])
        ys = sequence.Sequence[int]([1, 2, 3, 4, 5])
        self.assertEqual(xs.glb(ys), sequence.Sequence[int]([1, 2]))

    def test_compatible(self) -> None:
        x1 = sequence.Sequence[int]([1])
        x12 = sequence.Sequence[int]([1, 2])
        x2 = sequence.Sequence[int]([2])

        self.assertTrue(x1.compatible(x1))
        self.assertTrue(x1.compatible(x12))
        self.assertTrue(x12.compatible(x1))
        self.assertFalse(x2.compatible(x12))

    def test_lub(self) -> None:
        x1 = sequence.Sequence[int]([1])
        x12 = sequence.Sequence[int]([1, 2])
        x2 = sequence.Sequence[int]([2])

        self.assertEqual(x1.lub(x1), x1)
        self.assertEqual(x1.lub(x12), x12)
        self.assertEqual(x12.lub(x1), x12)
        self.assertEqual(x2.lub(x12), None)

    def test_contains(self) -> None:
        xs = sequence.Sequence[int]([1, 2, 3])
        self.assertTrue(xs.contains(1))
        self.assertTrue(xs.contains(2))
        self.assertTrue(xs.contains(3))
        self.assertFalse(xs.contains(4))

if __name__ == '__main__':
    unittest.main()
