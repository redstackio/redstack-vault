---
id: 3d42b32c-c309-471c-be8b-3ad37c796910
name: AWS Inline Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.568791+00:00'
updated_at: '2023-04-10T20:20:14.402789+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Cloud - AWS]]'
- '[[Listing inline policies of our user]]'
commands:
- '[[List user policies for IAM user]]'
---

# AWS Inline Policy Enumeration

## Summary

The AWS Inline Policy Enumeration procedure involves listing all inline policies associated with a particular user in AWS. This procedure can be used to identify any misconfigured policies that could potentially be exploited by an attacker. By listing inline policies, an attacker can gain a better 

## Description

# Description

The AWS Inline Policy Enumeration procedure involves listing all inline policies associated with a particular user in AWS. This procedure can be used to identify any misconfigured policies that could potentially be exploited by an attacker. By listing inline policies, an attacker can gain a better understanding of the permissions granted to a user and potentially use that information to escalate privileges or perform other malicious activities.

To list inline policies, the AWS CLI is used to query the AWS API. The AWS CLI requires valid AWS access keys and permissions to perform the necessary actions.

The business value of this procedure is that it can help identify and remediate misconfigured policies, reducing the risk of a successful attack.

## Requirements

1. Valid AWS access keys

1. Permissions to query AWS API

## Defense

1. Ensure that access keys are properly secured and not shared unnecessarily

1. Implement least privilege policies to limit the permissions granted to users

1. Regularly review and audit policies to identify and remediate misconfigurations

## Objectives

1. Identify all inline policies associated with a particular user in AWS

1. Assess the permissions granted to the user

1. Identify any misconfigured policies that could be exploited by an attacker

# Instructions

1. Use the 'aws iam list-user-policies' command to list all the policies attached to a specific IAM user. Replace 'example_name' with the actual name of the user.

This command lists all the policies that are attached to a specific IAM user. This can be useful in determining the level of access that a user has within the AWS environment. The policies listed will include both managed and inline policies.

**Command** ([[List user policies for IAM user]]):

```bash
aws iam list-user-policies --user-name example_name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List user policies for IAM user]]

## Tags

- [[5. Exploitation Scenario]]
- [[Cloud - AWS]]
- [[Listing inline policies of our user]]
