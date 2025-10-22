---
id: 09c4a992-7818-46ec-9c4d-3a1060aa1107
name: Modify Cloud Compute Infrastructure
type: technique
mitre_id: T1578
mitre_url: null
created_at: '2023-04-06T00:31:25.589544+00:00'
updated_at: '2023-04-06T03:56:28.341639+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Abusing coredumps and core_pattern in Docker containers]]'
- '[[EBS Volume Attachment]]'
- '[[Kerberos Unconstrained Delegation via SpoolService Abuse]]'
- '[[Kubernetes RBAC Pod Exec Privilege Escalation]]'
- '[[Mounted Docker Socket Pentest]]'
- '[[Mounting Elastic Block Store Volume to a Directory]]'
- '[[Windows Subsystem for Linux Persistence]]'
---

# Modify Cloud Compute Infrastructure

**MITRE ID**: T1578

## Description

An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses. A modification to the compute service infrastructure can include the creation, deletion, or modification of one or more components such as compute instances, virtual machines, and snapshots.

Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of their presence.(Citation: Mandiant M-Trends 2020)

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (7)

- [[Abusing coredumps and core_pattern in Docker containers]]
- [[EBS Volume Attachment]]
- [[Kerberos Unconstrained Delegation via SpoolService Abuse]]
- [[Kubernetes RBAC Pod Exec Privilege Escalation]]
- [[Mounted Docker Socket Pentest]]
- [[Mounting Elastic Block Store Volume to a Directory]]
- [[Windows Subsystem for Linux Persistence]]
