---
id: 6b21917e-9c1c-45b9-9074-1026ff9a3b0d
name: AWS Lambda Function Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.230530+00:00'
updated_at: '2023-04-10T20:20:05.648573+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Accessibility Features|T1546.008 - Accessibility Features]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing policy information about the function]]'
commands:
- '[[Get AWS Lambda function policy]]'
---

# AWS Lambda Function Policy Enumeration

## Summary

The AWS Lambda Function Policy Enumeration procedure is used to determine the permissions and access control policies associated with a particular AWS Lambda function. This information can be used to identify potential attack paths and vulnerabilities. Technical details include using the 'Get AWS L

## Description

# Description

The AWS Lambda Function Policy Enumeration procedure is used to determine the permissions and access control policies associated with a particular AWS Lambda function. This information can be used to identify potential attack paths and vulnerabilities. Technical details include using the 'Get AWS Lambda Function Policy' command to retrieve the policy information for a given function. Business value includes identifying and mitigating potential security risks, and ensuring compliance with industry regulations.

 

## Requirements

1. Valid AWS credentials with the necessary permissions to access the Lambda function

1. Network access to the AWS API endpoint

1. AWS CLI or equivalent tool

 

## Defense

1. Ensure that AWS credentials are properly secured and access is restricted to authorized personnel only

1. Implement least privilege access control policies to limit the potential attack surface

1. Regularly review and update access control policies to ensure compliance with industry regulations and best practices

 

## Objectives

1. Identify the permissions and access control policies associated with a particular AWS Lambda function

1. Determine potential attack paths and vulnerabilities

1. Mitigate potential security risks

1. Ensure compliance with industry regulations

 

# Instructions

1. To get the policy for an AWS Lambda function, use the 'aws lambda get-policy' command followed by the function name.

 

This command retrieves the resource-based policy associated with the specified Lambda function. The policy specifies who can invoke the function and what permissions they have. The function name must be specified as an argument. The output will be a JSON document that contains the policy statements.



**Command** ([[Get AWS Lambda function policy]]):

```bash
aws lambda get-policy --function-name function_name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[Accessibility Features|T1546.008 - Accessibility Features]]

## Commands Used

- [[Get AWS Lambda function policy]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing policy information about the function]]


