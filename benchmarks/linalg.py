from asv_runner.benchmarks.mark import SkipNotImplemented

from . import xp


class LinearAlgebraSuiteBinary:
    params = (
        [
            ((0,), (0,)),
            ((1,), (1,)),
            ((2**8,) * 2, (2**8,)),
            ((2**12,) * 2, (2**12,)),
        ],
        [
            (xp.int8, xp.int16),
            (xp.float32, xp.float64),
            (xp.complex128, xp.float64),
            (xp.complex64, xp.complex128),
        ],
    )
    param_names = ["shapes", "dtypes"]

    def setup(self, shapes, dtypes):
        self.arrs = []
        self.scratch = []
        for sh, dt in zip(shapes, dtypes):
            self.arrs.append(xp.ones(sh, dtype=dt))
            self.scratch.append(xp.zeros(sh, dtype=dt))

    def time_matmul(self, shapes, dtypes):
        self.arrs[0] @ self.arrs[1]

    def time_vecdot(self, shapes, dtypes):
        xp.vecdot(self.arrs[0], self.arrs[1])


class LinearAlgebraSuiteUnary:
    params = (
        [(1, 1), (2**8, 1), (1, 2**8), (2**8,) * 2, (2**12, 1), (1, 2**12)],
        [xp.float32, xp.float64, xp.complex128],
    )
    param_names = ["shape", "dtype"]

    def setup(self, shape, dtype, *args):
        if shape[-1] != shape[-2]:
            self.arr = xp.ones(shape, dtype=dtype)
        else:
            self.arr = xp.broadcast_to(xp.eye(shape[-1], dtype=dtype), shape)

    if hasattr(xp, "linalg"):

        def time_cholesky(self, shape, dtype):
            if shape[-1] != shape[-2]:
                raise SkipNotImplemented(
                    "`xp.linalg.cholesky` only implemented for square matrices."
                )
            xp.linalg.cholesky(self.arr)

        def time_det(self, shape, dtype):
            if shape[-1] != shape[-2]:
                raise SkipNotImplemented(
                    "`xp.linalg.det` only implemented for square matrices."
                )
            xp.linalg.det(self.arr)

        def time_diagonal(self, shape, dtype):
            xp.linalg.diagonal(self.arr)

        def time_eigh(self, shape, dtype):
            if shape[-1] != shape[-2]:
                raise SkipNotImplemented(
                    "`xp.linalg.eigh` only implemented for square matrices."
                )

            xp.linalg.eigh(self.arr)

        def time_eigvalsh(self, shape, dtype):
            if shape[-1] != shape[-2]:
                raise SkipNotImplemented(
                    "`xp.linalg.eigvalsh` only implemented for square matrices."
                )

            xp.linalg.eigvalsh(self.arr)

        def time_inv(self, shape, dtype):
            if shape[-1] != shape[-2]:
                raise SkipNotImplemented(
                    "`xp.linalg.inv` only implemented for square matrices."
                )

            xp.linalg.inv(self.arr)

        def time_matrix_norm(self, shape, dtype, ord):
            xp.linalg.matrix_norm(self.arr, ord=ord)

        time_matrix_norm.params = list(params)
        time_matrix_norm.params.append(
            ["fro", "nuc", 1, 2, float("inf"), -1, -2, float("-inf")]
        )
        time_matrix_norm.param_names = param_names.copy()
        time_matrix_norm.param_names.append("fro")

        def time_matrix_power(self, shape, dtype, n):
            if shape[-1] != shape[-2]:
                raise SkipNotImplemented(
                    "`xp.linalg.matrix_power` only implemented for square matrices."
                )

            xp.linalg.matrix_power(self.arr, n)

        time_matrix_power.params = list(params)
        time_matrix_power.params.append([2**p for p in range(2, 8)])
        time_matrix_power.param_names = param_names.copy()
        time_matrix_power.param_names.append("n")

        def time_matrix_rank(self, shape, dtype):
            xp.linalg.matrix_rank(self.arr)

        def time_pinv(self, shape, dtype):
            xp.linalg.pinv(self.arr)
