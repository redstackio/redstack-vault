---
id: a73b4c87-99c7-4eab-81ae-4458d3f5fd4a
name: Disable Windows Event Logging
type: sub-technique
mitre_id: T1562.002
mitre_url: null
created_at: '2023-04-06T00:31:26.072766+00:00'
updated_at: '2023-04-06T00:31:26.072766+00:00'
parent_technique: '[[Impair Defenses|T1562 - Impair Defenses]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Disable Windows Event Logging

**MITRE ID**: T1562.002

**Parent Technique**: [[Impair Defenses|T1562 - Impair Defenses]]

This is a sub-technique of T1562 - Impair Defenses.

## Summary

Adversaries may disable Windows event logging to limit data that can be leveraged for detections and audits. Windows event logs record user and system activity such as login attempts, process creation, and much more.(Citation: Windows Log Events) This data is used by security tools and analysts to g

## Description

Adversaries may disable Windows event logging to limit data that can be leveraged for detections and audits. Windows event logs record user and system activity such as login attempts, process creation, and much more.(Citation: Windows Log Events) This data is used by security tools and analysts to generate detections.

The EventLog service maintains event logs from various system components and applications.(Citation: EventLog_Core_Technologies) By default, the service automatically starts when a system powers on. An audit policy, maintained by the Local Security Policy (secpol.msc), defines which system events the EventLog service logs. Security audit policy settings can be changed by running secpol.msc, then navigating to <code>Security Settings\Local Policies\Audit Policy</code> for basic audit policy settings or <code>Security Settings\Advanced Audit Policy Configuration</code> for advanced audit policy settings.(Citation: Audit_Policy_Microsoft)(Citation: Advanced_sec_audit_policy_settings) <code>auditpol.exe</code> may also be used to set audit policies.(Citation: auditpol)

Adversaries may target system-wide logging or just that of a particular application. For example, the EventLog service may be disabled using the following PowerShell line: <code>Stop-Service -Name EventLog</code>.(Citation: Disable_Win_Event_Logging) Additionally, adversaries may use <code>auditpol</code> and its sub-commands in a command prompt to disable auditing or clear the audit policy. To enable or disable a specified setting or audit category, adversaries may use the <code>/success</code> or <code>/failure</code> parameters. For example, <code>auditpol /set /category:”Account Logon” /success:disable /failure:disable</code> turns off auditing for the Account Logon category.(Citation: auditpol.exe_STRONTIC)(Citation: T1562.002_redcanaryco) To clear the audit policy, adversaries may run the following lines: <code>auditpol /clear /y</code> or <code>auditpol /remove /allusers</code>.(Citation: T1562.002_redcanaryco)

By disabling Windows event logging, adversaries can operate while leaving less evidence of a compromise behind.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
