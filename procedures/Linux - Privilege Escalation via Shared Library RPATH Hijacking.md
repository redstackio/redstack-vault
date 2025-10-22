---
id: b50bca34-f027-4272-a53b-0723144bb608
name: Linux - Privilege Escalation via Shared Library RPATH Hijacking
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.418450+00:00'
updated_at: '2023-04-10T20:34:31.002051+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
sub_techniques:
- '[[Executable Installer File Permissions Weakness|T1574.005 - Executable Installer
  File Permissions Weakness]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[RPATH]]'
- '[[Shared Library]]'
commands:
- '[[Check dynamic linker dependencies]]'
- '[[Check Temp Directory]]'
- '[[Compile exploit.c to create libc.so.6]]'
- '[[Copy libc.so.6 to /var/tmp/flag15]]'
- '[[Filter Python Files]]'
- '[[List dynamic dependencies of flag15]]'
- '[[List files in /var/tmp/flag15/]]'
- '[[List needed shared libraries and RPATH of flag15]]'
- '[[List Python Files]]'
- '[[Save Python Files List]]'
---

# Linux - Privilege Escalation via Shared Library RPATH Hijacking

## Summary

Linux systems use shared libraries to save disk space and memory. They allow programs to reuse code that is already loaded into memory, rather than having to load the same code multiple times. RPATH is an environment variable that specifies the search path for shared libraries. Attackers can create

## Description

# Description

Linux systems use shared libraries to save disk space and memory. They allow programs to reuse code that is already loaded into memory, rather than having to load the same code multiple times. RPATH is an environment variable that specifies the search path for shared libraries. Attackers can create a malicious shared library and place it in a directory specified in the RPATH environment variable of a vulnerable program. When the vulnerable program is executed, it loads the malicious shared library and executes the attacker's code with the privileges of the vulnerable program. This technique can be used to escalate privileges on a Linux system.

Technical Explanation: The attacker copies a legitimate shared library to a temporary directory, modifies the library to include malicious code, and sets the RPATH environment variable to include the temporary directory. When the vulnerable program is executed, it loads the malicious shared library and executes the attacker's code. 

Business Value: Privilege escalation can allow an attacker to gain access to sensitive data or perform unauthorized actions on a system. This technique can be used to gain administrative access to a Linux system, allowing an attacker to install backdoors, exfiltrate data, or launch further attacks.

## Requirements

1. Access to a vulnerable program with RPATH environment variable set

1. Ability to copy files to a temporary directory

1. Ability to compile shared libraries

## Defense

1. Regularly review and update file permissions to prevent unauthorized modification of shared libraries

1. Use tools like AppArmor or SELinux to limit the privileges of vulnerable programs

1. Monitor system logs for suspicious activity, such as changes to the RPATH environment variable

## Objectives

1. Escalate privileges on a Linux system

1. Gain administrative access to a Linux system

# Instructions

1. To view the dependencies and library paths used by flag15, run the following commands:

**Code**: [[level15@nebula:/home/flag15$ readelf -d flag15 | e]]

> The command 'readelf -d flag15' is used to display the dynamic section of the binary file flag15. The 'egrep' command is used to filter the output and show only the lines containing 'NEEDED' or 'RPATH'.

The command 'ldd ./flag15' is used to print the shared libraries required by flag15. The output shows the path of each required library file. The library files are searched in the order they are listed in the output.

**Command** ([[List needed shared libraries and RPATH of flag15]]):

```bash
readelf -d flag15 | egrep "NEEDED|RPATH"
```

**Command** ([[List dynamic dependencies of flag15]]):

```bash
ldd ./flag15
```

2. To copy a library to the temporary directory, use the 'cp' command followed by the source file path and the destination directory path. For example, 'cp /path/to/lib.so /var/tmp/flag15/'

**Code**: [[/var/tmp/flag15/]]

> The 'cp' command is used to copy files or directories from one location to another. In this case, we are copying a library file from its original location to the temporary directory. The source file path is the path to the library file that needs to be copied, and the destination directory path is the path to the temporary directory where the file needs to be copied to. It is important to ensure that the destination directory has the appropriate permissions to allow the file to be copied to it.

**Command** ([[List files in /var/tmp/flag15/]]):

```bash
ls /var/tmp/flag15/
```

3. The RPATH command sets a relative path that will be used by the program in the specified location.

**Code**: [[RPATH]]

> This command is used to specify the relative path that will be used by the program. The relative path is used to locate files or directories that are located in the same directory as the program or in a subdirectory of the program. The RPATH command takes one argument, which is the relative path that will be used. The path can be specified as a string, and it should be relative to the current directory. If the path contains spaces or other special characters, it should be enclosed in quotes. Once the relative path is set, it can be used by the program to locate files or directories as needed.

**Command** ([[List Python Files]]):

```bash
ls -lR /usr/local/lib/python3.7/dist-packages/ | grep -E 'py$'
```

**Command** ([[Filter Python Files]]):

```bash
grep -E 'py$'
```

**Command** ([[Save Python Files List]]):

```bash
> py.txt
```

4. To copy the libc.so.6 file to the specified directory, run the following command: cp /lib/i386-linux-gnu/libc.so.6 /var/tmp/flag15/. To check the dependencies of the flag15 binary, run the following command: ldd ./flag15.

**Code**: [[level15@nebula:/home/flag15$ cp /lib/i386-linux-gn]]

> The 'cp' command is used to copy files from one location to another. In this case, the command is copying the 'libc.so.6' file from the '/lib/i386-linux-gnu/' directory to the '/var/tmp/flag15/' directory. 

The 'ldd' command is used to print the shared library dependencies of an executable file. In this case, the command is used to check the dependencies of the 'flag15' binary. The output shows that the 'libc.so.6' file is being used from the '/var/tmp/flag15/' directory.

**Command** ([[Copy libc.so.6 to /var/tmp/flag15]]):

```bash
cp /lib/i386-linux-gnu/libc.so.6 /var/tmp/flag15/
```

**Command** ([[Check dynamic linker dependencies]]):

```bash
ldd ./flag15
```

5. To create an evil library, follow the below steps:

1. Choose a name for your library.
2. Write the code for the library.
3. Compile the code and create a shared object (.so) file.
4. Move the .so file to the desired directory using the command 'mv'.

For example, to create an evil library named 'libevil.so' in the directory '/var/tmp', you can use the following commands:

1. Write the code for the library: vi evil.c
2. Compile the code: gcc -shared -o libevil.so evil.c
3. Move the .so file: mv libevil.so /var/tmp/

**Code**: [[/var/tmp]]

> The 'data' field in this JSON object specifies the directory where the evil library needs to be created. The 'text' field provides some context to the user about what needs to be done. The 'instruction' field provides a step-by-step guide to creating an evil library. The 'name' field provides a descriptive name for this command. The 'explain' field can be left blank as it is not required for this command.

**Command** ([[Check Temp Directory]]):

```bash
ls /var/tmp
```

6. To compile a shared library with GCC, use the following command:

**Code**: [[gcc -fPIC -shared -static-libgcc -Wl,--version-scr]]

> The 'gcc' command is used to invoke the GNU C Compiler. The '-fPIC' option generates position-independent code, which is required for shared libraries. The '-shared' option specifies that a shared library should be created. The '-static-libgcc' option links the GCC library statically. The '-Wl,--version-script=version' option specifies the version script to use, which controls the symbols that are exported by the library. The '-Bstatic' option forces the linker to use static libraries instead of shared ones. 'exploit.c' is the name of the C source file, and 'libc.so.6' is the name of the output file.

**Command** ([[Compile exploit.c to create libc.so.6]]):

```bash
gcc -fPIC -shared -static-libgcc -Wl,--version-script=version,-Bstatic exploit.c -o libc.so.6
```

7. Compile the code and run the resulting executable to start a shell.

**Code**: [[#include<stdlib.h>
#define SHELL "/bin/sh"

int __]]

> This code is written in C and when compiled, it creates an executable that starts a shell. The `#include<stdlib.h>` is a standard C library that provides functions for allocating memory and other general purpose functions. The `#define SHELL "/bin/sh"` defines the path to the shell that will be started. The `setresuid(geteuid(),geteuid(), geteuid())` function sets the real, effective, and saved user IDs to the effective user ID. The `execve(file,argv,0)` function executes the shell with the given arguments.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Hijack Execution Flow|T1574 - Hijack Execution Flow]]

### Sub-Techniques

- [[Executable Installer File Permissions Weakness|T1574.005 - Executable Installer File Permissions Weakness]]

## Commands Used

- [[Check dynamic linker dependencies]]
- [[Check Temp Directory]]
- [[Compile exploit.c to create libc.so.6]]
- [[Copy libc.so.6 to /var/tmp/flag15]]
- [[Filter Python Files]]
- [[List dynamic dependencies of flag15]]
- [[List files in /var/tmp/flag15/]]
- [[List needed shared libraries and RPATH of flag15]]
- [[List Python Files]]
- [[Save Python Files List]]

## Tags

- [[Linux - Privilege Escalation]]
- [[RPATH]]
- [[Shared Library]]
