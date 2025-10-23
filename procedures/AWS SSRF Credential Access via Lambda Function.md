---
id: c877d351-abc3-4cf3-9da4-95b3607c2d12
name: AWS SSRF Credential Access via Lambda Function
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.559019+00:00'
updated_at: '2023-04-10T20:20:27.832177+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Access]]'
- '[[Getting credentials using SSRF]]'
---

# AWS SSRF Credential Access via Lambda Function

## Summary

AWS Lambda functions are vulnerable to Server Side Request Forgery (SSRF) attacks. By invoking a next Lambda function, an attacker can leverage SSRF to retrieve AWS credentials. Once obtained, these credentials can be used to escalate privileges and gain access to sensitive data.  

## Description

# Description

AWS Lambda functions are vulnerable to Server Side Request Forgery (SSRF) attacks. By invoking a next Lambda function, an attacker can leverage SSRF to retrieve AWS credentials. Once obtained, these credentials can be used to escalate privileges and gain access to sensitive data.

 

## Requirements

1. Valid AWS credentials

1. Access to a vulnerable Lambda function

 

## Defense

1. Implement input validation and sanitization to prevent SSRF attacks

1. Use IAM roles and policies to restrict access to AWS resources

1. Monitor AWS activity logs for suspicious behavior

 

## Objectives

1. Retrieve AWS credentials

1. Escalate privileges

 

# Instructions

1. To invoke the next Lambda function in the sequence, use this command with the following arguments:

 



**Code**: [[https://apigateway/prod/example?url=http://localho]]



> Arguments:
- url: The URL of the API Gateway endpoint that triggers the Lambda function.

This command is useful when you have a sequence of Lambda functions that need to be executed in a specific order. By invoking the next Lambda function in the sequence, you can ensure that your application runs smoothly and without any errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Tags

- [[Cloud - AWS]]
- [[Credential Access]]
- [[Getting credentials using SSRF]]


