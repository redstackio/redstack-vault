---
id: 1e634360-1646-4755-905b-56005c80cb97
name: Linux - Privilege Escalation via LD_PRELOAD and NOPASSWD
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.009862+00:00'
updated_at: '2023-04-10T20:34:23.346708+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]'
sub_techniques:
- '[[Elevated Execution with Prompt|T1548.004 - Elevated Execution with Prompt]]'
- '[[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]'
tags:
- '[[LD_PRELOAD and NOPASSWD]]'
- '[[Linux - Privilege Escalation]]'
- '[[SUDO]]'
commands:
- '[[Add LD_PRELOAD to env_keep]]'
- '[[Compile shell.c with gcc]]'
- '[[Set LD_PRELOAD environment variable]]'
---

# Linux - Privilege Escalation via LD_PRELOAD and NOPASSWD

## Summary

Privilege escalation via LD_PRELOAD and NOPASSWD is a common technique used by attackers to gain elevated privileges on Linux systems. This technique involves using the LD_PRELOAD environment variable to load a shared object library that contains malicious code into a privileged process. This can b

## Description

# Description

Privilege escalation via LD_PRELOAD and NOPASSWD is a common technique used by attackers to gain elevated privileges on Linux systems. This technique involves using the LD_PRELOAD environment variable to load a shared object library that contains malicious code into a privileged process. This can be done by compiling a shared object with the malicious code and then executing a binary with LD_PRELOAD set to the path of the shared object. By abusing the SUDO NOPASSWD feature, attackers can execute commands as a privileged user without the need for a password. This technique can be used to gain access to sensitive data or execute malicious code on the system.

From a technical standpoint, LD_PRELOAD is an environment variable that specifies a shared object library to preload before all others when a program is run. This allows an attacker to inject their own code into a privileged process and gain elevated privileges. The NOPASSWD feature of SUDO allows a user to execute commands as a privileged user without the need for a password. This feature is often abused by attackers to gain elevated privileges.

From a business perspective, this technique can be used to gain access to sensitive data or execute malicious code on the system. This can result in data theft, system downtime, and reputational damage.

## Requirements

1. Access to a Linux system

1. Knowledge of SUDO NOPASSWD feature

1. Ability to compile a shared object with malicious code

## Defense

1. Regularly review SUDO configuration to ensure that the NOPASSWD feature is not being abused

1. Monitor for changes to the LD_PRELOAD environment variable

1. Implement least privilege access controls to limit the impact of privilege escalation

## Objectives

1. Gain elevated privileges on a Linux system

1. Execute commands as a privileged user without the need for a password

1. Access sensitive data or execute malicious code on the system

# Instructions

1. you want to preload a specific shared library before executing a program, you can use the LD_PRELOAD environment variable.

**Code**: [[LD_PRELOAD]]

> The LD_PRELOAD environment variable is used to specify one or more shared libraries that should be loaded before any other shared library when a program is run. This can be useful if you want to override the behavior of a function in a shared library. For example, if you have a program that uses the malloc() function from the standard C library, but you want to use a custom implementation of malloc() instead, you can create a shared library that defines a function called malloc() and then use LD_PRELOAD to load that library before the standard C library. Any calls to malloc() in the program will then be redirected to your custom implementation.

**Command** ([[Set LD_PRELOAD environment variable]]):

```bash
export LD_PRELOAD=/path/to/library.so
```

2. To set the environment variable LD_PRELOAD, use the following command:
export LD_PRELOAD=/path/to/library.so

To unset the environment variable LD_PRELOAD, use the following command:
unset LD_PRELOAD

**Code**: [[Defaults        env_keep += LD_PRELOAD]]

> The environment variable LD_PRELOAD is used to preload shared libraries before the standard libraries are loaded. This can be useful for debugging or performance tuning purposes. The env_keep directive in the sudoers file allows the user to preserve certain environment variables when running a command with sudo.

**Command** ([[Add LD_PRELOAD to env_keep]]):

```bash
Defaults        env_keep += LD_PRELOAD
```

3. To compile a shared object, use the gcc command followed by the -fPIC flag to generate position-independent code. Then, use the -shared flag to create a shared object. The -o flag specifies the output file name. Finally, specify the source code file name and the -nostartfiles flag to avoid linking with standard startup files.

**Code**: [[gcc -fPIC -shared -o shell.so shell.c -nostartfile]]

> The gcc command is used to compile C code into executable files or shared objects. The -fPIC flag generates position-independent code, which allows the code to be loaded at any address in memory. The -shared flag creates a shared object, which is a library that can be dynamically linked at runtime. The -o flag specifies the output file name. The source code file name should be specified after the flags. The -nostartfiles flag tells the linker to not include standard startup files, which are typically used to initialize the program's environment.

**Command** ([[Compile shell.c with gcc]]):

```bash
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```

4. To compile the program and create a shared object library, use the following commands:

	gcc -fPIC -shared -o libhijack.so hijack.c

Then, set the LD_PRELOAD environment variable to the full path of the shared object library and execute a setuid or setgid binary that is vulnerable to the attack. For example:

	export LD_PRELOAD=/full/path/to/libhijack.so
	./vulnerable_binary

**Code**: [[#include <stdio.h>
#include <sys/types.h>
#include]]

> The program creates a shared object library that contains the _init() function. When a setuid or setgid binary is executed with the LD_PRELOAD environment variable set to the full path of the shared object library, the _init() function is executed before the main program. This function sets the GID and UID to 0 (root) and executes a shell. This allows an attacker to escalate their privileges to root.

5. To execute a binary with LD_PRELOAD, run the following command in your terminal:

sudo LD_PRELOAD=<full_path_to_so_file> <program>

Replace <full_path_to_so_file> with the full path to the shared object file that you want to preload and <program> with the name of the binary that you want to execute.

**Code**: [[sudo LD_PRELOAD=<full_path_to_so_file> <program>]]

> - The LD_PRELOAD environment variable is used to specify a shared object file that should be loaded before all others when a program is run.
- This can be used to override or intercept functions in other shared libraries, or to add new functionality to a program.
- By using this command to execute a binary, you can spawn a shell with elevated privileges, which can be useful for various purposes such as debugging or system administration.

6. Use this command to find files with elevated privileges.

**Code**: [[sudo LD_PRELOAD=/tmp/shell.so find]]

> This command will allow you to search for files with elevated privileges. The 'sudo' command will run the 'find' command with elevated privileges. The 'LD_PRELOAD' environment variable is used to load a shared object file that will be used to run a shell command with elevated privileges. The 'find' command is used to search for files in a directory hierarchy based on various criteria such as name, type, size, and date modified. You can specify the directory to search in as an argument after the 'find' command. 

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]

### Sub-Techniques

- [[Elevated Execution with Prompt|T1548.004 - Elevated Execution with Prompt]]
- [[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]

## Commands Used

- [[Add LD_PRELOAD to env_keep]]
- [[Compile shell.c with gcc]]
- [[Set LD_PRELOAD environment variable]]

## Tags

- [[LD_PRELOAD and NOPASSWD]]
- [[Linux - Privilege Escalation]]
- [[SUDO]]
