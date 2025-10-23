---
id: 540f3976-3757-4dd9-9dbb-89f1464eb457
name: AWS Privilege Escalation via Default Policy Information
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.517831+00:00'
updated_at: '2023-04-10T20:19:47.770401+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Privilege Escalation]]'
- '[[Study Case]]'
---

# AWS Privilege Escalation via Default Policy Information

## Summary

This procedure involves exploiting default policy information in AWS to escalate privileges. An attacker can discover AWS resources and permissions associated with a compromised user or role, and then use this information to generate new access tokens with elevated permissions. This attack can resu

## Description

# Description

This procedure involves exploiting default policy information in AWS to escalate privileges. An attacker can discover AWS resources and permissions associated with a compromised user or role, and then use this information to generate new access tokens with elevated permissions. This attack can result in the attacker gaining complete control over the AWS environment, allowing them to exfiltrate sensitive data, modify or delete resources, and launch further attacks. Technical details include discovering the compromised user or role's AWS access key and secret access key, using the AWS CLI to list the resources and permissions associated with the user or role, and then using this information to generate new access tokens with elevated permissions. Business value includes the potential for significant financial and reputational damage resulting from data theft or service disruption.

 

## Requirements

1. Valid AWS access key and secret access key for a compromised user or role

1. Access to the AWS CLI

 

## Defense

1. Implement strong access control policies and limit the use of default policies

1. Regularly review and audit AWS access keys and secret access keys

1. Monitor for unusual or suspicious activity within the AWS environment

 

## Objectives

1. Escalate privileges within the AWS environment

1. Gain complete control over AWS resources

1. Exfiltrate sensitive data

1. Modify or delete AWS resources

1. Launch further attacks

 

# Instructions

1. To get the details of the default policy, use the command provided above.

 



**Code**: [[{
    "Version": "2021-10-17",
    "Statement" : []]



> This command provides the details of the default policy that is applied to all resources in an AWS account. The policy allows all actions on all resources, which can be a security risk. It is important to understand the details of this policy to ensure the security of your AWS resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Tags

- [[5. Exploitation Scenario]]
- [[Cloud - AWS]]
- [[Exploitation]]
- [[Privilege Escalation]]
- [[Study Case]]


