---
id: 1e5933a9-63eb-4ab3-9cb9-d0d02b280e8d
name: AWS Role Assumption for Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.906348+00:00'
updated_at: '2023-04-10T20:19:48.110916+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Accessing more credentials]]'
- '[[Cloud - AWS]]'
- '[[Getting temporary credentials for the role]]'
- '[[Persistence & Backdooring]]'
commands:
- '[[Assume AWS Role]]'
---

# AWS Role Assumption for Persistence

## Summary

Assuming an AWS role can provide an attacker with persistent access to a target's resources. By obtaining temporary credentials for the role, the attacker can maintain access even if the original credentials are revoked. This technique can be used to move laterally within an AWS environment and acc

## Description

# Description

Assuming an AWS role can provide an attacker with persistent access to a target's resources. By obtaining temporary credentials for the role, the attacker can maintain access even if the original credentials are revoked. This technique can be used to move laterally within an AWS environment and access additional sensitive data.

To assume a role, the attacker must first obtain valid AWS credentials. They can then use the AssumeRole API to request temporary security credentials for the role. These credentials can be used to perform actions on AWS resources that are allowed by the role's policy.

This technique can be valuable for an attacker seeking to maintain a long-term presence in an AWS environment.

 

## Requirements

1. Valid AWS credentials

 

## Defense

1. Enforce the principle of least privilege to limit the permissions of AWS roles

1. Monitor AWS CloudTrail logs for unusual activity, such as role assumption

1. Enable multi-factor authentication (MFA) for AWS accounts to prevent unauthorized access

 

## Objectives

1. Assume a role in an AWS environment

1. Obtain temporary credentials for the role

1. Maintain persistent access to target resources

 

# Instructions

1. To assume a role in AWS, use the 'aws sts assume-role' command followed by the ARN of the role you want to assume and a session name.

 

This command is used to temporarily assume a role in AWS. The role ARN is the Amazon Resource Name (ARN) of the role that you want to assume. The session name is a unique identifier for the session. The temporary security credentials that are returned by this command can be used to make AWS API calls with the permissions of the assumed role.



**Command** ([[Assume AWS Role]]):

```bash
aws sts assume-role --role-arn role_arn --role-session-name session_name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Assume AWS Role]]

## Tags

- [[5. Exploitation Scenario]]
- [[Accessing more credentials]]
- [[Cloud - AWS]]
- [[Getting temporary credentials for the role]]
- [[Persistence & Backdooring]]


