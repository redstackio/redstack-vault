---
id: caaf1337-b75d-4abd-a836-2f31c4b83246
name: AWS List EC2 AMIs
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:19.368656+00:00'
updated_at: '2023-05-25T20:04:43.584266+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws ec2 describe AMI image with filters]]'
- '[[aws ec2 list AMI images]]'
- '[[aws ev2 describe AMI by Image ID]]'
---

# AWS List EC2 AMIs

**Status**: ✓ Verified

## Summary

Gathering data about AMI Images on an account can be useful. 

## Description

# Description

Gathering data about AMI Images on an account can be useful.

##  Instructions

1. List all of the AMI's

**Command** ([[aws ec2 list AMI images]]):

```bash
aws ec2 describe-images

```

2. Describing an AMI by Image ID

**Command** ([[aws ev2 describe AMI by Image ID]]):

```bash
aws ec2 describe-images --image-ids $AWS_IMAGE_ID --profile $AWS_PROFILE --region $AWS_REGION

```

3. (Optional) Describing an OS specific AMI with EBS. Using these filters can provide contextual search results

**Command** ([[aws ec2 describe AMI image with filters]]):

```bash
aws ec2 describe-images --filters "Name=$TYPE,Values=$OS_TYPE" "Name=$TYPE,Values=$VOLUME_TYPE"

```

## Platforms

- Cloud

## Commands Used

- [[aws ec2 describe AMI image with filters]]
- [[aws ec2 list AMI images]]
- [[aws ev2 describe AMI by Image ID]]

## Tags

- [[AWS]]
- [[Cloud]]
