---
id: ba178458-4178-4501-85cd-b6a0e324cc80
name: EBS Enumeration via EC2 Volumes Description
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.705047+00:00'
updated_at: '2023-04-10T20:19:50.213877+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[Elastic Block Store]]'
- '[[Enumerating EBS volumes]]'
- '[[Enumeration]]'
commands:
- '[[Describe EC2 Volumes]]'
---

# EBS Enumeration via EC2 Volumes Description

## Summary

Elastic Block Store (EBS) is a persistent block storage service for Amazon Elastic Compute Cloud (EC2) instances. Attackers can enumerate EBS volumes to identify sensitive data or to identify potential targets for further attacks. The EC2 Volumes Description command can be used to enumerate EBS vol

## Description

# Description

Elastic Block Store (EBS) is a persistent block storage service for Amazon Elastic Compute Cloud (EC2) instances. Attackers can enumerate EBS volumes to identify sensitive data or to identify potential targets for further attacks. The EC2 Volumes Description command can be used to enumerate EBS volumes and obtain information such as volume ID, size, and attachment information. This information can then be used to mount the volume to another instance or to identify potential targets for further attacks.

Technical Description: An attacker can use the EC2 Volumes Description command to enumerate EBS volumes. The command returns a list of all EBS volumes in the account along with their ID, size, and attachment information. The attacker can then use this information to mount the volume to another instance or to identify potential targets for further attacks.

Business Value: An attacker can use this technique to identify potential targets for further attacks or to obtain sensitive data stored on EBS volumes.

## Requirements

1. Access to an AWS account with permissions to describe EC2 volumes

## Defense

1. Ensure that IAM policies are configured to restrict access to the EC2 Volumes Description command to only authorized users or roles

1. Monitor AWS CloudTrail logs for unusual or unauthorized use of the EC2 Volumes Description command

1. Implement encryption and access controls to protect sensitive data stored on EBS volumes

## Objectives

1. Identify EBS volumes in the target environment

1. Obtain information such as volume ID, size, and attachment information for identified EBS volumes

1. Identify potential targets for further attacks

1. Obtain sensitive data stored on EBS volumes

# Instructions

1. This command retrieves information about Amazon Elastic Block Store (Amazon EBS) volumes.

The 'aws ec2 describe-volumes' command can be used to retrieve information about Amazon EBS volumes. This command returns a list of all EBS volumes in the specified region, as well as their properties, such as size, status, and attachment information. You can use this command to obtain detailed information about your EBS volumes, which can be useful for troubleshooting, monitoring, and managing your Amazon EC2 instances.

**Command** ([[Describe EC2 Volumes]]):

```bash
aws ec2 describe-volumes
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Describe EC2 Volumes]]

## Tags

- [[Elastic Block Store]]
- [[Enumerating EBS volumes]]
- [[Enumeration]]
