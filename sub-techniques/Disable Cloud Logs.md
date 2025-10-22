---
id: 77146175-c674-4e3d-9107-ef9bdce2faeb
name: Disable Cloud Logs
type: sub-technique
mitre_id: T1562.008
mitre_url: null
created_at: '2023-04-06T00:31:26.931889+00:00'
updated_at: '2023-04-06T00:31:26.931889+00:00'
parent_technique: '[[Impair Defenses|T1562 - Impair Defenses]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Disable Cloud Logs

**MITRE ID**: T1562.008

**Parent Technique**: [[Impair Defenses|T1562 - Impair Defenses]]

This is a sub-technique of T1562 - Impair Defenses.

## Summary

An adversary may disable cloud logging capabilities and integrations to limit what data is collected on their activities and avoid detection. 

Cloud environments allow for collection and analysis of audit and application logs that provide insight into what activities a user does within the environm

## Description

An adversary may disable cloud logging capabilities and integrations to limit what data is collected on their activities and avoid detection. 

Cloud environments allow for collection and analysis of audit and application logs that provide insight into what activities a user does within the environment. If an adversary has sufficient permissions, they can disable logging to avoid detection of their activities. For example, in AWS an adversary may disable CloudWatch/CloudTrail integrations prior to conducting further malicious activity.(Citation: Following the CloudTrail: Generating strong AWS security signals with Sumo Logic)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
