---
id: 659229c7-a1fa-4091-aa60-288e248d3080
name: MSSQL Server Python Script Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.607808+00:00'
updated_at: '2023-04-10T20:36:47.172912+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[PowerShell|T1086 - PowerShell]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[MSSQL Server]]'
- '[[Python:]]'
---

# MSSQL Server Python Script Execution

## Summary

This procedure allows an attacker to execute PowerShell scripts and Python commands on a MSSQL server. By gaining access to a MSSQL server, an attacker can leverage this procedure to execute malicious code on the server, which can lead to data theft, privilege escalation, and further network compro

## Description

# Description

This procedure allows an attacker to execute PowerShell scripts and Python commands on a MSSQL server. By gaining access to a MSSQL server, an attacker can leverage this procedure to execute malicious code on the server, which can lead to data theft, privilege escalation, and further network compromise. The attacker can use PowerShell to run commands or scripts on the server, and use Python to interact with the server's resources and data. This procedure can be used to bypass security controls and gain persistent access to the server.

## Requirements

1. Access to a MSSQL server

1. Authentication credentials with sufficient privileges

1. Ability to run PowerShell scripts and Python commands on the server

## Defense

1. Restrict access to the MSSQL server to authorized personnel only

1. Limit the privileges of user accounts to only what is necessary

1. Monitor MSSQL server logs for suspicious activity and unauthorized access attempts

## Objectives

1. Execute PowerShell scripts and Python commands on a MSSQL server

1. Gain access to sensitive data and resources on the server

1. Maintain persistent access to the server

# Instructions

1. The 'Invoke-SQLOSCmdPython' command is used to execute a PowerShell script and a Python command. The 'Username' parameter specifies the SQL Server login name, the 'Password' parameter specifies the login password, and the 'Instance' parameter specifies the SQL Server instance name. The 'Command' parameter specifies the PowerShell script to execute in base64 encoded format. The 'sp_execute_external_script' command is used to execute the Python command. The '@language' parameter specifies the language of the script, and the '@script' parameter specifies the Python script to execute. The 'WITH RESULT SETS' clause specifies the format of the result set.

**Code**: [[Invoke-SQLOSCmdPython -Username sa -Password Passw]]

> The 'Invoke-SQLOSCmdPython' command executes a PowerShell script and a Python command on a SQL Server instance. The 'Username' parameter specifies the SQL Server login name, and the 'Password' parameter specifies the login password. The 'Instance' parameter specifies the SQL Server instance name. The 'Command' parameter specifies the PowerShell script to execute in base64 encoded format. The 'sp_execute_external_script' command is used to execute the Python command. The '@language' parameter specifies the language of the script, and the '@script' parameter specifies the Python script to execute. The 'WITH RESULT SETS' clause specifies the format of the result set. This command can be used to execute complex scripts that combine PowerShell and Python commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[PowerShell|T1086 - PowerShell]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[MSSQL Server]]
- [[Python:]]
