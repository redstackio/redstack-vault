---
id: 0ded9ec6-db5b-48d4-858a-54f4327a5d11
name: 'Reverse Shell: Spawn TTY Shell'
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.052262+00:00'
updated_at: '2023-04-10T20:25:23.486464+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Shared Webroot|T1051 - Shared Webroot]]'
tags:
- '[[Reverse Shell Cheat Sheet]]'
- '[[Spawn TTY Shell]]'
commands:
- '[[Start script]]'
- '[[Switch to user]]'
- '[[Switch to user with password]]'
---

# Reverse Shell: Spawn TTY Shell

## Summary

The Spawn TTY Shell command is used to create a new TTY shell on the target machine, allowing for interactive command execution. This technique can be useful in situations where a simple reverse shell is not enough to achieve the attacker's objectives. By spawning a new TTY shell, the attacker can 

## Description

# Description

The Spawn TTY Shell command is used to create a new TTY shell on the target machine, allowing for interactive command execution. This technique can be useful in situations where a simple reverse shell is not enough to achieve the attacker's objectives. By spawning a new TTY shell, the attacker can execute commands as if they were physically present at the machine.

From a technical perspective, this command uses a combination of Python and Bash commands to create a new TTY shell on the target machine. Once the shell is spawned, the attacker can interact with it as if they were physically present at the machine.

The business value of this technique lies in its ability to provide the attacker with a more interactive and flexible way to execute commands on the target machine, potentially allowing them to achieve their objectives more efficiently.

## Requirements

1. Access to the target machine.

1. Python and Bash commands available on the target machine.

## Defense

1. Implement strict access controls and authentication mechanisms to prevent unauthorized access to the target machine.

1. Regularly monitor and analyze system logs for any signs of suspicious activity.

1. Employ network segmentation to limit the attacker's ability to move laterally within the network.

## Objectives

1. Execute commands on the target machine as if physically present.

1. Gain a more interactive and flexible way to interact with the target machine.

1. Achieve attacker's objectives more efficiently.

# Instructions

1. To use this method, follow the steps below:
1. Run the command '/usr/bin/script -qc /bin/bash /dev/null'
2. Run the command 'su - user' and enter the password when prompted
3. You will now be logged in as the user

Note: If you receive the error 'su: must be run from a terminal', please ensure that you are running the command from a terminal

This command provides an alternative method for logging in as a different user. It uses the 'script' command to create a new shell and then switches to the desired user using the 'su' command. This method is useful when the traditional 'su' command is not working or when there is no access to a terminal.

**Command** ([[Switch to user]]):

```bash
su - user
```

**Command** ([[Start script]]):

```bash
/usr/bin/script -qc /bin/bash /dev/null
```

**Command** ([[Switch to user with password]]):

```bash
su - user
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Shared Webroot|T1051 - Shared Webroot]]

## Commands Used

- [[Start script]]
- [[Switch to user]]
- [[Switch to user with password]]

## Tags

- [[Reverse Shell Cheat Sheet]]
- [[Spawn TTY Shell]]
