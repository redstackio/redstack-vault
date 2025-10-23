---
id: 3df35023-6a80-4112-bef0-84874c2924a9
name: AWS Account ID Retrieval with STS Get Caller Identity
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.433316+00:00'
updated_at: '2023-04-10T20:20:26.434663+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Privilege Escalation]]'
- '[[Study Case]]'
commands:
- '[[AWS STS Get Caller Identity]]'
---

# AWS Account ID Retrieval with STS Get Caller Identity

## Summary

This procedure involves using the AWS Security Token Service (STS) Get Caller Identity API to retrieve the AWS account ID of the current user. This information can be useful for an attacker who has already gained access to an AWS instance or service and wants to escalate their privileges to gain ac

## Description

# Description

This procedure involves using the AWS Security Token Service (STS) Get Caller Identity API to retrieve the AWS account ID of the current user. This information can be useful for an attacker who has already gained access to an AWS instance or service and wants to escalate their privileges to gain access to additional resources. By retrieving the AWS account ID, the attacker can determine the level of access they have and plan their next steps accordingly.

Technical Explanation: The STS Get Caller Identity API returns details about the IAM user or role whose credentials are used to call the API. This includes the AWS account ID, which is a unique identifier for the AWS account that the user or role belongs to. An attacker can use this API to retrieve the AWS account ID of the current user and use it to escalate their privileges.

Business Value: An attacker who successfully escalates their privileges in an AWS environment can gain access to sensitive data and resources, potentially causing significant damage to the business.

 

## Requirements

1. Valid AWS credentials for the current user

1. Access to the AWS Security Token Service (STS) Get Caller Identity API

 

## Defense

1. Use strong authentication measures, such as multi-factor authentication (MFA), to prevent unauthorized access to AWS credentials

1. Monitor AWS API calls for suspicious activity, such as repeated calls to the STS Get Caller Identity API

1. Implement least privilege access controls to limit the impact of privilege escalation attacks

 

## Objectives

1. Retrieve the AWS account ID of the current user

1. Determine the level of access the attacker has

1. Plan next steps for escalating privileges

 

# Instructions

1. To retrieve the AWS Account ID using the STS Get Caller Identity command, follow these steps:

1. Open the AWS CLI on your local machine.
2. Type 'aws sts get-caller-identity' and press Enter.
3. The command will return the Account ID associated with the credentials used to make the call.

 

The 'aws sts get-caller-identity' command is used to retrieve information about the AWS account that is associated with the credentials used to make the call. This command returns the AWS Account ID, the Amazon Resource Name (ARN) of the IAM role or user making the call, and the unique identifier of the AWS account that owns the resource specified in the ARN. This command is useful for verifying that you are using the correct AWS account and for troubleshooting issues related to permissions and access to AWS resources.



**Command** ([[AWS STS Get Caller Identity]]):

```bash
aws sts get-caller-identity
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[AWS STS Get Caller Identity]]

## Tags

- [[5. Exploitation Scenario]]
- [[Cloud - AWS]]
- [[Exploitation]]
- [[Privilege Escalation]]
- [[Study Case]]


