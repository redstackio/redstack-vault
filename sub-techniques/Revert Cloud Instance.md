---
id: 754e753e-db34-452f-9e8b-757afe5396ba
name: Revert Cloud Instance
type: sub-technique
mitre_id: T1578.004
mitre_url: null
created_at: '2023-04-06T00:31:25.460775+00:00'
updated_at: '2023-04-06T00:31:25.460775+00:00'
parent_technique: '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute
  Infrastructure]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Revert Cloud Instance

**MITRE ID**: T1578.004

**Parent Technique**: [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]

This is a sub-technique of T1578 - Modify Cloud Compute Infrastructure.

## Summary

An adversary may revert changes made to a cloud instance after they have performed malicious activities in attempt to evade detection and remove evidence of their presence. In highly virtualized environments, such as cloud-based infrastructure, this may be accomplished by restoring virtual machine (

## Description

An adversary may revert changes made to a cloud instance after they have performed malicious activities in attempt to evade detection and remove evidence of their presence. In highly virtualized environments, such as cloud-based infrastructure, this may be accomplished by restoring virtual machine (VM) or data storage snapshots through the cloud management dashboard or cloud APIs.

Another variation of this technique is to utilize temporary storage attached to the compute instance. Most cloud providers provide various types of storage including persistent, local, and/or ephemeral, with the ephemeral types often reset upon stop/restart of the VM.(Citation: Tech Republic - Restore AWS Snapshots)(Citation: Google - Restore Cloud Snapshot)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
