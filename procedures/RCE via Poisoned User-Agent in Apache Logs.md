---
id: ece6eaad-3520-403d-855e-26346e1d7034
name: RCE via Poisoned User-Agent in Apache Logs
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.651243+00:00'
updated_at: '2023-04-10T20:22:16.636881+00:00'
tags:
- '[[File Inclusion]]'
- '[[LFI to RCE via controlled log file]]'
- '[[RCE via Apache logs]]'
commands:
- '[[Execute curl command]]'
---

# RCE via Poisoned User-Agent in Apache Logs

## Summary

This procedure involves exploiting a file inclusion vulnerability to achieve remote code execution (RCE) via poisoned User-Agent in Apache logs. An attacker can inject PHP code into the User-Agent field of an HTTP request, which will then be logged in the Apache access logs. The attacker can then u

## Description

# Description

This procedure involves exploiting a file inclusion vulnerability to achieve remote code execution (RCE) via poisoned User-Agent in Apache logs. An attacker can inject PHP code into the User-Agent field of an HTTP request, which will then be logged in the Apache access logs. The attacker can then use a local file inclusion (LFI) vulnerability to include the poisoned access log file, resulting in the execution of the injected PHP code. This technique can be used to gain remote access to the target system, steal data, or perform other malicious actions.

## Requirements

1. Access to a vulnerable web application with a file inclusion vulnerability

1. Ability to inject PHP code into the User-Agent field of an HTTP request

1. Knowledge of a local file inclusion (LFI) vulnerability on the target system

## Defense

1. Implement input validation and sanitization to prevent file inclusion vulnerabilities

1. Monitor access logs for suspicious User-Agent strings and LFI attempts

1. Restrict access to sensitive system files and directories to prevent unauthorized access

## Objectives

1. Achieve remote code execution on the target system

1. Gain unauthorized access to sensitive data

1. Perform other malicious actions on the target system

# Instructions

1. Replace `http://example.org/` with the target URL and `system(\$_GET['cmd']);` with the desired PHP code.

This command injects PHP code into the User-Agent field of an HTTP request, which will then be logged in the Apache access logs.

2. Replace `http://example.org/test.php` with the vulnerable URL and `/var/log/apache2/access.log` with the path to the poisoned access log file.

This command exploits the LFI vulnerability to include the poisoned access log file, resulting in the execution of the injected PHP code.

**Command** ([[Execute curl command]]):

```bash
$ curl http://example.org/test.php?page=/var/log/apache2/access.log&cmd=id
```

## Commands Used

- [[Execute curl command]]

## Tags

- [[File Inclusion]]
- [[LFI to RCE via controlled log file]]
- [[RCE via Apache logs]]
