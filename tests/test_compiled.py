from __future__ import annotations

import skbuild_only._core as m


def test_add():
    assert m.add(2, 3) == 5


def test_subtract():
    assert m.subtract(7, 5) == 2


def test_glfw():
    assert m.test_glfw() == "GLFW initialized successfully !\nGLFW terminated now."
