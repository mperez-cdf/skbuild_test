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

# Compilation

To install this package, we use scikit-build. This tool can create Python
packages as well as "binary extensions", ie. C++ code exposed in a Python
module. For C++ code, it uses CMake to create a build system and then compile
the C++ code. A main way to provide a Python module is to use Pybind11. The
CMakeLists.txt demonstrates how to download automatically Pybind11 and create a
Python module from C++ code.

# Task runner: Nox

Nox is a task runner. It automates common development tasks. Tasks are named
"sessions" in Nox. They are defined in the file `noxfile.py`.

To list all existing sessions: `pipx run nox -l`

## Annotations sessions

Static types are more and more used in python codes and allow to catch bugs
early and to produce well-thought codes. `mypy` is a static type checker: when
run, it will check that the type you annotated are coherent.

To run mypy, use `pipx run nox -s mypy`. It's configuration is in the tool.mypy
array of pyproject.toml.

When you use a C++ extension module, you have to create a stub file annotating
the C++ extension module. To create this stub file, use
`pipx run nox -s stubgen`.

## Code quality sessions

To ensure this code respect coding conventions, we use a couple of "linters".
Some directly modify your files, other will just point out things that you
should check.

### Pre-commit

Pre-commit is a tool to run numerous linters (including the next ones) before
being able to "git commit", to ensure that you only commit well-formated and
quality code.

Its configuration is in the file `.pre-commit-config.yaml`.

You can run all the pre-commit hooks at anytime with
`pipx run nox -s "precommit_checks(manual_stage=False)"`. From time to time,
change manual_stage to True to run more checks.

To install the hooks, so that they run before every commit, use
`pipx run nox -s install_precommit_hooks`.

### Flake8

pyproject-flake8 checks that coding rules are respected. For example, it will
detect blank lines with white spaces, the use of a bare except (it is
recommended to specify directly the exception you want to take care of)... It's
configuration is in the tool.flake8 array of pyproject.toml.

`pipx run nox -s flake` runs this tool.

### Black

Black modifies your files to respect formatting conventions. It's configuration
is in the tool.black array of pyproject.toml.

`pipx run nox -s lint` will run black and isort.

### isort

Isort is a tool to sort your import statements. It's configuration is in the
tool.isort array of pyproject.toml.

`pipx run nox -s lint` will run black and isort.

## Test sessions

To perform tests on your code, you can use pytest. It will detect every function
with a name beginning with "test\_" in the "tests" directory.

To run all the tests, use `pipx run nox -s tests`. Furthermore, to run all the
tests and have a coverage report, use `pipx run nox -s coverage`.

Pytest configuration is in the tool.pytest.ini_options array of pyproject.toml.
Coverage configuration is in the tool.coverage.run array of pyproject.toml.

**Note:** you can add a '-r' at the end of a nox command to re-use the same
virtual environment. The tests will run faster.

## Documentation sessions

See the docs/ directory. Build documentation with `pipx run nox -s docs`. It
uses sphinx to generate the documentation.

To serve locally the documentation, you can use `pipx run nox -s docs -- serve`.

**Note:** For small modifications, you can use `-R` at the end of a nox command
to re-user the same virtual environment and skip the installation part. checker

## Build sessions

### Manifest checker

The MANIFEST.in can be used to add essential non-python files to your package.
Before uploading your package anywhere, it's a good idea to run check-manifest,
which will list the source files under version control not included in your
MANIFEST.in.

To run check-manifest, use `pipx run nox -s check_manifest`. By default this
will not update automatically the MANIFEST.in file, but only show you files you
might have forgotten.

It's always a good idea to run check-manifest before building your package.

# Not yet tested

- documentation on readthedocs
- nox build (work with C++ ? don't know, should test)
- git(hub, lab) actions, cibuildwheels
- build & twine (first to gitlab repo)
