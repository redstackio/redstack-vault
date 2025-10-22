---
id: f851d96b-db3f-4ee9-9633-20e7d9d75824
name: AWS IAM User Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.012455+00:00'
updated_at: '2023-04-10T20:20:23.921365+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
tags:
- '[[1. Enumerating IAM users]]'
- '[[Cloud - AWS]]'
- '[[Listing IAM Users]]'
commands:
- '[[List IAM Users]]'
---

# AWS IAM User Enumeration

## Summary

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. IAM allows you to create and manage AWS users and groups, and assign permissions to them. This procedure involves enumerating IAM users in an AWS account. By listing IAM users, an atta

## Description

# Description

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. IAM allows you to create and manage AWS users and groups, and assign permissions to them. This procedure involves enumerating IAM users in an AWS account. By listing IAM users, an attacker can identify potential targets for further attacks such as password spraying, phishing or social engineering. An attacker can use various methods to list IAM users such as using the AWS CLI or accessing the Cloud Service Dashboard. 

Technical Explanation: AWS IAM users are a type of AWS identity that represents a person or service that interacts with AWS services and resources. IAM users can be granted permissions to access AWS resources such as EC2 instances, S3 buckets, and RDS databases. By listing IAM users, an attacker can identify potential targets for further attacks such as password spraying, phishing or social engineering. An attacker can use various methods to list IAM users such as using the AWS CLI or accessing the Cloud Service Dashboard.

Business Value: This procedure can help an attacker identify potential targets for further attacks such as password spraying, phishing or social engineering. By compromising an IAM user, an attacker can gain access to sensitive data or resources, which can result in financial loss, reputational damage, and legal liabilities.

## Requirements

1. Valid AWS credentials with IAM permissions

1. Access to the AWS CLI or Cloud Service Dashboard

## Defense

1. Implement multi-factor authentication (MFA) for IAM users

1. Monitor IAM user activity logs for suspicious behavior

1. Regularly review and remove unnecessary or unused IAM users

## Objectives

1. Identify potential targets for further attacks

1. Gain access to sensitive data or resources

# Instructions

1. To list all the users in AWS IAM, run the following command:

**Code**: [[aws iam list-users]]

> This command retrieves a list of all the users in the AWS Identity and Access Management (IAM) service. It returns a JSON object that contains information about each user, including their username, user ID, and ARN. This command can be useful for auditing and managing user access to AWS resources.

**Command** ([[List IAM Users]]):

```bash
aws iam list-users
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]

## Commands Used

- [[List IAM Users]]

## Tags

- [[1. Enumerating IAM users]]
- [[Cloud - AWS]]
- [[Listing IAM Users]]
