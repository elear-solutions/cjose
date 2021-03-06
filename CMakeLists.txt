#/*===================================================================================*/
#/*************************************************************************************/
#/**
# * @file      CMakeLists.txt
# * @brief     CMake build script
# * @details   Sets up boiler plate build template for HTTP-Client-Library
# * @see       https://cmake.org/cmake-tutorial
# * @author    Nutan Ghatge, nutanghatge@elear.solutions
#              Ashish Bajaj, ashish@elear.solutions
# * @copyright Copyright (c) 2018 Elear Solutions Tech Private Limited. All rights
# *            reserved.
# * @license   To any person (the "Recipient") obtaining a copy of this software and
# *            associated documentation files (the "Software"):\n
# *            All information contained in or disclosed by this software is
# *            confidential and proprietary information of Elear Solutions Tech
# *            Private Limited and all rights therein are expressly reserved.
# *            By accepting this material the recipient agrees that this material and
# *            the information contained therein is held in confidence and in trust
# *            and will NOT be used, copied, modified, merged, published, distributed,
# *            sublicensed, reproduced in whole or in part, nor its contents revealed
# *            in any manner to others without the express written permission of
# *            Elear Solutions Tech Private Limited.
# */
#/*************************************************************************************/
#/*===================================================================================*/
cmake_minimum_required(VERSION 2.6)

# Define the project name
project(cjose)

# Define link_directory to be relative path
cmake_policy(SET CMP0015 NEW)
#link_directories(../../elear-common-lib)

# Add subdirectories to the project. The CMakeLists.txt file in each
# subdirectory will be used for further setting up the project
#add_subdirectory(utest/test_util)
#add_subdirectory(utest/test_genericstatemachine_devtimer)

execute_process (COMMAND bash -c "./build.sh"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)

# Set global compilation flags at project level
set(CMAKE_C_FLAGS           "${CMAKE_C_FLAGS} -I ../include")
set(CMAKE_C_FLAGS           "${CMAKE_C_FLAGS} -I ../jansson/include")
set(CMAKE_C_FLAGS           "${CMAKE_C_FLAGS} -pedantic-errors -Wall -std=c11 -D_GNU_SOURCE -O2 -fPIC -Wl,--version-script=../exportmap")

# The following file GLOB command will search for all files within the current
# directory that match the specified expressions (*.c and *.h), and assign the
# resulting files to the variable SRCS. SRCS is a list of all C source and
# header files in the current directory.
file(GLOB CJOSE_SRCS ./src/*.c ${CMAKE_SOURCE_DIR}/src/include/*.h ${CMAKE_SOURCE_DIR}/include/cjose/*.h)
#file(GLOB CJOSE_SRCS *.c *.h)
file(GLOB HDRS ${CMAKE_SOURCE_DIR}/include/cjose/*.h)

# Add final library for this folder
file(GLOB OBJS ${CMAKE_SOURCE_DIR}/build/obj/*.o)

# Add final executable for this folder
#add_executable(elear-http-client ${SRCS})

# Set Libraries to be built
add_library(cjose SHARED ${CJOSE_SRCS} ${OBJS})
# Set compilation flags
# -fPIC is implicit in SHARED libraries, see POSITION_INDEPENDANT_CODE property in cmake documentation
#set_target_properties(elearcommon PROPERTIES COMPILE_FLAGS "-fPIC")
target_link_libraries(cjose m)
target_link_libraries(cjose ssl)
target_link_libraries(cjose crypto)

# Install library files
install (TARGETS cjose DESTINATION lib)
# Install headers
install (FILES ${HDRS} DESTINATION include/cjose)
#install(FILES foo DESTINATION ${CMAKE_CURRENT_BINARY_DIR}
#              PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ)


# ------------------------- Begin Generic CMake Variable Logging ------------------

# if you are building in-source, this is the same as CMAKE_SOURCE_DIR, otherwise
# this is the top level directory of your build tree
MESSAGE( STATUS "CMAKE_BINARY_DIR:         " ${CMAKE_BINARY_DIR} )

# if you are building in-source, this is the same as CMAKE_CURRENT_SOURCE_DIR, otherwise this
# is the directory where the compiled or generated files from the current CMakeLists.txt will go to
MESSAGE( STATUS "CMAKE_CURRENT_BINARY_DIR: " ${CMAKE_CURRENT_BINARY_DIR} )

# this is the directory, from which cmake was started, i.e. the top level source directory
MESSAGE( STATUS "CMAKE_SOURCE_DIR:         " ${CMAKE_SOURCE_DIR} )

# this is the directory where the currently processed CMakeLists.txt is located in
MESSAGE( STATUS "CMAKE_CURRENT_SOURCE_DIR: " ${CMAKE_CURRENT_SOURCE_DIR} )

# contains the full path to the top level directory of your build tree
MESSAGE( STATUS "PROJECT_BINARY_DIR: " ${PROJECT_BINARY_DIR} )

# contains the full path to the root of your project source directory,
# i.e. to the nearest directory where CMakeLists.txt contains the PROJECT() command
MESSAGE( STATUS "PROJECT_SOURCE_DIR: " ${PROJECT_SOURCE_DIR} )

# set this variable to specify a common place where CMake should put all executable files
# (instead of CMAKE_CURRENT_BINARY_DIR)
MESSAGE( STATUS "EXECUTABLE_OUTPUT_PATH: " ${EXECUTABLE_OUTPUT_PATH} )

# set this variable to specify a common place where CMake should put all libraries
# (instead of CMAKE_CURRENT_BINARY_DIR)
MESSAGE( STATUS "LIBRARY_OUTPUT_PATH:     " ${LIBRARY_OUTPUT_PATH} )

# tell CMake to search first in directories listed in CMAKE_MODULE_PATH
# when you use FIND_PACKAGE() or INCLUDE()
MESSAGE( STATUS "CMAKE_MODULE_PATH: " ${CMAKE_MODULE_PATH} )

# this is the complete path of the cmake which runs currently (e.g. /usr/local/bin/cmake)
MESSAGE( STATUS "CMAKE_COMMAND: " ${CMAKE_COMMAND} )

# this is the CMake installation directory
MESSAGE( STATUS "CMAKE_ROOT: " ${CMAKE_ROOT} )

# this is the filename including the complete path of the file where this variable is used.
MESSAGE( STATUS "CMAKE_CURRENT_LIST_FILE: " ${CMAKE_CURRENT_LIST_FILE} )

# this is linenumber where the variable is used
MESSAGE( STATUS "CMAKE_CURRENT_LIST_LINE: " ${CMAKE_CURRENT_LIST_LINE} )

# this is used when searching for include files e.g. using the FIND_PATH() command.
MESSAGE( STATUS "CMAKE_INCLUDE_PATH: " ${CMAKE_INCLUDE_PATH} )

# this is used when searching for libraries e.g. using the FIND_LIBRARY() command.
MESSAGE( STATUS "CMAKE_LIBRARY_PATH: " ${CMAKE_LIBRARY_PATH} )

# the complete system name, e.g. "Linux-2.4.22", "FreeBSD-5.4-RELEASE" or "Windows 5.1"
MESSAGE( STATUS "CMAKE_SYSTEM: " ${CMAKE_SYSTEM} )

# the short system name, e.g. "Linux", "FreeBSD" or "Windows"
MESSAGE( STATUS "CMAKE_SYSTEM_NAME: " ${CMAKE_SYSTEM_NAME} )

# only the version part of CMAKE_SYSTEM
MESSAGE( STATUS "CMAKE_SYSTEM_VERSION: " ${CMAKE_SYSTEM_VERSION} )

# the processor name (e.g. "Intel(R) Pentium(R) M processor 2.00GHz")
MESSAGE( STATUS "CMAKE_SYSTEM_PROCESSOR: " ${CMAKE_SYSTEM_PROCESSOR} )

# is TRUE on all UNIX-like OS's, including Apple OS X and CygWin
MESSAGE( STATUS "UNIX: " ${UNIX} )

# is TRUE on Windows, including CygWin
MESSAGE( STATUS "WIN32: " ${WIN32} )

# is TRUE on Apple OS X
MESSAGE( STATUS "APPLE: " ${APPLE} )

# is TRUE when using the MinGW compiler in Windows
MESSAGE( STATUS "MINGW: " ${MINGW} )

# is TRUE on Windows when using the CygWin version of cmake
MESSAGE( STATUS "CYGWIN: " ${CYGWIN} )

# is TRUE on Windows when using a Borland compiler
MESSAGE( STATUS "BORLAND: " ${BORLAND} )

# Microsoft compiler
MESSAGE( STATUS "MSVC: " ${MSVC} )
MESSAGE( STATUS "MSVC_IDE: " ${MSVC_IDE} )
MESSAGE( STATUS "MSVC60: " ${MSVC60} )
MESSAGE( STATUS "MSVC70: " ${MSVC70} )
MESSAGE( STATUS "MSVC71: " ${MSVC71} )
MESSAGE( STATUS "MSVC80: " ${MSVC80} )
MESSAGE( STATUS "CMAKE_COMPILER_2005: " ${CMAKE_COMPILER_2005} )


# set this to true if you don't want to rebuild the object files if the rules have changed,
# but not the actual source files or headers (e.g. if you changed the some compiler switches)
MESSAGE( STATUS "CMAKE_SKIP_RULE_DEPENDENCY: " ${CMAKE_SKIP_RULE_DEPENDENCY} )

# since CMake 2.1 the install rule depends on all, i.e. everything will be built before installing.
# If you don't like this, set this one to true.
MESSAGE( STATUS "CMAKE_SKIP_INSTALL_ALL_DEPENDENCY: " ${CMAKE_SKIP_INSTALL_ALL_DEPENDENCY} )

# If set, runtime paths are not added when using shared libraries. Default it is set to OFF
MESSAGE( STATUS "CMAKE_SKIP_RPATH: " ${CMAKE_SKIP_RPATH} )

# set this to true if you are using makefiles and want to see the full compile and link
# commands instead of only the shortened ones
MESSAGE( STATUS "CMAKE_VERBOSE_MAKEFILE: " ${CMAKE_VERBOSE_MAKEFILE} )

# this will cause CMake to not put in the rules that re-run CMake. This might be useful if
# you want to use the generated build files on another machine.
MESSAGE( STATUS "CMAKE_SUPPRESS_REGENERATION: " ${CMAKE_SUPPRESS_REGENERATION} )


# A simple way to get switches to the compiler is to use ADD_DEFINITIONS().
# But there are also two variables exactly for this purpose:

# the compiler flags for compiling C sources
MESSAGE( STATUS "CMAKE_C_FLAGS: " ${CMAKE_C_FLAGS} )

# the compiler flags for compiling C++ sources
MESSAGE( STATUS "CMAKE_CXX_FLAGS: " ${CMAKE_CXX_FLAGS} )


# Choose the type of build.  Example: SET(CMAKE_BUILD_TYPE Debug)
MESSAGE( STATUS "CMAKE_BUILD_TYPE: " ${CMAKE_BUILD_TYPE} )

# if this is set to ON, then all libraries are built as shared libraries by default.
MESSAGE( STATUS "BUILD_SHARED_LIBS: " ${BUILD_SHARED_LIBS} )

# the compiler used for C files
MESSAGE( STATUS "CMAKE_C_COMPILER: " ${CMAKE_C_COMPILER} )

# the compiler used for C++ files
MESSAGE( STATUS "CMAKE_CXX_COMPILER: " ${CMAKE_CXX_COMPILER} )

# if the compiler is a variant of gcc, this should be set to 1
MESSAGE( STATUS "CMAKE_COMPILER_IS_GNUCC: " ${CMAKE_COMPILER_IS_GNUCC} )

# if the compiler is a variant of g++, this should be set to 1
MESSAGE( STATUS "CMAKE_COMPILER_IS_GNUCXX : " ${CMAKE_COMPILER_IS_GNUCXX} )

# the tools for creating libraries
MESSAGE( STATUS "CMAKE_AR: " ${CMAKE_AR} )
MESSAGE( STATUS "CMAKE_RANLIB: " ${CMAKE_RANLIB} )

#
#MESSAGE( STATUS ": " ${} )

# ------------------------- End of Generic CMake Variable Logging ------------------
