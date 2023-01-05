# Installation

It is always recommended to use a
[python virtual environment](https://docs.python.org/3/library/venv.html): First
go to this directory, then type: `python -m venv .venv`, and activate it:
`source .venv/bin/activate` The following suppose that you are in this directory
and have activated the virtual environment.

## Local installation

To use the package locally: `pip install "."`

## Development

- To develop the package: `pip install ".[dev]"`

### Edition mode

To be able to see the change in your package without having to install it every
time, you can use the edition mode once: `pip install -e ".[dev]"`.

This mode is not directly compatible with the development of a C++ binary
extension. It will only work with the python part of the package. Every time you
change the C++ extension, to update locally the extension, you first need to
compile it with `pip install ".[dev]"` (without the edition mode !). It produces
a folder with the compile .so extension. Copy this .so file in your src folder.
Then you can go back to using editable mode for the python part with
`pip install -e ".[dev]"`.

# Tools

## Task runners

This skeleton includes two "task runners".

- Make for simple things,
- Nox for pythons scripts (to be preferred, but it might be too slow for
  repetitive tasks) They allow to perform various development tasks without the
  need to remember complex commands.

### Make

- `make -B clean`: remove some development artefacts
- `make -B requirements`: create a requirements.txt file
- `make -B lock_file`: create a locked-requirements.txt
- `make -B flake`: run flake on the project
- `make -B lint`: run all the pre-commit hooks
- `make -B simple_lint`: run black and isort
- `make -B install_precommit_hooks`: install the precommit hooks to git
- `make -B mypy`: run the static type checker
- `make -B check-manifest`: run the manifest checker
- `make -B tests`: install the package (check that you are in the right virtual
  environment first !) and launch tests.
- `make -B coverage`: install the package (check that you are in the right
  virtual environment first !) and launch tests and coverage.

### Nox

- `pipx run nox -l`: list all the possible nox sessions
- `pipx run nox -s lint`: run all the pre-commit hooks
- `pipx run nox -s simple_lint`: run black and isort
- `pipx run nox -s tests`: run the tests (no coverage)
- `pipx run nox -s coverage`: run the tests and show coverage
- `pipx run nox -s docs`: build the docs

## linters

To ensure this code respect coding conventions, we use a couple of "linters".
Some directly modify your files, other will just point out things that you
should check.

### Pre-commit

Pre-commit is a tool to run numerous linters (including the next ones) before
being able to "git commit", to ensure that you only commit well-formated and
quality code.

Its configuration is in the file `.pre-commit-config.yaml`.

You can run all the pre-commit hooks at anytime with `make lint` or
`pipx run nox -s lint`.

To install the hooks, so that they run before every commit, use
`make install_precommit_hooks`.

### Flake8

pyproject-flake8 checks that coding rules are respected. For example, it will
detect blank lines with white spaces, the use of a bare except (it is
recommended to specify directly the exception you want to take care of)... It's
configuration is in the tool.flake8 array of pyproject.toml.

`make flake` runs this tool.

### Black

Black modifies your files to respect formatting conventions. It's configuration
is in the tool.black array of pyproject.toml.

`make simple_lint` or `pipx run nox -s simple_lint` will run black and isort.

### isort

Isort is a tool to sort your import statements. It's configuration is in the
tool.isort array of pyproject.toml.

`make simple_lint` or `pipx run nox -s simple_lint` will run black and isort.

## Static type checker

Static types are more and more used in python codes and allow to catch bugs
early and to produce well-thought codes. `mypy` is a static type checker: when
run, it will check that the type you annotated are coherent.

To run mypy, use `make mypy`. It's configuration is in the tool.mypy array of
pyproject.toml.

## Manifest checker

The MANIFEST.in can be used to add essential non-python files to your package.
Before uploading your package anywhere, it's a good idea to run check-manifest,
which will list the source files under version control not included in your
MANIFEST.in.

To run check-manifest, use `make check-manifest`. By default this will not
update automatically the MANIFEST.in file, but only show you files you might
have forgotten.

## Test suite

To perform tests on your code, you can use pytest. It will detect every function
with a name beginning with "test\_" in the "tests" directory.

To run all the tests, use `make tests` or `pipx run nox -s tests`. Furthermore,
to run all the tests and have a coverage report, use `make coverage` or
`pipx run nox -s coverage`.

Pytest configuration is in the tool.pytest.ini_options array of pyproject.toml.
Coverage configuration is in the tool.coverage.run array of pyproject.toml.

# Compilation

To install this package, we use scikit-build. This tool can create Python
packages as well as "binary extensions", ie. C++ code exposed in a Python
module. For C++ code, it uses CMake to create a build system and then compile
the C++ code. A main way to provide a Python module is to use Pybind11. The
CMakeLists.txt demonstrates how to download automatically Pybind11 and create a
Python module from C++ code.

# Documentation

See the docs/ directory. Build documentation with `nox -s docs`. It uses sphinx
to generate the documentation.

# Not yet tested

- documentation on readthedocs
- nox build (work with C++ ? don't know, should test)
- git(hub, lab) actions, cibuildwheels
- build & twine (first to gitlab repo)
