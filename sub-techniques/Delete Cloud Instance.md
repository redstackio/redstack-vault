---
id: a624d754-df9b-4aaa-85c8-0eb66e4c8968
name: Delete Cloud Instance
type: sub-technique
mitre_id: T1578.003
mitre_url: null
created_at: '2023-04-06T00:31:26.339751+00:00'
updated_at: '2023-04-06T00:31:26.339751+00:00'
parent_technique: '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute
  Infrastructure]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Delete Cloud Instance

**MITRE ID**: T1578.003

**Parent Technique**: [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]

This is a sub-technique of T1578 - Modify Cloud Compute Infrastructure.

## Summary

An adversary may delete a cloud instance after they have performed malicious activities in an attempt to evade detection and remove evidence of their presence.  Deleting an instance or virtual machine can remove valuable forensic artifacts and other evidence of suspicious behavior if the instance is

## Description

An adversary may delete a cloud instance after they have performed malicious activities in an attempt to evade detection and remove evidence of their presence.  Deleting an instance or virtual machine can remove valuable forensic artifacts and other evidence of suspicious behavior if the instance is not recoverable.

An adversary may also [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and later terminate the instance after achieving their objectives.(Citation: Mandiant M-Trends 2020)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
