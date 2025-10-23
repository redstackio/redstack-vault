---
id: 2f0a7a4b-d05f-4c12-ad18-7aa7795c224c
name: RDS Lateral Movement via EC2 Route Tables
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.485334+00:00'
updated_at: '2023-04-10T20:20:55.505043+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Lateral Movement and Pivoting]]'
- '[[Listing routing tables]]'
- '[[RDS - Relational Database Service]]'
- '[[Scenario]]'
commands:
- '[[Describe Route Tables in VPC]]'
---

# RDS Lateral Movement via EC2 Route Tables

## Summary

RDS Lateral Movement via EC2 Route Tables is a technique used by attackers to pivot from an EC2 instance to an RDS instance within the same VPC. By querying the EC2 route tables, an attacker can identify the RDS instance and establish a connection to it. This technique requires valid credentials wi

## Description

# Description

RDS Lateral Movement via EC2 Route Tables is a technique used by attackers to pivot from an EC2 instance to an RDS instance within the same VPC. By querying the EC2 route tables, an attacker can identify the RDS instance and establish a connection to it. This technique requires valid credentials with appropriate permissions to query the route tables, and can be used to escalate privileges or exfiltrate data from the RDS instance.

Technical Explanation: EC2 instances and RDS instances within the same VPC can communicate with each other using private IP addresses. The EC2 route tables contain information about the network routes, including the destination IP addresses and the next hop. By querying the route tables, an attacker can identify the RDS instance and its IP address, and establish a connection to it.

Business Value: This technique can be used by attackers to access sensitive data stored in RDS instances, which can lead to data theft, financial loss, and reputational damage.

 

## Requirements

1. Valid credentials with appropriate permissions to query the EC2 route tables

1. Access to an EC2 instance within the same VPC as the target RDS instance

 

## Defense

1. Implement least privilege access control to the EC2 instances and RDS instances

1. Monitor network traffic for unusual connections or data transfers

1. Regularly review and update the EC2 route tables to remove unnecessary routes

 

## Objectives

1. Identify RDS instances within the same VPC as an EC2 instance

1. Establish a connection to the identified RDS instance

1. Escalate privileges or exfiltrate data from the RDS instance

 

# Instructions

1. Use the following command to describe all route tables associated with a specific VPC:

aws ec2 describe-route-tables --filters "Name=vpc-id,Values=ID"

Replace 'ID' with the ID of the VPC you want to describe the route tables for.

 

This command is used to retrieve information about the route tables associated with a specific VPC. The 'describe-route-tables' command returns a list of all the route tables and their associated details, including the routes they contain and the subnets they are associated with. The '--filters' option allows you to filter the results to only show the route tables associated with a specific VPC. In this case, we are filtering by 'vpc-id' and providing the ID of the VPC we want to retrieve information for.



**Command** ([[Describe Route Tables in VPC]]):

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=ID"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Describe Route Tables in VPC]]

## Tags

- [[Lateral Movement and Pivoting]]
- [[Listing routing tables]]
- [[RDS - Relational Database Service]]
- [[Scenario]]


