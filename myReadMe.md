# Installation

It is always recommended to use a [python virtual environment](https://docs.python.org/3/library/venv.html):
First go to this directory, then type: `python -m venv .venv`, and activate it: `source .venv/bin/activate`
The following suppose that you are in this directory and have activated the virtual environment.
## Local installation
To use the package locally: `pip install "."`

## Development
- To develop the package: `pip install ".[dev]"`

### Edition mode
To be able to see the change in your package without having to install it every time, you can use the edition mode once:
`pip install -e ".[dev]"`.

This mode is not directly compatible with the development of a C++ binary extension. It will only work with the python part of the package.
Every time you change the C++ extension, to update locally the extension, you first need to compile it with `pip install ".[dev]"` (without the edition mode !). It produces a folder with the compile .so extension. Copy this .so file in your src folder.
Then you can go back to using editable mode for the python part with `pip install -e ".[dev]"`.
# Tools

This skeleton includes two "task runners".
- Make for simple things,
- Nox for pythons scripts (to be preferred, but it might be too slow for repetitive tasks)

## Make

- `make clean`: remove some development artefacts
- `make requirements`: create a requirements.txt file
- `make lock_file`: create a locked-requirements.txt
- `make flake`: run flake on the project
- `make lint`: run all the pre-commit hooks
- `make simple_lint`: run black and isort
- `make test`: install the package (check that you are in the right virtual environment first !) and launch tests and coverage.


## Nox
- `pipx run nox -l`: list all the possible nox sessions
- `pipx run nox -s lint`: run all the pre-commit hooks
- `pipx run nox -s simple_lint`: run black and isort
- `pipx run nox -s tests`: run the tests (no coverage)
- `pipx run nox -s coverage`: run the tests and show coverage
- `pipx run nox -s docs`: build the docs

# Not yet tested

- documentation with sphinx
- documentation on readthedocs
- other thing than setuptools_scm (deprecation soon ?) or documentation on ho setuptools_scm work
- nox build (work with C++ ? don't know, should test)
- git(hub, lab) actions
- build & twine (first to gitlab repo)
