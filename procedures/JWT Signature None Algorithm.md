---
id: bd1674a7-7e24-45cb-a4e4-17db5df0a9e4
name: JWT Signature None Algorithm
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.614196+00:00'
updated_at: '2023-04-10T20:22:35.963511+00:00'
tags:
- '[[JWT - JSON Web Token]]'
- '[[JWT Signature]]'
- '[[JWT Signature - None Algorithm (CVE-2015-9235)]]'
commands:
- '[[Decode JWT with JWT Tool]]'
---

# JWT Signature None Algorithm

## Summary

JWT (JSON Web Token) is a widely used standard for token-based authentication and authorization. One of the most critical components of a JWT is the signature, which is used to verify the integrity and authenticity of the token. However, in some cases, the JWT signature algorithm is set to 'None', 

## Description

# Description

JWT (JSON Web Token) is a widely used standard for token-based authentication and authorization. One of the most critical components of a JWT is the signature, which is used to verify the integrity and authenticity of the token. However, in some cases, the JWT signature algorithm is set to 'None', which means that the token is not signed at all. This vulnerability, known as CVE-2015-9235, allows an attacker to modify the contents of the JWT without being detected.

An attacker can exploit this vulnerability to bypass authentication and gain unauthorized access to protected resources. The attacker can modify the claims in the JWT, such as the user ID, and impersonate another user. This can lead to a variety of attacks, such as privilege escalation, data theft, and lateral movement. Business value of this attack is that it can be used to bypass authentication and gain unauthorized access to sensitive data.

## Requirements

1. Access to the JWT token

1. Ability to modify the contents of the token

1. Knowledge of the vulnerability

## Defense

1. Always use a secure JWT signature algorithm, such as HMAC-SHA256 or RSA-SHA256.

1. Monitor the use of JWT tokens and look for any suspicious activity, such as tokens with the 'None' algorithm.

1. Regularly update and patch any software that uses JWT tokens to prevent known vulnerabilities, such as CVE-2015-9235.

## Objectives

1. Bypass authentication and gain unauthorized access to protected resources

1. Modify the contents of the JWT without being detected

1. Impersonate another user

# Instructions

1. Use the jwt_tool to decode the JWT token.

**Code**: [[python3 jwt_tool.py [JWT_HERE] -X a]]

> This command will decode the JWT token and display its contents in a human-readable format.

**Command** ([[Decode JWT with JWT Tool]]):

```bash
python3 jwt_tool.py [JWT_HERE] -X a
```

2. Use this code to manually modify the JWT token.

**Code**: [[import jwt

jwtToken = 'eyJhbGciOiJIUzI1NiIsInR5cC]]

> This command will decode the JWT token, modify its contents, and then re-encode it with the 'None' algorithm. This will create a new JWT token that is not signed and can be used by an attacker to bypass authentication.

## Commands Used

- [[Decode JWT with JWT Tool]]

## Tags

- [[JWT - JSON Web Token]]
- [[JWT Signature]]
- [[JWT Signature - None Algorithm (CVE-2015-9235)]]
