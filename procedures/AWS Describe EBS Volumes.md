---
id: a6f3a9e4-7d38-4f11-8395-643b8ea0e5a3
name: AWS Describe EBS Volumes
type: procedure
verified: false
submitted: false
created_at: '2020-07-31T04:25:29.602967+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws describe volume]]'
- '[[Describing filtered volumes]]'
---

# AWS Describe EBS Volumes

## Summary

You can find unused volumes containing sensitive information on them, it is a common mistake for an admin's to delete an EC2 instance and persist the volume. This allows the attacker the advantage to mount the volume on an existing ec2 instance (If you have access) or create a new EC2 instance and 

## Description

# Description

You can find unused volumes containing sensitive information on them, it is a common mistake for an admin's to delete an EC2 instance and persist the volume.

This allows the attacker the advantage to mount the volume on an existing ec2 instance (If you have access) or create a new EC2 instance and mount the volume there.

IF you find an EBS Volume with Multi-Attach enabled, you can mount it to a second machine simultanously.

[AWS EBS Multi-Attach Doc](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html)

##  Instructions

1. List all of the EBS volumes

**Command** ([[aws describe volume]]):

```bash
aws ec2 describe-volumes

```

**Command** ([[Describing filtered volumes]]):

```bash
aws ec2 describe-volumes --filters  Name=status,Values=creating | available | in-use | deleting | deleted | error

```

## Platforms

- Cloud

## Commands Used

- [[aws describe volume]]
- [[Describing filtered volumes]]

## Tags

- [[AWS]]
- [[Cloud]]
