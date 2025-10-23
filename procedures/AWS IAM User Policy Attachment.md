---
id: 17a46eb3-f11b-46cf-b301-24edb5f5134d
name: AWS IAM User Policy Attachment
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.544455+00:00'
updated_at: '2023-04-10T20:20:43.598047+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Attaching this policy into our user]]'
- '[[Cloud - AWS]]'
commands:
- '[[Create IAM user policy]]'
---

# AWS IAM User Policy Attachment

## Summary

The AWS IAM User Policy Attachment is a technique used by attackers to escalate privileges and maintain persistence in an AWS environment. By attaching a malicious policy to an existing IAM user, an attacker can grant themselves additional permissions and maintain access to the environment even if 

## Description

# Description

The AWS IAM User Policy Attachment is a technique used by attackers to escalate privileges and maintain persistence in an AWS environment. By attaching a malicious policy to an existing IAM user, an attacker can grant themselves additional permissions and maintain access to the environment even if their original access is revoked. This technique requires initial access to an AWS environment and the ability to add an IAM user policy. 

From a technical perspective, this technique involves adding a policy to an existing IAM user that grants the attacker additional permissions. The attacker can then use these permissions to perform further actions within the environment, such as creating new users or modifying existing resources. From a business value perspective, this technique can lead to a complete compromise of an AWS environment, resulting in data theft, service disruption, and reputational damage.

 

## Requirements

1. Access to an AWS environment

1. Ability to add an IAM user policy

 

## Defense

1. Regularly review IAM user policies for any unauthorized attachments

1. Implement least privilege access controls for IAM users

1. Enable MFA for all IAM users to prevent unauthorized access

 

## Objectives

1. Escalate privileges in an AWS environment

1. Maintain persistence in an AWS environment

1. Perform further actions within an AWS environment

 

# Instructions

1. Use the 'aws iam put-user-policy' command to add a policy to an IAM user.

 

This command allows you to add a policy to an IAM user. The 'user-name' parameter specifies the name of the user you want to add the policy to. The 'policy-name' parameter specifies the name of the policy. The 'policy-document' parameter specifies the JSON policy document that contains the permissions you want to grant to the user. The policy document must be stored in a file and the file path should be specified with the 'file://' prefix. This command can be useful when you want to grant permissions to an IAM user to access specific AWS resources.



**Command** ([[Create IAM user policy]]):

```bash
aws iam put-user-policy --user-name example_username --policy-name example_name --policy-document file://AdminPolicy.json
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]

## Commands Used

- [[Create IAM user policy]]

## Tags

- [[5. Exploitation Scenario]]
- [[Attaching this policy into our user]]
- [[Cloud - AWS]]


