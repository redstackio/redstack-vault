---
id: 17298077-c776-4b90-ba99-638c6158df6d
name: Github API Key Leakage
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:52.246442+00:00'
updated_at: '2023-04-06T03:55:52.282457+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Credentials in Registry|T1214 - Credentials in Registry]]'
tags:
- '[[API Key Leaks]]'
- '[[Exploit]]'
- '[[Github client id and client secret]]'
commands:
- '[[Send Request to GitHub API]]'
---

# Github API Key Leakage

## Summary

Github API Key Leakage is an attack that exploits Github's client id and client secret. Client ID and secret are used for authenticating a user or application. Attackers can obtain these keys by exploiting code vulnerabilities or through social engineering attacks. Once an attacker has these keys, 

## Description

# Description

Github API Key Leakage is an attack that exploits Github's client id and client secret. Client ID and secret are used for authenticating a user or application. Attackers can obtain these keys by exploiting code vulnerabilities or through social engineering attacks. Once an attacker has these keys, they can access sensitive data, manipulate repositories, and perform other malicious activities. This attack can be used to gain access to confidential information and intellectual property, and can also be used for ransomware attacks and data breaches.

 

## Requirements

1. Access to the target's Github account

1. Knowledge of the target's Github client id and client secret

 

## Defense

1. Regularly monitor Github accounts for unusual activity

1. Implement two-factor authentication for Github accounts

1. Rotate Github client id and client secret regularly

 

## Objectives

1. To obtain Github client id and client secret

1. To gain access to sensitive data and intellectual property

1. To manipulate repositories and perform other malicious activities

 

# Instructions

1. Run the following command in the terminal:

 



**Code**: [[curl 'https://api.github.com/users/whatever?client]]



> This command makes a request to the Github API using the target's client id and client secret. If the request is successful, it will return information about the target's Github account, including the client id and client secret. The attacker can then use these keys to gain access to sensitive data and perform malicious activities.



**Command** ([[Send Request to GitHub API]]):

```bash
curl 'https://api.github.com/users/whatever?client_id=xxxx&client_secret=yyyy'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Credentials in Registry|T1214 - Credentials in Registry]]

## Commands Used

- [[Send Request to GitHub API]]

## Tags

- [[API Key Leaks]]
- [[Exploit]]
- [[Github client id and client secret]]


