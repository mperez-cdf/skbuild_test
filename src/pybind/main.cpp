// Here comes pybind11's exposition code
#include <pybind11/pybind11.h>
namespace py = pybind11;
using namespace pybind11::literals;

#include "../cpp/my_lib.h"  // To find add and test_glfw functions

PYBIND11_MODULE(_core, m) {
  m.doc() = R"pbdoc(
Documentation for _core module
------------------------------
.. currentmodule:: skbuild_only._core
.. autosummary::
  :toctree: _generate

  add
  subtract
  test_glfw
)pbdoc";

  m.def("add", &add, "i"_a, "j"_a, R"pbdoc(
Add two numbers
Some other explanation about the add function.
)pbdoc");

  m.def(
      "subtract", [](int i, int j) { return i - j; }, "i"_a, "j"_a, R"pbdoc(
Subtract two numbers
Some other explanation about the subtract function.
)pbdoc");

  m.def("test_glfw", &test_glfw, R"pbdoc(
Test if GLFW is linked to this program.
Some other explanation about the test_glfw function.
)pbdoc");
}
