---
id: 4bb05c04-2b87-430c-92c2-3222efe71cc7
name: AWS Lambda Layer Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.276887+00:00'
updated_at: '2023-04-10T20:20:01.629584+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing Lambda Layers (Dependencies)]]'
---

# AWS Lambda Layer Enumeration

## Summary

AWS Lambda Layer Enumeration is a technique used to identify and list all the Lambda Layers present in a target AWS account. Lambda Layers are a type of serverless deployment package that can be used to manage common dependencies across multiple functions. Attackers can use this technique to identi

## Description

# Description

AWS Lambda Layer Enumeration is a technique used to identify and list all the Lambda Layers present in a target AWS account. Lambda Layers are a type of serverless deployment package that can be used to manage common dependencies across multiple functions. Attackers can use this technique to identify the presence of specific dependencies or libraries that can potentially be exploited.

 

## Requirements

1. Valid AWS credentials with permissions to access Lambda Layers

1. Access to the AWS Management Console or AWS CLI

 

## Defense

1. Ensure that AWS credentials are securely stored and not shared

1. Implement least privilege access control to limit access to Lambda Layers

1. Regularly update and patch dependencies and libraries used by Lambda Layers

 

## Objectives

1. Identify all Lambda Layers in the target AWS account

1. Identify the dependencies and libraries used by the Lambda Layers

1. Identify potential vulnerabilities in the dependencies and libraries

 

# Instructions

1. This command lists all the AWS Lambda layers in your account.

 

Arguments: None. 

This command does not require any arguments. It will simply return a list of all the Lambda layers in your account.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing Lambda Layers (Dependencies)]]


