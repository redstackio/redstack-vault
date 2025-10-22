---
id: 57a6b6b8-8a02-40bc-b3a5-56de9faecabd
name: AWS Lambda Function Details Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.721872+00:00'
updated_at: '2023-04-10T20:20:41.702751+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing information about the specified lambda]]'
- '[[Persistence]]'
commands:
- '[[Retrieve AWS Lambda Function]]'
---

# AWS Lambda Function Details Enumeration

## Summary

The AWS Lambda Function Details Enumeration procedure involves gathering information about a specified lambda function within an AWS environment. This information can be used by an attacker to gain a better understanding of the target environment and potentially identify other attack vectors. 

To 

## Description

# Description

The AWS Lambda Function Details Enumeration procedure involves gathering information about a specified lambda function within an AWS environment. This information can be used by an attacker to gain a better understanding of the target environment and potentially identify other attack vectors. 

To execute this procedure, the attacker can use the 'Get AWS Lambda Function Details' command, which will return details about the specified lambda function, such as its ARN, runtime, and code size. This information can be used to identify potential vulnerabilities or misconfigurations in the target environment, which can then be exploited to achieve the attacker's objectives. 

From a business perspective, this procedure highlights the importance of properly securing AWS environments and regularly monitoring for unauthorized access or activity.

## Requirements

1. Valid AWS credentials with permission to access the specified lambda function

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Regularly monitor AWS CloudTrail logs for unauthorized access or activity related to lambda functions

1. Implement least privilege access controls to limit the scope of potential attacks

## Objectives

1. Gather information about a specified lambda function within an AWS environment

1. Identify potential vulnerabilities or misconfigurations in the target environment

# Instructions

1. To get details of an AWS Lambda function, run the following command:

**Code**: [[aws lambda get-function --function-name name]]

> This command retrieves the configuration information for the specified Lambda function. You need to provide the name of the function as an argument to the --function-name option. The output will include details such as the function's ARN, runtime environment, memory size, and timeout value. You can use this information to troubleshoot issues with the function or to verify its configuration.

**Command** ([[Retrieve AWS Lambda Function]]):

```bash
aws lambda get-function --function-name name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Retrieve AWS Lambda Function]]

## Tags

- [[Cloud - AWS]]
- [[Listing information about the specified lambda]]
- [[Persistence]]
