---
id: c2a38f08-07b5-4d16-8753-f9cb72aa0367
name: AWS Lambda Function Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.698390+00:00'
updated_at: '2023-04-10T20:20:37.201360+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing all lambda functions]]'
- '[[Persistence]]'
commands:
- '[[List all Lambda functions in a region]]'
---

# AWS Lambda Function Enumeration

## Summary

The AWS Lambda Function Enumeration procedure involves listing all available Lambda functions within an AWS account. This can be done using the AWS command-line interface (CLI) or the Lambda API. This procedure can be used by an attacker to discover potential targets for further attacks, or by a de

## Description

# Description

The AWS Lambda Function Enumeration procedure involves listing all available Lambda functions within an AWS account. This can be done using the AWS command-line interface (CLI) or the Lambda API. This procedure can be used by an attacker to discover potential targets for further attacks, or by a defender to identify any unauthorized Lambda functions in their environment.

From a technical standpoint, this procedure involves querying the AWS API to retrieve a list of all Lambda functions within an account. This can be done using the "list-functions" command in the AWS CLI or by making a request to the Lambda API. The output of this procedure will include the name, runtime, and other metadata for each Lambda function.

The business value of this procedure is that it provides visibility into the Lambda functions running in an AWS environment, which can help organizations identify potential security risks and ensure compliance with regulatory requirements.

## Requirements

1. Valid AWS credentials with permissions to list Lambda functions

1. Access to the AWS CLI or the Lambda API

## Defense

1. Ensure that AWS credentials are properly secured and not exposed to unauthorized users

1. Implement least privilege access control to limit the ability of attackers to list Lambda functions

1. Monitor for suspicious activity, such as unexpected Lambda function creations or modifications

## Objectives

1. Identify all Lambda functions in an AWS account

1. Assist in identifying potential security risks

1. Ensure compliance with regulatory requirements

# Instructions

1. To list all AWS Lambda functions in a given region, use the following command:

The 'aws lambda list-functions' command is used to list all Lambda functions in a specific region. The '--region' flag is used to specify the region in which you want to list the functions. This command does not require any additional arguments.

**Command** ([[List all Lambda functions in a region]]):

```bash
aws lambda list-functions --region region
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]

## Commands Used

- [[List all Lambda functions in a region]]

## Tags

- [[Cloud - AWS]]
- [[Listing all lambda functions]]
- [[Persistence]]
