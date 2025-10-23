---
id: da62c60d-16b3-4608-a9b5-1fcf574415ab
name: PHP Magic Hashes Juggling Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.736533+00:00'
updated_at: '2023-04-06T03:56:40.748832+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Example vulnerable code]]'
- '[[PHP Juggling type and magic hashes]]'
- '[[Type Juggling]]'
---

# PHP Magic Hashes Juggling Attack

## Summary

The PHP Magic Hashes Juggling Attack is a technique that exploits the PHP type juggling vulnerability in order to bypass authentication mechanisms. This attack is possible because PHP uses loose comparison operators, which can be manipulated by an attacker to coerce a string into a different data t

## Description

# Description

The PHP Magic Hashes Juggling Attack is a technique that exploits the PHP type juggling vulnerability in order to bypass authentication mechanisms. This attack is possible because PHP uses loose comparison operators, which can be manipulated by an attacker to coerce a string into a different data type. By using specially crafted input, an attacker can bypass authentication mechanisms that rely on string comparisons. This technique can be used to gain access to sensitive information or to execute unauthorized actions on a system.

Technical Explanation: This attack takes advantage of the way PHP handles type conversion. In PHP, the == operator compares two values, and if they are not of the same type, PHP will attempt to convert them to the same type. This can lead to unexpected results, as certain values can be converted to other types in unexpected ways. For example, the string '0e1234' will be converted to the float 0.0, which can be used to bypass certain authentication mechanisms that rely on string comparisons.

Business Value: This attack can be used to gain unauthorized access to sensitive information or to execute unauthorized actions on a system. By bypassing authentication mechanisms, an attacker can gain access to user accounts, financial data, or other sensitive information. This can lead to data breaches, financial losses, and damage to a company's reputation.

 

## Requirements

1. Access to a vulnerable PHP application

 

## Defense

1. Ensure that all input is properly validated and sanitized

1. Use strict comparison operators (=== and !==) instead of loose comparison operators (== and !=)

1. Keep PHP up to date with the latest security patches and updates

 

## Objectives

1. Bypass authentication mechanisms

1. Gain unauthorized access to sensitive information

1. Execute unauthorized actions on a system

 

# Instructions

1. The hash_hmac command is used to generate a keyed hash value using the HMAC method. The command takes two arguments: the first argument is the key to use for the HMAC hash, and the second argument is the data to be hashed. In the provided example, the key is 'admin' and the data is a timestamp. The command generates a hash value for each timestamp value provided.

 



**Code**: [[hash_hmac(admin|1424869663) -> "e716865d1953e31049]]



> The hash_hmac command is commonly used for message authentication and integrity checking. It is a secure way to verify that a message has not been tampered with or altered in any way. The command uses a secret key to generate a unique hash value for each message, and the receiver can verify the integrity of the message by comparing the hash value they receive to the expected hash value.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Example vulnerable code]]
- [[PHP Juggling type and magic hashes]]
- [[Type Juggling]]


