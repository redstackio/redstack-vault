---
id: 4a3b411f-5dea-4345-b01d-1e3db63c8991
name: Directory Traversal using Dotdotpwn
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.754072+00:00'
updated_at: '2023-04-10T20:22:07.572649+00:00'
tags:
- '[[Directory Traversal]]'
- '[[Tools]]'
commands:
- '[[Clone dotdotpwn repository]]'
- '[[Exploit /etc/shadow file using dotdotpwn]]'
---

# Directory Traversal using Dotdotpwn

## Summary

Directory Traversal is a method used by attackers to access files and directories that are stored outside of the web root folder. Dotdotpwn is a tool that can be used to automate the process of directory traversal. It allows an attacker to traverse directories and read files that they should not ha

## Description

# Description

Directory Traversal is a method used by attackers to access files and directories that are stored outside of the web root folder. Dotdotpwn is a tool that can be used to automate the process of directory traversal. It allows an attacker to traverse directories and read files that they should not have access to. This tool can be used for both reconnaissance and privilege escalation. This procedure will use the Dotdotpwn tool to perform directory traversal and read sensitive files.

 

## Requirements

1. Access to a vulnerable web application.

1. Dotdotpwn tool installed on the attacker's machine.

 

## Defense

1. Implement input validation and output encoding to prevent directory traversal attacks.

1. Implement access control mechanisms to restrict access to sensitive files and directories.

1. Use web application firewalls to detect and block directory traversal attacks.

 

## Objectives

1. Discover files and directories that are outside the web root folder.

1. Read sensitive files that the attacker should not have access to.

 

# Instructions

1. To perform directory traversal using Dotdotpwn, follow these steps:

 



**Code**: [[git clone https://github.com/wireghoul/dotdotpwn
p]]



> 1. Clone the Dotdotpwn tool from the Github repository.
2. Run the Dotdotpwn tool using the appropriate command-line arguments.
3. Specify the target IP address and the protocol to be used (FTP/HTTP).
4. Specify the file to be read using the -f argument.
5. Use the -s argument to enable SSL encryption.
6. Use the -q argument to enable quiet mode.
7. Use the -b argument to enable batch mode.



**Command** ([[Clone dotdotpwn repository]]):

```bash
git clone https://github.com/wireghoul/dotdotpwn
```





**Command** ([[Exploit /etc/shadow file using dotdotpwn]]):

```bash
perl dotdotpwn.pl -h 10.10.10.10 -m ftp -t 300 -f /etc/shadow -s -q -b
```



## Commands Used

- [[Clone dotdotpwn repository]]
- [[Exploit /etc/shadow file using dotdotpwn]]

## Tags

- [[Directory Traversal]]
- [[Tools]]


