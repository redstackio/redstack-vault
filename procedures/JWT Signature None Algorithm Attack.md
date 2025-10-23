---
id: deab8dfc-20ce-431b-9d48-d6f1d488f488
name: JWT Signature None Algorithm Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.592746+00:00'
updated_at: '2023-04-10T20:22:37.274754+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
tags:
- '[[JWT - JSON Web Token]]'
- '[[JWT Signature]]'
- '[[JWT Signature - None Algorithm (CVE-2015-9235)]]'
---

# JWT Signature None Algorithm Attack

## Summary

The JSON Web Token (JWT) is a widely used method for representing claims securely between two parties. The signature of a JWT token is used to verify the authenticity of the token. The None algorithm is a reserved value indicating that no digital signature or MAC value is applied to the JWT. An att

## Description

# Description

The JSON Web Token (JWT) is a widely used method for representing claims securely between two parties. The signature of a JWT token is used to verify the authenticity of the token. The None algorithm is a reserved value indicating that no digital signature or MAC value is applied to the JWT. An attacker can exploit this vulnerability by tampering with the header of the JWT and changing the algorithm to 'none', which will allow them to bypass the signature verification process and gain unauthorized access to the application or system. The business impact of this attack can be severe as it can result in the compromise of sensitive data and systems.

 

## Requirements

1. Access to the JWT token

1. Knowledge of the vulnerability

1. Tampering tools

 

## Defense

1. Always use a strong algorithm for JWT signature verification

1. Implement proper input validation to prevent tampering with the JWT token

1. Monitor for any suspicious activity related to JWT tokens

 

## Objectives

1. To bypass the signature verification process of a JWT token

1. To gain unauthorized access to an application or system

 

# Instructions

1. 

 



**Code**: [[None]]



> 

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]

## Tags

- [[JWT - JSON Web Token]]
- [[JWT Signature]]
- [[JWT Signature - None Algorithm (CVE-2015-9235)]]


