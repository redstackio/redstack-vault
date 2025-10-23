---
id: c2842a10-bd38-4def-a681-d57df0cd2e64
name: RDS Subnet Group Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.901936+00:00'
updated_at: '2023-04-10T20:20:39.624272+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Enumeration]]'
- '[[Listing information about subnet groups in RDS]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Describe DB Subnet Groups]]'
---

# RDS Subnet Group Enumeration

## Summary

RDS Subnet Group Enumeration is a reconnaissance technique that allows an attacker to gather information about the subnet groups used by an RDS instance. This information can be used to identify potential targets for further exploitation. To perform this technique, the attacker uses the 'RDS DB Sub

## Description

# Description

RDS Subnet Group Enumeration is a reconnaissance technique that allows an attacker to gather information about the subnet groups used by an RDS instance. This information can be used to identify potential targets for further exploitation. To perform this technique, the attacker uses the 'RDS DB Subnet Groups Description' command to list the subnet groups associated with an RDS instance.

Technical Description: The RDS DB Subnet Groups Description command provides information about the subnet groups associated with an RDS instance. This includes the name of the subnet group, the description, and the VPC ID. By enumerating the subnet groups, an attacker can identify potential targets for further exploitation.

Business Value: This technique can be used by attackers to identify potential targets for further exploitation. By identifying vulnerable RDS instances, attackers can gain access to sensitive data and compromise the confidentiality, integrity, and availability of the target organization's data.


 

## Requirements

1. Access to the AWS Management Console or API

1. Valid credentials with permissions to access the RDS service

 

## Defense

1. Ensure that RDS instances are not publicly accessible

1. Implement network segmentation to restrict access to RDS instances

1. Enable VPC Flow Logs to monitor network traffic to and from RDS instances

 

## Objectives

1. Identify potential targets for further exploitation

1. Gather information about the subnet groups used by an RDS instance

 

# Instructions

1. Use this command to describe RDS DB subnet groups.

 

This command returns information about the specified RDS DB subnet group, including VPC ID, subnet group name, description, and the subnets in the subnet group. The command takes no arguments and returns a JSON object with the details of the DB subnet group.



**Command** ([[Describe DB Subnet Groups]]):

```bash
N/A
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[Describe DB Subnet Groups]]

## Tags

- [[Enumeration]]
- [[Listing information about subnet groups in RDS]]
- [[RDS - Relational Database Service]]


