---
id: e1aa602f-60e6-4bfc-9f10-bf74128a0b6a
name: AWS Internet Gateway
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:29.834856+00:00'
updated_at: '2023-05-25T20:08:44.883205+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws ec2 attach internet gateway to vpc]]'
- '[[aws ec2 create an internet gateway]]'
---

# AWS Internet Gateway

**Status**: ✓ Verified

## Summary

Internet Gateway's are used to route traffic for public ip's on ec2 instances and other AWS services inside of a VPC. 

## Description

# Description

Internet Gateway's are used to route traffic for public ip's on ec2 instances and other AWS services inside of a VPC.

##  Instructions

1. Create an Internet Gateway



**Command** ([[aws ec2 create an internet gateway]]):

```bash
aws ec2 create-internet-gateway --region $AWS_REGION

```





2. Attach the Internet Gateway to a VPC



**Command** ([[aws ec2 attach internet gateway to vpc]]):

```bash
aws ec2 attach-internet-gateway --internet-gateway-id $AWS_INTERNET_GATEWAY_ID --vpc-id $AWS_VPC_ID --region $AWS_REGION

```







## Platforms

- Cloud

## Commands Used

- [[aws ec2 attach internet gateway to vpc]]
- [[aws ec2 create an internet gateway]]

## Tags

- [[AWS]]
- [[Cloud]]


