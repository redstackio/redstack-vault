---
id: b0c79a94-571e-46cb-b350-62bba97dfd6e
name: RDS Security Group Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.993100+00:00'
updated_at: '2023-05-25T20:09:40.796139+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Data exfiltration]]'
- '[[List information about the specified security group]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Describe EC2 Security Group]]'
---

# RDS Security Group Information Gathering

## Summary

The RDS Security Group Information Gathering procedure involves listing information about a specified security group in order to gain insight into the security posture of the RDS instance. This information can be used to plan a future attack or to identify vulnerabilities that can be exploited. Tec

## Description

# Description

The RDS Security Group Information Gathering procedure involves listing information about a specified security group in order to gain insight into the security posture of the RDS instance. This information can be used to plan a future attack or to identify vulnerabilities that can be exploited. Technical details of this procedure include querying the RDS API for security group details and analyzing the returned data. The business value of this procedure is that it can help to identify and mitigate security risks before they are exploited by attackers.

 

## Requirements

1. Access to the RDS API

1. Valid AWS credentials with appropriate permissions

 

## Defense

1. Ensure that RDS security groups are configured to restrict access to only necessary IP addresses and ports

1. Monitor RDS API calls for suspicious activity

1. Regularly review and update RDS security group configurations

 

## Objectives

1. List information about the specified security group

1. Identify potential vulnerabilities in the RDS instance

1. Plan future attacks based on the gathered information

 

# Instructions

1. To get the details of a specific security group, use the 'describe-security-groups' command followed by the ID of the security group you want to inspect.

 

This command will return a JSON object with detailed information about the specified security group, including its name, description, inbound and outbound rules, and more. The 'group-ids' parameter specifies which security group to describe, and can be a single ID or a comma-separated list of IDs. If the command is successful, the output will include the requested details of the security group.



**Command** ([[Describe EC2 Security Group]]):

```bash
aws ec2 describe-security-groups --group-ids id
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Describe EC2 Security Group]]

## Tags

- [[Data exfiltration]]
- [[List information about the specified security group]]
- [[RDS - Relational Database Service]]


