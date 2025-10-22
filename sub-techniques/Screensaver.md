---
id: 30d6a26f-2f06-4d4f-a587-ce5f5286664b
name: Screensaver
type: sub-technique
mitre_id: T1546.002
mitre_url: null
created_at: '2023-04-06T00:31:26.961093+00:00'
updated_at: '2023-04-06T00:31:26.961093+00:00'
parent_technique: '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Dart Reverse PowerShell Shell]]'
- '[[DCOM Shell Command Execution via MMC Application Class]]'
---

# Screensaver

**MITRE ID**: T1546.002

**Parent Technique**: [[Event Triggered Execution|T1546 - Event Triggered Execution]]

This is a sub-technique of T1546 - Event Triggered Execution.

## Summary

Adversaries may establish persistence by executing malicious content triggered by user inactivity. Screensavers are programs that execute after a configurable time of user inactivity and consist of Portable Executable (PE) files with a .scr file extension.(Citation: Wikipedia Screensaver) The Window

## Description

Adversaries may establish persistence by executing malicious content triggered by user inactivity. Screensavers are programs that execute after a configurable time of user inactivity and consist of Portable Executable (PE) files with a .scr file extension.(Citation: Wikipedia Screensaver) The Windows screensaver application scrnsave.scr is located in <code>C:\Windows\System32\</code>, and <code>C:\Windows\sysWOW64\</code>  on 64-bit Windows systems, along with screensavers included with base Windows installations.

The following screensaver settings are stored in the Registry (<code>HKCU\Control Panel\Desktop\</code>) and could be manipulated to achieve persistence:

* <code>SCRNSAVE.exe</code> - set to malicious PE path
* <code>ScreenSaveActive</code> - set to '1' to enable the screensaver
* <code>ScreenSaverIsSecure</code> - set to '0' to not require a password to unlock
* <code>ScreenSaveTimeout</code> - sets user inactivity timeout before screensaver is executed

Adversaries can use screensaver settings to maintain persistence by setting the screensaver to run malware after a certain timeframe of user inactivity.(Citation: ESET Gazer Aug 2017)

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[Dart Reverse PowerShell Shell]]
- [[DCOM Shell Command Execution via MMC Application Class]]
