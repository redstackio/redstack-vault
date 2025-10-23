---
id: 2a914e7d-ff82-4ce2-8388-6aad83eda32b
name: Mounting EBS Volume to EC2 Linux Instance
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.547207+00:00'
updated_at: '2023-04-10T20:19:52.297837+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
- '[[Internal Spearphishing|T1534 - Internal Spearphishing]]'
tags:
- '[[AWS - Mount EBS volume to EC2 Linux]]'
- '[[Cloud - AWS]]'
commands:
- '[[Attach EBS volume to EC2 instance]]'
- '[[Create EBS volume from snapshot]]'
---

# Mounting EBS Volume to EC2 Linux Instance

## Summary

Mounting an EBS volume to an EC2 Linux instance is a common task in AWS. This procedure allows the user to attach an EBS volume to an EC2 Linux instance and mount it to the instance's file system. This can be useful for expanding the storage capacity of an instance, or for persisting data that need

## Description

# Description

Mounting an EBS volume to an EC2 Linux instance is a common task in AWS. This procedure allows the user to attach an EBS volume to an EC2 Linux instance and mount it to the instance's file system. This can be useful for expanding the storage capacity of an instance, or for persisting data that needs to survive instance termination. From an offensive perspective, an attacker could use this procedure to gain access to sensitive data stored on the EBS volume. From a defensive perspective, this procedure can be used to monitor for unauthorized access or changes to EBS volumes.

 

## Requirements

1. Authenticated access to the AWS console or API

1. An EC2 Linux instance

1. An EBS volume

 

## Defense

1. Limit access to the AWS console or API to only authorized personnel

1. Encrypt sensitive data stored on EBS volumes

1. Monitor for unauthorized access or changes to EBS volumes

 

## Objectives

1. Attach an EBS volume to an EC2 Linux instance

1. Mount the EBS volume to the instance's file system

1. Access data stored on the EBS volume

 

# Instructions

1. To create and attach an EBS volume to an EC2 instance using this command, follow these steps:
1. Replace 'snapshot_id' with the ID of the snapshot from which you want to create the volume.
2. Replace 'zone' with the availability zone in which you want to create the volume.
3. Replace 'volume_id' with the ID of the volume that you want to attach.
4. Replace 'instance_id' with the ID of the instance to which you want to attach the volume.
5. Replace 'device' with the device name that you want to use to attach the volume to the instance.

 



**Code**: [[aws ec2 create-volume –snapshot-id snapshot_id --a]]



> This command is used to create a new EBS volume from a snapshot and attach it to an EC2 instance. The first part of the command 'aws ec2 create-volume' is used to create a new EBS volume from a snapshot. The 'snapshot_id' parameter specifies the ID of the snapshot from which you want to create the volume, and the 'availability-zone' parameter specifies the availability zone in which you want to create the volume.

The second part of the command 'aws ec2 attach-volume' is used to attach the volume to an EC2 instance. The 'volume_id' parameter specifies the ID of the volume that you want to attach, and the 'instance_id' parameter specifies the ID of the instance to which you want to attach the volume. The 'device' parameter specifies the device name that you want to use to attach the volume to the instance.

This command is useful if you want to create a duplicate of an existing EBS volume or if you want to attach an EBS volume to an EC2 instance to store data or files.



**Command** ([[Create EBS volume from snapshot]]):

```bash
aws ec2 create-volume --snapshot-id snapshot_id --availability-zone zone
```





**Command** ([[Attach EBS volume to EC2 instance]]):

```bash
aws ec2 attach-volume --volume-id volume_id --instance-id instance_id --device device
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]
- [[Internal Spearphishing|T1534 - Internal Spearphishing]]

## Commands Used

- [[Attach EBS volume to EC2 instance]]
- [[Create EBS volume from snapshot]]

## Tags

- [[AWS - Mount EBS volume to EC2 Linux]]
- [[Cloud - AWS]]


