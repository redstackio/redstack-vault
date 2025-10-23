---
id: 7a1bc42f-c7ba-4a19-abce-ec00d94cb5e7
name: AWS IAM Role Policies Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.858163+00:00'
updated_at: '2023-04-10T20:20:43.949739+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Accessing more credentials]]'
- '[[Cloud - AWS]]'
- '[[Listing all managed policies attached to the specific IAM role]]'
- '[[Persistence & Backdooring]]'
commands:
- '[[List Attached Role Policies]]'
---

# AWS IAM Role Policies Enumeration

## Summary

AWS IAM Role Policies Enumeration is a technique used by attackers to discover and list all managed policies attached to a specific IAM role. Attackers can use this information to identify potential privilege escalation opportunities and further their attack. This technique can be used as part of a

## Description

# Description

AWS IAM Role Policies Enumeration is a technique used by attackers to discover and list all managed policies attached to a specific IAM role. Attackers can use this information to identify potential privilege escalation opportunities and further their attack. This technique can be used as part of an AWS IAM Privilege Escalation attack.

To perform this technique, an attacker would use the 'List Attached Role Policies' command. This command returns a list of all managed policies attached to a specific IAM role. The attacker can then analyze this information to identify potential escalation paths.

This technique provides attackers with valuable information that can be used to further their attack and gain access to sensitive data or resources. Organizations should be aware of this technique and take steps to prevent and detect AWS IAM Privilege Escalation attacks.

 

## Requirements

1. Valid AWS credentials with IAM permissions

 

## Defense

1. Implement the principle of least privilege for IAM roles and policies

1. Monitor and analyze AWS CloudTrail logs for suspicious activity

1. Regularly review and audit IAM roles and policies for unnecessary permissions

 

## Objectives

1. Discover all managed policies attached to a specific IAM role

1. Identify potential privilege escalation opportunities

 

# Instructions

1. To list the policies attached to a specific IAM role, use the following command:

 

This command lists all of the policies that are attached to the specified IAM role. The --role-name flag is used to specify the name of the role that you want to list the attached policies for. This command can be useful for auditing and troubleshooting purposes, as well as for managing access control within your AWS environment.



**Command** ([[List Attached Role Policies]]):

```bash
aws iam liast-attached-role-policies --role-name role_name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Attached Role Policies]]

## Tags

- [[5. Exploitation Scenario]]
- [[Accessing more credentials]]
- [[Cloud - AWS]]
- [[Listing all managed policies attached to the specific IAM role]]
- [[Persistence & Backdooring]]


