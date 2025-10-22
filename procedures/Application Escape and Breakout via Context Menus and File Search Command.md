---
id: 7964e0ea-dc6a-452f-bfc2-76e3f02ac086
name: Application Escape and Breakout via Context Menus and File Search Command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.429866+00:00'
updated_at: '2023-04-06T03:56:17.439609+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[File Permissions Modification|T1222 - File Permissions Modification]]'
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tags:
- '[[Application Escape and Breakout]]'
- '[[Bypass file restrictions]]'
- '[[Exploring Context Menus]]'
---

# Application Escape and Breakout via Context Menus and File Search Command

## Summary

Application Escape and Breakout via Context Menus and File Search Command is a technique used by attackers to bypass file restrictions and escape from a sandboxed environment. This technique involves exploiting the context menus of an application to perform actions that are normally restricted, and

## Description

# Description

Application Escape and Breakout via Context Menus and File Search Command is a technique used by attackers to bypass file restrictions and escape from a sandboxed environment. This technique involves exploiting the context menus of an application to perform actions that are normally restricted, and using the File Search Command to locate and access files that are not normally accessible. 

From an offensive perspective, this technique can be used to gain access to sensitive files and data that are normally protected, and to execute malicious code on a target system. From a technical perspective, this technique involves manipulating the application's user interface and file system to achieve the desired outcome. From a business value perspective, this technique can result in data theft, system compromise, and reputational damage.

The objectives of this procedure are to bypass file restrictions, escape from a sandboxed environment, and gain access to sensitive files and data. The goals of the user who is using this procedure are to execute malicious code, steal data, and compromise the target system.

## Requirements

1. Access to the target system

1. Authentication credentials

1. Access to the application

1. Knowledge of the application's context menus and file search command

## Defense

1. Implement proper access controls and permissions to restrict unauthorized access to sensitive files and data

1. Monitor for suspicious activity and behavior, such as unusual file access or attempts to modify file permissions

1. Implement security measures such as sandboxing and application whitelisting to prevent unauthorized access and execution of malicious code

## Objectives

1. Bypass file restrictions

1. Escape from a sandboxed environment

1. Gain access to sensitive files and data

# Instructions

1. search <file name or pattern>

**Code**: [[File name]]

> This command is used to search for a file or multiple files in the current directory. The argument should be either the full name of the file or a pattern that matches the file name. For example, 'search myfile.txt' will search for a file named 'myfile.txt' in the current directory, while 'search *.txt' will search for all files with a '.txt' extension in the current directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[File Permissions Modification|T1222 - File Permissions Modification]]
- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

## Tags

- [[Application Escape and Breakout]]
- [[Bypass file restrictions]]
- [[Exploring Context Menus]]
