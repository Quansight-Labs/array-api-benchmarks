import os
from importlib import import_module

__all__ = ["xp", "api_version", "xps"]


# You can comment the following out and instead import the specific array module
# you want to test, e.g. `import numpy.array_api as xp`.
if "ARRAY_API_TESTS_MODULE" in os.environ:
    xp_name = os.environ["ARRAY_API_TESTS_MODULE"]
    _module, _sub = xp_name, None
    if "." in xp_name:
        _module, _sub = xp_name.split(".", 1)
    xp = import_module(_module)
    if _sub:
        try:
            xp = getattr(xp, _sub)
        except AttributeError:
            # _sub may be a submodule that needs to be imported. WE can't
            # do this in every case because some array modules are not
            # submodules that can be imported (like mxnet.nd).
            xp = import_module(xp_name)
else:
    raise RuntimeError(
        "No array module specified - either edit __init__.py or set the "
        "ARRAY_API_TESTS_MODULE environment variable."
    )


api_version = os.getenv(
    "ARRAY_API_TESTS_VERSION", getattr(xp, "__array_api_version__", "2021.12")
)
