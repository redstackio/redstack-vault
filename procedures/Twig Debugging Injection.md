---
id: c0b4bddd-c4a7-4812-9143-dc66ef5c6c02
name: Twig Debugging Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.278039+00:00'
updated_at: '2023-04-10T20:23:53.022031+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Server Side Template Injection]]'
- '[[Twig]]'
- '[[Twig - Basic injection]]'
---

# Twig Debugging Injection

## Summary

Twig is a popular templating engine used by many PHP web applications. When Twig's debugging mode is enabled, it's possible to execute arbitrary code on the server. This can be achieved by injecting Twig syntax into user input fields such as form data, cookies, or HTTP headers. This technique can b

## Description

# Description

Twig is a popular templating engine used by many PHP web applications. When Twig's debugging mode is enabled, it's possible to execute arbitrary code on the server. This can be achieved by injecting Twig syntax into user input fields such as form data, cookies, or HTTP headers. This technique can be used to gain access to sensitive information or execute commands on the server. The attacker can also use this technique to bypass input validation or execute code in the context of the web application.

## Requirements

1. Access to a web application that uses Twig templating engine

1. Knowledge of Twig syntax

1. Ability to inject user input

## Defense

1. Disable Twig debugging mode in production environments

1. Implement input validation to prevent injection attacks

1. Monitor web application logs for suspicious activity

## Objectives

1. Execute arbitrary code on the server

1. Gain access to sensitive information

# Instructions

1. To debug your Twig templates, you can use the dump() function to print out variable values or the entire context. Additionally, you can use the join() filter to concatenate multiple server variables.

**Code**: [[{{7*7}}
{{7*'7'}} would result in 49
{{dump(app)}}]]

> The 'data' field contains multiple examples of how to use the dump() function and the join() filter in Twig. The 'lang' field specifies the programming language used in the examples. The 'text' field contains a link to the official Twig website. The 'instruction' field provides guidance on how to use the dump() function and join() filter for debugging purposes. The 'name' field provides a descriptive name for this command based on its purpose.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Server Side Template Injection]]
- [[Twig]]
- [[Twig - Basic injection]]
