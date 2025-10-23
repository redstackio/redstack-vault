---
id: e3304800-d0bb-49fa-9b55-5a0a6d3b374b
name: EBS Snapshot Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.778224+00:00'
updated_at: '2023-04-10T20:20:15.882238+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Elastic Block Store]]'
- '[[Exploitation & Data Exfiltration]]'
- '[[Listing snapshots]]'
commands:
- '[[List all available snapshots]]'
---

# EBS Snapshot Enumeration

## Summary

EBS Snapshot Enumeration is a technique used by attackers to gain information about the target AWS environment. This technique involves listing all available snapshots for an EBS volume. Attackers can use this information to identify sensitive data or to find snapshots that can be used to launch ne

## Description

# Description

EBS Snapshot Enumeration is a technique used by attackers to gain information about the target AWS environment. This technique involves listing all available snapshots for an EBS volume. Attackers can use this information to identify sensitive data or to find snapshots that can be used to launch new instances with the same data as the original instance. This technique requires access to the AWS account and knowledge of the EBS volume ID.

Technical Explanation: AWS provides a service called Elastic Block Store (EBS) that allows users to create block-level storage volumes for use with EC2 instances. Snapshots are point-in-time copies of these volumes that can be used to restore data or create new volumes. By listing all available snapshots for a volume, attackers can gain valuable information about the data stored on the volume.

Business Value: This technique can be used by attackers to quickly identify sensitive data stored in EBS volumes. By identifying these volumes, attackers can then focus their efforts on exfiltrating this data for financial gain or other nefarious purposes.

 

## Requirements

1. Access to the AWS account

1. Knowledge of the EBS volume ID

 

## Defense

1. Limit access to AWS accounts and resources to only authorized personnel

1. Enable AWS CloudTrail to monitor and log all API calls made to the AWS environment

1. Implement network security measures, such as firewalls and intrusion detection systems, to detect and prevent unauthorized access to the AWS environment

 

## Objectives

1. Identify EBS snapshots associated with a particular volume

1. Determine the contents of EBS snapshots

1. Identify sensitive data stored in EBS snapshots

 

# Instructions

1. To list all available snapshots in your AWS EC2 account, run the following command:

 



**Code**: [[aws ec2 describe-snapshots]]



> This command will provide a detailed list of all snapshots associated with your AWS EC2 account. This includes information such as the snapshot ID, volume ID, creation date, and description. You can use this information to manage your snapshots, such as deleting or copying them. Additionally, you can use filters to narrow down the results based on specific criteria, such as snapshot age or volume ID. For more information on available filters and their usage, refer to the AWS EC2 documentation.



**Command** ([[List all available snapshots]]):

```bash
aws ec2 describe-snapshots
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List all available snapshots]]

## Tags

- [[Elastic Block Store]]
- [[Exploitation & Data Exfiltration]]
- [[Listing snapshots]]


