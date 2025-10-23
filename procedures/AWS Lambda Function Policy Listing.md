---
id: 9f71c953-7362-4c8f-a1e8-86f46fa2bce0
name: AWS Lambda Function Policy Listing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.747081+00:00'
updated_at: '2023-04-10T20:20:28.184144+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing policy information about the specific lambda function]]'
- '[[Persistence]]'
commands:
- '[[Get policy for AWS Lambda function]]'
---

# AWS Lambda Function Policy Listing

## Summary

AWS Lambda Function Policy Listing technique involves retrieving the policy information of a specific AWS Lambda function. This technique can be used by an attacker to gain knowledge about the permissions granted to the function, which can be useful for privilege escalation or lateral movement. 

T

## Description

# Description

AWS Lambda Function Policy Listing technique involves retrieving the policy information of a specific AWS Lambda function. This technique can be used by an attacker to gain knowledge about the permissions granted to the function, which can be useful for privilege escalation or lateral movement. 

To retrieve the policy information, an attacker can use the 'Retrieve AWS Lambda Function Policy' command. The command requires authentication credentials with permissions to access the function.

The business value of this technique lies in identifying and mitigating potential security risks in AWS Lambda functions, ensuring that only authorized users have access to the function and its data.

 

## Requirements

1. Valid AWS authentication credentials with permissions to access the specific Lambda function

 

## Defense

1. Ensure that AWS authentication credentials are properly secured and not exposed

1. Implement the principle of least privilege to restrict access to AWS Lambda functions

1. Monitor and review AWS CloudTrail logs for any suspicious activity related to Lambda functions

 

## Objectives

1. Retrieve the policy information of a specific AWS Lambda function

1. Gain knowledge about the permissions granted to the function

 

# Instructions

1. To retrieve the policy for an AWS Lambda function, use the following command:

 

The 'aws lambda get-policy' command is used to retrieve the resource-based policy for an AWS Lambda function. The function name must be provided using the --function-name parameter. The --profile parameter can be used to specify the AWS CLI profile to use and the --region parameter is used to specify the region in which the function is located. This command returns the policy document in JSON format.



**Command** ([[Get policy for AWS Lambda function]]):

```bash
aws lambda get-policy --function-name name --profile profile --region region
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Commands Used

- [[Get policy for AWS Lambda function]]

## Tags

- [[Cloud - AWS]]
- [[Listing policy information about the specific lambda function]]
- [[Persistence]]


