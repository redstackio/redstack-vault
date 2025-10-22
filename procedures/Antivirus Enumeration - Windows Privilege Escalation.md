---
id: 07eea62c-a51d-4ff7-9fba-297ebea7c7ce
name: Antivirus Enumeration - Windows Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.749497+00:00'
updated_at: '2023-04-10T20:37:53.508273+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
- '[[Security Software Discovery|T1063 - Security Software Discovery]]'
tags:
- '[[Antivirus Enumeration]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Get AntivirusProduct Display Name]]'
---

# Antivirus Enumeration - Windows Privilege Escalation

## Summary

Antivirus Enumeration is a technique used to discover information about the antivirus software installed on a target system. This information can be used to identify potential vulnerabilities and weaknesses that can be exploited to escalate privileges on the system. This technique involves querying

## Description

# Description

Antivirus Enumeration is a technique used to discover information about the antivirus software installed on a target system. This information can be used to identify potential vulnerabilities and weaknesses that can be exploited to escalate privileges on the system. This technique involves querying the system for information about installed antivirus software and its configuration. This information can then be used to identify potential vulnerabilities and weaknesses that can be exploited to escalate privileges on the system. By identifying the antivirus software installed on the system, an attacker can determine if any known vulnerabilities exist that can be exploited to gain escalated privileges. Additionally, the attacker can use the information gathered to determine if any antivirus software is incorrectly configured or can be bypassed.

## Requirements

1. Access to the target system.

1. Command-line access to the target system.

## Defense

1. Ensure that antivirus software is properly configured and up-to-date.

1. Limit the privileges of users and applications to prevent privilege escalation.

1. Implement network segmentation to limit lateral movement in case of a breach.

## Objectives

1. Identify potential vulnerabilities and weaknesses that can be exploited to escalate privileges on the system.

1. Determine if any known vulnerabilities exist that can be exploited to gain escalated privileges.

1. Determine if any antivirus software is incorrectly configured or can be bypassed.

# Instructions

1. To enumerate all antivirus products installed on a local or remote computer, run the following command:

WMIC /Node:<ComputerName> /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get displayName

Replace <ComputerName> with the name of the remote computer you want to query.

**Code**: [[WMIC /Node:localhost /Namespace:\\root\SecurityCen]]

> This command uses Windows Management Instrumentation (WMI) to query the Security Center namespace and retrieve the display names of all installed antivirus products on a computer. The command can be run locally or remotely by specifying the name of the remote computer with the /Node parameter. The command is useful for troubleshooting antivirus-related issues or verifying that antivirus software is installed and up-to-date on a computer.

**Command** ([[Get AntivirusProduct Display Name]]):

```bash
WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get displayName
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Bypass User Account Control|T1088 - Bypass User Account Control]]
- [[Security Software Discovery|T1063 - Security Software Discovery]]

## Commands Used

- [[Get AntivirusProduct Display Name]]

## Tags

- [[Antivirus Enumeration]]
- [[Windows - Privilege Escalation]]
