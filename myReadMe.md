# Outils

## Flake8

Malheureusement ne peut pas être dans pyproject.toml donc autant le mettre dans son propre fichier pour se débarasser de setup.cfg



.flake8
```ini
[flake8]
extend-ignore = E203, E501, E722
extend-select = B902, B903, B904
per-file-ignores =
    tests/*: T
    noxfile.py: T
```
