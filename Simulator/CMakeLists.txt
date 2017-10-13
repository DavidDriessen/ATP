cmake_minimum_required (VERSION 2.6)
project (Simulator)

include_directories("${PROJECT_BINARY_DIR}")
include_directories("pybind11")
#add_executable(Simulator main.cpp)
SET(GCC_COVERAGE_COMPILE_FLAGS "-I/usr/include/python2.7 -lpython2.7 -std=c++11 ")
add_definitions(${GCC_COVERAGE_COMPILE_FLAGS})

add_executable(Simulator
        main.cpp
        pybind11/include/pybind11/embed.h
        )


