clean:
	rm -rf .nox _skbuild __pycache__ .pytest_cache .coverage .mypy_cache

requirements:
	pipx run pipdeptree -f --warn silence | grep -E '^[a-zA-Z0-9\-]+' | tee requirements.txt

lock_file:
	pipx run pipdeptree -f | tee locked-requirements.txt

flake:
	pipx run pyproject-flake8

lint:
	pipx run pre-commit run --all-files

simple_lint:
	pipx run black src && pipx run isort src

test:
	pip install .[test] && pytest --cov=skbuild_only
