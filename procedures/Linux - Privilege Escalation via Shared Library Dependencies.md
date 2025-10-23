---
id: 4decf20c-2d95-42d7-aaa0-2e6db43b0190
name: Linux - Privilege Escalation via Shared Library Dependencies
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.376124+00:00'
updated_at: '2023-04-10T20:34:33.723882+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
- '[[Local Job Scheduling|T1168 - Local Job Scheduling]]'
tags:
- '[[ldconfig]]'
- '[[Linux - Privilege Escalation]]'
- '[[Shared Library]]'
commands:
- '[[Check shared library dependencies]]'
- '[[List Dynamic Dependencies]]'
---

# Linux - Privilege Escalation via Shared Library Dependencies

## Summary

This procedure involves exploiting shared library dependencies to escalate privileges on a Linux system. By manipulating the search path of shared libraries, an attacker can load a malicious library that will execute with elevated privileges. This can be achieved by creating a shared library with t

## Description

# Description

This procedure involves exploiting shared library dependencies to escalate privileges on a Linux system. By manipulating the search path of shared libraries, an attacker can load a malicious library that will execute with elevated privileges. This can be achieved by creating a shared library with the same name as a legitimate library or by modifying the search path used by ldconfig.

From a technical perspective, this involves identifying a vulnerable binary that loads shared libraries and determining the search path used by ldconfig. Once a vulnerable binary is identified, the attacker can create a malicious shared library and place it in a directory that is searched before the legitimate library. Alternatively, the attacker can modify the search path used by ldconfig to include a directory containing the malicious library.

The business value of this procedure is that it allows an attacker to escalate privileges on a Linux system, potentially gaining access to sensitive data or systems.

 

## Requirements

1. Access to a vulnerable Linux system

1. Ability to create and load shared libraries

 

## Defense

1. Implement least privilege access controls to limit the impact of privilege escalation attacks

1. Monitor system logs for suspicious activity related to shared library dependencies

1. Regularly update and patch software to minimize the risk of exploitation

 

## Objectives

1. Escalate privileges on a Linux system

1. Gain access to sensitive data or systems

 

# Instructions

1. The 'ldd' command is used to identify the shared libraries that a binary executable is dependent upon.

 



**Code**: [[ldd]]



> The 'ldd' command prints the shared libraries required by each program or shared library specified on the command line. When invoked without any arguments, it displays the shared libraries that the dynamic linker/loader would use to load the executable or shared library specified. The output includes the full path to each shared library, along with any version information that is available.



**Command** ([[List Dynamic Dependencies]]):

```bash
ldd <executable>
```



2. To view the dependencies of a binary file, use the command 'ldd' followed by the path to the binary file.

 



**Code**: [[$ ldd /opt/binary
    linux-vdso.so.1 (0x00007ffe9]]



> The 'ldd' command lists the shared libraries required by the specified binary file. In the given example, the dependencies of '/opt/binary' are listed. The output shows the name of the shared library followed by its location in memory. The 'linux-vdso.so.1' library is a special library that allows the program to access certain system calls directly, while the 'vulnlib.so.8' library is required by the program and is located in '/usr/lib/'. The last library listed is the dynamic linker, which is responsible for loading and linking the shared libraries at run time.



**Command** ([[Check shared library dependencies]]):

```bash
$ ldd /opt/binary
```



3. To create a library, use the 'mkdir' command followed by the name of the library you wish to create. For example, 'mkdir my_library'.

 



**Code**: [[/tmp]]



> The 'mkdir' command allows you to create a new directory or folder. In this case, we are using it to create a library within the '/tmp' directory. The name of the library should be provided after the 'mkdir' command, and it will be created as a subdirectory of '/tmp'.

4. Compile and load a shared library into memory

 



**Code**: [[gcc –Wall –fPIC –shared –o vulnlib.so /tmp/vulnlib]]



> This command compiles a shared library from the source code located at /tmp/vulnlib.c using the gcc compiler with the following options:
-Wall: enable all warnings
-fPIC: generate position-independent code
-shared: generate a shared object
-o: specify the output file name

The compiled shared library is then loaded into memory using the ldconfig command with the -l option to specify the path to the compiled shared library.

Finally, the path to the directory containing the compiled shared library is added to the /etc/ld.so.conf.d/exploit.conf file and ldconfig is run again to ensure that the shared library can be found by the system.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Hijack Execution Flow|T1574 - Hijack Execution Flow]]
- [[Local Job Scheduling|T1168 - Local Job Scheduling]]

## Commands Used

- [[Check shared library dependencies]]
- [[List Dynamic Dependencies]]

## Tags

- [[ldconfig]]
- [[Linux - Privilege Escalation]]
- [[Shared Library]]


