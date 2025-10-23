---
id: c2f91bbe-e227-4f8d-8f32-c9b7788b7604
name: AWS DynamoDB Table Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.815899+00:00'
updated_at: '2023-04-10T20:20:03.406928+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[DynamoDB]]'
commands:
- '[[List DynamoDB Tables]]'
---

# AWS DynamoDB Table Enumeration

## Summary

The AWS DynamoDB Table Enumeration procedure involves listing all the DynamoDB tables in an AWS account. This information can be used by an attacker to identify potential targets for further attacks, such as data exfiltration or privilege escalation. From a technical perspective, this procedure inv

## Description

# Description

The AWS DynamoDB Table Enumeration procedure involves listing all the DynamoDB tables in an AWS account. This information can be used by an attacker to identify potential targets for further attacks, such as data exfiltration or privilege escalation. From a technical perspective, this procedure involves making an API call to the AWS CLI to retrieve a list of all DynamoDB tables in the account. From a business perspective, this procedure can be used to identify potential security weaknesses in an organization's cloud infrastructure.

 

## Requirements

1. Valid AWS credentials with permissions to list DynamoDB tables

1. Access to the AWS CLI

 

## Defense

1. Ensure that AWS credentials are properly secured and not leaked to unauthorized parties

1. Implement least privilege access control for AWS IAM roles and users

1. Enable AWS CloudTrail to monitor for suspicious activity related to DynamoDB table enumeration

 

## Objectives

1. Identify all DynamoDB tables in an AWS account

1. Identify potential targets for further attacks

 

# Instructions

1. To list all the tables present in DynamoDB, run the following command:

 



**Code**: [[$ aws --endpoint-url http://s3.bucket.htb dynamodb]]



> This command lists all the tables present in DynamoDB. The `--endpoint-url` flag specifies the endpoint URL for DynamoDB, and `list-tables` is the command to list all the tables. In this case, the command returns a JSON object with the `TableNames` field, which contains an array of table names present in DynamoDB.



**Command** ([[List DynamoDB Tables]]):

```bash
$ aws --endpoint-url http://s3.bucket.htb dynamodb list-tables
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List DynamoDB Tables]]

## Tags

- [[Cloud - AWS]]
- [[DynamoDB]]


