---
id: 08e3dc2f-052e-404e-9374-9f77b6691bab
name: CloudTrail Logs Listing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.108444+00:00'
updated_at: '2023-04-10T20:20:31.613627+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[CloudTrail]]'
- '[[List trails]]'
- '[[RDS - Relational Database Service]]'
- '[[Useful Commands]]'
commands:
- '[[List trails]]'
---

# CloudTrail Logs Listing

## Summary

The CloudTrail Logs Listing procedure enables an attacker to discover CloudTrail logs for the targeted AWS account. CloudTrail logs provide a record of all AWS API calls made in an account. By retrieving these logs, an attacker can gain insight into the actions taken by the account owner and identi

## Description

# Description

The CloudTrail Logs Listing procedure enables an attacker to discover CloudTrail logs for the targeted AWS account. CloudTrail logs provide a record of all AWS API calls made in an account. By retrieving these logs, an attacker can gain insight into the actions taken by the account owner and identify potential targets for further attacks. To list the CloudTrail logs, the attacker can use the 'ListTrails' command, which returns a list of all the trails in the account.

 

## Requirements

1. Valid AWS credentials with permissions to access CloudTrail logs

 

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Monitor CloudTrail logs for suspicious activity

1. Implement least privilege access control to limit the amount of access granted to AWS accounts

 

## Objectives

1. Discover the CloudTrail logs for the targeted AWS account

1. Identify potential targets for further attacks

 

# Instructions

1. Use this command to list all the CloudTrail logs available in your AWS account.

 



**Code**: [[aws cloudtrail list-trails]]



> The `list-trails` command is used to retrieve a list of all the trails available in your AWS account. This command does not require any arguments. Once you run this command, it will return a JSON object containing the name, ARN, and home region of each trail. This information can be useful for auditing and compliance purposes. If you have a large number of trails, you may need to paginate through the results using the `--starting-token` and `--max-items` options.



**Command** ([[List trails]]):

```bash
aws cloudtrail list-trails
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List trails]]

## Tags

- [[CloudTrail]]
- [[List trails]]
- [[RDS - Relational Database Service]]
- [[Useful Commands]]


