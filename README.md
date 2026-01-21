# README


## Prerequisites


There are some prerequisites for this. Please create an account on [TestPypi](https://test.pypi.org), enable two factor authentication and then under your account settings please create an [API Token](https://test.pypi.org/help/#apitoken). Please save the token based on the instructions on TestPypi.

Create a github repository with the name picacl_<netid>, and clone it.

For the purpose of this we will use [uv](https://docs.astral.sh/uv/)

## How to create your package

While in your terminal please run:
```bash
cd picacl_<netid>
uv init --package picalc_<netid> –build_backend setuptools
```

And your package is ready. If you inspect the folder you should see the following tree:

```bash
├── pyproject.toml
├── README.md
├── src
│   ├── picalc_ip8725
│   │   ├── __init__.py
```

Inspect `pyproject.toml` to see the sections that are created. You now have a minimal python package

## Installing your package
Installation under `uv` is pretty straight forward. Just run:
```bash
uv sync
```

and `uv` will create the necessary environment variable, and install everything. To test your package just run:
```bash 
uv run picalc-<netid>
```

In case you want to access the environment variable that uv created you can do:
```bash
source .venv/bin/activate
```

## Adding dependencies

To add a depencency to your package you can run:
```bash
uv add numpy
```
and see how your `pyproject.toml` has changed.

You and also add your dependencies manually by updating the `dependencies` list in `pyproject.toml`

### Optional dependencies

There are two main types of optional dependencies. Those you want to ship as part of your package (called extras), and those that you want to have as part of your local development environment.

#### Dependency groups (development dependencies)

Dependency groups are used for dependencies that are only needed during development (like testing frameworks, doc parsers, etc.) and should not be shipped with your package.

To add a dependency group with uv:
```bash
uv add --group dev pytest
```

This will add a `[dependency-groups]` section to your `pyproject.toml`:
```toml
[dependency-groups]
dev = ["pytest>=8.0.0"]
```

You can create multiple groups for different purposes:
```bash
uv add --group docs sphinx
```

#### Optional dependencies (extras)

Optional dependencies (also called "extras") are dependencies that ship with your package but are not required for basic functionality. Users can choose to install them when needed.

To add an optional dependency with uv:
```bash
uv add --optional win pandas
```

This will add an `[project.optional-dependencies]` section to your `pyproject.toml`:
```toml
[project.optional-dependencies]
win = [
    "pandas>=2.3.3",
]
```

You can create multiple extras for different features:
```bash
uv add --optional viz matplotlib seaborn
```

## Adding new code

To add new functionality to your package, create Python modules inside the `src/picalc_<netid>/` directory. For example, this project includes a `pi` module that estimates π using a Monte Carlo simulation.

### Project structure

```bash
src/
└── picalc_<netid>/
    ├── __init__.py
    └── pi/
        ├── __init__.py
        └── pi.py
```

### Creating a submodule

1. Create a new folder inside your package directory:
```bash
mkdir src/picalc_<netid>/pi
```

2. Add an `__init__.py` file to make it a Python module. This file can export functions from your implementation:
```python
# src/picalc_<netid>/pi/__init__.py
from .pi import main
```

3. Add your implementation file (e.g., `pi.py`):
```python
# src/picalc_<netid>/pi/pi.py
import numpy as np
from multiprocessing import Pool
from functools import reduce

def estimate_pi(total_samples, n_processes=4):
    """Estimate π using map-reduce Monte Carlo simulation."""
    # ... implementation
    return pi_estimate

def main():
    n_samples = 10_000_000
    pi_est = estimate_pi(n_samples)
    print(f"Estimated π: {pi_est}")
```

### Using your module

Once your code is in place, you can use it in two ways. The first way is to import it as the following example:

```python
from picalc_<netid>.pi import main
main()
```

The second way is to call it as an executable, but first we need to add it. In your `pyproject.toml` under `[project.scripts]`
add the following:
```pyproject.toml
example-pi = "picalc_ip8725.pi.pi:main"
```

Installing and running under uv, will update your project:
```bash
uv sync
uv run example-pi
```

## Building your package
Building your package is straight forward. Run:
```bash
uv build
```

A new folder `dist` will appear with your built package. It should look like:
```
.
├── dist
│   ├── picalc_ip8725-0.2.0-py3-none-any.whl
│   └── picalc_ip8725-0.2.0.tar.gz
├── pyproject.toml
├── README.md
├── src
│   ├── picalc_ip8725
│   │   ├── __init__.py
│   │   ├── pi
│   │   │   ├── __init__.py
│   │   └── └──pi.py
└── uv.lock
```
