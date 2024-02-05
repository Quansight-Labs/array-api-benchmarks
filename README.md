# `array-api-benchmarks`
Benchmarks for libraries conforming to the Array API Standard

## Usage
1. Create a `conda` environment or a virtual environment with `asv` installed.
2. Create an `asv.conf.json` using one of the following methods:

    * Manually, by following the [`asv` documentation](https://asv.readthedocs.io/en/stable/using.html#setting-up-a-new-benchmarking-project),
    * By copying and editing `asv.conf.example.json`.

3. Use `asv` to run the benchmarks, see [this page](https://asv.readthedocs.io/en/stable/using.html#running-benchmarks) for the available options.

Please note that either you'll need add an environment variable `ARRAY_API_TESTS_MODULE` to each environment; or manually edit `benchmarks/__init__.py` to define the relevant variables.
