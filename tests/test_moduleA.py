from __future__ import annotations

import skbuild_only.moduleA as m


def test_add_five():
    assert m.add_five(1) == 6
    assert m.add_five(0) == 5
    assert m.add_five(-1) == 4
