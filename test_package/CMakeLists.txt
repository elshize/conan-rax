cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_FLAGS -fpermissive)
add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
