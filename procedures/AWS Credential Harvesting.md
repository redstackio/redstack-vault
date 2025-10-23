---
id: 20a46a29-4c22-4a0a-89f3-7afd444f9b79
name: AWS Credential Harvesting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.582021+00:00'
updated_at: '2023-04-10T20:21:03.049088+00:00'
tags:
- '[[After the initial access]]'
- '[[Cloud - AWS]]'
- '[[Credential Access]]'
- '[[Exploitation]]'
commands:
- '[[Retrieve IAM Security Credentials]]'
---

# AWS Credential Harvesting

## Summary

AWS Credential Harvesting is a technique used to obtain access to AWS resources by stealing AWS access keys and secret keys. This technique can be used by an attacker who has already gained initial access to a target's AWS environment. The attacker can then use these credentials to move laterally w

## Description

# Description

AWS Credential Harvesting is a technique used to obtain access to AWS resources by stealing AWS access keys and secret keys. This technique can be used by an attacker who has already gained initial access to a target's AWS environment. The attacker can then use these credentials to move laterally within the environment and access sensitive resources. This technique can be used to gain access to sensitive data, launch further attacks, and potentially cause significant damage to the target's business.

Technical Explanation: This technique involves retrieving AWS security credentials from a compromised instance, application, or container. The attacker can then use these credentials to authenticate to other AWS services and resources. This is often done through the use of AWS CLI or SDKs. The attacker can then use these credentials to perform actions such as creating new instances, modifying security groups, and accessing sensitive data.

Business Value: This technique can be used by attackers to gain access to sensitive data, launch further attacks, and potentially cause significant damage to the target's business. By stealing AWS access keys and secret keys, the attacker can bypass security controls and gain access to resources that they would not normally have access to.

 

## Requirements

1. Access to the target's AWS environment

1. Knowledge of AWS CLI or SDKs

 

## Defense

1. Implement strong access controls and monitoring for AWS credentials

1. Use multi-factor authentication for AWS accounts

1. Regularly rotate AWS access keys and secret keys

 

## Objectives

1. Steal AWS access keys and secret keys

1. Move laterally within the target's AWS environment

1. Access sensitive resources within the AWS environment

 

# Instructions

1. To retrieve the security credentials for an AWS IAM Role, use the following command:

 

This command uses the cURL tool to query the AWS metadata service for the security credentials associated with an IAM Role. The 'ROLE_OF_PREVIOUS_COMMAND' argument should be replaced with the name of the IAM Role for which you want to retrieve the security credentials. The output of this command will be a JSON document containing the access key, secret access key, and security token for the specified IAM Role.



**Command** ([[Retrieve IAM Security Credentials]]):

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_OF_PREVIOUS_COMMAND
```



## Commands Used

- [[Retrieve IAM Security Credentials]]

## Tags

- [[After the initial access]]
- [[Cloud - AWS]]
- [[Credential Access]]
- [[Exploitation]]


