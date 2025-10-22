---
id: 9736e617-19e3-42e4-95ab-edaea93405b0
name: Git Hook Backdoor Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.326844+00:00'
updated_at: '2023-04-10T20:34:17.575447+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Modify Existing Service|T1031 - Modify Existing Service]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Backdooring Git]]'
- '[[Git Hooks]]'
- '[[Linux - Persistence]]'
commands:
- '[[List all files in .git/hooks directory]]'
---

# Git Hook Backdoor Persistence

## Summary

Git hooks are scripts that run automatically when certain actions occur in Git repositories. By backdooring Git hooks, an attacker can gain persistence on a system and execute arbitrary code every time a Git command is run. This technique can be used to maintain access to a compromised system or to

## Description

# Description

Git hooks are scripts that run automatically when certain actions occur in Git repositories. By backdooring Git hooks, an attacker can gain persistence on a system and execute arbitrary code every time a Git command is run. This technique can be used to maintain access to a compromised system or to establish a foothold in a new environment. To backdoor Git hooks, an attacker can modify existing hooks or create new ones that execute their own code. Once the hooks are in place, they can be made executable to ensure they run automatically.

## Requirements

1. Access to a Git repository

1. Ability to modify Git hooks

1. Ability to make Git hooks executable

## Defense

1. Regularly review Git hooks for unexpected changes

1. Restrict access to Git repositories and hooks to trusted users only

1. Monitor system logs for suspicious Git activity

## Objectives

1. Gain persistence on a compromised system

1. Establish a foothold in a new environment

1. Execute arbitrary code every time a Git command is run

# Instructions

1. To use Git Hooks, navigate to the .git/hooks directory and create a file with the name of the hook you want to use. Then, add the necessary code to the file to execute the desired action. Make sure the file is executable by running 'chmod +x filename'.

**Code**: [[.git/hooks]]

> Git Hooks are scripts that run automatically when certain actions occur in a Git repository. They can be used to enforce coding standards, run tests, or perform other tasks at various points in the Git workflow. The .git/hooks directory contains sample hook scripts that can be used as a starting point for creating your own custom hooks.

**Command** ([[List all files in .git/hooks directory]]):

```bash
ls .git/hooks
```

2. To make Git hooks executable, use the following command:

**Code**: [[chmod +x]]

> This command changes the file permissions of Git hooks to make them executable. Git hooks are scripts that run automatically when certain actions are performed in a Git repository. By default, Git hooks are not executable, so this command is necessary to make them run properly. The hooks are stored in the `.git/hooks` directory, and are run when their name matches the current Git action and the hook is marked as executable.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Modify Existing Service|T1031 - Modify Existing Service]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[List all files in .git/hooks directory]]

## Tags

- [[Backdooring Git]]
- [[Git Hooks]]
- [[Linux - Persistence]]
