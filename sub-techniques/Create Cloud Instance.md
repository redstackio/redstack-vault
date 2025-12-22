---
id: ae6d699a-5121-496b-8831-c0fbea62c65f
name: Create Cloud Instance
type: sub-technique
mitre_id: T1578.002
mitre_url: null
created_at: '2023-04-06T00:31:26.964571+00:00'
updated_at: '2023-04-06T00:31:26.964571+00:00'
parent_technique: '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute
  Infrastructure]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Abuse-Core-Dumps-and-Core-Pattern-for-Privilege-Escalation-in-Docker]]'
- '[[Attach-EBS-Volume-to-EC2-Instance]]'
- '[[Deploy-BadPods-for-Kubernetes-Security-Testing]]'
- '[[Kubernetes-RBAC-Pod-Exec-Privilege-Escalation]]'
- '[[Escape-Container-Using-Mounted-Docker-Socket]]'
- '[[Install-and-Persist-via-WSL-with-Kali-Linux]]'
---

# Create Cloud Instance

**MITRE ID**: T1578.002

**Parent Technique**: [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]

This is a sub-technique of T1578 - Modify Cloud Compute Infrastructure.

## Summary

An adversary may create a new instance or virtual machine (VM) within the compute service of a cloud account to evade defenses. Creating a new instance may allow an adversary to bypass firewall rules and permissions that exist on instances currently residing within an account. An adversary may [Crea

## Description

An adversary may create a new instance or virtual machine (VM) within the compute service of a cloud account to evade defenses. Creating a new instance may allow an adversary to bypass firewall rules and permissions that exist on instances currently residing within an account. An adversary may [Create Snapshot](https://attack.mitre.org/techniques/T1578/001) of one or more volumes in an account, create a new instance, mount the snapshots, and then apply a less restrictive security policy to collect [Data from Local System](https://attack.mitre.org/techniques/T1005) or for [Remote Data Staging](https://attack.mitre.org/techniques/T1074/002).(Citation: Mandiant M-Trends 2020)

Creating a new instance may also allow an adversary to carry out malicious activity within an environment without affecting the execution of current running instances.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 6 procedures using this sub-technique:

- [[Abuse-Core-Dumps-and-Core-Pattern-for-Privilege-Escalation-in-Docker]]
- [[Attach-EBS-Volume-to-EC2-Instance]]
- [[Deploy-BadPods-for-Kubernetes-Security-Testing]]
- [[Kubernetes-RBAC-Pod-Exec-Privilege-Escalation]]
- [[Escape-Container-Using-Mounted-Docker-Socket]]
- [[Install-and-Persist-via-WSL-with-Kali-Linux]]
