import json
import os
import pathlib

ARRAY_API_MODULE = os.getenv("ARRAY_API_TESTS_MODULE", "array_api_strict")
PYTHON_VERSION = "3.11"
PROJECT_REPO = "."

def main() -> None:
    conf = {
        "version": 1,
        "project": "array-api-benchmarks",
        "project_url": "https://data-apis.org/array-api",
        "repo": PROJECT_REPO,
        "branches": ["main"],
        "pythons": [PYTHON_VERSION],
        "matrix": {
            "req": {
                "pip+array-api-strict": ""
            },
            "env_nobuild": {
                "ARRAY_API_TESTS_MODULE": ARRAY_API_MODULE
            },
            "env": {},
        },
        "environment_type": "conda",
    }

    with pathlib.Path("asv.conf.json").open("w") as f:
        json.dump(conf, f, indent=4)

    print("`asv.conf.json` successfully created.")

if __name__ == "__main__":
    main()
