---
id: 47604e5e-d531-48e8-853c-5e3397a8a6cd
name: Local Data Staging
type: sub-technique
mitre_id: T1074.001
mitre_url: null
created_at: '2023-04-06T00:31:25.667827+00:00'
updated_at: '2023-04-06T00:31:25.667827+00:00'
parent_technique: '[[Data Staged|T1074 - Data Staged]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Local Data Staging

**MITRE ID**: T1074.001

**Parent Technique**: [[Data Staged|T1074 - Data Staged]]

This is a sub-technique of T1074 - Data Staged.

## Summary

Adversaries may stage collected data in a central location or directory on the local system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells m

## Description

Adversaries may stage collected data in a central location or directory on the local system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.

Adversaries may also stage collected data in various available formats/locations of a system, including local storage databases/repositories or the Windows Registry.(Citation: Prevailion DarkWatchman 2021)

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
