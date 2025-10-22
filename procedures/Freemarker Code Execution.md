---
id: 3f16face-f05c-4be5-b478-f393c0614c83
name: Freemarker Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.053200+00:00'
updated_at: '2023-04-10T20:23:36.340725+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Freemarker]]'
- '[[Freemarker - Code execution]]'
- '[[Server Side Template Injection]]'
---

# Freemarker Code Execution

## Summary

Freemarker is a Java-based template engine that allows developers to generate dynamic web pages. However, if a web application is vulnerable to server-side template injection (SSTI), an attacker can execute arbitrary code on the server. This can lead to complete compromise of the application and po

## Description

# Description

Freemarker is a Java-based template engine that allows developers to generate dynamic web pages. However, if a web application is vulnerable to server-side template injection (SSTI), an attacker can execute arbitrary code on the server. This can lead to complete compromise of the application and potentially the underlying system. The attacker can use this technique to steal sensitive data, modify or delete data, or even take control of the server. From a technical perspective, the attacker can insert malicious code into a template file that is then executed by the server. This technique is highly effective as it allows the attacker to bypass traditional security controls such as firewalls and intrusion detection systems. From a business perspective, this attack can lead to loss of reputation, financial loss, and legal liability.

## Requirements

1. Access to a web application vulnerable to SSTI

1. Knowledge of Freemarker syntax

1. Ability to inject malicious code into a template file

## Defense

1. Ensure that all input is properly validated and sanitized to prevent injection attacks

1. Implement a web application firewall (WAF) to detect and block SSTI attacks

1. Regularly update and patch the web application and underlying system to prevent known vulnerabilities

## Objectives

1. Execute arbitrary code on the server

1. Steal sensitive data

1. Modify or delete data

1. Take control of the server

# Instructions

1. This command allows remote code execution on a server that uses FreeMarker template engine. The attacker can inject malicious code into the 'id' parameter to execute arbitrary commands on the target system.

**Code**: [[<#assign ex = "freemarker.template.utility.Execute]]

> The 'data' field contains the payload that can be used to exploit the vulnerability. The payload creates a new instance of the 'freemarker.template.utility.Execute' class and then executes the 'id' parameter within it. The 'lang' field specifies the language used in the payload, which is JavaScript in this case. The 'instruction' field provides a brief explanation of the attack and its impact. The 'explain' field provides a detailed explanation of the attack, its impact, and how it can be prevented.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Freemarker]]
- [[Freemarker - Code execution]]
- [[Server Side Template Injection]]
