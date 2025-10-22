---
id: d0328130-b732-48bb-8234-939096e1a7c7
name: Unicode Directory Traversal
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.812849+00:00'
updated_at: '2023-04-10T20:22:06.864725+00:00'
tags:
- '[[16 bits Unicode encoding]]'
- '[[Basic exploitation]]'
- '[[Directory Traversal]]'
commands:
- '[[Character Encoding]]'
---

# Unicode Directory Traversal

## Summary

Unicode Directory Traversal is a technique used by attackers to access files and directories that are outside of the web server's root directory. This can be achieved by encoding the directory traversal string in Unicode format, which can bypass certain security measures. Attackers can use this tec

## Description

# Description

Unicode Directory Traversal is a technique used by attackers to access files and directories that are outside of the web server's root directory. This can be achieved by encoding the directory traversal string in Unicode format, which can bypass certain security measures. Attackers can use this technique to access sensitive files such as configuration files, user credentials, and other sensitive information. This technique is commonly used in combination with other attacks such as SQL injection or cross-site scripting (XSS). 

Technical Explanation: In Unicode encoding, each character is represented by a 16-bit code unit. The Unicode encoding can be used to represent special characters that cannot be represented in ASCII encoding. Attackers can use this technique to encode the directory traversal string in Unicode format, which can bypass certain security measures. For example, the directory traversal string '../' can be encoded in Unicode format as '%u002e%u002e%u002f'.

Business Value: By using Unicode Directory Traversal, attackers can gain access to sensitive information that can be used to compromise the web server or the entire network. This can lead to data breaches, financial loss, and damage to the organization's reputation.

## Requirements

1. Access to the web server

1. Knowledge of the directory structure

1. Ability to encode the directory traversal string in Unicode format

## Defense

1. Implement input validation to prevent directory traversal attacks

1. Implement access control to restrict access to sensitive files and directories

1. Implement logging and monitoring to detect and respond to directory traversal attacks

## Objectives

1. Gain access to sensitive files and directories outside of the web server's root directory

1. Bypass security measures that prevent directory traversal attacks

1. Compromise the web server or the entire network

# Instructions

1. Encode the directory traversal string in Unicode format using the table provided.

**Code**: [[. = %u002e
/ = %u2215
\ = %u2216]]

> The directory traversal string can be encoded in Unicode format using the table provided. For example, the directory traversal string '../' can be encoded as '%u002e%u002e%u002f'.

**Command** ([[Character Encoding]]):

```bash
. = %u002e
/ = %u2215
\ = %u2216
```

## Commands Used

- [[Character Encoding]]

## Tags

- [[16 bits Unicode encoding]]
- [[Basic exploitation]]
- [[Directory Traversal]]
