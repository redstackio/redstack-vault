---
id: a5540974-84db-45f0-9477-05cd7f8a974e
name: AWS Create EC2 AMI Image
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:34.254229+00:00'
updated_at: '2023-05-25T20:08:07.978661+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws create AMI image]]'
- '[[aws create AMI image without reboot]]'
---

# AWS Create EC2 AMI Image

**Status**: ✓ Verified

## Summary

You can take an AMI image of an EC2 instance (optionally without rebooting) and share the AMI image with a different AWS Account ID, Enabling you to export Images of running machines to your attacker account, and building machines from AMI images there. Deploying the EC2 instance on your attacker a

## Description

# Description

You can take an AMI image of an EC2 instance (optionally without rebooting) and share the AMI image with a different AWS Account ID,

Enabling you to export Images of running machines to your attacker account, and building machines from AMI images there.

Deploying the EC2 instance on your attacker account will avoid EC2 Instance alarms and notifications that may be configured with cloudtrail

or third party monitoring services.

# Instructions

1. Create an AMI image from a EC2 instance ID and give it a description.



**Command** ([[aws create AMI image]]):

```bash
aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description $AWS_AMI_DESCRIPTION

```







2. (Optional) Create an AMI image from an EC2 instance ID without rebooting the instance



**Command** ([[aws create AMI image without reboot]]):

```bash
aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description $AWS_AMI_DESCRIPTION --no-reboot

```







## Platforms

- Cloud

## Commands Used

- [[aws create AMI image]]
- [[aws create AMI image without reboot]]

## Tags

- [[AWS]]
- [[Cloud]]


