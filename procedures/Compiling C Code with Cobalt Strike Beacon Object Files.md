---
id: faa80fbf-1788-4702-a3f7-7f2fe2bd24e6
name: Compiling C Code with Cobalt Strike Beacon Object Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.791690+00:00'
updated_at: '2023-04-10T20:36:20.720248+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
sub_techniques:
- '[[Binary Padding|T1027.001 - Binary Padding]]'
tags:
- '[[Beacon Object Files]]'
- '[[Cobalt Strike]]'
commands:
- '[[Compiling hello.c with Visual Studio]]'
- '[[Compiling hello.c with x64 MinGW]]'
- '[[Compiling hello.c with x86 MinGW]]'
---

# Compiling C Code with Cobalt Strike Beacon Object Files

## Summary

Compiling C code with Cobalt Strike Beacon Object Files is a technique used to evade detection by antivirus software. This technique involves compiling C code into an object file and then loading that object file into the Beacon payload. Once loaded, the object file can be executed within the Beaco

## Description

# Description

Compiling C code with Cobalt Strike Beacon Object Files is a technique used to evade detection by antivirus software. This technique involves compiling C code into an object file and then loading that object file into the Beacon payload. Once loaded, the object file can be executed within the Beacon payload, allowing the attacker to execute arbitrary code on the target system. This technique is commonly used in post-exploitation scenarios where the attacker has already gained a foothold on the target system.

From a technical standpoint, this technique involves using the 'Compile C Code' command in Cobalt Strike to compile the C code into an object file. The object file is then loaded into the Beacon payload using the 'beacon_object' command. Once loaded, the object file can be executed within the Beacon payload using the 'execute_assembly' command.

The business value of this technique is that it allows attackers to evade detection by antivirus software and execute arbitrary code on the target system. This can be used to maintain persistence, escalate privileges, and exfiltrate data.

## Requirements

1. Access to a system with Cobalt Strike installed

1. C code to compile

## Defense

1. Implement strict application whitelisting policies

1. Regularly update antivirus software

1. Monitor for suspicious behavior and network activity

## Objectives

1. Compile C code into an object file

1. Load the object file into the Beacon payload

1. Execute the object file within the Beacon payload

# Instructions

1. To compile C code using this command, follow the steps below:

**Code**: [[# To compile this with Visual Studio:
cl.exe /c /G]]

> 1. Copy the code you want to compile into a file named hello.c
2. Open a command prompt or terminal window
3. Navigate to the directory where hello.c is saved
4. Run the appropriate command for your system, as listed in the 'data' field of this JSON object
5. If the compilation is successful, an object file named hello.o will be created in the same directory as hello.c

**Command** ([[Compiling hello.c with Visual Studio]]):

```bash
cl.exe /c /GS- hello.c /Fohello.o
```

**Command** ([[Compiling hello.c with x86 MinGW]]):

```bash
i686-w64-mingw32-gcc -c hello.c -o hello.o
```

**Command** ([[Compiling hello.c with x64 MinGW]]):

```bash
x86_64-w64-mingw32-gcc -c hello.c -o hello.o
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

### Sub-Techniques

- [[Binary Padding|T1027.001 - Binary Padding]]

## Commands Used

- [[Compiling hello.c with Visual Studio]]
- [[Compiling hello.c with x64 MinGW]]
- [[Compiling hello.c with x86 MinGW]]

## Tags

- [[Beacon Object Files]]
- [[Cobalt Strike]]
