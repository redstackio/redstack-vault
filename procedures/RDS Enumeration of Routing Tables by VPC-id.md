---
id: 5cf79d88-84d4-41c9-80eb-d3bf716b3823
name: RDS Enumeration of Routing Tables by VPC-id
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.386168+00:00'
updated_at: '2023-04-10T20:20:11.833313+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Enumeration]]'
- '[[Listing routing tables by VPC-id]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Describe Route Tables for VPC ID]]'
---

# RDS Enumeration of Routing Tables by VPC-id

## Summary

The RDS Enumeration of Routing Tables by VPC-id procedure involves listing all routing tables associated with a specific VPC-id. This procedure can be used to identify potential targets for further enumeration, as well as to discover the network topology of the target organization. 

To perform thi

## Description

# Description

The RDS Enumeration of Routing Tables by VPC-id procedure involves listing all routing tables associated with a specific VPC-id. This procedure can be used to identify potential targets for further enumeration, as well as to discover the network topology of the target organization. 

To perform this procedure, the EC2 Route Table Description command is used to obtain information about the routing tables associated with a specific VPC-id. This information can then be used to map the network topology of the target organization and identify potential targets for further exploitation. 

The business value of this procedure is that it allows an attacker to gain a better understanding of the target organization's network topology and identify potential targets for further exploitation.

 

## Requirements

1. Access to the EC2 Route Table Description command

1. Knowledge of the target VPC-id

 

## Defense

1. Ensure that access to the EC2 Route Table Description command is restricted to authorized personnel only

1. Regularly monitor network traffic and look for signs of unauthorized access or enumeration

1. Implement network segmentation to limit the impact of a successful attack

 

## Objectives

1. Identify potential targets for further enumeration

1. Discover the network topology of the target organization

 

# Instructions

1. To describe the route tables for a specific VPC, use the following AWS CLI command:

 

This command will return a list of all the route tables associated with the specified VPC ID. The output will include information such as the route table ID, the VPC ID, the main route table association, and the routes associated with the route table. You can use this command to get detailed information about the routing configuration of your VPC and troubleshoot any routing issues.



**Command** ([[Describe Route Tables for VPC ID]]):

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=ID"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[Describe Route Tables for VPC ID]]

## Tags

- [[Enumeration]]
- [[Listing routing tables by VPC-id]]
- [[RDS - Relational Database Service]]


