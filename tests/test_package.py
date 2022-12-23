from __future__ import annotations

import skbuild_only as m


def test_version():
    assert m.__version__
    assert m.coucou == 4
