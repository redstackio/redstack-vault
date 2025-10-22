---
id: 201e2cb5-7602-4e27-b7c5-df8dac88d538
name: Server Side Template Injection Detection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.877004+00:00'
updated_at: '2023-04-10T20:23:51.223674+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Detection]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection Detection

## Summary

Server Side Template Injection (SSTI) is a vulnerability that occurs when an application incorporates user input into a server-side template, which is then rendered and executed on the server. This can allow an attacker to execute arbitrary code on the server, leading to a variety of attacks such a

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that occurs when an application incorporates user input into a server-side template, which is then rendered and executed on the server. This can allow an attacker to execute arbitrary code on the server, leading to a variety of attacks such as data exfiltration, privilege escalation, and complete compromise of the server. 

To detect SSTI, it is recommended to use a combination of manual and automated techniques. One way to detect SSTI is to look for unusual or unexpected behavior in the application, such as error messages or unexpected output. Another way is to use automated tools that can scan the application for known SSTI vulnerabilities. 

The business value of detecting SSTI lies in preventing potential data breaches and maintaining the integrity of the application and server. By detecting and mitigating SSTI, organizations can protect sensitive data and maintain the trust of their users.

## Requirements

1. Access to the application

1. Knowledge of SSTI vulnerabilities

1. Automated tools for vulnerability scanning (optional)

## Defense

1. Implement input validation and sanitization to prevent SSTI vulnerabilities

1. Use automated tools to regularly scan the application for vulnerabilities

1. Monitor and analyze application logs for unusual behavior or unexpected output

## Objectives

1. Detect and mitigate SSTI vulnerabilities

1. Prevent data breaches and maintain the integrity of the application and server

# Instructions

1. To use this cheatsheet, follow the instructions below:

1. Identify the target and find out if it uses a templating engine.
2. Choose the appropriate payload from the cheatsheet based on the engine used.
3. Inject the payload into the target and observe the response.
4. If successful, proceed with exploiting the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Detection]]
- [[Server Side Template Injection]]
