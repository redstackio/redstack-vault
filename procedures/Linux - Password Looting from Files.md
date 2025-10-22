---
id: 4eb9ecd7-be60-4729-a7bc-b282b7af397a
name: Linux - Password Looting from Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.459223+00:00'
updated_at: '2023-04-10T20:34:28.644594+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Credentials in Files|T1081 - Credentials in Files]]'
tags:
- '[[Files containing passwords]]'
- '[[Linux - Privilege Escalation]]'
- '[[Looting for passwords]]'
---

# Linux - Password Looting from Files

## Summary

This procedure involves searching for files on a Linux system that contain plain text passwords. Attackers can use this information to escalate their privileges and gain access to additional systems or sensitive data. This technique is commonly used in combination with other methods to achieve a fu

## Description

# Description

This procedure involves searching for files on a Linux system that contain plain text passwords. Attackers can use this information to escalate their privileges and gain access to additional systems or sensitive data. This technique is commonly used in combination with other methods to achieve a full compromise of a system.

To execute this procedure, the attacker must have already gained initial access to the system and have the ability to execute commands as a low-privileged user. The attacker will search for files that contain passwords, either by using a tool or manually searching through the file system. Once the files are found, the attacker can use the passwords to escalate their privileges and gain access to additional systems or data.

This procedure can be valuable for an attacker as it allows them to quickly gain access to additional systems or data without having to go through the effort of cracking passwords or performing other time-consuming attacks.

## Requirements

1. Access to a Linux system

1. Ability to execute commands as a low-privileged user

## Defense

1. Ensure that file permissions are set correctly and that sensitive files are not readable by low-privileged users

1. Implement strong password policies and ensure that passwords are not stored in plain text files

1. Monitor file system activity for suspicious behavior, such as large numbers of files being accessed or modified

## Objectives

1. Locate files containing plain text passwords

1. Escalate privileges on the system

1. Gain access to additional systems or sensitive data

# Instructions

1. This command can be used to search for the word 'PASSWORD' in all the files in the current directory and its subdirectories. It will return the file name and the line number where the word is found. 

The command can also be used to search for the word in a specific directory by replacing the '/' with the path to the directory.

The output can be piped to a file by adding '> output.txt' at the end of the command.

The '2> /dev/null' part of the command is used to suppress error messages.

The second part of the command is used to search for the word 'PASSWORD' in all files in the current directory and its subdirectories. It will return the file name and the line number where the word is found. The '{}' and '/null' are used to ensure that the command works with file names that contain spaces.

**Code**: [[grep --color=auto -rnw '/' -ie "PASSWORD" --color=]]

> The command 'grep' is used to search for a specific pattern in a file or multiple files. The options used in this command are:

--color=auto: This option is used to highlight the search term in the output.
-r: This option is used to search for the term recursively in all subdirectories.
-n: This option is used to print the line number where the term is found.
-w: This option is used to match the search term as a whole word.
-ie: This option is used to ignore case when searching for the term.
2> /dev/null: This option is used to redirect error messages to null so they are not displayed.

The command 'find' is used to search for files in a directory hierarchy. The options used in this command are:

-type f: This option is used to search for files only.
-exec: This option is used to execute a command on the files that are found.
-i: This option is used to ignore case when searching for the term.
-I: This option is used to ignore binary files.
{} /null: These options are used to ensure that the command works with file names that contain spaces.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Credentials in Files|T1081 - Credentials in Files]]

## Tags

- [[Files containing passwords]]
- [[Linux - Privilege Escalation]]
- [[Looting for passwords]]
