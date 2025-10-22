---
id: e05e0587-45ed-4b9d-bb59-b8b77e2c21aa
name: TAR Argument Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:54.096759+00:00'
updated_at: '2023-04-06T03:55:54.119692+00:00'
tags:
- '[[Argument Injection]]'
- '[[List of exposed commands]]'
- '[[TAR]]'
commands:
- '[[Execute command on checkpoint]]'
- '[[Extract tar file]]'
- '[[Specify compression program]]'
- '[[Specify input program]]'
- '[[Transfer files]]'
---

# TAR Argument Injection

## Summary

TAR is a command-line utility for archiving files. Attackers can inject malicious commands into the arguments of the TAR command, leading to command execution. The attacker may use this technique to evade defenses and execute arbitrary code on the target system. This technique can be used in conjun

## Description

# Description

TAR is a command-line utility for archiving files. Attackers can inject malicious commands into the arguments of the TAR command, leading to command execution. The attacker may use this technique to evade defenses and execute arbitrary code on the target system. This technique can be used in conjunction with other techniques to achieve various objectives such as data exfiltration or privilege escalation. 

When an attacker is successful in injecting malicious code into the TAR command, it can be executed with the same privileges as the user running the TAR command. This can be particularly dangerous if the user is a privileged user. The attacker may use this technique to execute code that allows them to take control of the system or steal sensitive information.

## Requirements

1. Access to the command line interface on the target system

1. Knowledge of the TAR command

## Defense

1. Use input validation to ensure that only expected values are accepted as input.

1. Limit the privileges of the user running the TAR command.

1. Use a host-based intrusion detection system (HIDS) to detect and alert on suspicious activity.

## Objectives

1. Execute arbitrary code on the target system

1. Evade defenses

1. Achieve privilege escalation

# Instructions

1. 

**Code**: [[tar]]

> 

**Command** ([[Extract tar file]]):

```bash
tar -xf file.tar
```

2. To inject a command into the extract command, use the following options:

**Code**: [[--to-command <command>
--checkpoint=1 --checkpoint]]

> The --to-command option allows the attacker to specify a command to be executed for each extracted file. The --checkpoint and --checkpoint-action options allow the attacker to execute a command after a specified number of files have been processed. The -T or --files-from option allows the attacker to specify a file containing a list of files to be extracted.

**Command** ([[Execute command on checkpoint]]):

```bash
--checkpoint=1 --checkpoint-action=exec=<command>
```

**Command** ([[Transfer files]]):

```bash
-T <file> or --files-from <file>
```

3. 

**Code**: [[-I=<program> or -I <program>
--use-compres-program]]

> The -I or --use-compress-program option allows the attacker to specify a program to be used for compression instead of the default gzip program. The attacker can specify a program that executes arbitrary code.

**Command** ([[Specify input program]]):

```bash
-I=<program> or -I <program>
```

**Command** ([[Specify compression program]]):

```bash
--use-compres-program=<program>
```

4. 

**Code**: [[-T<file>
-I"/path/to/exec"]]

> The -T option can be used without a space between the option and the file name. The -I option can be used with a space or an equals sign between the option and the program name. The attacker can use these options to evade detection.

## Commands Used

- [[Execute command on checkpoint]]
- [[Extract tar file]]
- [[Specify compression program]]
- [[Specify input program]]
- [[Transfer files]]

## Tags

- [[Argument Injection]]
- [[List of exposed commands]]
- [[TAR]]
