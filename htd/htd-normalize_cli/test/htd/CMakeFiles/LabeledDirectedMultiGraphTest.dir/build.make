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
include test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/depend.make

# Include the progress variables for this target.
include test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/progress.make

# Include the compile flags for this target's objects.
include test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/flags.make

test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.o: test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/flags.make
test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.o: test/htd/LabeledDirectedMultiGraphTest.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mohamednadeem/project/htd/htd-normalize_cli/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.o"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.o -c /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/LabeledDirectedMultiGraphTest.cpp

test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.i"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/LabeledDirectedMultiGraphTest.cpp > CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.i

test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.s"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/LabeledDirectedMultiGraphTest.cpp -o CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.s

# Object files for target LabeledDirectedMultiGraphTest
LabeledDirectedMultiGraphTest_OBJECTS = \
"CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.o"

# External object files for target LabeledDirectedMultiGraphTest
LabeledDirectedMultiGraphTest_EXTERNAL_OBJECTS =

test/htd/LabeledDirectedMultiGraphTest: test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/LabeledDirectedMultiGraphTest.cpp.o
test/htd/LabeledDirectedMultiGraphTest: test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/build.make
test/htd/LabeledDirectedMultiGraphTest: lib/libhtd.so.0.0.0
test/htd/LabeledDirectedMultiGraphTest: test/googletest/googletest-release-1.8.0/googlemock/gtest/libgtest_main.so
test/htd/LabeledDirectedMultiGraphTest: test/googletest/googletest-release-1.8.0/googlemock/gtest/libgtest.so
test/htd/LabeledDirectedMultiGraphTest: test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mohamednadeem/project/htd/htd-normalize_cli/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable LabeledDirectedMultiGraphTest"
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/LabeledDirectedMultiGraphTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/build: test/htd/LabeledDirectedMultiGraphTest

.PHONY : test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/build

test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/clean:
	cd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd && $(CMAKE_COMMAND) -P CMakeFiles/LabeledDirectedMultiGraphTest.dir/cmake_clean.cmake
.PHONY : test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/clean

test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/depend:
	cd /home/mohamednadeem/project/htd/htd-normalize_cli && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mohamednadeem/project/htd/htd-normalize_cli /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd /home/mohamednadeem/project/htd/htd-normalize_cli /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd /home/mohamednadeem/project/htd/htd-normalize_cli/test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/htd/CMakeFiles/LabeledDirectedMultiGraphTest.dir/depend

