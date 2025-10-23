---
id: e034c869-bfe3-4e7b-b49e-8fd280ea3fd5
name: LaTex Injection - Write File
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.773485+00:00'
updated_at: '2023-04-06T03:56:01.791871+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[LaTex Injection]]'
- '[[Write file]]'
---

# LaTex Injection - Write File

## Summary

LaTeX Injection is a technique used to inject LaTeX code into a document. This technique can be used to execute arbitrary code on the target system. This procedure focuses on writing a file using LaTeX Injection. The attacker can use this technique to write arbitrary files on the target system. The

## Description

# Description

LaTeX Injection is a technique used to inject LaTeX code into a document. This technique can be used to execute arbitrary code on the target system. This procedure focuses on writing a file using LaTeX Injection. The attacker can use this technique to write arbitrary files on the target system. The business value of this technique is that it can be used to exfiltrate data or to gain persistence on the target system.

 

## Requirements

1. Access to the target system

1. Knowledge of LaTeX syntax

 

## Defense

1. Implement input validation to prevent untrusted input from being processed as LaTeX code.

1. Use a whitelist approach to only allow known safe LaTeX commands and syntax.

1. Implement least privilege access controls to limit the damage that can be done by a successful LaTeX Injection attack.

 

## Objectives

1. Write a file on the target system using LaTeX Injection

 

# Instructions

1. The command writes a single lined file using LaTeX Injection.

 



**Code**: [[\newwrite\outfile
\openout\outfile=cmd.tex
\write\]]



> The command creates a new file using the \newwrite command, opens the file for writing using the \openout command, writes the contents of the file using the \write command, and then closes the file using the \closeout command. The file contents are specified within the curly braces of the \write command.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Tags

- [[LaTex Injection]]
- [[Write file]]


