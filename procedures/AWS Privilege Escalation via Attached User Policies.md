---
id: dd09db1a-6e60-4497-b8ba-cfb77685c6b4
name: AWS Privilege Escalation via Attached User Policies
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.459044+00:00'
updated_at: '2023-04-10T20:20:50.264486+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Privilege Escalation]]'
- '[[Study Case]]'
commands:
- '[[List Attached User Policies for IAM User]]'
---

# AWS Privilege Escalation via Attached User Policies

## Summary

This procedure involves exploiting a misconfigured AWS IAM policy to escalate privileges within the AWS environment. Attackers can use the 'List Attached User Policies' command to identify policies that are attached to a specific user, and then modify the policy to grant themselves additional privi

## Description

# Description

This procedure involves exploiting a misconfigured AWS IAM policy to escalate privileges within the AWS environment. Attackers can use the 'List Attached User Policies' command to identify policies that are attached to a specific user, and then modify the policy to grant themselves additional privileges. This can allow an attacker to gain access to sensitive resources, such as customer data or intellectual property.

Technical Explanation: An attacker with access to a user's AWS access key can use the 'ListAttachedUserPolicies' API call to identify the policies attached to that user. The attacker can then modify the policy to grant themselves additional privileges, such as the ability to read or write to an S3 bucket. This is possible if the policy is not properly scoped to the resources that the user needs access to. Business Value: This procedure can allow attackers to gain access to sensitive data or intellectual property, which can be sold or used for competitive advantage.

## Requirements

1. Valid AWS access key for a user with attached policies

## Defense

1. Ensure that AWS IAM policies are properly scoped to the resources that the user needs access to

1. Monitor for modifications to IAM policies

1. Implement multi-factor authentication for AWS accounts to prevent unauthorized access

## Objectives

1. Gain additional privileges within the AWS environment

1. Access sensitive resources such as customer data or intellectual property

# Instructions

1. Use this command to list all the policies that are attached to a specific IAM user.

The 'aws iam list-attached-user-policies' command is a helpful tool for administrators who need to manage the policies that are attached to their IAM users. The '--user-name' parameter specifies the name of the IAM user whose attached policies you want to list. The '--profile' parameter specifies the named profile you want to use to interact with AWS. If you don't specify a profile, this command will use the default profile. Once you run this command, you will receive a list of all the policies that are attached to the specified IAM user.

**Command** ([[List Attached User Policies for IAM User]]):

```bash
aws iam list-attached-user-policies --user-name example_name --profile example_profile
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[List Attached User Policies for IAM User]]

## Tags

- [[5. Exploitation Scenario]]
- [[Cloud - AWS]]
- [[Exploitation]]
- [[Privilege Escalation]]
- [[Study Case]]
