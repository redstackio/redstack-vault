---
id: 97998e8b-1451-4bb2-95a3-37a00c86f790
name: AWS IAM Role Trust Relationship Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.831987+00:00'
updated_at: '2023-04-10T20:20:40.333958+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Accessing more credentials]]'
- '[[Cloud - AWS]]'
- '[[Listing trust relationship between role and user (Which roles we can assume)]]'
- '[[Persistence & Backdooring]]'
commands:
- '[[Get IAM Role]]'
---

# AWS IAM Role Trust Relationship Enumeration

## Summary

This procedure involves enumerating the trust relationship between AWS IAM roles and users to identify which roles can be assumed by the user. By using the 'Retrieve IAM Role Details' command, the attacker can list all the roles in the AWS account and their trust relationships with users. This info

## Description

# Description

This procedure involves enumerating the trust relationship between AWS IAM roles and users to identify which roles can be assumed by the user. By using the 'Retrieve IAM Role Details' command, the attacker can list all the roles in the AWS account and their trust relationships with users. This information can be used to identify high-value roles that the attacker can assume and gain access to sensitive resources.

Technical Explanation: The AWS IAM Access Advisor, ListRoles, and GetRole APIs are used to retrieve information about the roles and their trust relationships with users. The attacker can then analyze this information to identify the roles that can be assumed by the user.

Business Value: This procedure can help an attacker gain access to sensitive resources in an AWS account, allowing them to steal data, disrupt operations, or launch further attacks.

## Requirements

1. Valid AWS access keys with permissions to use the IAM APIs

## Defense

1. Regularly review and audit the trust relationships between IAM roles and users

1. Implement least privilege access controls to limit the impact of compromised IAM roles

1. Enable AWS CloudTrail to monitor and log all API activity in the AWS account

## Objectives

1. Identify high-value roles that can be assumed by the attacker

1. Gain access to sensitive resources in an AWS account

# Instructions

1. To retrieve details of an IAM Role, use the following command:

This command retrieves the details of an IAM Role specified by the role_name argument. The command returns a JSON object that contains information about the role, such as its name, ARN, and policies attached to the role.

**Command** ([[Get IAM Role]]):

```bash
aws iam get-role --role-name role_name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get IAM Role]]

## Tags

- [[5. Exploitation Scenario]]
- [[Accessing more credentials]]
- [[Cloud - AWS]]
- [[Listing trust relationship between role and user (Which roles we can assume)]]
- [[Persistence & Backdooring]]
