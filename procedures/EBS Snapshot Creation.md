---
id: 37472d2c-71f5-45c1-ac6f-873328419100
name: EBS Snapshot Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.754858+00:00'
updated_at: '2023-04-10T20:20:36.180679+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
tags:
- '[[Creating a snapshot of a specified volume]]'
- '[[Elastic Block Store]]'
- '[[Exploitation & Data Exfiltration]]'
commands:
- '[[Create Snapshot of EC2 Volume]]'
---

# EBS Snapshot Creation

## Summary

The EBS Snapshot Creation procedure involves creating a snapshot of a specified volume in order to exfiltrate data from the local system. This technique can be used by an attacker to steal sensitive data from an AWS environment. To create an EBS snapshot, the attacker can use the 'Create EC2 Snapsh

## Description

# Description

The EBS Snapshot Creation procedure involves creating a snapshot of a specified volume in order to exfiltrate data from the local system. This technique can be used by an attacker to steal sensitive data from an AWS environment. To create an EBS snapshot, the attacker can use the 'Create EC2 Snapshot' command. This command will create a snapshot of the specified volume and store it in S3. The attacker can then download the snapshot from S3 and extract any sensitive data.

From a technical perspective, the EBS Snapshot Creation procedure involves creating a copy of the EBS volume and storing it as a snapshot. This snapshot can then be used to create a new EBS volume or to restore an existing volume to a previous state. This procedure can be used to exfiltrate data from an AWS environment by creating a snapshot of a volume that contains sensitive data.

The business value of this procedure is that it can be used by an attacker to steal sensitive data from an AWS environment. This data can be used for financial gain or to gain a competitive advantage over a business.

 

## Requirements

1. Access to an AWS environment

1. Authentication credentials for the AWS environment

1. The 'Create EC2 Snapshot' command

 

## Defense

1. Limit access to AWS environments to only authorized personnel

1. Monitor for unusual activity, such as large amounts of data being transferred out of an environment

1. Encrypt sensitive data to make it harder for attackers to exfiltrate

 

## Objectives

1. Create a snapshot of a specified EBS volume

1. Exfiltrate data from the local system

 

# Instructions

1. This command is used to create a snapshot of an EC2 volume. The 'volumeID' argument specifies the ID of the volume for which you want to create a snapshot. The 'description' argument is an optional field that allows you to provide a description for the snapshot. The 'profile_name' argument is also optional and is used to specify the name of the AWS CLI profile to use for this command.

 

The 'create-snapshot' command is used to create a snapshot of an EBS volume. Snapshots can be used to create new volumes or to restore data from a previous point in time. The 'volumeID' argument specifies the ID of the volume for which you want to create a snapshot. The 'description' argument allows you to provide a description for the snapshot, which can be useful for identifying the snapshot later. The 'profile_name' argument is used to specify the name of the AWS CLI profile to use for this command. If you don't specify a profile, the default profile will be used. Note that you must have the necessary permissions to create snapshots in order to use this command.



**Command** ([[Create Snapshot of EC2 Volume]]):

```bash
aws ec2 create-snapshot --volume volumeID --description "Example" --profile profile_name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]

## Commands Used

- [[Create Snapshot of EC2 Volume]]

## Tags

- [[Creating a snapshot of a specified volume]]
- [[Elastic Block Store]]
- [[Exploitation & Data Exfiltration]]


