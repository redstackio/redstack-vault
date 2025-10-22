---
id: 6299d3b1-180a-4f2e-8adf-8d4726ee14c1
name: 'RDS Enumeration: Listing Routing Tables'
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.361355+00:00'
updated_at: '2023-04-10T20:20:02.706751+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Enumeration]]'
- '[[Listing routing tables]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[List Route Tables]]'
---

# RDS Enumeration: Listing Routing Tables

## Summary

The RDS Enumeration: Listing Routing Tables procedure involves scanning the network for routing tables related to Amazon EC2 instances. A routing table is a set of rules, often viewed as a table, that is used to determine where network traffic is directed. By listing routing tables, an attacker can

## Description

# Description

The RDS Enumeration: Listing Routing Tables procedure involves scanning the network for routing tables related to Amazon EC2 instances. A routing table is a set of rules, often viewed as a table, that is used to determine where network traffic is directed. By listing routing tables, an attacker can gain information about the network topology, including which subnets are in use and which EC2 instances are associated with each subnet. This information can be used to plan further attacks against the network.

Technical Explanation: The procedure involves using the EC2 Route Tables Description command to list routing tables associated with EC2 instances. This command requires access to the AWS Management Console or API and the necessary permissions to describe the routing tables. The output of the command includes information such as the routing table ID, the VPC ID, and the subnets associated with the routing table.

Business Value: The RDS Enumeration: Listing Routing Tables procedure can be used by attackers to gain a better understanding of the network topology and plan further attacks. By identifying subnets and EC2 instances, an attacker can target specific systems or services and potentially gain access to sensitive data or systems.

## Requirements

1. Access to the AWS Management Console or API

1. Necessary permissions to describe routing tables

## Defense

1. Implement network segmentation and access controls to limit access to sensitive systems and data

1. Regularly review and update routing table configurations to ensure they are appropriate for the network environment

1. Monitor network traffic for unusual activity, such as unexpected access attempts or data exfiltration

## Objectives

1. Identify routing tables associated with EC2 instances

1. Gain information about the network topology

# Instructions

1. This command describes one or more of your VPC route tables. The output includes the route table ID, VPC ID, and routes.

Arguments:

--filters (list) - One or more filters.

--route-table-ids (list) - One or more route table IDs.

--dry-run (boolean) - Checks whether you have the required permissions for the action, without actually making the request. If you have the required permissions, the command returns DryRunOperation; otherwise, it returns UnauthorizedOperation.

**Command** ([[List Route Tables]]):

```bash
aws ec2 describe-route-tables
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[List Route Tables]]

## Tags

- [[Enumeration]]
- [[Listing routing tables]]
- [[RDS - Relational Database Service]]
