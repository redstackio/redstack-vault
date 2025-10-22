---
id: 1f665aaa-0155-4968-bd8c-fb7466b4f3bf
name: Active Directory Man-in-the-Middle and Password Cracking
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.308708+00:00'
updated_at: '2023-04-10T20:25:44.757110+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Man-in-the-Middle attacks & relaying]]'
commands:
- '[[Crack Password Hashes with Hashcat]]'
- '[[Hashcat Installation]]'
---

# Active Directory Man-in-the-Middle and Password Cracking

## Summary

Active Directory Man-in-the-Middle and Password Cracking is a technique used to obtain credentials for a target user account. This procedure involves relaying authentication requests to a target system, allowing an attacker to intercept authentication attempts and capture the user's password hash. 

## Description

# Description

Active Directory Man-in-the-Middle and Password Cracking is a technique used to obtain credentials for a target user account. This procedure involves relaying authentication requests to a target system, allowing an attacker to intercept authentication attempts and capture the user's password hash. The password hash can then be cracked using tools like Hashcat to reveal the plaintext password. This attack can be used to escalate privileges or gain access to sensitive information.

From a technical perspective, this attack exploits the way Windows systems authenticate users. When a user logs in, their password is hashed and sent to the domain controller for verification. By relaying this authentication request to another system, an attacker can intercept the hashed password and use it to authenticate to other systems within the domain. This attack can be particularly effective when combined with other techniques like Pass the Ticket, which allows an attacker to authenticate to a target system using a Kerberos ticket.

From a business perspective, this attack can be used to gain access to sensitive information or systems within an organization. It is particularly effective against organizations that rely heavily on Active Directory for authentication and authorization.

## Requirements

1. Access to a system on the target network that can be used for relaying authentication requests

1. Tools like Hashcat for cracking password hashes

## Defense

1. Implementing two-factor authentication can help prevent this type of attack

1. Enforcing strong password policies can make cracking password hashes more difficult

1. Monitoring network traffic for signs of relaying attacks can help detect and mitigate this type of attack

## Objectives

1. Obtain credentials for a target user account

1. Escalate privileges

1. Gain access to sensitive information or systems within an organization

# Instructions

1. To use hashcat, you need to provide the hash file and the wordlist file. The hash file contains the hashed password(s) you want to crack, while the wordlist file contains a list of words that will be used to guess the password. You can also use rules to modify the words in the wordlist to increase your chances of success. The basic syntax is as follows: hashcat [options] hashfile wordlist

**Code**: [[hashcat]]

> The arguments for hashcat are as follows:

-hashfile : The file containing the hashed password(s) you want to crack.

-wordlist : The file containing the list of words that will be used to guess the password.

-options : Various options that can be used to modify the behavior of hashcat, such as the type of hash, the type of attack, the use of rules, etc.

**Command** ([[Hashcat Installation]]):

```bash
sudo apt-get install hashcat
```

2. To crack password hashes using Hashcat, use the following command:

**Code**: [[hashcat -m 5600 -a 0 hash.txt crackstation.txt]]

> -m 5600: specifies the hash type to be cracked
-a 0: specifies the attack mode (0 for straight)
hash.txt: the file containing the password hashes
crackstation.txt: the wordlist file used for cracking the hashes

**Command** ([[Crack Password Hashes with Hashcat]]):

```bash
hashcat -m 5600 -a 0 hash.txt crackstation.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Crack Password Hashes with Hashcat]]
- [[Hashcat Installation]]

## Tags

- [[Active Directory Attacks]]
- [[Man-in-the-Middle attacks & relaying]]
