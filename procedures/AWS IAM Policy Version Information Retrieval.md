---
id: d698bc9a-db5d-46c9-afc3-74278058a21f
name: AWS IAM Policy Version Information Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.258417+00:00'
updated_at: '2023-04-10T20:20:13.613243+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Exfiltration]]'
- '[[Retrieving information about a specific version of policy]]'
commands:
- '[[Get IAM policy version]]'
---

# AWS IAM Policy Version Information Retrieval

## Summary

This procedure involves retrieving information about a specific version of an AWS Identity and Access Management (IAM) policy. This can be useful for an attacker attempting to understand the permissions and access levels of a particular user or role. By obtaining this information, an attacker can i

## Description

# Description

This procedure involves retrieving information about a specific version of an AWS Identity and Access Management (IAM) policy. This can be useful for an attacker attempting to understand the permissions and access levels of a particular user or role. By obtaining this information, an attacker can identify potential misconfigurations or weaknesses that can be exploited to escalate privileges or exfiltrate sensitive data. Technical details of this procedure include using the Get IAM Policy Version command to retrieve the specified policy version. From there, the attacker can analyze the policy document to identify potential vulnerabilities or areas of weakness. From a business perspective, this procedure can help identify areas where access controls can be improved or where additional monitoring is needed to prevent unauthorized access to sensitive data.

## Requirements

1. Valid AWS credentials with appropriate permissions to access IAM policies

## Defense

1. Regularly review and audit AWS IAM policies to identify and remediate potential vulnerabilities

1. Implement multi-factor authentication (MFA) for all AWS accounts and roles

1. Limit permissions of AWS IAM users and roles to only what is necessary for their job functions

## Objectives

1. Retrieve information about a specific version of an AWS IAM policy

1. Identify potential misconfigurations or weaknesses in the policy

1. Escalate privileges or exfiltrate sensitive data

# Instructions

1. To get the details of a specific version of an IAM policy, use the following command:

**Code**: [[aws iam get-policy-version --policy-arn arn --vers]]

> This command retrieves the details of a specific version of an IAM policy. The `--policy-arn` parameter specifies the Amazon Resource Name (ARN) of the policy, and the `--version-id` parameter specifies the version ID of the policy. The output includes information about the policy, such as the policy name, description, and permissions.

**Command** ([[Get IAM policy version]]):

```bash
aws iam get-policy-version --policy-arn arn --version-id id
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]

## Commands Used

- [[Get IAM policy version]]

## Tags

- [[Cloud - AWS]]
- [[Credential Exfiltration]]
- [[Retrieving information about a specific version of policy]]
