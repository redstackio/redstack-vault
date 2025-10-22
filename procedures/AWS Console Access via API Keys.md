---
id: 7b99933a-748e-404c-9923-ec22b8c563cf
name: AWS Console Access via API Keys
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.467624+00:00'
updated_at: '2023-04-10T20:20:55.843316+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[AWS - Gaining AWS Console Access via API Keys]]'
- '[[Cloud - AWS]]'
commands:
- '[[Clone aws_consoler from GitHub]]'
- '[[Run aws_consoler with provided arguments]]'
---

# AWS Console Access via API Keys

## Summary

This procedure involves gaining access to an AWS console via API keys. By obtaining these keys, an attacker can bypass traditional authentication methods and gain access to the console. Once access is gained, an attacker can perform a variety of actions including creating, modifying, or deleting re

## Description

# Description

This procedure involves gaining access to an AWS console via API keys. By obtaining these keys, an attacker can bypass traditional authentication methods and gain access to the console. Once access is gained, an attacker can perform a variety of actions including creating, modifying, or deleting resources within the AWS environment. This attack can be executed remotely and can be difficult to detect as it appears to be a legitimate user accessing the console.

To execute this attack, an attacker first needs to obtain valid API keys. This can be done by compromising an AWS access key or secret access key. Once the keys are obtained, the attacker can use them to authenticate with the AWS console and gain access to the environment.

The business value of this procedure is that it allows attackers to gain access to sensitive data and resources within an AWS environment. This can result in data theft, resource modification or destruction, and ultimately financial loss for the victim organization.

## Requirements

1. Valid AWS API keys

## Defense

1. Ensure that AWS access keys and secret access keys are properly secured and not easily accessible

1. Implement multi-factor authentication for AWS console access

1. Monitor AWS console access logs for suspicious activity

## Objectives

1. Gain access to an AWS console via API keys

1. Perform actions within the AWS environment such as modifying or deleting resources

# Instructions

1. To use AWS Consoler, first clone the repository and then run the command with the appropriate arguments. The -a flag is used to specify the access key ID and the -s flag is used to specify the secret access key. Once the command has been run, a URL will be generated that can be used to access the AWS console.

**Code**: [[$> git clone https://github.com/NetSPI/aws_console]]

> AWS Consoler is a command line utility that allows you to convert your AWS CLI credentials into AWS console access. This can be useful if you prefer to use the console for some tasks rather than the CLI. The command requires you to specify your access key ID and secret access key as arguments. Once the command has been run, a URL will be generated that can be used to access the AWS console. The URL will be valid for a limited time and can be used to log in to the console without having to enter your credentials again.

**Command** ([[Clone aws_consoler from GitHub]]):

```bash
$> git clone https://github.com/NetSPI/aws_consoler
```

**Command** ([[Run aws_consoler with provided arguments]]):

```bash
$> aws_consoler -v -a AKIA[REDACTED] -s [REDACTED]
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]
- [[Valid Accounts|T1078 - Valid Accounts]]

### Sub-Techniques

- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[Clone aws_consoler from GitHub]]
- [[Run aws_consoler with provided arguments]]

## Tags

- [[AWS - Gaining AWS Console Access via API Keys]]
- [[Cloud - AWS]]
