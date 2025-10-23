---
id: f953efd8-0251-4135-a694-477660aaf389
name: AWS IAM Role Inline Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.243186+00:00'
updated_at: '2023-04-10T20:20:30.584608+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[3. Enumeratig Roles]]'
- '[[Cloud - AWS]]'
- '[[Listing the names of the inline policies embedded in the specified IAM role]]'
commands:
- '[[List Role Policies]]'
---

# AWS IAM Role Inline Policy Enumeration

## Summary

The AWS Identity and Access Management (IAM) service allows users to manage access to AWS services and resources securely. One of the key components of IAM is roles, which define a set of permissions for making AWS service requests. This procedure involves enumerating the names of the inline polici

## Description

# Description

The AWS Identity and Access Management (IAM) service allows users to manage access to AWS services and resources securely. One of the key components of IAM is roles, which define a set of permissions for making AWS service requests. This procedure involves enumerating the names of the inline policies embedded in a specified IAM role. An inline policy is a policy that is embedded in the same JSON document as the role. This technique can be used by an attacker to gain a better understanding of the permissions associated with a specific role, potentially leading to privilege escalation or lateral movement.

Technical Explanation: The ListRolePolicies API call is used to enumerate the names of the inline policies associated with a specified IAM role. The attacker can use this technique to gather information about the permissions associated with a role, which can be used to identify potential targets for further exploitation.

Business Value: This procedure can be used by security teams to identify potential security weaknesses in their AWS environment, and to ensure that permissions are correctly configured to prevent privilege escalation.

 

## Requirements

1. Valid AWS credentials with permissions to call the ListRolePolicies API

 

## Defense

1. Ensure that IAM roles are configured with the principle of least privilege

1. Monitor AWS CloudTrail logs for suspicious activity related to IAM roles and policies

1. Implement multi-factor authentication (MFA) for AWS IAM users to prevent unauthorized access to AWS resources

 

## Objectives

1. Enumerate the names of the inline policies embedded in a specified IAM role

1. Gain a better understanding of the permissions associated with a specific role

1. Identify potential targets for further exploitation

 

# Instructions

1. To list all the policies attached to a specific role, use the following command:

 

The 'aws iam list-role-policies' command is used to list all the policies that are attached to a specific IAM role. The command requires the 'role-name' argument to be specified, which is the name of the role you want to list the policies for. This command can be helpful in identifying the policies attached to a role, which can be useful for auditing and troubleshooting purposes. The output of this command will be a JSON array containing the names of the policies attached to the specified role.



**Command** ([[List Role Policies]]):

```bash
aws iam list-role-policies --role-name role-name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Role Policies]]

## Tags

- [[3. Enumeratig Roles]]
- [[Cloud - AWS]]
- [[Listing the names of the inline policies embedded in the specified IAM role]]


