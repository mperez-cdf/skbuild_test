#include <GLFW/glfw3.h> // to test the use of external librairy
#include <string>

#include "my_lib.h"

int add(int i, int j) { return i + j; }

// Test if we can call GLFW functions
std::string test_glfw() {
    std::string result = "";

    if (!glfwInit())
    {
        result += "Failed to initialize GLFW";
    }
    else
    {
        result += "GLFW initialized successfully !\n";
        glfwTerminate(); // deallocate things
        result += "GLFW terminated now.";
    }

    return result;
}
