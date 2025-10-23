---
id: 30e1c192-d4dc-4eda-8230-1a3275962777
name: Exotic Payloads for Bypassing Email Filters
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.636755+00:00'
updated_at: '2023-04-10T20:21:50.226603+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Bypass email filter]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Exotic Payloads for Bypassing Email Filters

## Summary

Exotic payloads can be used to bypass email filters and deliver malicious payloads. By using obfuscated files or information, attackers can evade detection and deliver payloads that can exploit cross-site scripting vulnerabilities. These payloads can be used to steal sensitive information, spread m

## Description

# Description

Exotic payloads can be used to bypass email filters and deliver malicious payloads. By using obfuscated files or information, attackers can evade detection and deliver payloads that can exploit cross-site scripting vulnerabilities. These payloads can be used to steal sensitive information, spread malware, and launch other types of attacks. Businesses should be aware of the risks associated with email filters and take steps to mitigate these risks.

 

## Requirements

1. Access to email system

1. Knowledge of email filter bypass techniques

 

## Defense

1. Implement strict email filtering policies

1. Train employees on email security best practices

1. Regularly update and patch email systems

 

## Objectives

1. Deliver malicious payloads via email

1. Exploit cross-site scripting vulnerabilities

1. Evade email filters and detection mechanisms

 

# Instructions

1. Use this command to validate the format of an email address. The command takes an email address as an argument and returns either true or false depending on whether the format is valid or not.

 



**Code**: [["><svg/onload=confirm(1)>"@x.y]]



> The email address should be in the standard format of local-part@domain, where the local-part can contain letters, digits, and special characters like !#$%&'*+-/=?^_`{|}~. The domain should be a valid domain name consisting of letters, digits, and hyphens, separated by periods. The domain must also have at least one period and cannot start or end with a hyphen. If the email address is valid, the command will return true. Otherwise, it will return false.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Data Obfuscation|T1001 - Data Obfuscation]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Bypass email filter]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


