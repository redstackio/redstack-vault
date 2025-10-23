---
id: 9ba693da-af0d-4937-8d83-3e67dcb3a59e
name: AWS VPC
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:22.995321+00:00'
updated_at: '2023-05-25T20:05:50.127974+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[Allowing DNS hostnames]]'
- '[[Creating A VPC]]'
---

# AWS VPC

**Status**: ✓ Verified

## Summary

You can create a VPC in an alternate region to hide EC2 instances, subnets, gateways from prying eyes. 

# Description

You can create a VPC in an alternate region to hide EC2 instances, subnets, gateways from prying eyes.



## Instructions

1. Create a VPC



**Command** ([[Creating A VPC]]):

```bash
aws ec2 create-vpc --cidr-block <cidr_block> --regiosn <region>

```





2. (Optional) allow dns hostnames



**Command** ([[Allowing DNS hostnames]]):

```bash
aws ec2 modify-vpc-attribute --vpc-id <vpc_id> --enable-dns-hostnames "{\"Value\":true}" --region <region>

```





## Platforms

- Cloud

## Commands Used

- [[Allowing DNS hostnames]]
- [[Creating A VPC]]

## Tags

- [[AWS]]
- [[Cloud]]


