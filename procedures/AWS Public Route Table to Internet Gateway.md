---
id: fb932118-3097-4efb-8a2d-925950182ff7
name: AWS Public Route Table to Internet Gateway
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:16.648177+00:00'
updated_at: '2023-05-25T20:06:05.124251+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws associate public subnet with route table]]'
- '[[aws associate route table id with subnet id]]'
- '[[aws create route table for vpc and region]]'
- '[[aws create route using route table ID and gateway ID]]'
- '[[Create the Route Table:]]'
---

# AWS Public Route Table to Internet Gateway

**Status**: ✓ Verified

## Summary

Public routes should be setup with an Interet Gateway. 

## Description

# Description

Public routes should be setup with an Interet Gateway.

##  Instructions

1. Creating A Public Route Table

**Command** ([[aws create route table for vpc and region]]):

```bash
aws ec2 create-route-table --vpc-id $AWS_VPC_ID --region $AWS_REGION

```

2. Create a route for an Internet Gateway using the route table ID

**Command** ([[aws create route using route table ID and gateway ID]]):

```bash
aws ec2 create-route --route-table-id $AWS_ROUTE_TABLE_ID --destination-cidr-block $IP_ADDRESS_CIDR --gateway-id $AWS_GATEWAY_ID --region $AWS_REGION

```

3. Finally, associate the public subnet with the Route Table

**Command** ([[aws associate route table id with subnet id]]):

```bash
aws ec2 associate-route-table --route-table-id $AWS_ROUTE_TABLE_ID --subnet-id $AWS_SUBNET_ID --region $AWS_REGION

```

## Platforms

- Cloud

## Commands Used

- [[aws associate public subnet with route table]]
- [[aws associate route table id with subnet id]]
- [[aws create route table for vpc and region]]
- [[aws create route using route table ID and gateway ID]]
- [[Create the Route Table:]]

## Tags

- [[AWS]]
- [[Cloud]]
