---
id: 69766ec5-624c-4f1f-abe6-0d14ea8cf962
name: PowerShell
type: sub-technique
mitre_id: T1059.001
mitre_url: null
created_at: '2023-04-06T00:31:26.600693+00:00'
updated_at: '2023-04-06T00:31:26.600693+00:00'
parent_technique: '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Abuse GPO with PowerView to Push Empire Stager]]'
- '[[ASP Razor Server Side Template Injection with C# Command Execution]]'
- '[[Dart Reverse PowerShell Shell]]'
- '[[Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks]]'
- '[[Jinja2 Server Side Template Injection with Remote Code Execution]]'
- '[[Jinjava Command Execution]]'
- '[[MSSQL Server External Script Execution]]'
- '[[Reflective Assembly Loading with Powershell]]'
- '[[Server Side Template Injection with Django Templates using Burp Payload Calculation]]'
- '[[Session Management with Metasploit]]'
- '[[Windows - PowerShell Remoting Protocol with PSSESSION]]'
- '[[XLM Excel 4.0 - SharpShooter Payload Creation]]'
---

# PowerShell

**MITRE ID**: T1059.001

**Parent Technique**: [[Command-Line Interface|T1059 - Command-Line Interface]]

This is a sub-technique of T1059 - Command-Line Interface.

## Summary

Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system.(Citation: TechNet PowerShell) Adversaries can use PowerShell to perform a number of actions, including 

## Description

Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system.(Citation: TechNet PowerShell) Adversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code. Examples include the <code>Start-Process</code> cmdlet which can be used to run an executable and the <code>Invoke-Command</code> cmdlet which runs a command locally or on a remote computer (though administrator permissions are required to use PowerShell to connect to remote systems).

PowerShell may also be used to download and run executables from the Internet, which can be executed from disk or in memory without touching disk.

A number of PowerShell-based offensive testing tools are available, including [Empire](https://attack.mitre.org/software/S0363),  [PowerSploit](https://attack.mitre.org/software/S0194), [PoshC2](https://attack.mitre.org/software/S0378), and PSAttack.(Citation: Github PSAttack)

PowerShell commands/scripts can also be executed without directly invoking the <code>powershell.exe</code> binary through interfaces to PowerShell's underlying <code>System.Management.Automation</code> assembly DLL exposed through the .NET framework and Windows Common Language Interface (CLI).(Citation: Sixdub PowerPick Jan 2016)(Citation: SilentBreak Offensive PS Dec 2015)(Citation: Microsoft PSfromCsharp APR 2014)

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]

## Related Procedures

There are 12 procedures using this sub-technique:

- [[Abuse GPO with PowerView to Push Empire Stager]]
- [[ASP Razor Server Side Template Injection with C# Command Execution]]
- [[Dart Reverse PowerShell Shell]]
- [[Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks]]
- [[Jinja2 Server Side Template Injection with Remote Code Execution]]
- [[Jinjava Command Execution]]
- [[MSSQL Server External Script Execution]]
- [[Reflective Assembly Loading with Powershell]]
- [[Server Side Template Injection with Django Templates using Burp Payload Calculation]]
- [[Session Management with Metasploit]]
- [[Windows - PowerShell Remoting Protocol with PSSESSION]]
- [[XLM Excel 4.0 - SharpShooter Payload Creation]]
