---
id: 8bdd9ade-059b-40f8-930f-e22ac8355354
name: AWS Credential Testing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.690027+00:00'
updated_at: '2023-04-10T20:20:56.173241+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Cloud - AWS]]'
- '[[Persistence & Backdooring]]'
- '[[Testing the credential]]'
commands:
- '[[AWS STS Get Caller Identity]]'
---

# AWS Credential Testing

## Summary

The AWS Credential Testing procedure involves testing the validity of AWS credentials using the 'Get Caller Identity' command. This command returns metadata about the IAM user or role whose credentials were used to call the operation. An attacker can use this command to test the validity of stolen 

## Description

# Description

The AWS Credential Testing procedure involves testing the validity of AWS credentials using the 'Get Caller Identity' command. This command returns metadata about the IAM user or role whose credentials were used to call the operation. An attacker can use this command to test the validity of stolen or brute-forced credentials. If the command returns a valid response, the attacker can use the credentials to perform further actions on the AWS environment.

From a technical perspective, an attacker can use a script to automate the process of testing multiple credentials. This can be done by iterating through a list of credentials and using the 'Get Caller Identity' command to test each one. The output can then be parsed to identify valid credentials.

The business value of this procedure is that it allows an attacker to gain access to an AWS environment, which can lead to data theft, data destruction, or ransomware attacks.

 

## Requirements

1. Valid AWS credentials

1. Access to the AWS environment

 

## Defense

1. Use strong, unique passwords for AWS credentials

1. Enable multi-factor authentication for IAM users

1. Monitor AWS CloudTrail logs for suspicious activity

 

## Objectives

1. Test the validity of AWS credentials

1. Identify valid credentials for further exploitation

 

# Instructions

1. The 'aws sts get-caller-identity' command returns details about the IAM user or role whose credentials are used to call the command. This command does not accept any arguments.

 

This command is useful in situations where you need to verify the identity of the user or role that is currently authenticated. It can also be used to troubleshoot issues with IAM roles and policies. The '--profile' option is used to specify the profile to use from the AWS credentials file. If this option is not specified, the default profile will be used. It's important to note that a user can have a maximum of 2 access keys at any given time.



**Command** ([[AWS STS Get Caller Identity]]):

```bash
aws sts get-caller-identity --profile example_profile
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[AWS STS Get Caller Identity]]

## Tags

- [[5. Exploitation Scenario]]
- [[Cloud - AWS]]
- [[Persistence & Backdooring]]
- [[Testing the credential]]


