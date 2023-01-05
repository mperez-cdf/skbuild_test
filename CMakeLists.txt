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
    SHA256=6bd528c4dbe2276635dc787b6b1f2e5316cf6b49ee3e150264e455a0d68d19c1
  DOWNLOAD_EXTRACT_TIMESTAMP true)

FetchContent_MakeAvailable(pybind11) # include pybind11 and their variables
# ======== Pybind11 acquired ==========

# Now we create a _core target python module thanks to source code at src/cpp
# exposed in src/pybind
pybind11_add_module(_core MODULE src/pybind/main.cpp src/cpp/my_lib.cpp
                    src/cpp/my_lib.h)
# Note: the headers are not in fact needed.

# === Find and link a C++ library (example, not necessary) ===
# If you want to use external libraries in your C++ code and python module by
# extension...

# add directory with macros : we put a FindGLFW3.cmake in the directory cmake
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR}/cmake)

# Find required library
find_package(GLFW3 3.3 REQUIRED)

# Hopefully, GLFW3 is found by CMake, if it is installed in your system of
# course.

# find_package by convention will create several variables: - <LIB>_FOUND -
# <LIB>_LIBRARIES - <LIB>_INCLUDE_DIR
if(GLFW_FOUND)
  include_directories(${GLFW_INCLUDE_DIR}) # Add include directories
  target_link_libraries(_core PRIVATE ${GLFW_LIBRARIES}) # link GLFW libraries
else()
  # Normally the failure to find GLFW3 is handled in FindGLFW3.cmake...
  message(FATAL_ERROR "GLFW not found ! Exiting...")
endif()
# ============================================================

# Install the _core.so python module
install(TARGETS _core DESTINATION .)
