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
include test/htd/CMakeFiles/GraphPreprocessorTest.dir/depend.make

# Include the progress variables for this target.
include test/htd/CMakeFiles/GraphPreprocessorTest.dir/progress.make

# Include the compile flags for this target's objects.
include test/htd/CMakeFiles/GraphPreprocessorTest.dir/flags.make

test/htd/CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.o: test/htd/CMakeFiles/GraphPreprocessorTest.dir/flags.make
test/htd/CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.o: test/htd/GraphPreprocessorTest.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mohamednadeem/project/htd/htd-normalize_cli/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/htd/CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.o"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.o -c /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/GraphPreprocessorTest.cpp

test/htd/CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.i"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/GraphPreprocessorTest.cpp > CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.i

test/htd/CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.s"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/GraphPreprocessorTest.cpp -o CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.s

# Object files for target GraphPreprocessorTest
GraphPreprocessorTest_OBJECTS = \
"CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.o"

# External object files for target GraphPreprocessorTest
GraphPreprocessorTest_EXTERNAL_OBJECTS =

test/htd/GraphPreprocessorTest: test/htd/CMakeFiles/GraphPreprocessorTest.dir/GraphPreprocessorTest.cpp.o
test/htd/GraphPreprocessorTest: test/htd/CMakeFiles/GraphPreprocessorTest.dir/build.make
test/htd/GraphPreprocessorTest: lib/libhtd.so.0.0.0
test/htd/GraphPreprocessorTest: test/googletest/googletest-release-1.8.0/googlemock/gtest/libgtest_main.so
test/htd/GraphPreprocessorTest: test/googletest/googletest-release-1.8.0/googlemock/gtest/libgtest.so
test/htd/GraphPreprocessorTest: test/htd/CMakeFiles/GraphPreprocessorTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mohamednadeem/project/htd/htd-normalize_cli/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable GraphPreprocessorTest"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/GraphPreprocessorTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/htd/CMakeFiles/GraphPreprocessorTest.dir/build: test/htd/GraphPreprocessorTest

.PHONY : test/htd/CMakeFiles/GraphPreprocessorTest.dir/build

test/htd/CMakeFiles/GraphPreprocessorTest.dir/clean:
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && $(CMAKE_COMMAND) -P CMakeFiles/GraphPreprocessorTest.dir/cmake_clean.cmake
.PHONY : test/htd/CMakeFiles/GraphPreprocessorTest.dir/clean

test/htd/CMakeFiles/GraphPreprocessorTest.dir/depend:
	cd /home/mohamednadeem/project/htd/htd-normalize_cli && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mohamednadeem/project/htd/htd-normalize_cli /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd /home/mohamednadeem/project/htd/htd-normalize_cli /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/CMakeFiles/GraphPreprocessorTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/htd/CMakeFiles/GraphPreprocessorTest.dir/depend

