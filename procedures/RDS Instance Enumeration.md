---
id: a5bd50e5-99d9-4e74-b856-92f73a249e21
name: RDS Instance Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.879764+00:00'
updated_at: '2023-04-10T20:20:42.743924+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Enumeration]]'
- '[[Listing information about RDS instances]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[List all DB instances in region]]'
---

# RDS Instance Enumeration

## Summary

RDS Instance Enumeration is a process of discovering and listing information about RDS instances in an AWS environment. This technique can be used by an attacker to gain knowledge about the target environment and identify potential targets for further attacks. By using the AWS RDS Describe DB Insta

## Description

# Description

RDS Instance Enumeration is a process of discovering and listing information about RDS instances in an AWS environment. This technique can be used by an attacker to gain knowledge about the target environment and identify potential targets for further attacks. By using the AWS RDS Describe DB Instances command, an attacker can obtain information such as the name, engine, status, endpoint, and other details about the RDS instances.

From a technical perspective, this technique involves leveraging the AWS API to query the RDS service for information about the instances. The AWS CLI or SDK can be used to automate this process and obtain information about multiple instances in a single command. 

The business value of this technique is that it allows an attacker to gain a better understanding of the target environment and identify potentially valuable targets for further attacks.

 

## Requirements

1. Valid AWS credentials with permissions to access the RDS service

1. Network access to the RDS service endpoint

1. AWS CLI or SDK installed on the attacker's machine

 

## Defense

1. Monitor AWS API calls for unusual activity, such as a high volume of DescribeDBInstances requests

1. Implement least privilege access controls to limit the permissions of AWS credentials to only the necessary resources and actions

1. Enable AWS CloudTrail to log API activity and analyze the logs for suspicious behavior

 

## Objectives

1. Discover and list information about RDS instances in an AWS environment

1. Identify potential targets for further attacks

 

# Instructions

1. This command provides information about all of your Amazon RDS DB instances and their current status. It returns a list of DB instances and their details such as instance identifier, engine, status, endpoint, and more.

 

The 'aws rds describe-db-instances' command takes no arguments and will display information about all DB instances in the current region. If you want to retrieve information about a specific DB instance, you can use the --db-instance-identifier parameter followed by the instance identifier. You can also use filters to narrow down the search results. For example, you can use the --filters parameter followed by a list of filters to retrieve only the DB instances that match the specified criteria. The output of this command is in JSON format.



**Command** ([[List all DB instances in region]]):

```bash
aws rds describe-db-instances
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[List all DB instances in region]]

## Tags

- [[Enumeration]]
- [[Listing information about RDS instances]]
- [[RDS - Relational Database Service]]


