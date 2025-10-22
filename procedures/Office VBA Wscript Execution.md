---
id: 45dc1625-520b-41a7-8992-8f69a5bf5033
name: Office VBA Wscript Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.477110+00:00'
updated_at: '2023-04-10T20:36:50.409298+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[DOCM - VBA Wscript]]'
- '[[Office - Attacks]]'
---

# Office VBA Wscript Execution

## Summary

Office VBA Wscript Execution is a technique used to execute commands on a victim's machine by leveraging the Windows Script Host (Wscript) executable. This technique is commonly used by attackers to bypass security controls and execute malicious scripts in order to gain a foothold on a target syste

## Description

# Description

Office VBA Wscript Execution is a technique used to execute commands on a victim's machine by leveraging the Windows Script Host (Wscript) executable. This technique is commonly used by attackers to bypass security controls and execute malicious scripts in order to gain a foothold on a target system. 

In this procedure, the attacker uses VBA macros embedded in a Microsoft Office document to execute the Wscript executable and run commands on the victim's machine. This technique can be used to download and execute additional payloads, steal sensitive data, or gain access to the victim's network. 

This technique is particularly dangerous because it can be used to bypass security controls that are designed to block the execution of malicious code. It is also difficult to detect because the commands are executed using a legitimate Windows executable.

## Requirements

1. Access to a Microsoft Office document containing VBA macros

1. Victim must have Windows Script Host (Wscript) installed

## Defense

1. Disable Windows Script Host (Wscript) if it is not needed for business purposes

1. Implement application whitelisting to prevent the execution of unauthorized scripts

1. Educate users on the risks of opening Microsoft Office documents from untrusted sources

## Objectives

1. Execute commands on a victim's machine

1. Download and execute additional payloads

1. Steal sensitive data

1. Gain access to the victim's network

# Instructions

1. This VBA script opens Notepad using the Windows Script Host. It can be used as a starting point for automating other tasks using VBA.

**Code**: [[Sub parent_change()
    Dim objOL
    Set objOL = ]]

> This script contains three subroutines. The first subroutine, 'parent_change', creates an instance of the Outlook application and then uses the Windows Script Host to open Notepad. The other two subroutines, 'AutoOpen' and 'Auto_Open', call the 'parent_change' subroutine when the workbook is opened. This allows the user to open Notepad automatically when the workbook is opened.

2. This command opens both the Calculator and Notepad applications on the system.

**Code**: [[CreateObject("WScript.Shell").Run "calc.exe"
Creat]]

> The command uses the WScript.Shell object to run the 'calc.exe' executable file to open the Calculator application. It then uses the same object to execute the 'notepad.exe' executable file to open the Notepad application. The 'Run' method is used to open the Calculator application and the 'Exec' method is used to open the Notepad application. Both methods are part of the WScript.Shell object and are used to execute commands on the system. 

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]

## Tags

- [[DOCM - VBA Wscript]]
- [[Office - Attacks]]
