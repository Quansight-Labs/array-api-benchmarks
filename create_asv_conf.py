#!/usr/bin/env python

import json
import os
import pathlib

ARRAY_API_MODULE = os.getenv("ARRAY_API_TESTS_MODULE")
REQUIREMENTS = os.getenv("ARRAY_API_BENCH_REQS")
PYTHON_VERSION = os.getenv("ARRAY_API_BENCH_PYTHON", "3.11")
PROJECT_REPO = os.getenv("ARRAY_API_REPO", ".")


def main() -> None:
    reqs = {}

    for req in REQUIREMENTS.split(";"):
        k, v = req.split("=")
        k, v = k.strip(), v.strip()
        reqs[k] = v

    conf = {
        "version": 1,
        "project": "array-api-benchmark",
        "project_url": "https://data-apis.org/array-api",
        "repo": PROJECT_REPO,
        "matrix": {"req": {}, "env": {}, "env_nobuild": {}},
        "environment_type": "conda",
        "include": [
            {
                "python": PYTHON_VERSION,
                "req": reqs,
                "env_nobuild": {"ARRAY_API_TESTS_MODULE": ARRAY_API_MODULE},
            },
        ],
        "exclude": [{"python": PYTHON_VERSION}],
    }

    if PROJECT_REPO == ".":
        conf.update(
            {
                "build_command": [],
                "install_command": [],
                "uninstall_command": [],
            }
        )

    with pathlib.Path("asv.conf.json").open("w") as f:
        json.dump(conf, f, indent=4)

    print("`asv.conf.json` successfully created.")


if __name__ == "__main__":
    main()
