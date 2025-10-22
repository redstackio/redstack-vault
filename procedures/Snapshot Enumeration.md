---
id: 8cd85e90-b5f2-474e-901a-dd78237f72b7
name: Snapshot Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.729501+00:00'
updated_at: '2023-04-10T20:20:00.914225+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
tags:
- '[[Elastic Block Store]]'
- '[[Enumerating Snapshots]]'
- '[[Enumeration]]'
commands:
- '[[Describe Snapshots]]'
---

# Snapshot Enumeration

## Summary

Snapshot Enumeration is an offensive technique used to discover the snapshots of Elastic Block Store volumes. By listing the snapshots, an attacker can identify and target specific snapshots for further attacks. This technique can be used for persistence, defense evasion, or data exfiltration. To e

## Description

# Description

Snapshot Enumeration is an offensive technique used to discover the snapshots of Elastic Block Store volumes. By listing the snapshots, an attacker can identify and target specific snapshots for further attacks. This technique can be used for persistence, defense evasion, or data exfiltration. To execute this technique, the attacker needs to have access to the AWS console or API.

## Requirements

1. Access to the AWS console or API

## Defense

1. Limit access to the AWS console or API to authorized personnel only

1. Implement strong authentication and authorization controls

1. Monitor for unusual activity, such as listing of snapshots by unauthorized users

## Objectives

1. Identify snapshots of Elastic Block Store volumes

1. Select specific snapshots for further attacks

1. Maintain persistence on the target system

# Instructions

1. This command lists all the snapshots owned by the account running the command

The `aws ec2 describe-snapshots` command is used to describe one or more snapshots available in Amazon Elastic Block Store (Amazon EBS). In this case, `--owner-ids self` specifies that the command should only return snapshots that are owned by the account running the command. This command can be useful for monitoring the snapshots that are available to an account and for identifying snapshots that are no longer needed and can be deleted.

**Command** ([[Describe Snapshots]]):

```bash
aws ec2 describe-snapshots --owner-ids self
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]

## Commands Used

- [[Describe Snapshots]]

## Tags

- [[Elastic Block Store]]
- [[Enumerating Snapshots]]
- [[Enumeration]]
