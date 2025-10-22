---
id: 533dd375-ddfb-4cd5-b032-495d1726e51a
name: RDS Lateral Movement - Listing Subnets
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.459826+00:00'
updated_at: '2023-04-10T20:20:10.789280+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Lateral Movement and Pivoting]]'
- '[[Listing subnets of specific VPC (Important because the access can be restricted
  to specific subnets to other VPC''s)]]'
- '[[RDS - Relational Database Service]]'
- '[[Scenario]]'
commands:
- '[[Describe Subnets]]'
---

# RDS Lateral Movement - Listing Subnets

## Summary

RDS Lateral Movement - Listing Subnets is a technique used by attackers to pivot within a target network. Attackers can use this technique to identify subnets within a specific VPC to which they can gain access. This technique is commonly used by attackers to identify potential targets for further 

## Description

# Description

RDS Lateral Movement - Listing Subnets is a technique used by attackers to pivot within a target network. Attackers can use this technique to identify subnets within a specific VPC to which they can gain access. This technique is commonly used by attackers to identify potential targets for further exploitation.

To perform this attack, an attacker will typically use a compromised EC2 instance to list the subnets within a specific VPC. Once they have identified the subnets, they can then attempt to gain access to those subnets using various techniques such as port scanning or exploiting known vulnerabilities.

The business value of this technique is that it allows an attacker to gain access to additional resources within a target network, potentially leading to the compromise of sensitive data.

## Requirements

1. Access to a compromised EC2 instance within the target network

## Defense

1. Restrict access to subnets within a VPC to only authorized users and systems

1. Implement network segmentation to prevent lateral movement within a target network

1. Monitor network traffic for signs of lateral movement

## Objectives

1. Identify subnets within a specific VPC

1. Gain access to additional resources within a target network

# Instructions

1. The above command is used to describe the subnets in a specified VPC. Replace 'ID' with the ID of the VPC you want to describe the subnets for.

**Code**: [[aws ec2 describe-subnets --filters "Name=vpc-id,Va]]

> This command retrieves information about the subnets in a specified VPC. The output includes the subnet ID, availability zone, CIDR block, and the VPC ID. You can filter the results using various parameters such as the VPC ID, availability zone, and subnet ID. The command can be used to get a detailed view of the subnets in a VPC, which can be useful for troubleshooting network issues and for planning network architecture.

**Command** ([[Describe Subnets]]):

```bash
aws ec2 describe-subnets --filters "Name=vpc-id,Values=ID"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Describe Subnets]]

## Tags

- [[Lateral Movement and Pivoting]]
- [[Listing subnets of specific VPC (Important because the access can be restricted to specific subnets to other VPC's)]]
- [[RDS - Relational Database Service]]
- [[Scenario]]
