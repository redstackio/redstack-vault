---
id: 3838b234-5709-438b-8f59-58bd5246ace5
name: Dictionary Hash Cracking with Hashcat
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.566408+00:00'
updated_at: '2023-04-06T03:56:17.580162+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Two-Factor Authentication Interception|T1111 - Two-Factor Authentication Interception]]'
tags:
- '[[Dictionary]]'
- '[[Hashcat]]'
- '[[Hash Cracking]]'
---

# Dictionary Hash Cracking with Hashcat

## Summary

Dictionary hash cracking with Hashcat is a technique used to recover passwords from hashed values. This technique relies on the use of a pre-generated dictionary file containing a list of commonly used passwords, which is then compared against the hashed values until a match is found. This approach

## Description

# Description

Dictionary hash cracking with Hashcat is a technique used to recover passwords from hashed values. This technique relies on the use of a pre-generated dictionary file containing a list of commonly used passwords, which is then compared against the hashed values until a match is found. This approach can be effective against weak passwords and can be used in a variety of scenarios, such as post-exploitation or red teaming activities. Hashcat is a popular tool used for this purpose, as it supports a wide range of hash types and algorithms, and can be run on both CPUs and GPUs.

From a technical perspective, this technique works by taking the hashed value and comparing it against each entry in the dictionary file. If a match is found, the corresponding password is considered to be the correct one. This process can be time-consuming, as it involves iterating through a large number of entries in the dictionary file. However, it can be optimized by using techniques such as rule-based cracking, which involves applying various transformations to the entries in the dictionary file to generate new password candidates.

From a business perspective, this technique can be used to test the strength of an organization's password policies and identify weak passwords that could be exploited by attackers. It can also be used to recover lost or forgotten passwords, or to gain access to systems or applications where the password has been lost or forgotten.

## Requirements

1. Access to the hashed values

1. Access to a pre-generated dictionary file

1. Hashcat installed on the system

## Defense

1. Use strong passwords that are resistant to dictionary attacks

1. Implement multi-factor authentication to reduce the risk of password-based attacks

1. Monitor for suspicious activity, such as repeated failed login attempts

## Objectives

1. Recover passwords from hashed values

1. Test the strength of password policies

1. Identify weak passwords that could be exploited by attackers

1. Recover lost or forgotten passwords

1. Gain access to systems or applications where the password has been lost or forgotten

# Instructions

1. This command is used for brute force hash cracking. The command takes in a hash file and a wordlist file as input, and tries to crack the hash using various combinations of words from the wordlist file. The '-r' option specifies a rule file which can be used to modify the wordlist and create more complex combinations. The '--attack-mode 0' option specifies the brute force attack mode. The '--hash-type $number' option specifies the type of hash being cracked.

**Code**: [[hashcat --attack-mode 0 --hash-type $number $hashe]]

> The arguments of the command are:
1. $hashes_file: The file containing the hashes to be cracked.
2. $wordlist_file: The file containing the list of words to be used for cracking.
3. $my_rules: The rule file containing the rules to be applied to the wordlist for creating more complex combinations.
4. $number: The number representing the type of hash being cracked. This can be obtained from the hash file header or by using the '--help' option with hashcat.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Two-Factor Authentication Interception|T1111 - Two-Factor Authentication Interception]]

## Tags

- [[Dictionary]]
- [[Hashcat]]
- [[Hash Cracking]]
