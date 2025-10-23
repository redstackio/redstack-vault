---
id: 929d1942-4196-4035-b124-fdb69d785f6f
name: AWS Temporary Credential Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.959307+00:00'
updated_at: '2023-04-10T20:19:57.210492+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Accessing more credentials]]'
- '[[Cloud - AWS]]'
- '[[Getting information about the temporary credential]]'
- '[[Persistence & Backdooring]]'
commands:
- '[[AWS STS Get Caller Identity]]'
---

# AWS Temporary Credential Information Gathering

## Summary

The AWS Temporary Credential Information Gathering procedure is used to obtain information about the temporary credentials that are created when an AWS instance is launched. This information can be used to escalate privileges and gain access to additional resources within the AWS environment. 

Tec

## Description

# Description

The AWS Temporary Credential Information Gathering procedure is used to obtain information about the temporary credentials that are created when an AWS instance is launched. This information can be used to escalate privileges and gain access to additional resources within the AWS environment. 

Technical Description: Temporary credentials are dynamically created by AWS when an instance is launched. These credentials are used to access other AWS services and can be used to escalate privileges if obtained by an attacker. This procedure is used to gather information about these temporary credentials. 

Business Value: By gaining access to additional resources within an AWS environment, an attacker can steal sensitive data, disrupt business operations, and cause reputational damage.

 

## Requirements

1. Valid AWS credentials

1. Access to an AWS instance

 

## Defense

1. Implement least privilege access controls to limit the damage an attacker can do if they obtain temporary AWS credentials

1. Monitor AWS logs for any suspicious activity related to temporary credentials

1. Rotate temporary credentials frequently to limit the window of opportunity for attackers

 

## Objectives

1. Gather information about temporary AWS credentials

1. Escalate privileges within the AWS environment

 

# Instructions

1. Use the AWS CLI to retrieve the account identity of the current IAM user or role.

 



**Code**: [[aws sts get-caller-identity]]



> The 'aws sts get-caller-identity' command returns information about the AWS account that is associated with the credentials used to call the command. This includes the AWS account ID, the Amazon Resource Name (ARN) of the IAM entity that called the command, and the AWS region that the credentials are configured to use. This command is useful for verifying that your credentials are correctly configured and that you are calling AWS services with the intended permissions.



**Command** ([[AWS STS Get Caller Identity]]):

```bash
aws sts get-caller-identity
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[AWS STS Get Caller Identity]]

## Tags

- [[5. Exploitation Scenario]]
- [[Accessing more credentials]]
- [[Cloud - AWS]]
- [[Getting information about the temporary credential]]
- [[Persistence & Backdooring]]


