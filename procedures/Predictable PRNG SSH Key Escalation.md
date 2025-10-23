---
id: e791e589-cee1-46c7-b9c4-7af5504cd4ff
name: Predictable PRNG SSH Key Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.605587+00:00'
updated_at: '2023-04-10T20:34:28.983556+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[SSH Key]]'
- '[[SSH Key Predictable PRNG (Authorized_Keys) Process]]'
---

# Predictable PRNG SSH Key Escalation

## Summary

The Predictable PRNG SSH Key Escalation technique is a method of escalating privileges on a Linux system by exploiting a predictable random number generator (PRNG) used in the creation of SSH keys. This technique involves manipulating the authorized_keys file, which contains public keys that are al

## Description

# Description

The Predictable PRNG SSH Key Escalation technique is a method of escalating privileges on a Linux system by exploiting a predictable random number generator (PRNG) used in the creation of SSH keys. This technique involves manipulating the authorized_keys file, which contains public keys that are allowed to connect to a user's account via SSH. By replacing a legitimate public key with a malicious one, an attacker can gain access to the system as the user whose key was replaced.

To carry out this technique, an attacker must first gain access to a user's account on the target system. They can then generate a new SSH key pair using a predictable PRNG, such as one that uses the current time as a seed. The attacker can then add the public key to the authorized_keys file, replacing the legitimate key of the target user. When the user next logs in via SSH, the attacker's key will be used instead, granting them access to the system as the target user.

This technique can be used to escalate privileges on a compromised system, allowing an attacker to move laterally through the network and access sensitive data.

 

## Requirements

1. Access to a user's account on the target system

1. Ability to generate a new SSH key pair using a predictable PRNG

1. Ability to modify the authorized_keys file

 

## Defense

1. Use a strong PRNG when generating SSH keys

1. Regularly monitor the authorized_keys file for unauthorized changes

1. Implement two-factor authentication for SSH access

 

## Objectives

1. Gain elevated privileges on a Linux system

1. Access sensitive data on a compromised system

1. Move laterally through a network

 

# Instructions

1. To use authorized keys for SSH access, follow these steps:
1. Obtain the authorized_keys file for the user you wish to access.
2. Copy the authorized_keys file to your local machine.
3. Use a text editor to open the file and copy the contents.
4. On your local machine, open the SSH configuration file (/etc/ssh/ssh_config or ~/.ssh/config) and add the following lines:

Host <hostname>
    IdentityFile <path/to/authorized_keys/file>

5. Save the SSH configuration file.
6. Use the SSH command to connect to the remote host:

ssh <username>@<hostname>

 



**Code**: [[ssh-dss AAAA487rt384ufrgh432087fhy02nv84u7fg839247]]



> The authorized_keys file contains public keys that are authorized for SSH access. By copying this file to your local machine and adding it to your SSH configuration file, you can use the private key associated with the public key to authenticate with the remote host. This method of authentication is more secure than using a password, as it requires possession of the private key.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Linux - Privilege Escalation]]
- [[SSH Key]]
- [[SSH Key Predictable PRNG (Authorized_Keys) Process]]


