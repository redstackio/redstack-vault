---
id: 8605d4eb-4d06-4757-8c68-7d9c5bee5168
name: Downgrade Attack
type: sub-technique
mitre_id: T1562.010
mitre_url: null
created_at: '2023-04-06T00:31:26.489735+00:00'
updated_at: '2023-04-06T00:31:26.489735+00:00'
parent_technique: '[[Impair Defenses|T1562 - Impair Defenses]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Downgrade Attack

**MITRE ID**: T1562.010

**Parent Technique**: [[Impair Defenses|T1562 - Impair Defenses]]

This is a sub-technique of T1562 - Impair Defenses.

## Summary

Adversaries may downgrade or use a version of system features that may be outdated, vulnerable, and/or does not support updated security controls such as logging. For example, [PowerShell](https://attack.mitre.org/techniques/T1059/001) versions 5+ includes Script Block Logging (SBL) which can record

## Description

Adversaries may downgrade or use a version of system features that may be outdated, vulnerable, and/or does not support updated security controls such as logging. For example, [PowerShell](https://attack.mitre.org/techniques/T1059/001) versions 5+ includes Script Block Logging (SBL) which can record executed script content. However, adversaries may attempt to execute a previous version of PowerShell that does not support SBL with the intent to [Impair Defenses](https://attack.mitre.org/techniques/T1562) while running malicious scripts that may have otherwise been detected.(Citation: CrowdStrike BGH Ransomware 2021)(Citation: Mandiant BYOL 2018)(Citation: att_def_ps_logging)

Adversaries may downgrade and use less-secure versions of various features of a system, such as [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)s or even network protocols that can be abused to enable [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557).(Citation: Praetorian TLS Downgrade Attack 2014)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
