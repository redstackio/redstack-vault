---
id: 12188406-134b-48ae-b473-89d2d122ac68
name: AWS Lambda Event Source Mapping Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.256023+00:00'
updated_at: '2023-04-10T20:20:21.471865+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing the event source mapping information about a lambda function]]'
commands:
- '[[List Event Source Mappings for AWS Lambda Function]]'
---

# AWS Lambda Event Source Mapping Enumeration

## Summary

AWS Lambda is a popular serverless computing service that allows developers to run code without provisioning or managing servers. One of the key features of AWS Lambda is the ability to trigger functions in response to various events, such as changes in data stored in an S3 bucket or messages sent 

## Description

# Description

AWS Lambda is a popular serverless computing service that allows developers to run code without provisioning or managing servers. One of the key features of AWS Lambda is the ability to trigger functions in response to various events, such as changes in data stored in an S3 bucket or messages sent to an SQS queue. This procedure involves listing the event source mapping information about a lambda function, which can provide valuable information for an attacker.

Technical Explanation: The `List Lambda Event Source Mappings` command is used to list the event source mapping information about a lambda function. This information includes the ARN of the event source, the type of event source, and the state of the mapping. An attacker can use this information to identify potential attack vectors, such as S3 buckets or SQS queues that trigger the lambda function.

Business Value: An attacker can use this information to identify potential attack vectors and plan their attack accordingly. For example, an attacker could identify an S3 bucket that triggers a lambda function and upload a malicious file to the bucket, which would then trigger the lambda function and execute the attacker's code.

## Requirements

1. Valid AWS credentials with permissions to list lambda event source mappings

## Defense

1. Ensure that AWS credentials are properly secured and not leaked

1. Implement least privilege access control for AWS IAM roles and policies

1. Regularly review CloudTrail logs for suspicious activity

## Objectives

1. Identify potential attack vectors

1. Plan attacks accordingly

# Instructions

1. Use this command to list all the event source mappings for a specific AWS Lambda function.

The `list-event-source-mappings` command is used to retrieve a list of all the event source mappings for a specific AWS Lambda function. The `--function-name` argument is used to specify the name of the Lambda function for which you want to list the event source mappings. This command can be helpful in scenarios where you need to troubleshoot issues related to event source mappings or if you simply want to get an overview of all the event sources that are currently mapped to your Lambda function.

**Command** ([[List Event Source Mappings for AWS Lambda Function]]):

```bash
aws lambda list-event-source-mappings --function-name function_name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[List Event Source Mappings for AWS Lambda Function]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing the event source mapping information about a lambda function]]
