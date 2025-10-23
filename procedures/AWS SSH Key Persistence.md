---
id: 5bbd719a-bd1b-4077-8b30-0b0c45422084
name: AWS SSH Key Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.626536+00:00'
updated_at: '2023-04-10T20:20:00.587475+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Install Root Certificate|T1130 - Install Root Certificate]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Persistence]]'
- '[[SSH Persistence example]]'
commands:
- '[[Generate SSH Key Pair]]'
---

# AWS SSH Key Persistence

## Summary

AWS SSH Key Persistence is a technique used by attackers to maintain access to an AWS instance. The attacker generates an SSH key pair and adds the public key to the authorized_keys file on the target instance. This allows the attacker to authenticate as the user associated with the private key and

## Description

# Description

AWS SSH Key Persistence is a technique used by attackers to maintain access to an AWS instance. The attacker generates an SSH key pair and adds the public key to the authorized_keys file on the target instance. This allows the attacker to authenticate as the user associated with the private key and maintain access even if the instance is terminated and a new one is launched in its place. This technique can be used to maintain persistence in an AWS environment and can be difficult to detect and remediate.

From a technical perspective, an attacker can generate an SSH key pair using the SSH Key Generation command. The attacker can then add the public key to the authorized_keys file on the target instance using SSH or a tool like Terraform. Once the key is added, the attacker can authenticate to the instance using the associated private key.

From a business value perspective, an attacker can use this technique to maintain access to an AWS environment even if the organization terminates or replaces instances. This can allow the attacker to steal data, install malware, or further pivot within the environment.

 

## Requirements

1. Access to an AWS instance

1. Ability to generate SSH key pair

1. Ability to add public key to authorized_keys file

 

## Defense

1. Regularly review authorized_keys file for unauthorized keys

1. Implement multi-factor authentication for SSH access

1. Monitor SSH logs for suspicious activity

 

## Objectives

1. Maintain access to an AWS instance

1. Maintain persistence in an AWS environment

 

# Instructions

1. The ssh-keygen command is used to generate a new SSH key pair. By default, the command generates a 2048-bit RSA key pair, which is secure enough for most use cases. However, you can customize the key type, size, and other parameters using command-line options.

 

The ssh-keygen command takes several arguments, including the path to the file where you want to save the key pair, the type of key to generate (RSA, DSA, ECDSA, or ED25519), and the size of the key (in bits). You can also specify a passphrase to protect the private key, or use an existing key as a template for the new one. Once the key pair is generated, you can use it to authenticate with remote servers using the SSH protocol.



**Command** ([[Generate SSH Key Pair]]):

```bash
ssh-keygen
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Install Root Certificate|T1130 - Install Root Certificate]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Generate SSH Key Pair]]

## Tags

- [[Cloud - AWS]]
- [[Exploitation]]
- [[Persistence]]
- [[SSH Persistence example]]


