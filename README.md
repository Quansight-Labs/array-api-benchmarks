# array-api-benchmarks
Benchmarks for libraries conforming to the Array API Standard

## Usage
1. Create a `conda` environment with `asv` installed.
2. Create an `asv.conf.json` manually, following the [asv documentation](https://asv.readthedocs.io/en/stable/using.html#setting-up-a-new-benchmarking-project), or copy and edit `asv.conf.example.json`. Keep in mind that each configuration must have the environment variable `ARRAY_API_TESTS_MODULE`.
3. Use `asv` to run the benchmarks.
