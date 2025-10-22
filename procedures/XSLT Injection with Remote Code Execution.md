---
id: e3025521-9a12-427b-adcf-75d89c8d8a94
name: XSLT Injection with Remote Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.521148+00:00'
updated_at: '2023-04-10T20:24:50.741101+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Exploit]]'
- '[[Remote Code Execution with Embedded Script Blocks]]'
- '[[XSLT Injection]]'
---

# XSLT Injection with Remote Code Execution

## Summary

XSLT Injection is an attack that targets web applications that use XSLT to transform XML documents. Attackers can inject malicious code into the XSLT stylesheet, which can lead to Remote Code Execution (RCE) on the server. In this specific scenario, the attacker can exploit the vulnerability by emb

## Description

# Description

XSLT Injection is an attack that targets web applications that use XSLT to transform XML documents. Attackers can inject malicious code into the XSLT stylesheet, which can lead to Remote Code Execution (RCE) on the server. In this specific scenario, the attacker can exploit the vulnerability by embedding script blocks within the XSLT stylesheet. This can allow them to execute arbitrary code on the server and take control of the system.

From an offensive perspective, XSLT Injection can be used to gain access to sensitive data, escalate privileges, and pivot to other systems. The technical explanation involves injecting malicious code into the XSLT stylesheet, which can then be executed on the server. The business value of this attack lies in the fact that it can lead to data theft, system compromise, and reputational damage for the targeted organization.

## Requirements

1. Access to the vulnerable web application.

1. Knowledge of XSLT Injection techniques.

1. Ability to inject malicious code into the XSLT stylesheet.

## Defense

1. Validate and sanitize all user input, especially those that are used in XSLT transformations.

1. Implement strict input validation and output encoding to prevent injection attacks.

1. Use web application firewalls (WAFs) to detect and block XSLT Injection attacks.

## Objectives

1. Execute arbitrary code on the server.

1. Gain access to sensitive data.

1. Escalate privileges.

1. Pivot to other systems.

# Instructions

1. To list the contents of a directory, execute the following command:

**Code**: [[<?xml version="1.0" encoding="UTF-8"?>
<xsl:styles]]

> This command will execute the 'dir' command in the command prompt and return the list of files and folders in the current directory. The command prompt will be launched using the 'cmd.exe' program located in the 'C:\windows\system32' folder. The '/c' argument is used to run the specified command and then terminate the command prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Tags

- [[Exploit]]
- [[Remote Code Execution with Embedded Script Blocks]]
- [[XSLT Injection]]
