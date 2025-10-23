---
id: 033f6b16-c98c-4be1-ad3d-e7cb3e088124
name: AWS Setup NAT Gateway
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:19.930177+00:00'
updated_at: '2023-05-25T20:08:33.690434+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws allocate elastic ip address in vpc region]]'
- '[[aws create nat gateway in region]]'
---

# AWS Setup NAT Gateway

**Status**: ✓ Verified

## Summary

You may come across a private subnet in AWS that cannot access the internet, you can create a route table entry pointing to a NAT Gateway to help those servers reach the internet egress, for example data exfiltration. 

## Description

# Description

You may come across a private subnet in AWS that cannot access the internet, you can create a route table entry pointing to a NAT Gateway

to help those servers reach the internet egress, for example data exfiltration.

##  Instructions

Setting Up A NAT Gateway

1. allocate an elaastic ip within a VPC & region



**Command** ([[aws allocate elastic ip address in vpc region]]):

```bash
aws ec2 allocate-address --domain vpc --region $AWS_REGION

```







2. then use the AllocationId to create the NAT Gateway for the public zone in the vpc region



**Command** ([[aws create nat gateway in region]]):

```bash
aws ec2 create-nat-gateway --subnet-id $AWS_SUBNET_ID --allocation-id $AWS_ALLOCATION_ID --region $AWS_REGION

```







## Platforms

- Cloud

## Commands Used

- [[aws allocate elastic ip address in vpc region]]
- [[aws create nat gateway in region]]

## Tags

- [[AWS]]
- [[Cloud]]


