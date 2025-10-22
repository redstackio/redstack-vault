---
id: 7f8f9f5b-3311-4d56-9702-31c4bbdfa83c
name: Ruby Server Side Template Injection - List Files and Directories
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.201972+00:00'
updated_at: '2023-04-10T20:23:50.436321+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[Ruby]]'
- '[[Ruby - List files and directories]]'
- '[[Server Side Template Injection]]'
---

# Ruby Server Side Template Injection - List Files and Directories

## Summary

This procedure allows an attacker to execute a server-side template injection attack in a Ruby application, specifically to list all files and directories in the root directory. Server-side template injection attacks can be used to execute arbitrary code on a server and can lead to complete comprom

## Description

# Description

This procedure allows an attacker to execute a server-side template injection attack in a Ruby application, specifically to list all files and directories in the root directory. Server-side template injection attacks can be used to execute arbitrary code on a server and can lead to complete compromise of the application and the underlying system. In this case, the attacker is able to list all files and directories in the root directory, which can reveal sensitive information about the system and potentially lead to further attacks.

To accomplish this attack, the attacker would need to inject code into a template that is then executed by the server. The injected code would use Ruby's built-in Dir class to list all files and directories in the root directory. The output of this command would then be returned to the attacker.

The business value of this attack is that it allows an attacker to gain access to sensitive information about the system, which can be used for further attacks. It also demonstrates a vulnerability in the application that can be used to compromise the system.

## Requirements

1. Access to a vulnerable Ruby application

1. Knowledge of the template syntax used by the application

## Defense

1. Ensure that all input is properly sanitized and validated to prevent injection attacks

1. Implement access controls to limit the ability of attackers to execute arbitrary code on the server

1. Regularly monitor and review server logs for suspicious activity

## Objectives

1. List all files and directories in the root directory of the target system

# Instructions

1. To list all files and directories in the root directory, use the following command:

> The command used to list all files and directories in the root directory is 'Dir.entries('/')'. This command uses the 'Dir' class in Ruby to access the root directory ('/') and the 'entries' method to list all files and directories within it. The output is an array of strings, where each string represents a file or directory name. The '.' and '..' entries represent the current and parent directory respectively.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Tags

- [[Ruby]]
- [[Ruby - List files and directories]]
- [[Server Side Template Injection]]
