---
id: dc7ffca2-360c-4736-8254-a5b742ae9a54
name: AWS SSH Persistence with Authorized Keys
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.652166+00:00'
updated_at: '2023-04-10T20:20:48.483307+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Create or Modify System Process|T1543 - Create or Modify System Process]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
- '[[Domain Accounts|T1078.002 - Domain Accounts]]'
- '[[Windows Service|T1543.003 - Windows Service]]'
tags:
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Persistence]]'
- '[[SSH Persistence example]]'
commands:
- '[[Add public key to authorized keys]]'
---

# AWS SSH Persistence with Authorized Keys

## Summary

AWS SSH Persistence with Authorized Keys is a technique used by attackers to maintain access to a compromised AWS instance. By adding a public key to the SSH authorized keys file, an attacker can gain persistent access to the instance even after the original access has been revoked. This technique 

## Description

# Description

AWS SSH Persistence with Authorized Keys is a technique used by attackers to maintain access to a compromised AWS instance. By adding a public key to the SSH authorized keys file, an attacker can gain persistent access to the instance even after the original access has been revoked. This technique is particularly useful for maintaining access in situations where the attacker does not have access to the original credentials.

## Requirements

1. Access to an AWS instance

1. Ability to add a public key to the SSH authorized keys file

## Defense

1. Regularly review and remove unauthorized public keys from the SSH authorized keys file

1. Implement multi-factor authentication for SSH access to AWS instances

1. Monitor access logs for unusual activity, such as multiple failed login attempts

## Objectives

1. Maintain persistent access to an AWS instance

1. Maintain access even after the original access has been revoked

# Instructions

1. To add a public key to the authorized keys file, use the following command:

The 'echo' command is used to write the public key to the end of the authorized keys file. The '>>' operator is used to append the output of the 'echo' command to the end of the file. The file path '/home/user/.ssh/authorized_keys' specifies the location of the authorized keys file. Replace 'PUBLIC_Key' with the actual public key you want to add.

**Command** ([[Add public key to authorized keys]]):

```bash
echo "PUBLIC_Key" >> /home/user/.ssh/authorized_keys
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Create or Modify System Process|T1543 - Create or Modify System Process]]
- [[Valid Accounts|T1078 - Valid Accounts]]

### Sub-Techniques

- [[Domain Accounts|T1078.002 - Domain Accounts]]
- [[Windows Service|T1543.003 - Windows Service]]

## Commands Used

- [[Add public key to authorized keys]]

## Tags

- [[Cloud - AWS]]
- [[Exploitation]]
- [[Persistence]]
- [[SSH Persistence example]]
