---
id: 8501b37d-6b91-49dd-88f2-dbbc43046862
name: mingw-compile-useradd-to-adduser-exe
type: command
executor: bash
data: i586-mingw32msvc-gcc -o adduser.exe useradd.c
output: null
created_at: '2023-04-06T03:56:29.741238+00:00'
updated_at: '2023-04-10T20:37:42.754482+00:00'
platforms:
  - Linux
tags:
  - compilation
  - cross-compile
  - mingw
verified: true
validated: true
---

# mingw-compile-useradd-to-adduser-exe

## Command

```bash
i586-mingw32msvc-gcc -o adduser.exe useradd.c
```

## Description

This command cross-compiles a C source file (useradd.c) into a 32-bit Windows executable (adduser.exe) using the MinGW GCC toolchain on Linux. It is used to prepare payloads for Windows kernel exploitation, such as adding a backdoor user during privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o adduser.exe` | Specifies the output filename for the executable | Yes |
| `useradd.c` | Input C source file containing the user addition code | Yes |
| `i586-mingw32msvc-gcc` | MinGW cross-compiler for 32-bit Windows targets | Built-in |

## Examples

### Basic Usage

```bash
i586-mingw32msvc-gcc -o adduser.exe useradd.c
```

Compiles useradd.c to adduser.exe without additional flags.

### Advanced Usage

```bash
i586-mingw32msvc-gcc -o adduser.exe useradd.c -ladvapi32 -v
```

Links the advapi32 library for Windows API calls and enables verbose output for debugging compilation issues.

## Expected Output

Successful compilation produces no stderr output, just creates the adduser.exe file. If errors occur (e.g., syntax issues in useradd.c), GCC will display messages like "useradd.c: In function 'main': error: 'NetUserAdd' undeclared". Verify with `file adduser.exe` showing "PE32 executable".

## Related

- [[procedures/Compile-Useradd-C-to-Adduser-Exe-for-Kernel-Exploitation]]
