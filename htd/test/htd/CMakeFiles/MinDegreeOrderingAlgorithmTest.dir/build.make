# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mohamednadeem/project/htd

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mohamednadeem/project/htd

# Include any dependencies generated for this target.
include test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/depend.make

# Include the progress variables for this target.
include test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/progress.make

# Include the compile flags for this target's objects.
include test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/flags.make

test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.o: test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/flags.make
test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.o: test/htd/MinDegreeOrderingAlgorithmTest.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mohamednadeem/project/htd/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.o"
	cd /home/mohamednadeem/project/htd/test/htd && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.o -c /home/mohamednadeem/project/htd/test/htd/MinDegreeOrderingAlgorithmTest.cpp

test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.i"
	cd /home/mohamednadeem/project/htd/test/htd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mohamednadeem/project/htd/test/htd/MinDegreeOrderingAlgorithmTest.cpp > CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.i

test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.s"
	cd /home/mohamednadeem/project/htd/test/htd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mohamednadeem/project/htd/test/htd/MinDegreeOrderingAlgorithmTest.cpp -o CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.s

# Object files for target MinDegreeOrderingAlgorithmTest
MinDegreeOrderingAlgorithmTest_OBJECTS = \
"CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.o"

# External object files for target MinDegreeOrderingAlgorithmTest
MinDegreeOrderingAlgorithmTest_EXTERNAL_OBJECTS =

test/htd/MinDegreeOrderingAlgorithmTest: test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/MinDegreeOrderingAlgorithmTest.cpp.o
test/htd/MinDegreeOrderingAlgorithmTest: test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/build.make
test/htd/MinDegreeOrderingAlgorithmTest: lib/libhtd.so.0.0.0
test/htd/MinDegreeOrderingAlgorithmTest: test/googletest/googletest-release-1.8.0/googlemock/gtest/libgtest_main.so
test/htd/MinDegreeOrderingAlgorithmTest: test/googletest/googletest-release-1.8.0/googlemock/gtest/libgtest.so
test/htd/MinDegreeOrderingAlgorithmTest: test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mohamednadeem/project/htd/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable MinDegreeOrderingAlgorithmTest"
	cd /home/mohamednadeem/project/htd/test/htd && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/build: test/htd/MinDegreeOrderingAlgorithmTest

.PHONY : test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/build

test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/clean:
	cd /home/mohamednadeem/project/htd/test/htd && $(CMAKE_COMMAND) -P CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/cmake_clean.cmake
.PHONY : test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/clean

test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/depend:
	cd /home/mohamednadeem/project/htd && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mohamednadeem/project/htd /home/mohamednadeem/project/htd/test/htd /home/mohamednadeem/project/htd /home/mohamednadeem/project/htd/test/htd /home/mohamednadeem/project/htd/test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/htd/CMakeFiles/MinDegreeOrderingAlgorithmTest.dir/depend

