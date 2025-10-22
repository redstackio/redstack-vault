---
id: f0e0ab35-ec25-410e-9e69-605e356e76ec
name: AWS Lambda Role Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.985140+00:00'
updated_at: '2023-04-10T20:20:06.327768+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[AppCert DLLs|T1182 - AppCert DLLs]]'
- '[[Execution through API|T1106 - Execution through API]]'
tags:
- '[[Cloud - AWS]]'
- '[[Create a lambda function and attach a role to it]]'
- '[[Privilege Escalation]]'
commands:
- '[[Create AWS Lambda Function]]'
---

# AWS Lambda Role Privilege Escalation

## Summary

AWS Lambda is a serverless computing service provided by AWS. By creating a Lambda function and attaching a role to it, an attacker can potentially escalate their privileges within an AWS environment. This can be achieved by abusing the functionality of the Lambda service and executing code through

## Description

# Description

AWS Lambda is a serverless computing service provided by AWS. By creating a Lambda function and attaching a role to it, an attacker can potentially escalate their privileges within an AWS environment. This can be achieved by abusing the functionality of the Lambda service and executing code through the AWS API. Privilege escalation can result in the attacker gaining access to sensitive data, resources, and control over the environment. From a technical standpoint, the attacker would need to have valid AWS credentials and be able to create a Lambda function and attach a role to it. From a business perspective, this attack can result in significant financial and reputational damage.

## Requirements

1. Valid AWS credentials

1. Ability to create a Lambda function and attach a role to it

## Defense

1. Limit and monitor access to AWS credentials

1. Implement least privilege access controls to limit access to sensitive data and resources

1. Monitor AWS API calls for suspicious activity

## Objectives

1. Escalate privileges within an AWS environment

1. Gain access to sensitive data and resources

1. Assume control over the environment

# Instructions

1. Fill in the details for creating an AWS Lambda function.

This command creates a new AWS Lambda function with the specified name, runtime, zip file, handler, IAM role, and region. The `--function-name` flag specifies the name of the function. The `--runtime` flag specifies the runtime environment for the function. The `--zip-file` flag specifies the location of the zip file containing the code for the function. The `--handler` flag specifies the handler function within the code. The `--role` flag specifies the IAM role used by the function. The `--region` flag specifies the AWS region in which to create the function.

**Command** ([[Create AWS Lambda Function]]):

```bash
aws lambda create-function --function-name my-function --runtime python3.7 --zip-file fileb://my-function.zip --handler my-function.handler --role ARN --region region
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[AppCert DLLs|T1182 - AppCert DLLs]]
- [[Execution through API|T1106 - Execution through API]]

## Commands Used

- [[Create AWS Lambda Function]]

## Tags

- [[Cloud - AWS]]
- [[Create a lambda function and attach a role to it]]
- [[Privilege Escalation]]
