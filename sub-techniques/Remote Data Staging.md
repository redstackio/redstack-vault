---
id: b98f6742-be06-4fa9-8245-b23e1d6d8f29
name: Remote Data Staging
type: sub-technique
mitre_id: T1074.002
mitre_url: null
created_at: '2023-04-06T00:31:25.896960+00:00'
updated_at: '2023-04-06T00:31:25.896960+00:00'
parent_technique: '[[Data Staged|T1074 - Data Staged]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Remote Data Staging

**MITRE ID**: T1074.002

**Parent Technique**: [[Data Staged|T1074 - Data Staged]]

This is a sub-technique of T1074 - Data Staged.

## Summary

Adversaries may stage data collected from multiple systems in a central location or directory on one system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive 

## Description

Adversaries may stage data collected from multiple systems in a central location or directory on one system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and stage data in that instance.(Citation: Mandiant M-Trends 2020)

By staging data on one system prior to Exfiltration, adversaries can minimize the number of connections made to their C2 server and better evade detection.

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
