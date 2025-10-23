---
id: 654a90f4-254a-435c-8662-e4dc7889feba
name: Basic LFI with Double Encoding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.063930+00:00'
updated_at: '2023-04-10T20:22:18.342570+00:00'
tags:
- '[[Basic LFI]]'
- '[[Double encoding]]'
- '[[File Inclusion]]'
---

# Basic LFI with Double Encoding

## Summary

Basic LFI (Local File Inclusion) is a vulnerability that allows an attacker to read files on a server. Double encoding is a technique that can be used to bypass some filters that are looking for specific characters. This command demonstrates how to use double encoding to exploit a basic LFI vulnera

## Description

# Description

Basic LFI (Local File Inclusion) is a vulnerability that allows an attacker to read files on a server. Double encoding is a technique that can be used to bypass some filters that are looking for specific characters. This command demonstrates how to use double encoding to exploit a basic LFI vulnerability. An attacker could use this technique to read sensitive files on the server, such as password files, configuration files, or log files. This could lead to further exploitation of the system.

To exploit this vulnerability, the attacker sends a specially crafted request to the server. This request includes the path to the file the attacker wants to read. By using double encoding, the attacker can bypass filters that are looking for specific characters, such as the dot (.) or slash (/). This allows the attacker to read files that they shouldn't have access to. 

Business Value: This technique can be used to gain access to sensitive information on a server, such as passwords or configuration files. This information can then be used to further exploit the system and gain access to additional resources.

 

## Requirements

1. Access to a vulnerable web application with a basic LFI vulnerability

 

## Defense

1. Input validation should be performed on user-supplied input to prevent this type of vulnerability

1. Access controls should be implemented to prevent unauthorized access to sensitive files

1. Web application firewalls (WAFs) can be used to detect and block attempts to exploit LFI vulnerabilities

 

## Objectives

1. To demonstrate how to use double encoding to bypass filters and exploit a basic LFI vulnerability

1. To read sensitive files on the server that the attacker doesn't have access to

 

# Instructions

1. Send a specially crafted request to the server with the path to the file you want to read. Use double encoding to bypass filters that are looking for specific characters.

 



**Code**: [[http://example.com/index.php?page=%252e%252e%252fe]]



> The command sends a request to the server with the path to the file the attacker wants to read. The %25 characters are used to represent the % character in the URL, which is then interpreted as a % character by the server. By using %252e%252e%252f to represent ../, the attacker can bypass filters that are looking for the dot (.) and slash (/) characters. The %00 character is used to terminate the string and prevent any additional characters from being interpreted.

## Tags

- [[Basic LFI]]
- [[Double encoding]]
- [[File Inclusion]]


