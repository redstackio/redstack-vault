---
id: 98219e0f-2eab-46d2-94ec-a7d677e7dfdb
name: Linux File Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.984500+00:00'
updated_at: '2023-04-10T20:22:06.509755+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[Directory Traversal]]'
- '[[Interesting Linux files]]'
- '[[Path Traversal]]'
---

# Linux File Enumeration

## Summary

Linux File Enumeration is a technique used to discover interesting files on a Linux system. This technique involves traversing through directories and files on a Linux system to locate files of interest. This technique is commonly used by attackers to identify files that may contain sensitive infor

## Description

# Description

Linux File Enumeration is a technique used to discover interesting files on a Linux system. This technique involves traversing through directories and files on a Linux system to locate files of interest. This technique is commonly used by attackers to identify files that may contain sensitive information such as credentials, configuration files, and system information. Attackers can use this information to further their attack and gain access to the system.

From a technical perspective, this technique involves using path traversal to navigate through directories and files on a Linux system. This can be accomplished through various means including command line tools, web applications, and other means of interacting with the system.

The business value of this technique is that it can help organizations identify weaknesses in their Linux systems and take steps to secure them before attackers can exploit them.

## Requirements

1. Access to a Linux system

## Defense

1. Implement proper access controls to limit access to sensitive files

1. Regularly monitor file system changes and file access logs

1. Implement file integrity monitoring to detect unauthorized changes to files

## Objectives

1. Discover interesting files on a Linux system

1. Identify sensitive information such as credentials and configuration files

1. Assist in securing Linux systems by identifying weaknesses

# Instructions

1. The command above will traverse through all directories and files on the Linux system and list the files and their attributes. The output can be redirected to a file or piped to other commands for further processing.

**Code**: [[/etc/issue
/etc/passwd
/etc/shadow
/etc/group
/etc]]

> The 'find' command is used to search for files on a Linux system. The '-type f' option specifies that only files should be returned, and the '-name "*"' option specifies that all files should be returned. The '-exec' option is used to execute a command on each file found. In this case, the 'ls -al {}' command is executed on each file. The '{}' is a placeholder for the file name. The '2>/dev/null' option is used to redirect error messages to '/dev/null', which discards them.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Tags

- [[Directory Traversal]]
- [[Interesting Linux files]]
- [[Path Traversal]]
