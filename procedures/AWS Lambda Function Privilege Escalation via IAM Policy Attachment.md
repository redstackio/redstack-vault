---
id: 03578124-672d-4482-b2c5-ddfa02fc6b7e
name: AWS Lambda Function Privilege Escalation via IAM Policy Attachment
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:12.007768+00:00'
updated_at: '2023-05-25T20:08:57.084101+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
tags:
- '[[Cloud - AWS]]'
- '[[Create a lambda function and attach a role to it]]'
- '[[Example code to add the permissions]]'
- '[[Privilege Escalation]]'
---

# AWS Lambda Function Privilege Escalation via IAM Policy Attachment

**Status**: ✓ Verified

## Summary

AWS Lambda Function Privilege Escalation via IAM Policy Attachment is a technique used by attackers to escalate their privileges within an AWS environment. This technique involves creating a new Lambda function and attaching an IAM role to it. The IAM role is then granted permissions that the attac

## Description

# Description

AWS Lambda Function Privilege Escalation via IAM Policy Attachment is a technique used by attackers to escalate their privileges within an AWS environment. This technique involves creating a new Lambda function and attaching an IAM role to it. The IAM role is then granted permissions that the attacker can use to carry out malicious activities. This technique can be used to bypass least privilege access controls and gain access to sensitive data or resources.

From a technical perspective, this technique involves creating a new Lambda function with a custom IAM role attached to it. The IAM role is granted permissions to access sensitive resources such as S3 buckets, RDS instances, or EC2 instances. Once the attacker has access to these resources, they can carry out malicious activities such as data exfiltration, lateral movement, or privilege escalation.

Businesses can protect themselves from this attack by implementing the principle of least privilege and monitoring their AWS environment for suspicious activity.

 

## Requirements

1. Access to an AWS environment

1. Permissions to create a new Lambda function and attach an IAM role to it

 

## Defense

1. Implement the principle of least privilege to restrict access to sensitive resources

1. Monitor AWS CloudTrail logs for suspicious activity

1. Regularly review and audit IAM policies and roles for unnecessary permissions

 

## Objectives

1. Escalate privileges within an AWS environment

1. Gain access to sensitive data or resources

 

# Instructions

1. Use this command to attach an IAM policy to an IAM role or user.

 



**Code**: [[import boto3
import json

def handler(event,contex]]



> This command takes two arguments: RoleName and PolicyArn. The RoleName argument specifies the name of the IAM role to which the policy will be attached. The PolicyArn argument specifies the Amazon Resource Name (ARN) of the policy to attach. The command can be used to attach policies to both IAM roles and users. The command returns a success message upon successful attachment of the policy.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]

## Tags

- [[Cloud - AWS]]
- [[Create a lambda function and attach a role to it]]
- [[Example code to add the permissions]]
- [[Privilege Escalation]]


