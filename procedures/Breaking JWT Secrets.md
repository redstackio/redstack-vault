---
id: e81082fc-1af6-462a-9641-f746a4349f09
name: Breaking JWT Secrets
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.738950+00:00'
updated_at: '2023-04-10T20:22:35.234709+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Break JWT secret]]'
- '[[JWT - JSON Web Token]]'
- '[[JWT Secret]]'
commands:
- '[[Set JWT Secret]]'
---

# Breaking JWT Secrets

## Summary

JSON Web Tokens (JWTs) are commonly used for authentication and authorization purposes. The JWT contains a secret key that is used to verify its authenticity. An attacker may try to break the JWT secret to gain access to sensitive information or perform unauthorized actions. This procedure explains

## Description

# Description

JSON Web Tokens (JWTs) are commonly used for authentication and authorization purposes. The JWT contains a secret key that is used to verify its authenticity. An attacker may try to break the JWT secret to gain access to sensitive information or perform unauthorized actions. This procedure explains how to break a JWT secret using brute force.

Technical Explanation: An attacker can use a tool like John the Ripper or Hashcat to try different combinations of characters until the correct JWT secret is found. This is a time-consuming process, but it can be automated to increase the chances of success. Once the attacker has the JWT secret, they can generate their own JWTs and impersonate a legitimate user.

Business Value: An attacker who successfully breaks a JWT secret can gain access to sensitive information or perform unauthorized actions, such as modifying user data or accessing restricted resources.

 

## Requirements

1. Access to the JWT that needs to be broken.

1. A tool like John the Ripper or Hashcat to perform the brute force attack.

 

## Defense

1. Use a strong and complex JWT secret.

1. Implement rate limiting or other measures to detect and prevent brute force attacks.

1. Monitor JWT usage and revoke any suspicious or unauthorized tokens.

 

## Objectives

1. To break the JWT secret and gain access to sensitive information or perform unauthorized actions.

1. To generate a new JWT using the stolen secret and impersonate a legitimate user.

 

# Instructions

1. Set the JWT secret to the one that needs to be broken.

 



**Code**: [[your_jwt_secret]]



> 



**Command** ([[Set JWT Secret]]):

```bash
your_jwt_secret
```



2. Use a tool like John the Ripper or Hashcat to perform a brute force attack on the JWT secret.

 



**Code**: [[change_this_super_secret_random_string]]



> The tool will try different combinations of characters until the correct JWT secret is found. The length and complexity of the secret will affect the time it takes to find it. Once the secret is found, the attacker can generate their own JWTs and impersonate a legitimate user.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Set JWT Secret]]

## Tags

- [[Break JWT secret]]
- [[JWT - JSON Web Token]]
- [[JWT Secret]]


