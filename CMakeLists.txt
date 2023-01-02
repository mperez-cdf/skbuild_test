# Always try to give ranges for versions (3.12+), from minimal version to
# maximal version tested
cmake_minimum_required(VERSION 3.11...3.22) # 3.12 needed to FetchContent

# Range syntax was added to CMake 3.12. On lesser version it will not exactly
# work so to really fix the version policy we add this
if(${CMAKE_VERSION} VERSION_LESS 3.12)
  cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})
endif()

# Project declaration
set(VERSION_STRING "0.1")
project(skbuild_only VERSION ${VERSION_STRING})

# ======= Get Pybind11 ==========
include(FetchContent) # CMake 3.11+
# Check if version is less than CMake 3.14 to add the FetchContent_MakeAvailable
# feature
if(${CMAKE_VERSION} VERSION_LESS 3.14)
  macro(FetchContent_MakeAvailable NAME)
    FetchContent_GetProperties(${NAME}) # first step to get NAME_* variables.
    if(NOT ${NAME}_POPULATED)
      FetchContent_Populate(
        ${NAME}) # Check NAME_POPULATED, and if not populated, use
                 # FetchContent_Populate(NAME)
      add_subdirectory(${${NAME}_SOURCE_DIR} ${${NAME}_BINARY_DIR}
      )# if a package, add_subdirectory
    endif()
  endmacro()
endif()

# download pybind11
FetchContent_Declare(
  pybind11
  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.9.2.tar.gz
  URL_HASH
    SHA256=6bd528c4dbe2276635dc787b6b1f2e5316cf6b49ee3e150264e455a0d68d19c1)

FetchContent_MakeAvailable(pybind11) # include pybind11 and their variables
# ======== Pybind11 acquired ==========

# Now we create a _core target python module thanks to source code at
# src/main.cpp
pybind11_add_module(_core MODULE src/main.cpp)
# Install the _core.so python module
install(TARGETS _core DESTINATION .)
