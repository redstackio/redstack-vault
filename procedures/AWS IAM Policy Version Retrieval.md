---
id: 86ca81ec-4402-4695-b933-db5557fe81a6
name: AWS IAM Policy Version Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.882744+00:00'
updated_at: '2023-04-10T20:20:32.613842+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Accessing more credentials]]'
- '[[Cloud - AWS]]'
- '[[Persistence & Backdooring]]'
- '[[Retrieving information about the specified version of the policy]]'
commands:
- '[[Get IAM policy version]]'
---

# AWS IAM Policy Version Retrieval

## Summary

The AWS IAM Policy Version Retrieval procedure is used to retrieve information about the specified version of the policy. This procedure can be used to gain access to additional credentials and escalate privileges. By accessing the specified version of the policy, an attacker can gain a better unde

## Description

# Description

The AWS IAM Policy Version Retrieval procedure is used to retrieve information about the specified version of the policy. This procedure can be used to gain access to additional credentials and escalate privileges. By accessing the specified version of the policy, an attacker can gain a better understanding of the permissions granted to an IAM role, and potentially identify additional roles that can be assumed. Additionally, this procedure can be used to identify misconfigurations in the IAM policy that can be exploited to gain unauthorized access.

To execute this procedure, the attacker needs to have access to an IAM role that has the necessary permissions to retrieve the specified version of the policy. This can be achieved by exploiting a vulnerability in the application or by using stolen credentials. Once the attacker has access to the necessary permissions, they can use the 'Get IAM Policy Version' command to retrieve the specified version of the policy.

The business value of this procedure is that it allows an attacker to gain access to additional credentials and escalate privileges. This can be used to gain unauthorized access to sensitive data or resources, and can result in financial loss or damage to a company's reputation.

## Requirements

1. Access to an IAM role with the necessary permissions to retrieve the specified version of the policy

## Defense

1. Implement strong authentication mechanisms, such as multi-factor authentication, to prevent unauthorized access to AWS resources

1. Regularly review and audit IAM policies to identify and remediate misconfigurations

1. Enable AWS CloudTrail to monitor and log all API activity in your AWS account

## Objectives

1. Retrieve information about the specified version of the IAM policy

1. Identify additional roles that can be assumed

1. Identify misconfigurations in the IAM policy

# Instructions

1. To get a specific version of an IAM policy, use the 'aws iam get-policy-version' command.

This command retrieves a specific version of an IAM policy. To use this command, you need to specify the policy ARN and version ID. The policy ARN uniquely identifies the IAM policy and the version ID is the identifier for the specific version of the policy. The output of this command includes the policy version details, including the policy document, the policy name, and the version ID. This command is useful when you need to retrieve a specific version of an IAM policy for auditing or troubleshooting purposes.

**Command** ([[Get IAM policy version]]):

```bash
aws iam get-policy-version --policy-arn policy_arn --version-id ID
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get IAM policy version]]

## Tags

- [[5. Exploitation Scenario]]
- [[Accessing more credentials]]
- [[Cloud - AWS]]
- [[Persistence & Backdooring]]
- [[Retrieving information about the specified version of the policy]]
