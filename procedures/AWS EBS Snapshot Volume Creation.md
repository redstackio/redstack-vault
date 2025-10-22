---
id: 8d283cd7-110a-4b90-9cd0-e4b8b98e6f72
name: AWS EBS Snapshot Volume Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.804617+00:00'
updated_at: '2023-04-10T20:20:10.438647+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Internal Spearphishing|T1534 - Internal Spearphishing]]'
tags:
- '[[Creating a volume from a snapshot]]'
- '[[Elastic Block Store]]'
- '[[Exploitation & Data Exfiltration]]'
commands:
- '[[Create EC2 Volume from Snapshot]]'
---

# AWS EBS Snapshot Volume Creation

## Summary

The AWS EBS Snapshot Volume Creation procedure involves creating a new EBS volume from a previously taken snapshot. This technique can be used by attackers to gain access to sensitive data stored in EBS volumes. The attacker can create a new volume from a snapshot of a target EBS volume and then at

## Description

# Description

The AWS EBS Snapshot Volume Creation procedure involves creating a new EBS volume from a previously taken snapshot. This technique can be used by attackers to gain access to sensitive data stored in EBS volumes. The attacker can create a new volume from a snapshot of a target EBS volume and then attach it to an EC2 instance. Once attached, the attacker can access and exfiltrate sensitive data from the volume. This technique can be used in conjunction with other AWS exploitation techniques to gain access to sensitive data stored in the cloud.

From a technical perspective, this procedure involves using the 'Create AWS EBS Volume from Snapshot' command to create a new EBS volume from a previously taken snapshot. The attacker then attaches the new volume to an EC2 instance and mounts the volume to access the data stored on it.

The business value of this technique lies in the fact that AWS EBS volumes are commonly used to store sensitive data in the cloud. By gaining access to these volumes, attackers can steal sensitive data and use it for malicious purposes.

## Requirements

1. Valid AWS credentials with permissions to create EBS volumes and attach them to EC2 instances

1. Access to a previously taken EBS snapshot

## Defense

1. Implement strict access control policies to prevent unauthorized access to AWS resources

1. Regularly monitor AWS EBS volumes for any unauthorized changes or access

1. Encrypt sensitive data stored in EBS volumes to protect it from unauthorized access

## Objectives

1. Create a new EBS volume from a previously taken snapshot

1. Attach the new volume to an EC2 instance

1. Access and exfiltrate sensitive data from the volume

# Instructions

1. To create a new EBS volume from a snapshot, use the following command:

**Code**: [[aws ec2 create-volume --snapshot-id ID --availabil]]

> The `aws ec2 create-volume` command is used to create a new Amazon Elastic Block Store (EBS) volume from a snapshot. The `--snapshot-id` option specifies the ID of the snapshot that you want to use as the basis for the new volume. The `--availability-zone` option specifies the availability zone in which to create the new volume. The `--profile` option specifies the AWS CLI profile to use for this command.

Note that the `create-volume` command only creates the volume. You will still need to attach it to an instance using the `aws ec2 attach-volume` command.

**Command** ([[Create EC2 Volume from Snapshot]]):

```bash
aws ec2 create-volume --snapshot-id ID --availability-zone ZONE --profile profile_name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Internal Spearphishing|T1534 - Internal Spearphishing]]

## Commands Used

- [[Create EC2 Volume from Snapshot]]

## Tags

- [[Creating a volume from a snapshot]]
- [[Elastic Block Store]]
- [[Exploitation & Data Exfiltration]]
