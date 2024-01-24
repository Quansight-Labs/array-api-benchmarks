from asv_runner.benchmarks.mark import SkipNotImplemented

from . import xp


class ElemwiseUnarySuite:
    params = (
        [0, 1, (2**8,) * 2, (2**12,) * 2],
        [xp.bool, xp.int8, xp.int16, xp.float32, xp.float64, xp.complex128],
    )
    param_names = ["shape", "dtype"]

    def setup(self, shape, dtype):
        self.arr = xp.ones(shape, dtype=dtype)

    def time_pos(self, n_elements, dtype):
        if not xp.isdtype(dtype, "numeric"):
            raise SkipNotImplemented(
                "`operator.pos` only implemented for numeric dtypes."
            )
        +self.arr

    def time_neg(self, n_elements, dtype):
        if not xp.isdtype(dtype, "numeric"):
            raise SkipNotImplemented(
                "`operator.neg` only implemented for numeric dtypes."
            )
        -self.arr

    def time_invert(self, n_elements, dtype):
        if not xp.isdtype(dtype, ("integral", "bool")):
            raise SkipNotImplemented(
                "`operator.neg` only implemented for numeric dtypes."
            )
        ~self.arr

    def time_abs(self, n_elements, dtype):
        if not xp.isdtype(dtype, "numeric"):
            raise SkipNotImplemented("`xp.abs` only implemented for numeric dtypes.")
        xp.abs(self.arr)

    def time_acos(self, n_elements, dtype):
        if not xp.isdtype(dtype, ("real floating", "complex floating")):
            raise SkipNotImplemented(
                "`xp.acos` only implemented for floating point dtypes."
            )
        xp.acos(self.arr)

    def time_acosh(self, n_elements, dtype):
        if not xp.isdtype(dtype, ("real floating", "complex floating")):
            raise SkipNotImplemented(
                "`xp.acosh` only implemented for floating point dtypes."
            )
        xp.acosh(self.arr)

    def time_cos(self, n_elements, dtype):
        if not xp.isdtype(dtype, ("real floating", "complex floating")):
            raise SkipNotImplemented(
                "`xp.cos` only implemented for floating point dtypes."
            )
        xp.cos(self.arr)

    def time_cosh(self, n_elements, dtype):
        if not xp.isdtype(dtype, ("real floating", "complex floating")):
            raise SkipNotImplemented(
                "`xp.cosh` only implemented for floating point dtypes."
            )
        xp.cosh(self.arr)


class ElemwiseBinarySuite:
    params = (
        [
            (0, 0),
            (1, 1),
            ((2**8,) * 2, 2**8),
            ((2**12,) * 2, 2**12),
            ((2**12,) * 2,) * 2,
        ],
        [
            (xp.bool, xp.bool),
            (xp.int8, xp.int16),
            (xp.float32, xp.float64),
            (xp.complex128, xp.float64),
            (xp.complex64, xp.complex128),
        ],
    )
    param_names = ["shapes", "dtypes"]

    def setup(self, shapes, dtypes):
        self.arrs = []
        for sh, dt in zip(shapes, dtypes):
            self.arrs.append(xp.ones(sh, dtype=dt))

    def time_add(self, shapes, dtypes):
        self.arrs[0] + self.arrs[1]
