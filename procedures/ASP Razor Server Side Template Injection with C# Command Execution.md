---
id: ce1b4a73-dedf-4cc4-833e-42ce1610eec7
name: ASP Razor Server Side Template Injection with C# Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.922524+00:00'
updated_at: '2023-04-10T20:23:41.206018+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[ASP.NET Razor]]'
- '[[ASP.NET Razor - Command execution]]'
- '[[Server Side Template Injection]]'
---

# ASP Razor Server Side Template Injection with C# Command Execution

## Summary

ASP Razor Server Side Template Injection with C# Command Execution is a technique used by attackers to execute arbitrary commands on a target system. This attack is made possible by exploiting a vulnerability in the ASP.NET Razor view engine. The attacker can inject malicious code into a server-sid

## Description

# Description

ASP Razor Server Side Template Injection with C# Command Execution is a technique used by attackers to execute arbitrary commands on a target system. This attack is made possible by exploiting a vulnerability in the ASP.NET Razor view engine. The attacker can inject malicious code into a server-side template, which is then executed by the server. The malicious code can be used to execute arbitrary commands on the server, allowing the attacker to take control of the system.

From a technical perspective, this attack takes advantage of the ability of the Razor view engine to execute C# code within templates. The attacker injects C# code into the template, which is then executed by the server. The C# code can be used to execute arbitrary commands on the server.

The business value of this attack is that it allows an attacker to gain control of a target system, which can be used for further attacks or to steal sensitive data.

## Requirements

1. Access to a vulnerable ASP.NET Razor application

## Defense

1. Ensure that all input is properly sanitized and validated to prevent injection attacks

1. Implement strict input validation to prevent malicious input from being processed

1. Limit the privileges of the user account running the web server to minimize the impact of any successful attacks

## Objectives

1. Execute arbitrary commands on the target system

1. Take control of the target system

# Instructions

1. Please fill in the details for multiple commands, instruction fields, and explain the arguments of the command in detail.

**Code**: [[@{
  // C# code
}]]

> To use this command, you will need to fill in the details for multiple commands. The 'data' field should contain the C# code that you want to execute. The 'lang' field should be set to 'csharp' to indicate that the code is written in C#. The 'text' field can be left blank. The 'instruction' field should contain instructions for how to use the command, including any required arguments. Finally, the 'explain' field should provide a detailed explanation of the arguments and how to use them.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]
- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[ASP.NET Razor]]
- [[ASP.NET Razor - Command execution]]
- [[Server Side Template Injection]]
