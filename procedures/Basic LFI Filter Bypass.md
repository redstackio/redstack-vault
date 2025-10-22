---
id: 1f9dd23e-7141-4f29-ab3d-14894e46de1b
name: Basic LFI Filter Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.151008+00:00'
updated_at: '2023-04-10T20:22:19.055909+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Basic LFI]]'
- '[[File Inclusion]]'
- '[[Filter bypass tricks]]'
commands:
- '[[Directory Traversal Vulnerability Check]]'
- '[[Directory Traversal Vulnerability Check]]'
- '[[Directory Traversal Vulnerability Check]]'
---

# Basic LFI Filter Bypass

## Summary

Basic LFI filter bypass is a technique used to bypass input filters in PHP applications that are designed to prevent Local File Inclusion (LFI) attacks. This technique can be used to access sensitive files on the server, such as configuration files or password files. The attacker can use this techn

## Description

# Description

Basic LFI filter bypass is a technique used to bypass input filters in PHP applications that are designed to prevent Local File Inclusion (LFI) attacks. This technique can be used to access sensitive files on the server, such as configuration files or password files. The attacker can use this technique to gain access to sensitive information and escalate privileges on the target system.

The technique works by using a combination of ../ and null byte (%00) characters to bypass the input filters. The ../ is used to navigate up the directory structure, while the null byte is used to terminate the file extension and any characters that follow it. This allows the attacker to include files that are normally blocked by the input filters.

## Requirements

1. Access to a vulnerable PHP application

## Defense

1. Ensure that input filters are properly configured to prevent LFI attacks

1. Use a web application firewall (WAF) to detect and block LFI attacks

1. Implement access controls to restrict access to sensitive files

## Objectives

1. To bypass input filters in PHP applications

1. To access sensitive files on the server

1. To escalate privileges on the target system

# Instructions

1. To perform a basic LFI filter bypass attack, follow these steps:
1. Identify a vulnerable PHP application that is susceptible to LFI attacks.
2. Construct a URL that includes the ../ and null byte (%00) characters to bypass the input filters.
3. Submit the URL to the vulnerable PHP application and observe the response.
4. If successful, the response should include the contents of the requested file.

**Code**: [[http://example.com/index.php?page=....//....//etc/]]

> The command takes advantage of a vulnerability in the PHP application by constructing a URL that includes the ../ and null byte (%00) characters to bypass the input filters. The ../ is used to navigate up the directory structure, while the null byte is used to terminate the file extension and any characters that follow it. This allows the attacker to include files that are normally blocked by the input filters. The command submits the URL to the vulnerable PHP application and observes the response. If successful, the response should include the contents of the requested file.

**Command** ([[Directory Traversal Vulnerability Check]]):

```bash
http://example.com/index.php?page=....//....//etc/passwd
```

**Command** ([[Directory Traversal Vulnerability Check]]):

```bash
http://example.com/index.php?page=..///////..////..//////etc/passwd
```

**Command** ([[Directory Traversal Vulnerability Check]]):

```bash
http://example.com/index.php?page=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Commands Used

- [[Directory Traversal Vulnerability Check]]
- [[Directory Traversal Vulnerability Check]]
- [[Directory Traversal Vulnerability Check]]

## Tags

- [[Basic LFI]]
- [[File Inclusion]]
- [[Filter bypass tricks]]
