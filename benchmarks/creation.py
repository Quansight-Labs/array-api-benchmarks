from asv_runner.benchmarks.mark import SkipNotImplemented

from . import xp


class CreationSuite1D:
    params = (
        [0, 1, 2**10, 2**20],
        [xp.bool, xp.int8, xp.int16, xp.float32, xp.float64, xp.complex128],
    )
    param_names = ["n_elements", "dtype"]

    def setup(self, n_elements, dtype):
        self.l = [0] * n_elements

    def time_arange(self, n_elements, dtype):
        if dtype == xp.bool:
            raise SkipNotImplemented("`xp.arange` not implemented for `dtype=xp.bool`.")
        xp.arange(n_elements, dtype=dtype)

    def time_asarray(self, n_elements, dtype):
        xp.asarray(self.l, dtype=dtype)

    def time_empty(self, n_elements, dtype):
        xp.empty(n_elements, dtype=dtype)

    def time_zeros(self, n_elements, dtype):
        xp.zeros(n_elements, dtype=dtype)

    def time_full(self, n_elements, dtype):
        xp.full(n_elements, 7, dtype=dtype)


class CreationSuite2D:
    params = (
        [0, 1, 2**8, 2**10],
        [xp.bool, xp.int8, xp.int16, xp.float32, xp.float64, xp.complex128],
    )
    param_names = ["side_len", "dtype"]

    def setup(self, side_len, dtype):
        self.sample_1d = xp.ones(side_len, dtype=dtype)
        self.sample_2d = xp.ones((side_len, side_len), dtype=dtype)

    def time_eye(self, side_len, dtype):
        xp.eye(side_len, dtype=dtype)

    def time_meshgrid(self, side_len, dtype):
        xp.meshgrid(self.sample_1d, self.sample_1d)

    def time_tril(self, side_len, dtype):
        xp.tril(self.sample_2d)

    def time_triu(self, side_len, dtype):
        xp.triu(self.sample_2d)
