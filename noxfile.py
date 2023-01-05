from __future__ import annotations

import shutil
from pathlib import Path

import nox

DIR = Path(__file__).parent.resolve()

nox.options.sessions = ["lint", "coverage"]


@nox.session(tags=["annotations"], reuse_venv=True)
def stubgen(session: nox.Session) -> None:
    """(annotations) Generate stub type file for mypy from the generated C++ module"""
    session.install(".[dev]")
    session.install("mypy")
    session.run("stubgen", "-m", "skbuild_only._core", "-o", "src")


@nox.session(python=False, tags=["annotations"])
def mypy(session: nox.Session) -> None:
    """(annotations) Run mypy"""
    session.run("pipx", "run", "mypy")


@nox.session(python=False, tags=["style", "fix"])
def lint(session: nox.Session) -> None:
    """
    (quality) Run Black and isort.
    """
    # This needs to be installed into the package environment, and is slower
    # than a pre-commit check
    session.run("pipx", "run", "black", "src", *session.posargs)
    session.run("pipx", "run", "isort", "src", *session.posargs)


@nox.session(python=False, tags=["style"])
def flake(session: nox.Session) -> None:
    """(quality) Run Flake8"""
    session.run("pipx", "run", "pyproject-flake8")


@nox.session(tags=["full fix and style"])
@nox.parametrize("manual_stage", [True, False])
def precommit_checks(session: nox.Session, manual_stage) -> None:
    """
    (quality) Run all linters. Will be a bit long the first time only.
    Manual stage : check-manifest
    """
    session.install("pre-commit")
    if manual_stage:
        session.run("pre-commit", "run", "--all-files", "--hook-stage", "manual")
    else:
        session.run("pre-commit", "run", "--all-files")


@nox.session
def tests(session: nox.Session) -> None:
    """
    (test) Run tests.
    """
    session.install(".[test]")
    session.run("pytest", *session.posargs)


@nox.session
def coverage(session: nox.Session) -> None:
    """
    (test) Run tests and show coverage.
    """

    session.posargs.append("--cov=skbuild_only")
    # session.posargs.append("--cov-report")
    # session.posargs.append("html")
    tests(session)


@nox.session
def docs(session: nox.Session) -> None:
    """
    (docs) Build the docs. Pass "serve" to serve.
    """

    session.install(".[docs]")
    session.chdir("docs")
    session.run("sphinx-build", "-M", "html", ".", "_build")

    if session.posargs:
        if "serve" in session.posargs:
            print("Launching docs at http://localhost:8000/ - use Ctrl-C to quit")
            session.run("python", "-m", "http.server", "8000", "-d", "_build/html")
        else:
            session.warn("Unsupported argument to docs")


@nox.session(python=False)
def check_manifest(session: nox.Session) -> None:
    """(build) Run check-manifest"""
    session.run("pipx", "run", "check-manifest", "-c", "-v")


@nox.session
def build(session: nox.Session) -> None:
    """
    (build) Build an SDist and wheel.
    """

    build_p = DIR.joinpath("build")
    if build_p.exists():
        shutil.rmtree(build_p)

    session.install("build")
    session.run("python", "-m", "build")


@nox.session(python=False)
def requirements(session: nox.Session) -> None:
    """Generate a requirements.txt file."""
    session.run(
        "sh",
        "-c",
        r"pipx run pipdeptree -f --warn silence | grep -E '^[a-zA-Z0-9\-]+' | tee requirements.txt",
    )


@nox.session(python=False)
def lock_file(session: nox.Session) -> None:
    """Generate a locked-requirements.txt file."""
    session.run("sh", "-c", "pipx run pipdeptree -f | tee locked-requirements.txt")


@nox.session(python=False)
def clean(session: nox.Session) -> None:
    """Delete cache folders and files."""
    folders = [
        ".nox",
        "_skbuild",
        "__pycache__",
        ".pytest_cache",
        ".coverage",
        ".mypy_cache",
        "docs/_build",
        "docs/_generate",
    ]
    for folder in folders:
        session.run("rm", "-rf", folder)


@nox.session(python=False)
def install_precommit_hooks(session: nox.Session) -> None:
    """(installation) Install the pre-commit hooks."""
    session.run("pipx", "run", "pre-commit", "install")
