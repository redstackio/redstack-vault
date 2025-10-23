---
id: 306c8cbe-b073-485a-94c9-2647fb004cbf
name: AWS IAM Inline Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.371713+00:00'
updated_at: '2023-04-10T20:20:04.805438+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[4. Enumerating Policies]]'
- '[[Cloud - AWS]]'
- '[[Retrieving the specified inline policy document that is embedded on the specified
  IAM user / group / role]]'
commands:
- '[[Get group policy]]'
- '[[Get role policy]]'
- '[[Get user policy]]'
---

# AWS IAM Inline Policy Enumeration

## Summary

AWS Identity and Access Management (IAM) is a service that enables you to manage access to AWS resources within your organization. Attackers can enumerate policies to identify permissions and potentially escalate their privileges. This procedure focuses on retrieving the specified inline policy doc

## Description

# Description

AWS Identity and Access Management (IAM) is a service that enables you to manage access to AWS resources within your organization. Attackers can enumerate policies to identify permissions and potentially escalate their privileges. This procedure focuses on retrieving the specified inline policy document that is embedded on the specified IAM user / group / role. The attacker can then use this information to identify potential paths for privilege escalation.

Technical Description: The attacker can use the 'Retrieve IAM Policy Details' command to retrieve the inline policy document embedded on an IAM user, group or role. This document contains the permissions granted to the user, group or role. The attacker can then analyze the document to identify potential paths for privilege escalation.

Business Value: By identifying potential paths for privilege escalation, the attacker can gain access to sensitive data and resources within the organization. This can lead to data theft, financial loss, and damage to the organization's reputation.

 

## Requirements

1. Valid AWS credentials with IAM permissions

 

## Defense

1. Regularly review and audit IAM policies to ensure they are up-to-date and necessary

1. Use AWS trusted advisor to identify and remediate any security issues related to IAM policies

1. Implement multi-factor authentication (MFA) for all IAM users to prevent unauthorized access

 

## Objectives

1. Retrieve the inline policy document embedded on an IAM user, group or role

1. Identify potential paths for privilege escalation

 

# Instructions

1. To retrieve details about an IAM policy, use one of the following commands:

1. `aws iam get-user-policy --user-name user-name --policy-name policy-name`
This command retrieves the specified policy attached to the specified user.

2. `aws iam get-group-policy --group-name group-name --policy-name policy-name`
This command retrieves the specified policy attached to the specified group.

3. `aws iam get-role-policy --role-name role-name --policy-name policy-name`
This command retrieves the specified policy attached to the specified role.

 



**Code**: [[aws iam get-user-policy --user-name user-name --po]]



> The `--user-name`, `--group-name`, and `--role-name` parameters are used to specify the name of the user, group, or role that the policy is attached to. The `--policy-name` parameter is used to specify the name of the policy you want to retrieve.

For example, to retrieve the policy named 'S3-ReadOnly' attached to the user named 'JohnDoe', you would run the following command:

`aws iam get-user-policy --user-name JohnDoe --policy-name S3-ReadOnly`



**Command** ([[Get user policy]]):

```bash
aws iam get-user-policy --user-name user-name --policy-name policy-name
```





**Command** ([[Get group policy]]):

```bash
aws iam get-group-policy --group-name group-name --policy-name policy-name
```





**Command** ([[Get role policy]]):

```bash
aws iam get-role-policy --role-name role-name --policy-name policy-name
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

- [[Get group policy]]
- [[Get role policy]]
- [[Get user policy]]

## Tags

- [[4. Enumerating Policies]]
- [[Cloud - AWS]]
- [[Retrieving the specified inline policy document that is embedded on the specified IAM user / group / role]]


