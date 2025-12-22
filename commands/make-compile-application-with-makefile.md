---
type: command
executor: bash
data: make
output: |-
  root@0ef3d0f0bb80:~# make
  gcc -g -Wall -o hello hello.c
platforms:
  - Linux
tags:
  - Build
verified: true
validated: true
---

# make-compile-application-with-makefile

## Command

```bash
make
```

## Description

Compiles an application or program based on the instructions defined in a Makefile. This command reads the Makefile in the current directory and executes the necessary build rules, such as compiling source files into executables.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | The basic `make` invocation uses the default target in the Makefile. Targets can be specified as arguments, e.g., `make target_name`. | No |

## Examples

### Basic Usage

```bash
make
```

This runs the default target, typically building the entire project.

### Advanced Usage

```bash
make clean
make install
```

`make clean` removes build artifacts, while `make install` installs the built program.

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@0ef3d0f0bb80:~# make
gcc -g -Wall -o hello hello.c
```

The output shows the compiler commands executed based on the Makefile rules.

## Related

- [[Related Procedure]] (if applicable)
- [[tools/make]] (tool)
