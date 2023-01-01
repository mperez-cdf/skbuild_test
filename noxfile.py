from __future__ import annotations

import shutil
from pathlib import Path

import nox

DIR = Path(__file__).parent.resolve()

nox.options.sessions = ["lint", "tests"]


@nox.session
def lint(session: nox.Session) -> None:
    """
    Run the linter.
    """
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", *session.posargs)


@nox.session
def lint(session: nox.Session) -> None:
    """
    Run Black and isort.
    """
    # This needs to be installed into the package environment, and is slower
    # than a pre-commit check
    session.install(".", "black")
    session.install(".", "isort")
    session.run("black", "src", *session.posargs)
    session.run("isort", "src", *session.posargs)


@nox.session
def tests(session: nox.Session) -> None:
    """
    Run the unit and regular tests.
    """
    session.install(".[test]")
    session.run("pytest", *session.posargs)


@nox.session
def coverage(session: nox.Session) -> None:
    """
    Run tests and compute coverage.
    """

    session.posargs.append("--cov=skbuild_only")
    tests(session)


@nox.session
def docs(session: nox.Session) -> None:
    """
    Build the docs. Pass "serve" to serve.
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


@nox.session
def build(session: nox.Session) -> None:
    """
    Build an SDist and wheel.
    """

    build_p = DIR.joinpath("build")
    if build_p.exists():
        shutil.rmtree(build_p)

    session.install("build")
    session.run("python", "-m", "build")


@nox.session
def release(session: nox.Session) -> None:
    """
    Kicks off an automated release process by creating and pushing a new tag.

    Invokes bump2version with the posarg setting the version.

    Usage:
    $ nox -s release -- [major|minor|patch]
    """
    parser = argparse.ArgumentParser(description="Release a semver version.")
    parser.add_argument(
        "version",
        type=str,
        nargs=1,
        help="The type of semver release to make.",
        choices={"major", "minor", "patch"},
    )
    args: argparse.Namespace = parser.parse_args(args=session.posargs)
    version: str = args.version.pop()

    # If we get here, we should be good to go
    # Let's do a final check for safety
    confirm = input(
        f"You are about to bump the {version!r} version. Are you sure? [y/n]: "
    )

    # Abort on anything other than 'y'
    if confirm.lower().strip() != "y":
        session.error(f"You said no when prompted to bump the {version!r} version.")


    session.install("bump2version")

    session.log(f"Bumping the {version!r} version")
    session.run("bump2version", version)

    session.log("Pushing the new tag")
    session.run("git", "push", external=True)
    session.run("git", "push", "--tags", external=True)