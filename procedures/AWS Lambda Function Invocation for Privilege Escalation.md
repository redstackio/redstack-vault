---
id: e78ebd3f-414a-40d4-9d54-e211a43eebed
name: AWS Lambda Function Invocation for Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.033250+00:00'
updated_at: '2023-04-10T20:20:09.748163+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Cloud - AWS]]'
- '[[Invoke a lambda function]]'
- '[[Privilege Escalation]]'
commands:
- '[[Invoke AWS Lambda Function]]'
---

# AWS Lambda Function Invocation for Privilege Escalation

## Summary

This procedure involves invoking a lambda function in AWS to escalate privileges. AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the compute resources for you. By invoking a lambda function, an attacker can potentially escalate their p

## Description

# Description

This procedure involves invoking a lambda function in AWS to escalate privileges. AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the compute resources for you. By invoking a lambda function, an attacker can potentially escalate their privileges and gain access to sensitive data or perform unauthorized actions. This technique can be used to bypass access controls and gain access to restricted resources.

Technical Explanation: The attacker can use the AWS Lambda Invoke command to execute the function and gain access to elevated privileges. The attacker can also modify the function code to perform malicious actions or to exfiltrate data. AWS Lambda functions can be invoked by other AWS services or by custom applications.

Business Value: This procedure can allow an attacker to gain access to sensitive data or perform unauthorized actions, potentially causing significant damage to the business.

## Requirements

1. Access to AWS environment

1. Permissions to invoke lambda functions

## Defense

1. Limit access to AWS environment to authorized personnel only

1. Implement least privilege access controls to limit access to sensitive resources

1. Monitor for unauthorized access and unusual activity in AWS environment

## Objectives

1. Escalate privileges in AWS environment

1. Gain access to sensitive data or perform unauthorized actions

# Instructions

1. Use the AWS Lambda Invoke command to invoke a specific function in your AWS Lambda account.

The AWS Lambda Invoke command is used to invoke a specific function in your AWS Lambda account. This command requires the name of the function you want to invoke, the name of the output file to save the response to, and the region where the function is located. The function name and region are required arguments.

Example: aws lambda invoke --function-name myFunctionName response.json --region us-west-2

This command will invoke the function named 'myFunctionName' located in the 'us-west-2' region and save the response to a file named 'response.json'.

**Command** ([[Invoke AWS Lambda Function]]):

```bash
aws lambda invoke --function-name name response.json --region region
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Invoke AWS Lambda Function]]

## Tags

- [[Cloud - AWS]]
- [[Invoke a lambda function]]
- [[Privilege Escalation]]
