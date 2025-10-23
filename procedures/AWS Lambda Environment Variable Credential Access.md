---
id: b0393ab5-a3e2-4544-89f7-ed59ade44058
name: AWS Lambda Environment Variable Credential Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.603944+00:00'
updated_at: '2023-04-10T20:20:46.008165+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Access]]'
- '[[Getting credentials from lambda environment variables (cli)]]'
commands:
- '[[Get AWS Lambda function]]'
---

# AWS Lambda Environment Variable Credential Access

## Summary

AWS Lambda is a serverless compute service that allows users to run code without provisioning or managing servers. By default, Lambda functions are given an execution role that grants them permissions to access AWS resources. If an attacker gains access to the Lambda function's environment variable

## Description

# Description

AWS Lambda is a serverless compute service that allows users to run code without provisioning or managing servers. By default, Lambda functions are given an execution role that grants them permissions to access AWS resources. If an attacker gains access to the Lambda function's environment variables, they may be able to extract sensitive credentials or keys that can be used to access other AWS resources. This technique can be used by attackers to escalate privileges and perform lateral movement within an AWS environment.

 

## Requirements

1. Access to the AWS CLI or SDK

1. Knowledge of the Lambda function's name and region

1. Permissions to execute the 'aws lambda get-function-configuration' command

 

## Defense

1. Ensure that Lambda environment variables do not contain sensitive credentials or keys

1. Enable AWS CloudTrail to log all API calls to Lambda functions

1. Use AWS IAM policies to restrict permissions for Lambda functions and their associated roles

 

## Objectives

1. Extract sensitive credentials or keys from Lambda environment variables

1. Use extracted credentials to access other AWS resources

 

# Instructions

1. To retrieve details of an AWS Lambda function, run the following command:

 

This command retrieves details of an AWS Lambda function such as its configuration, tags, and code location. The --function-name argument specifies the name of the function for which you want to retrieve the details. You can also use the --query option to filter the output and retrieve specific details of the function. For example, to retrieve the ARN of the function, you can use the following query: 'aws lambda get-function --function-name NAME --query Configuration.FunctionArn'



**Command** ([[Get AWS Lambda function]]):

```bash
aws lambda get-function --function-name NAME
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get AWS Lambda function]]

## Tags

- [[Cloud - AWS]]
- [[Credential Access]]
- [[Getting credentials from lambda environment variables (cli)]]


