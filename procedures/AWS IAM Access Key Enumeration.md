---
id: 34e73b25-7b63-48f9-9123-bfe645b92153
name: AWS IAM Access Key Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.956216+00:00'
updated_at: '2023-04-10T20:20:23.576984+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials In Files|T1552.001 - Credentials In Files]]'
- '[[Credentials in Registry|T1552.002 - Credentials in Registry]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing IAM access Keys]]'
commands:
- '[[List IAM Access Keys]]'
---

# AWS IAM Access Key Enumeration

## Summary

The AWS IAM Access Key Enumeration procedure involves listing all the access keys associated with an AWS Identity and Access Management (IAM) user account. This procedure is commonly used by attackers to obtain valid access keys that can be used to access and control AWS resources. 

Technical Desc

## Description

# Description

The AWS IAM Access Key Enumeration procedure involves listing all the access keys associated with an AWS Identity and Access Management (IAM) user account. This procedure is commonly used by attackers to obtain valid access keys that can be used to access and control AWS resources. 

Technical Description: AWS IAM is a web service that helps you securely control access to AWS resources. Access keys consist of an access key ID and a secret access key. These keys are used to sign programmatic requests made to AWS services. When an IAM user is created, access keys are generated for that user. The access keys are used to authenticate requests made to AWS resources. 

Business Value: This procedure can be used by attackers to gain access to sensitive data or resources stored in AWS. It is important for organizations to regularly audit their IAM users and access keys to ensure that only authorized users have access to resources.

 

## Requirements

1. Valid AWS IAM user credentials

1. Access to the AWS Management Console or AWS CLI

 

## Defense

1. Regularly audit IAM users and access keys to ensure that only authorized users have access to resources

1. Enable multi-factor authentication (MFA) for IAM users to add an extra layer of security

1. Monitor AWS CloudTrail logs for any unauthorized access key usage

 

## Objectives

1. Enumerate all the access keys associated with an AWS IAM user account

1. Identify any unauthorized access keys

 

# Instructions

1. Use this command to list all the access keys for an IAM user.

 



**Code**: [[aws iam list-access-keys]]



> The 'aws iam list-access-keys' command is used to retrieve a list of all access keys associated with an IAM user. Access keys are used to make programmatic calls to AWS services. This command can be useful for auditing purposes or when troubleshooting issues related to access keys. The command takes no arguments and simply returns a JSON object containing the access key details such as the access key ID, status, and creation date.



**Command** ([[List IAM Access Keys]]):

```bash
aws iam list-access-keys
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files|T1552.001 - Credentials In Files]]
- [[Credentials in Registry|T1552.002 - Credentials in Registry]]

## Commands Used

- [[List IAM Access Keys]]

## Tags

- [[Cloud - AWS]]
- [[Listing IAM access Keys]]


