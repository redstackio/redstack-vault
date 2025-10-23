---
id: 3c0b1141-58b3-46ff-a737-2a060e4550c3
name: Enclosed Alphanumeric Server-Side Request Forgery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.562230+00:00'
updated_at: '2023-04-10T20:24:13.226637+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
- '[[File Deletion|T1107 - File Deletion]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using enclosed alphanumerics]]'
- '[[Server-Side Request Forgery]]'
---

# Enclosed Alphanumeric Server-Side Request Forgery

## Summary

Enclosed Alphanumeric Server-Side Request Forgery is a technique that allows an attacker to bypass filters implemented to prevent Server-Side Request Forgery (SSRF) attacks. In this technique, the attacker encloses the target URL within an alphanumeric string to bypass the filter. This technique wo

## Description

# Description

Enclosed Alphanumeric Server-Side Request Forgery is a technique that allows an attacker to bypass filters implemented to prevent Server-Side Request Forgery (SSRF) attacks. In this technique, the attacker encloses the target URL within an alphanumeric string to bypass the filter. This technique works because many filters only look for exact matches of blacklisted keywords or patterns. Enclosing the target URL within an alphanumeric string makes it difficult for the filter to detect the malicious URL. This technique can be used to exploit vulnerable web applications to perform unauthorized actions, such as accessing internal systems, exfiltrating data, or executing arbitrary commands.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the target URL to be accessed

 

## Defense

1. Implement input validation and sanitization to prevent SSRF attacks

1. Implement filters that look for encodings and obfuscation techniques

1. Monitor network traffic for suspicious activity, such as requests to internal systems

 

## Objectives

1. Exploit vulnerabilities in web applications to perform unauthorized actions

1. Access internal systems

1. Exfiltrate data

1. Execute arbitrary commands

 

# Instructions

1. To get the Twitter account link for a user, replace 'EdOverflow' with the desired Twitter username.

 



**Code**: [[http://example.com

List:
① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ]]



> This command provides a quick way to get the Twitter account link for a user. Simply replace 'EdOverflow' in the 'text' field with the desired Twitter username and run the command. The resulting link will be displayed in the 'data' field. The 'instruction' field provides clear guidance on how to use the command, and the 'explain' field provides additional context and details about the command.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]
- [[File Deletion|T1107 - File Deletion]]
- [[Remote File Copy|T1105 - Remote File Copy]]

## Tags

- [[Bypassing filters]]
- [[Bypass using enclosed alphanumerics]]
- [[Server-Side Request Forgery]]


