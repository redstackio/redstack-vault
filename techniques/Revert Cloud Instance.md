---
id: 1fe3010b-caeb-441c-a69a-710b64c06069
name: Revert Cloud Instance
type: technique
mitre_id: T1536
mitre_url: null
created_at: '2023-04-06T00:31:25.952259+00:00'
updated_at: '2023-04-06T03:56:09.767765+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Disable CloudTrail on AWS]]'
---

# Revert Cloud Instance

**MITRE ID**: T1536

## Description

An adversary may revert changes made to a cloud instance after they have performed malicious activities in attempt to evade detection and remove evidence of their presence. In highly virtualized environments, such as cloud-based infrastructure, this may be accomplished by restoring virtual machine (VM) or data storage snapshots through the cloud management dashboard or cloud APIs.

Another variation of this technique is to utilize temporary storage attached to the compute instance. Most cloud providers provide various types of storage including persistent, local, and/or ephemeral, with the ephemeral types often reset upon stop/restart of the VM.(Citation: Tech Republic - Restore AWS Snapshots)(Citation: Google - Restore Cloud Snapshot)

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (1)

- [[Disable CloudTrail on AWS]]
