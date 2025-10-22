---
id: 33642f6f-aa7b-46ce-8514-5e5c602ad75e
name: ASP.NET Razor Basic Injection with Addition Command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.901483+00:00'
updated_at: '2023-04-10T20:23:49.231312+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[ASP.NET Razor]]'
- '[[ASP.NET Razor - Basic injection]]'
- '[[Server Side Template Injection]]'
---

# ASP.NET Razor Basic Injection with Addition Command

## Summary

ASP.NET Razor is a popular templating engine for creating dynamic web pages. However, it is vulnerable to server side template injection attacks. An attacker can inject malicious code into a template, which will be executed on the server. This can lead to sensitive data disclosure, privilege escala

## Description

# Description

ASP.NET Razor is a popular templating engine for creating dynamic web pages. However, it is vulnerable to server side template injection attacks. An attacker can inject malicious code into a template, which will be executed on the server. This can lead to sensitive data disclosure, privilege escalation, and remote code execution.

In this basic injection scenario, the attacker uses the Addition Command to demonstrate how arbitrary code can be executed on the server. The attacker injects the following code into a template: @{int a = 1; int b = 2; int c = a + b;}. This code declares three integer variables, assigns them values, and then adds them together. The result of the addition is then printed to the screen. This demonstrates that arbitrary code can be executed on the server using server side template injection.

## Requirements

1. Access to a vulnerable ASP.NET Razor application

## Defense

1. Ensure that all input is properly sanitized and validated

1. Regularly monitor and analyze server logs for suspicious activity

1. Implement strict access controls and least privilege principles

## Objectives

1. Execute arbitrary code on the server

1. Demonstrate the impact of server side template injection

# Instructions

1. To use this command, simply replace the values '1' and '2' with your desired numbers and execute the command.

**Code**: [[3]]

> This command performs a simple addition operation on two values and returns the result.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[ASP.NET Razor]]
- [[ASP.NET Razor - Basic injection]]
- [[Server Side Template Injection]]
