---
id: f2b96ff8-c1b3-4964-86f7-ab831efed7af
name: C Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.744630+00:00'
updated_at: '2023-04-10T20:25:26.334469+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Compile After Delivery|T1500 - Compile After Delivery]]'
tags:
- '[[C]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
commands:
- '[[Compile shell.c using gcc and run csh]]'
---

# C Reverse Shell

## Summary

A C reverse shell is a technique used to establish a connection from a target machine back to an attacker-controlled machine. This is achieved by compiling and executing a C program on the target machine. Once executed, the C program will establish a connection back to the attacker's machine, allow

## Description

# Description

A C reverse shell is a technique used to establish a connection from a target machine back to an attacker-controlled machine. This is achieved by compiling and executing a C program on the target machine. Once executed, the C program will establish a connection back to the attacker's machine, allowing the attacker to execute commands on the target machine. This technique is commonly used by attackers to maintain persistence and gain further access to a compromised network.

From a technical standpoint, a C reverse shell works by creating a socket and connecting to the attacker's machine. Once the connection is established, the C program will redirect standard input, output, and error to the socket, allowing the attacker to execute commands on the target machine.

The business value of a C reverse shell is that it allows an attacker to maintain persistence and execute commands on a compromised machine without being detected.

## Requirements

1. Ability to compile and execute C programs on the target machine

1. Network access to the attacker-controlled machine

## Defense

1. Implement network segmentation to limit the attacker's ability to move laterally within the network

1. Use strong authentication measures to prevent unauthorized access to the target machine

1. Monitor network traffic for suspicious activity, such as connections to known malicious IP addresses

## Objectives

1. Establish a connection from a target machine back to an attacker-controlled machine

1. Execute commands on the target machine

# Instructions

1. This command is used to compile a C program. The 'gcc' command is used to invoke the GNU C Compiler. The input file '/tmp/shell.c' is the C source code file that needs to be compiled. The '--output csh' option specifies the name of the output file as 'csh'. The '&&' operator is used to execute the 'csh' file only if the compilation is successful.

**Code**: [[gcc /tmp/shell.c --output csh && csh]]

> The 'gcc' command is a widely used compiler for C programs. It is used to convert the C source code into an executable file. The '--output' option is used to specify the name of the output file. The '&&' operator is used to execute the 'csh' file only if the compilation is successful.

**Command** ([[Compile shell.c using gcc and run csh]]):

```bash
gcc /tmp/shell.c --output csh && csh
```

2. To use the Reverse Shell, compile the program and run it on the target machine. Replace the IP address in the code with the IP address of the machine running the listener. Once the connection is established, the shell of the target machine can be accessed from the listener.

**Code**: [[#include <stdio.h>
#include <sys/socket.h>
#includ]]

> This C program creates a reverse shell on the target machine by connecting to a listener on a specified IP address and port. Once the connection is established, it redirects the standard input, output, and error to the socket and executes a shell. This allows the attacker to remotely access the shell of the target machine and execute commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Compile After Delivery|T1500 - Compile After Delivery]]

## Commands Used

- [[Compile shell.c using gcc and run csh]]

## Tags

- [[C]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
