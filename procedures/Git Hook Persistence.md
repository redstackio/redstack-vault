---
id: cb713ba5-3e7b-4e7a-867d-e0c186646b74
name: Git Hook Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.377786+00:00'
updated_at: '2023-04-10T20:34:17.900959+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
- '[[Modify Existing Service|T1031 - Modify Existing Service]]'
tags:
- '[[Backdooring Git]]'
- '[[Git Hooks]]'
- '[[Linux - Persistence]]'
commands:
- '[[Set hooks path]]'
- '[[View Git Configurations]]'
---

# Git Hook Persistence

## Summary

Git Hooks are scripts that run automatically when certain actions occur in Git, such as committing or pushing code. By customizing the Git Hooks path and setting a Git config variable to a common directory, an attacker can backdoor Git and maintain persistence on a Linux system. This technique can 

## Description

# Description

Git Hooks are scripts that run automatically when certain actions occur in Git, such as committing or pushing code. By customizing the Git Hooks path and setting a Git config variable to a common directory, an attacker can backdoor Git and maintain persistence on a Linux system. This technique can be used to execute arbitrary code or steal sensitive data. From a technical perspective, an attacker can modify the Git Hooks path to point to a malicious script that they control. The Git config variable can be set to a directory that the attacker can write to, allowing them to add or modify Git Hooks scripts as needed. From a business perspective, this technique can be used to maintain access to a network or steal intellectual property.

## Requirements

1. Access to a Linux system with Git installed

1. Ability to modify Git configuration settings

## Defense

1. Regularly monitor Git Hooks for unauthorized changes

1. Restrict access to Git configuration settings

1. Implement file integrity monitoring to detect changes to Git Hooks scripts

## Objectives

1. Maintain persistence on a Linux system

1. Execute arbitrary code

1. Steal sensitive data

# Instructions

1. git config --global core.hooksPath <path>

**Code**: [[core.hooksPath]]

> This command allows you to customize the path of a user's git hooks by setting the core.hooksPath configuration variable. This is useful if you want to store your hooks in a different directory than the default location. The <path> argument should be the path to the directory where you want to store your hooks. This command sets the configuration globally for all repositories on your system, but you can also set it locally for a specific repository by omitting the --global flag.

**Command** ([[Set hooks path]]):

```bash
$ git config --global core.hooksPath /path/to/hooks/folder

```

2. To set a Git config variable to a common directory in the user-level Git config file, use the following command:

**Code**: [[~/.gitconfig]]

> git config --global <variable-name> <directory-path>

Replace <variable-name> with the name of the Git config variable you want to set and <directory-path> with the path of the common directory you want to use. The --global option sets the variable globally for the user-level Git config file, which is located at ~/.gitconfig. This allows you to easily reference the common directory in multiple Git repositories on your system.

**Command** ([[View Git Configurations]]):

```bash
cat ~/.gitconfig
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Hijack Execution Flow|T1574 - Hijack Execution Flow]]
- [[Modify Existing Service|T1031 - Modify Existing Service]]

## Commands Used

- [[Set hooks path]]
- [[View Git Configurations]]

## Tags

- [[Backdooring Git]]
- [[Git Hooks]]
- [[Linux - Persistence]]
