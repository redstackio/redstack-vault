---
id: a88f10ef-eaf4-4340-afdd-8384fe629013
name: XDG Autostart Entries
type: sub-technique
mitre_id: T1547.013
mitre_url: null
created_at: '2023-04-06T00:31:27.067151+00:00'
updated_at: '2023-04-06T00:31:27.067151+00:00'
parent_technique: '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart
  Execution]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# XDG Autostart Entries

**MITRE ID**: T1547.013

**Parent Technique**: [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]

This is a sub-technique of T1547 - Boot or Logon Autostart Execution.

## Summary

Adversaries may modify XDG autostart entries to execute programs or commands during system boot. Linux desktop environments that are XDG compliant implement functionality for XDG autostart entries. These entries will allow an application to automatically start during the startup of a desktop environ

## Description

Adversaries may modify XDG autostart entries to execute programs or commands during system boot. Linux desktop environments that are XDG compliant implement functionality for XDG autostart entries. These entries will allow an application to automatically start during the startup of a desktop environment after user logon. By default, XDG autostart entries are stored within the <code>/etc/xdg/autostart</code> or <code>~/.config/autostart</code> directories and have a .desktop file extension.(Citation: Free Desktop Application Autostart Feb 2006)

Within an XDG autostart entry file, the <code>Type</code> key specifies if the entry is an application (type 1), link (type 2) or directory (type 3). The <code>Name</code> key indicates an arbitrary name assigned by the creator and the <code>Exec</code> key indicates the application and command line arguments to execute.(Citation: Free Desktop Entry Keys)

Adversaries may use XDG autostart entries to maintain persistence by executing malicious commands and payloads, such as remote access tools, during the startup of a desktop environment. Commands included in XDG autostart entries with execute after user logon in the context of the currently logged on user. Adversaries may also use [Masquerading](https://attack.mitre.org/techniques/T1036) to make XDG autostart entries look as if they are associated with legitimate programs.

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
