---
id: 27945bd4-7af2-4fbe-bd5b-793a16cc5ca2
name: Transfer Data to Cloud Account
type: technique
mitre_id: T1537
mitre_url: null
created_at: '2023-04-06T00:31:27.015455+00:00'
updated_at: '2023-04-06T00:31:27.877497+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
---

# Transfer Data to Cloud Account

**MITRE ID**: T1537

## Description

Adversaries may exfiltrate data by transferring the data, including backups of cloud environments, to another cloud account they control on the same service to avoid typical file transfers/downloads and network-based exfiltration detection.

A defender who is monitoring for large transfers to outside the cloud environment through normal file transfers or over command and control channels may not be watching for data transfers to another account within the same cloud provider. Such transfers may utilize existing cloud provider APIs and the internal address space of the cloud provider to blend into normal traffic or avoid data transfers over external network interfaces.

Incidents have been observed where adversaries have created backups of cloud instances and transferred them to separate accounts.(Citation: DOJ GRU Indictment Jul 2018) 

## Tactics

- [[Exfiltration|TA0010 - Exfiltration]]
