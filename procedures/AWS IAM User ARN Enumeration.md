---
id: f18affd9-0bd0-4e61-9e1d-b71afa7a4173
name: AWS IAM User ARN Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.890520+00:00'
updated_at: '2023-04-10T20:19:52.986021+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[ARN]]'
- '[[Cloud - AWS]]'
---

# AWS IAM User ARN Enumeration

## Summary

The AWS IAM User ARN Enumeration procedure involves discovering AWS IAM user ARNs. This can be done by using the 'AWS IAM User ARN' command. This procedure can be used by an attacker to discover the AWS IAM user ARNs in order to identify potential targets for further attacks. 

Technical Descriptio

## Description

# Description

The AWS IAM User ARN Enumeration procedure involves discovering AWS IAM user ARNs. This can be done by using the 'AWS IAM User ARN' command. This procedure can be used by an attacker to discover the AWS IAM user ARNs in order to identify potential targets for further attacks. 

Technical Description: AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. When you create an IAM user, AWS automatically assigns a unique Amazon Resource Name (ARN) to the user. The ARN is used to identify the user in AWS Identity and Access Management (IAM) policies, Amazon S3 bucket policies, and elsewhere. By using the 'AWS IAM User ARN' command, an attacker can discover the ARNs of all the IAM users in an AWS account. 

Business Value: By discovering the ARNs of all the IAM users in an AWS account, an attacker can identify potential targets for further attacks. This can lead to unauthorized access to sensitive data, theft of intellectual property, and other malicious activities.

## Requirements

1. Valid AWS credentials with the necessary permissions to run the 'AWS IAM User ARN' command.

## Defense

1. Regularly review and audit IAM users and their permissions.

1. Implement multi-factor authentication (MFA) for IAM users.

1. Monitor AWS CloudTrail logs for suspicious activity related to IAM users.

## Objectives

1. Discover the ARNs of all the IAM users in an AWS account.

# Instructions

1. The AWS IAM User ARN (Amazon Resource Name) is a unique identifier assigned to each user in the AWS Identity and Access Management (IAM) service. The ARN is a string of characters that identifies the user and their account. The ARN can be used to reference the user in various AWS services and APIs.

**Code**: [[arn:aws:iam:100:user/admin]]

> The 'arn:aws:iam:100:user/admin' value in this JSON object is an example of an IAM User ARN. The '100' in the ARN represents the AWS account ID, while 'user' indicates that the resource is a user. 'admin' is the name of the user. The ARN can be used to identify the user in various AWS services such as Amazon S3, Amazon EC2, or AWS Lambda. It can also be used in IAM policies to grant or deny access to specific resources or actions. It is important to keep the ARN of the user confidential to prevent unauthorized access to AWS resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Tags

- [[ARN]]
- [[Cloud - AWS]]
