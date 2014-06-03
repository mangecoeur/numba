from __future__ import absolute_import, print_function, division
import numpy as np
from numbapro import vectorize
from numbapro.testsupport import unittest


class TestVectorizeComplex(unittest.TestCase):
    def test_vectorize_complex(self):
        @vectorize(['complex128(complex128)'], target='gpu')
        def vcomp(a):
            return a * a + 1.

        A = np.arange(5, dtype=np.complex128)
        B = vcomp(A)
        self.assertTrue(np.allclose(A * A + 1., B))


if __name__ == '__main__':
    unittest.main()