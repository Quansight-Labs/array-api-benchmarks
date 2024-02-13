from . import xp


class IndexingSuite1D:
    params = [
        [(1,), (2**8,), (2**16,), (2**20,)],
        [xp.bool, xp.int8, xp.int16, xp.float32, xp.float64, xp.complex128],
    ]
    param_names = ["shape", "dtype"]

    def setup(self, shape, dtype, *args):
        self.arr = xp.ones(shape, dtype=dtype)

    def time_element(self, shape, dtype):
        self.arr[0]

    def time_slice(self, shape, dtype, step):
        self.arr[0 : shape[0] // 2 : step]

    time_slice.params = params.copy()
    time_slice.params.append([None, 1, 2, 8, 64])
    time_slice.param_names = param_names.copy()
    time_slice.param_names.append("step")


class IndexingSuite2D:
    params = [
        [(1, 1), (2**8,) * 2, (2**10,) * 2],
        [xp.bool, xp.int8, xp.int16, xp.float32, xp.float64, xp.complex128],
    ]
    param_names = ["shape", "dtype"]

    def setup(self, shape, dtype, *args):
        self.arr = xp.ones(shape, dtype=dtype)

    def time_element(self, shape, dtype):
        self.arr[0, 0]

    def time_slice_axis0(self, shape, dtype, step):
        self.arr[0 : shape[0] // 2 : step, :]

    def time_slice_axis1(self, shape, dtype, step):
        self.arr[:, 0 : shape[0] // 2 : step]

    def time_slice_axes(self, shape, dtype, step):
        self.arr[0 : shape[0] // 2 : step, 0 : shape[0] // 2 : step]

    time_slice_axis0.params = params.copy()
    time_slice_axis0.params.append([None, 1, 2, 8, 64])
    time_slice_axis0.param_names = param_names.copy()
    time_slice_axis0.param_names.append("step")

    time_slice_axis1.params = time_slice_axis0.params
    time_slice_axis1.param_names = time_slice_axis0.param_names

    time_slice_axes.params = time_slice_axis0.params
    time_slice_axes.param_names = time_slice_axis0.param_names


class IndexingSuite3D:
    params = [
        [(1, 1, 1), (2**7,) * 3],
        [xp.bool, xp.int8, xp.int16, xp.float32, xp.float64, xp.complex128],
    ]
    param_names = ["shape", "dtype"]

    def setup(self, shape, dtype, *args):
        self.arr = xp.ones(shape, dtype=dtype)

    def time_element(self, shape, dtype):
        self.arr[0, 0, 0]

    def time_slice_axis0(self, shape, dtype, step):
        self.arr[0 : shape[0] // 2 : step, :, :]

    def time_slice_axis1(self, shape, dtype, step):
        self.arr[:, 0 : shape[0] // 2 : step, :]

    def time_slice_axis2(self, shape, dtype, step):
        self.arr[:, :, 0 : shape[0] // 2 : step]

    def time_slice_axes(self, shape, dtype, step):
        self.arr[
            0 : shape[0] // 2 : step, 0 : shape[0] // 2 : step, 0 : shape[0] // 2 : step
        ]

    time_slice_axis0.params = params.copy()
    time_slice_axis0.params.append([None, 1, 2, 8, 64])
    time_slice_axis0.param_names = param_names.copy()
    time_slice_axis0.param_names.append("step")

    time_slice_axis1.params = time_slice_axis0.params
    time_slice_axis1.param_names = time_slice_axis0.param_names

    time_slice_axis2.params = time_slice_axis0.params
    time_slice_axis2.param_names = time_slice_axis0.param_names

    time_slice_axes.params = time_slice_axis0.params
    time_slice_axes.param_names = time_slice_axis0.param_names
