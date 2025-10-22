---
id: 1f701e65-b056-49c3-8a8a-4a8e29f0e3ab
name: Jinja2 Server Side Template Injection Debugging
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.603238+00:00'
updated_at: '2023-04-10T20:23:37.438495+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Debug Statement]]'
- '[[Server Side Template Injection]]'
---

# Jinja2 Server Side Template Injection Debugging

## Summary

Jinja2 is a popular templating engine used for web applications. Debugging is an important part of software development, but it can also be used by attackers to gain information about the application's inner workings. The debug statement in Jinja2 allows developers to print variables and other info

## Description

# Description

Jinja2 is a popular templating engine used for web applications. Debugging is an important part of software development, but it can also be used by attackers to gain information about the application's inner workings. The debug statement in Jinja2 allows developers to print variables and other information during development, but it can also be used by attackers to gain information about the application's internals. An attacker can use this information to craft more targeted attacks against the application.

This procedure focuses on using the debug statement in Jinja2 for server-side template injection attacks. By injecting malicious code into the debug statement, an attacker can execute arbitrary code on the server and potentially gain access to sensitive data or perform other malicious actions.

## Requirements

1. Access to the target web application

1. Knowledge of Jinja2 templating engine and server-side template injection techniques

1. Ability to inject code into the debug statement

## Defense

1. Disable debug mode in production environments to prevent the debug statement from being used by attackers

1. Sanitize user input to prevent malicious code from being injected into the debug statement

1. Regularly monitor and audit the application logs for suspicious activity

## Objectives

1. Inject malicious code into the debug statement to execute arbitrary code on the server

1. Gain access to sensitive data or perform other malicious actions

# Instructions

1. To enable the Debug Extension, follow these steps:
1. Open the Settings menu.
2. Click on the Extensions tab.
3. Find the Debug Extension and click on the toggle switch to enable it.

**Code**: [[{% debug %}]]

> The {% debug %} command is used to display debug information, such as the values of variables, in the output of your code. This command is only useful if the Debug Extension is enabled. If you do not have the Debug Extension enabled, this command will not produce any output.

2. To use this command, simply add {% debug %} to your code where you want to inspect variables and their values.

**Code**: [[<pre>{% debug %}</pre>]]

> This command is used for debugging purposes. When {% debug %} is added to your code, it will pause the execution at that point and display a panel showing all the variables and their values at that point in the code. This can be useful for troubleshooting and identifying errors in your code.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Jinja2]]
- [[Jinja2 - Debug Statement]]
- [[Server Side Template Injection]]
