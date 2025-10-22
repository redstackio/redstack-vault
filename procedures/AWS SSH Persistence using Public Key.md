---
id: 6e925707-c166-4217-85ed-c8c853d6417c
name: AWS SSH Persistence using Public Key
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.680892+00:00'
updated_at: '2023-04-10T20:20:29.899593+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Install Root Certificate|T1130 - Install Root Certificate]]'
tags:
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Persistence]]'
- '[[SSH Persistence example]]'
commands:
- '[[SSH into instance]]'
---

# AWS SSH Persistence using Public Key

## Summary

AWS SSH Persistence using Public Key is a technique used to maintain access to an AWS instance by adding a public key to the authorized_keys file. This technique can be used by an attacker to ensure that they can regain access to the instance even if the original credentials have been changed or re

## Description

# Description

AWS SSH Persistence using Public Key is a technique used to maintain access to an AWS instance by adding a public key to the authorized_keys file. This technique can be used by an attacker to ensure that they can regain access to the instance even if the original credentials have been changed or removed. The attacker can use this technique to maintain persistence on the instance and continue to exfiltrate data or perform other malicious activities.

To use this technique, the attacker must have access to the AWS instance and the ability to modify the authorized_keys file. This can be accomplished through a variety of means, including exploiting vulnerabilities in the instance or stealing credentials. Once the attacker has access, they can add their own public key to the authorized_keys file, allowing them to access the instance using their own private key.

This technique can be valuable for an attacker who wants to maintain long-term access to an AWS instance and continue to exfiltrate data or perform other malicious activities.

## Requirements

1. Access to an AWS instance

1. Ability to modify the authorized_keys file

## Defense

1. Limit access to AWS instances to only trusted individuals

1. Monitor authorized_keys file for unexpected changes

1. Implement multi-factor authentication to prevent unauthorized access

## Objectives

1. Maintain access to an AWS instance

1. Ensure access to the instance even if credentials are changed or removed

1. Exfiltrate data or perform other malicious activities

# Instructions

1. To SSH into an instance using a public key, use the following command:

The SSH command is used to securely connect to a remote server. In this case, we are using a public key to authenticate the connection instead of a password. The -i flag specifies the location of the public key file. The user@instance argument specifies the username and IP address or hostname of the instance you want to connect to.

**Command** ([[SSH into instance]]):

```bash
ssh -i public_key user@instance
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Install Root Certificate|T1130 - Install Root Certificate]]

## Commands Used

- [[SSH into instance]]

## Tags

- [[Cloud - AWS]]
- [[Exploitation]]
- [[Persistence]]
- [[SSH Persistence example]]
