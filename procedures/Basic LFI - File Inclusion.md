---
id: ed53350c-6a78-4975-84ec-e8a004ace675
name: Basic LFI - File Inclusion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.015534+00:00'
updated_at: '2023-04-10T20:22:12.737075+00:00'
tags:
- '[[Basic LFI]]'
- '[[File Inclusion]]'
---

# Basic LFI - File Inclusion

## Summary

Basic LFI (Local File Inclusion) is a technique used by attackers to exploit web applications that dynamically include files or resources. Attackers can use this technique to read sensitive files on the server or execute malicious code. In this scenario, the attacker is including the /etc/passwd fi

## Description

# Description

Basic LFI (Local File Inclusion) is a technique used by attackers to exploit web applications that dynamically include files or resources. Attackers can use this technique to read sensitive files on the server or execute malicious code. In this scenario, the attacker is including the /etc/passwd file to retrieve sensitive information about the system's users.

## Requirements

1. Access to a vulnerable web application

## Defense

1. Ensure that the web application is up-to-date and patched against known vulnerabilities

1. Implement input validation to prevent malicious input

1. Use server-side includes (SSI) instead of client-side includes (CSI) to prevent LFI vulnerabilities

## Objectives

1. Retrieve sensitive information from the server

1. Gain unauthorized access to the system

# Instructions

1. 

**Code**: [[/etc/passwd]]

> 

2. 

> 

3. curl http://example.com/index.php?page=../../../etc/passwd

**Code**: [[http://example.com/index.php?page=../../../etc/pas]]

> This command sends a GET request to the vulnerable web application and includes the /etc/passwd file using a URL. The server will return the contents of the file, which can include sensitive information about the system's users.

## Tags

- [[Basic LFI]]
- [[File Inclusion]]
