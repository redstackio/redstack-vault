---
id: b8713660-5865-4f7f-bdc2-ad0a4846b22f
name: Linux and Mac File and Directory Permissions Modification
type: sub-technique
mitre_id: T1222.002
mitre_url: null
created_at: '2023-04-06T00:31:25.476112+00:00'
updated_at: '2023-04-06T00:31:25.476112+00:00'
parent_technique: '[[File Permissions Modification|T1222 - File Permissions Modification]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Linux and Mac File and Directory Permissions Modification

**MITRE ID**: T1222.002

**Parent Technique**: [[File Permissions Modification|T1222 - File Permissions Modification]]

This is a sub-technique of T1222 - File Permissions Modification.

## Summary

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file

## Description

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Most Linux and Linux-based platforms provide a standard set of permission groups (user, group, and other) and a standard set of permissions (read, write, and execute) that are applied to each group. While nuances of each platform’s permissions implementation may vary, most of the platforms provide two primary commands used to manipulate file and directory ACLs: <code>chown</code> (short for change owner), and <code>chmod</code> (short for change mode).

Adversarial may use these commands to make themselves the owner of files and directories or change the mode if current permissions allow it. They could subsequently lock others out of the file. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [Unix Shell Configuration Modification](https://attack.mitre.org/techniques/T1546/004) or tainting/hijacking other instrumental binary/configuration files via [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574).(Citation: 20 macOS Common Tools and Techniques) 

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
