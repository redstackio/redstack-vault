---
id: 3381f0e2-68a4-4229-9184-08e758e3a753
name: AWS Create EBS Volume Snapshots
type: procedure
verified: false
submitted: false
created_at: '2020-07-31T04:25:23.822633+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Bypass]]'
- '[[Cloud]]'
commands:
- '[[aws create a snapshot with volume ID]]'
- '[[aws create a snapshot with volume ID and date description]]'
---

# AWS Create EBS Volume Snapshots

## Summary

You can take a snapshot of a volume and mount it to a new EC2 Instances with a new key pair that you have access to All of these AWS functions can set off cloudtrail alarms, but in a highly automated environment,  alerts for ec2 instance deployments could be ignored or turned off. 

## Description

# Description

You can take a snapshot of a volume and mount it to a new EC2 Instances with a new key pair that you have access to

All of these AWS functions can set off cloudtrail alarms, but in a highly automated environment,  alerts for ec2 instance deployments could be ignored or turned off.

##  Instructions

1. Create a snapshot using the Volume ID

**Command** ([[aws create a snapshot with volume ID]]):

```bash
aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID

```

2. (Optional) Create a snapshot and backdate it to fool the admins :)

**Command** ([[aws create a snapshot with volume ID and date description]]):

```bash
aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID --description $AWS_DESCRIPTION

```

## Platforms

- Cloud

## Commands Used

- [[aws create a snapshot with volume ID]]
- [[aws create a snapshot with volume ID and date description]]

## Tags

- [[AWS]]
- [[Bypass]]
- [[Cloud]]
