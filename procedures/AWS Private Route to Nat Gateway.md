---
id: 34af1e52-31e3-4230-82c0-b2867e5f3468
name: AWS Private Route to Nat Gateway
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:33.457118+00:00'
updated_at: '2023-05-25T20:07:30.574223+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Other Network Medium|T1011 - Exfiltration Over Other Network
  Medium]]'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws associate public subnet with route table]]'
- '[[aws associate route table id with subnet id]]'
- '[[aws create route table for nat gateway]]'
- '[[aws create route table for vpc and region]]'
- '[[Create the Route Table:]]'
---

# AWS Private Route to Nat Gateway

**Status**: ✓ Verified

## Summary

You may come across a private subnet in AWS that cannot access the internet, you can create a route table entry pointing to a NAT Gateway to help those servers reach the internet egress, for example data exfiltration. (See AWS Setup Nat Gateway) on how to setup a nat-gateway in a VPC. 

## Description

# Description

You may come across a private subnet in AWS that cannot access the internet, you can create a route table entry pointing to a NAT Gateway

to help those servers reach the internet egress, for example data exfiltration.

(See AWS Setup Nat Gateway) on how to setup a nat-gateway in a VPC.

##  Instructions

1. (Optional) Create the Route Table



**Command** ([[Create the Route Table:]]):

```bash
aws ec2 create-route-table --vpc-id $AWS_VPC_ID --region $AWS_REGION

```







2. then create a route that points to a NAT Gateway



**Command** ([[aws create route table for nat gateway]]):

```bash
aws ec2 create-route --route-table-id $AWS_ROUTE_TABLE_ID --destination-cidr-block $IP_ADDRESS_CIDR --nat-gateway-id $AWS_NAT_GATEWAY_ID --region $AWS_REGION

```







3. Associate the subnet with the route table



**Command** ([[aws associate public subnet with route table]]):

```bash
aws ec2 associate-route-table --route-table-id $AWS_ROUTE_TABLE_ID --subnet-id $AWS_SUBNET_ID --region $AWS_REGION

```







## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Other Network Medium|T1011 - Exfiltration Over Other Network Medium]]

## Commands Used

- [[aws associate public subnet with route table]]
- [[aws associate route table id with subnet id]]
- [[aws create route table for nat gateway]]
- [[aws create route table for vpc and region]]
- [[Create the Route Table:]]

## Tags

- [[AWS]]
- [[Cloud]]


