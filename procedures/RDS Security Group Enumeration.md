---
id: 268328e1-6a95-4c0f-9183-20011e531eac
name: RDS Security Group Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.922701+00:00'
updated_at: '2023-04-10T20:20:54.796917+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Enumeration]]'
- '[[Listing information about database security groups in RDS]]'
- '[[RDS - Relational Database Service]]'
---

# RDS Security Group Enumeration

## Summary

The RDS Security Group Enumeration procedure aims to gather information about database security groups within an RDS instance. This procedure can be used to identify potential misconfigurations or vulnerabilities in the security groups that could be exploited by an attacker. The procedure involves 

## Description

# Description

The RDS Security Group Enumeration procedure aims to gather information about database security groups within an RDS instance. This procedure can be used to identify potential misconfigurations or vulnerabilities in the security groups that could be exploited by an attacker. The procedure involves listing the security group descriptions for all RDS instances in the target environment.

Technical Detail: The procedure involves using the 'RDS DB Security Group Description' command to list the description for each security group in an RDS instance. This information can then be used to identify security groups with overly permissive rules or other misconfigurations.

Business Value: By identifying potential vulnerabilities in RDS security groups, this procedure can help organizations improve their overall security posture and reduce the risk of a data breach.

## Requirements

1. Valid credentials for the target RDS instance

## Defense

1. Ensure that RDS security groups are properly configured with least privilege access controls

1. Implement network segmentation to limit access to RDS instances

1. Monitor RDS security groups for changes or suspicious activity

## Objectives

1. Identify potential misconfigurations or vulnerabilities in RDS security groups

1. Gather information about security groups within an RDS instance

# Instructions

1. This command retrieves information about the security groups associated with a specified RDS DB instance.

The 'describe-db-security-groups' command is used to get information about the security groups that are associated with an RDS DB instance. The command requires the name of the DB instance as an argument. The output of this command includes the name of the security group, its description, and the VPC ID where the security group is located. Additionally, it includes a list of EC2 security groups that are associated with the DB instance's security group. This command can be useful for troubleshooting connectivity issues with an RDS DB instance.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Tags

- [[Enumeration]]
- [[Listing information about database security groups in RDS]]
- [[RDS - Relational Database Service]]
