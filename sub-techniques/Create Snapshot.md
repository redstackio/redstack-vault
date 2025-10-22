---
id: 04c1df01-cf43-468f-b528-f511380a005e
name: Create Snapshot
type: sub-technique
mitre_id: T1578.001
mitre_url: null
created_at: '2023-04-06T00:31:27.141589+00:00'
updated_at: '2023-04-06T00:31:27.141589+00:00'
parent_technique: '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute
  Infrastructure]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Mounted Docker Socket Pentest]]'
---

# Create Snapshot

**MITRE ID**: T1578.001

**Parent Technique**: [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]

This is a sub-technique of T1578 - Modify Cloud Compute Infrastructure.

## Summary

An adversary may create a snapshot or data backup within a cloud account to evade defenses. A snapshot is a point-in-time copy of an existing cloud compute component such as a virtual machine (VM), virtual hard drive, or volume. An adversary may leverage permissions to create a snapshot in order to 

## Description

An adversary may create a snapshot or data backup within a cloud account to evade defenses. A snapshot is a point-in-time copy of an existing cloud compute component such as a virtual machine (VM), virtual hard drive, or volume. An adversary may leverage permissions to create a snapshot in order to bypass restrictions that prevent access to existing compute service infrastructure, unlike in [Revert Cloud Instance](https://attack.mitre.org/techniques/T1578/004) where an adversary may revert to a snapshot to evade detection and remove evidence of their presence.

An adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002), mount one or more created snapshots to that instance, and then apply a policy that allows the adversary access to the created instance, such as a firewall policy that allows them inbound and outbound SSH access.(Citation: Mandiant M-Trends 2020)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Mounted Docker Socket Pentest]]
