---
id: e2e69ef2-69b9-4a37-80c2-dbc2c0c0f7b6
name: Lessjs Command Execution via Server Side Template Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.014024+00:00'
updated_at: '2023-04-10T20:23:45.533969+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Lessjs]]'
- '[[Lessjs < v3 - Command Execution]]'
- '[[Server Side Template Injection]]'
---

# Lessjs Command Execution via Server Side Template Injection

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server by injecting code into a template. Lessjs is a CSS preprocessor that allows users to write dynamic stylesheets using variables and functions. Lessjs < v3 is vulnerable to SSTI, w

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server by injecting code into a template. Lessjs is a CSS preprocessor that allows users to write dynamic stylesheets using variables and functions. Lessjs < v3 is vulnerable to SSTI, which can be exploited to execute commands on the server. By setting the text color based on the user ID, an attacker can inject arbitrary commands into the template and execute them on the server. This can lead to full compromise of the server.

## Requirements

1. Access to the application

1. Knowledge of the user ID

## Defense

1. Upgrade to Lessjs v3 or later, which is not vulnerable to SSTI

1. Sanitize user input to prevent injection attacks

1. Implement strict input validation to prevent command injection

## Objectives

1. Execute arbitrary commands on the server

1. Gain full access to the server

# Instructions

1. This command sets the color of the text on the page based on the user ID. The command uses the child_process module to execute the 'id' command and returns the output as the value for the 'color' property in the CSS 'body' selector.

**Code**: [[body {
  color: `global.process.mainModule.require]]

> The 'global.process.mainModule.require' function is used to import the 'child_process' module which allows us to execute shell commands. The 'execSync' function is then used to execute the 'id' command which returns the user ID. The output of the command is then used as the value for the 'color' property in the CSS 'body' selector. This command can be useful for identifying users based on their ID, or for creating user-specific themes or styles.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Lessjs]]
- [[Lessjs < v3 - Command Execution]]
- [[Server Side Template Injection]]
