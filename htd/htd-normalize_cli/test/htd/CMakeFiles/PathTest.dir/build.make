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
CMAKE_SOURCE_DIR = /home/mohamednadeem/project/htd/htd-normalize_cli

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mohamednadeem/project/htd/htd-normalize_cli

# Include any dependencies generated for this target.
include test/htd/CMakeFiles/PathTest.dir/depend.make

# Include the progress variables for this target.
include test/htd/CMakeFiles/PathTest.dir/progress.make

# Include the compile flags for this target's objects.
include test/htd/CMakeFiles/PathTest.dir/flags.make

test/htd/CMakeFiles/PathTest.dir/PathTest.cpp.o: test/htd/CMakeFiles/PathTest.dir/flags.make
test/htd/CMakeFiles/PathTest.dir/PathTest.cpp.o: test/htd/PathTest.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mohamednadeem/project/htd/htd-normalize_cli/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/htd/CMakeFiles/PathTest.dir/PathTest.cpp.o"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/PathTest.dir/PathTest.cpp.o -c /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/PathTest.cpp

test/htd/CMakeFiles/PathTest.dir/PathTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/PathTest.dir/PathTest.cpp.i"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/PathTest.cpp > CMakeFiles/PathTest.dir/PathTest.cpp.i

test/htd/CMakeFiles/PathTest.dir/PathTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/PathTest.dir/PathTest.cpp.s"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/PathTest.cpp -o CMakeFiles/PathTest.dir/PathTest.cpp.s

# Object files for target PathTest
PathTest_OBJECTS = \
"CMakeFiles/PathTest.dir/PathTest.cpp.o"

# External object files for target PathTest
PathTest_EXTERNAL_OBJECTS =

test/htd/PathTest: test/htd/CMakeFiles/PathTest.dir/PathTest.cpp.o
test/htd/PathTest: test/htd/CMakeFiles/PathTest.dir/build.make
test/htd/PathTest: lib/libhtd.so.0.0.0
test/htd/PathTest: test/googletest/googletest-release-1.8.0/googlemock/gtest/libgtest_main.so
test/htd/PathTest: test/googletest/googletest-release-1.8.0/googlemock/gtest/libgtest.so
test/htd/PathTest: test/htd/CMakeFiles/PathTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mohamednadeem/project/htd/htd-normalize_cli/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable PathTest"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/PathTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/htd/CMakeFiles/PathTest.dir/build: test/htd/PathTest

.PHONY : test/htd/CMakeFiles/PathTest.dir/build

test/htd/CMakeFiles/PathTest.dir/clean:
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && $(CMAKE_COMMAND) -P CMakeFiles/PathTest.dir/cmake_clean.cmake
.PHONY : test/htd/CMakeFiles/PathTest.dir/clean

test/htd/CMakeFiles/PathTest.dir/depend:
	cd /home/mohamednadeem/project/htd/htd-normalize_cli && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mohamednadeem/project/htd/htd-normalize_cli /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd /home/mohamednadeem/project/htd/htd-normalize_cli /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/CMakeFiles/PathTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/htd/CMakeFiles/PathTest.dir/depend

