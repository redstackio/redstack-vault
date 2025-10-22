---
id: 2b53747c-effa-4f6e-bd4f-496325223d7c
name: RDS VPC Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.232794+00:00'
updated_at: '2023-04-10T20:20:37.911680+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Enumeration]]'
- '[[Listing VPC''s]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[EC2 Describe VPCs]]'
---

# RDS VPC Enumeration

## Summary

RDS VPC Enumeration is a technique used to discover AWS Virtual Private Clouds (VPCs) associated with RDS instances. This information can be used to identify potential targets for further exploitation. To carry out this technique, attackers use the 'List VPCs' command to enumerate the VPCs associat

## Description

# Description

RDS VPC Enumeration is a technique used to discover AWS Virtual Private Clouds (VPCs) associated with RDS instances. This information can be used to identify potential targets for further exploitation. To carry out this technique, attackers use the 'List VPCs' command to enumerate the VPCs associated with the RDS instances. This command provides the attacker with a list of VPCs and their respective IDs, which can be used in subsequent attacks.

From a technical perspective, this technique relies on the fact that RDS instances are often associated with VPCs, and that the 'List VPCs' command is available to anyone with the necessary permissions. From a business value perspective, this technique can be used by attackers to identify valuable targets for further exploitation, such as databases containing sensitive information.

## Requirements

1. Valid AWS credentials with permissions to execute the 'List VPCs' command

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Limit access to the 'List VPCs' command to only those users who require it

1. Monitor for unusual activity related to the 'List VPCs' command and associated API calls

## Objectives

1. Discover VPCs associated with RDS instances

# Instructions

1. To list all the VPCs in your AWS account, run the following command:

This command will provide you with the details of all the VPCs present in your AWS account. It will include information such as the VPC ID, the CIDR block, the tenancy option, the state, and more. This command is useful for getting an overview of your VPCs and their current configurations.

**Command** ([[EC2 Describe VPCs]]):

```bash
aws ec2 describe-vpcs
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[EC2 Describe VPCs]]

## Tags

- [[Enumeration]]
- [[Listing VPC's]]
- [[RDS - Relational Database Service]]
