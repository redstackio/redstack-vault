---
id: 902c8599-29e4-41bc-9084-74c9fcde04ae
name: AWS Credential Export
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.932325+00:00'
updated_at: '2023-04-10T20:19:53.671950+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Accessing more credentials]]'
- '[[Cloud - AWS]]'
- '[[Configuring AWS cli with newer credentials (On Linux)]]'
- '[[Persistence & Backdooring]]'
commands:
- '[[Export AWS credentials]]'
---

# AWS Credential Export

## Summary

The AWS Credential Export procedure is used to gain access to more AWS credentials by configuring the AWS CLI with newer credentials. This procedure is useful for attackers who already have some AWS credentials but want to escalate their privileges and gain access to more sensitive data. To execute

## Description

# Description

The AWS Credential Export procedure is used to gain access to more AWS credentials by configuring the AWS CLI with newer credentials. This procedure is useful for attackers who already have some AWS credentials but want to escalate their privileges and gain access to more sensitive data. To execute this procedure, the attacker needs to export the newly obtained credentials and configure them in the AWS CLI. Once configured, the attacker can use these credentials to access different AWS services and data.

## Requirements

1. Valid AWS credentials

1. Access to a Linux machine

## Defense

1. Ensure that AWS credentials are stored securely and not easily accessible

1. Implement multi-factor authentication to prevent unauthorized access to AWS accounts

1. Regularly monitor and review AWS account activity for any suspicious behavior

## Objectives

1. Gain access to more AWS credentials

1. Escalate privileges

1. Access sensitive data

# Instructions

1. To export your AWS credentials, execute the following commands:

This command exports the AWS access key, secret key, and session token into the environment variables of your current shell. These credentials are required to authenticate AWS CLI commands and SDK calls to AWS services.

**Command** ([[Export AWS credentials]]):

```bash
export AWS_ACCESS_KEY_ID
export AWS_SECRET_KEY
export AWS_SESSION_TOKEN
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[Export AWS credentials]]

## Tags

- [[5. Exploitation Scenario]]
- [[Accessing more credentials]]
- [[Cloud - AWS]]
- [[Configuring AWS cli with newer credentials (On Linux)]]
- [[Persistence & Backdooring]]
