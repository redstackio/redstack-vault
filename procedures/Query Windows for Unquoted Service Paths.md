---
id: 63d7f636-8076-471b-8f8a-34a998802de7
name: Query Windows for Unquoted Service Paths
type: procedure
verified: true
submitted: true
created_at: '2020-01-27T20:41:03.462931+00:00'
updated_at: '2023-05-25T19:54:14.229283+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Path Interception|T1034 - Path Interception]]'
platforms:
- Windows
tags:
- '[[Misconfiguration]]'
commands:
- '[[wmic Query System for Unquoted Service Paths]]'
---

# Query Windows for Unquoted Service Paths

**Status**: ✓ Verified

## Summary

Unquoted service paths are a category of vulnerability where a service calls an application, but executes a completely different program unintentionally. This occurs because the path to the application contains spaces in it, and is not enclosed with quotation marks. If quotation marks were included

## Description

# Description

Unquoted service paths are a category of vulnerability where a service calls an application, but executes a completely different program unintentionally. This occurs because the path to the application contains spaces in it, and is not enclosed with quotation marks. If quotation marks were included, the full path to the application would be evaluated, but without them, Windows will come across the space attempt to execute it if a file exists at that location with the ".exe" extension. 

For example, if a service tries to launch:

C:\Program Files\RealVNC\VNC Viewer\vncviewer.exe

Because the path contains a space and is not enclosed with quotation marks, if an attacker  creates  C:\Program Files\RealVNC\VNC.exe,  then any service trying to execute C:\Program Files\RealVNC\VNC Viewer\vncviewer.exe with unquoted paths will actually execute the payload. These vulnerabilities can only be exploited if the attacker can write a file to the vulnerable path.

# Instructions

Query the system for vulnerable paths

**Command** ([[wmic Query System for Unquoted Service Paths]]):

```bash
wmic.exe service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """
```

Note: this command should be run from cmd.exe, as PowerShell will misinterpret the quotation marks. To run it from PowerShell, prefix the command with "cmd.exe /C" and enclose the rest of the command with single quotes.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Path Interception|T1034 - Path Interception]]

## Commands Used

- [[wmic Query System for Unquoted Service Paths]]

## Tags

- [[Misconfiguration]]
