---
id: 65920c43-4a89-4c25-aab5-a9fb62af6334
name: AWS Subnets
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:18.368271+00:00'
updated_at: '2023-05-25T20:04:15.403715+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws ec2 auto assign public IPs]]'
- '[[aws ec2 create subnet in vpc]]'
---

# AWS Subnets

**Status**: ✓ Verified

## Summary

You can create subnets inside of a VPC, these can be mapped to public IP's with an Interet Gateway, or a private subnet with a nat gateway. 

## Description

# Description

You can create subnets inside of a VPC, these can be mapped to public IP's with an Interet Gateway, or a private subnet with a nat gateway.

##  Instructions

1. Create a subnet in a vpc, choosing the availability zone, region and ip cidr block.



**Command** ([[aws ec2 create subnet in vpc]]):

```bash
aws ec2 create-subnet --vpc-id <vpc_id> --cidr-block <cidr_block> --availability-zone <availability_zone> --region <region>

```





2. (Optional) Auto assign public IPs to ec2 instances



**Command** ([[aws ec2 auto assign public IPs]]):

```bash
aws ec2 modify-subnet-attribute --subnet-id <subnet_id> --map-public-ip-on-launch --region <region>

```





## Platforms

- Cloud

## Commands Used

- [[aws ec2 auto assign public IPs]]
- [[aws ec2 create subnet in vpc]]

## Tags

- [[AWS]]
- [[Cloud]]


