---
id: ea86aada-3a2c-4280-a94c-2c6f20a27c9e
name: Jinjava Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.966388+00:00'
updated_at: '2023-04-10T20:23:32.930978+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Jinjava]]'
- '[[Jinjava - Command execution]]'
- '[[Server Side Template Injection]]'
---

# Jinjava Command Execution

## Summary

Jinjava is a template engine for Python that allows you to generate dynamic HTML pages. However, if an attacker can control the input to the Jinjava engine, they can inject arbitrary code that can be executed on the server. In this case, the attacker can use the Java Script Engine command execution

## Description

# Description

Jinjava is a template engine for Python that allows you to generate dynamic HTML pages. However, if an attacker can control the input to the Jinjava engine, they can inject arbitrary code that can be executed on the server. In this case, the attacker can use the Java Script Engine command execution to execute arbitrary commands on the server. This can lead to a full compromise of the server and potentially the entire network.

From a technical perspective, Jinjava allows for the injection of code into templates, which can then be executed by the server. This can be leveraged by an attacker to execute arbitrary commands on the server. From a business perspective, this can lead to a loss of sensitive data, downtime, and potentially legal and financial repercussions.

## Requirements

1. Ability to inject code into Jinjava templates

## Defense

1. Ensure that input to the Jinjava engine is properly sanitized

1. Implement a web application firewall (WAF) to detect and block attacks that exploit Jinjava vulnerabilities

1. Regularly update Jinjava and all related software to ensure that known vulnerabilities are patched

## Objectives

1. Execute arbitrary commands on the server

1. Compromise the server and potentially the entire network

# Instructions

1. This command executes arbitrary commands on the target system using Java Script Engine. The command can be modified to execute any command on the target system.

**Code**: [[{{'a'.getClass().forName('javax.script.ScriptEngin]]

> The 'data' field contains four commands separated by newlines. The first command creates a new Java String object. The next three commands create a new Java ProcessBuilder object and execute various commands (whoami, netstat, and uname -a) on the target system. The output of these commands can be retrieved using the org.apache.commons.io.IOUtils.toString() method.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]
- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Jinjava]]
- [[Jinjava - Command execution]]
- [[Server Side Template Injection]]
