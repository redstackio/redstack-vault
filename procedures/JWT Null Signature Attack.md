---
id: 027738f8-fe16-46bd-80ab-0e1bb0829624
name: JWT Null Signature Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.546134+00:00'
updated_at: '2023-04-10T20:22:35.598929+00:00'
tags:
- '[[JWT - JSON Web Token]]'
- '[[JWT Signature]]'
- '[[JWT Signature - Null Signature Attack (CVE-2020-28042)]]'
commands:
- '[[Create JWT Header]]'
- '[[Create JWT Payload]]'
- '[[Decode JWT]]'
---

# JWT Null Signature Attack

## Summary

The JWT Null Signature Attack is a vulnerability in the JWT specification that allows an attacker to bypass authentication by creating a JWT token without a signature. This vulnerability can be exploited by an attacker to impersonate any user and gain access to sensitive data or systems. The attack

## Description

# Description

The JWT Null Signature Attack is a vulnerability in the JWT specification that allows an attacker to bypass authentication by creating a JWT token without a signature. This vulnerability can be exploited by an attacker to impersonate any user and gain access to sensitive data or systems. The attacker can create a JWT token without a signature and send it to the server, which will treat it as a valid token and grant access to the attacker. This attack can be used to bypass authentication in web applications that use JWT tokens for authentication.

## Requirements

1. Access to a web application that uses JWT tokens for authentication

## Defense

1. Always use a signature when creating JWT tokens

1. Use a strong algorithm for signing JWT tokens

1. Regularly update the JWT library to the latest version to prevent known vulnerabilities

## Objectives

1. Bypass authentication

1. Impersonate users

1. Gain access to sensitive data

# Instructions

1. Use a tool like jwt_tool.py to create a JWT token with the HS256 algorithm but without a signature.

**Code**: [[eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxM]]

> The 'alg' parameter in the header of the JWT token specifies the algorithm used to sign the token. By setting the 'alg' parameter to 'none', the token is created without a signature.

2. Use the jwt_tool.py script to send the JWT token to the server and exploit the vulnerability.

**Code**: [[python3 jwt_tool.py JWT_HERE -X n]]

> The '-X n' parameter in the jwt_tool.py script tells the server to treat the JWT token as a valid token even though it doesn't have a signature. This allows the attacker to bypass authentication and gain access to the system.

**Command** ([[Decode JWT]]):

```bash
python3 jwt_tool.py JWT_HERE -X n
```

3. Deconstruct the JWT token to understand its structure.

**Code**: [[{"alg":"HS256","typ":"JWT"}.
{"sub":"1234567890","]]

> The JWT token is composed of three parts: the header, the payload, and the signature. The header contains the algorithm used to sign the token, the payload contains the data, and the signature is used to verify the authenticity of the token. In the case of the Null Signature Attack, the signature is missing.

**Command** ([[Create JWT Header]]):

```bash
{"alg":"HS256","typ":"JWT"}
```

**Command** ([[Create JWT Payload]]):

```bash
{"sub":"1234567890","name":"John Doe","iat":1516239022}
```

## Commands Used

- [[Create JWT Header]]
- [[Create JWT Payload]]
- [[Decode JWT]]

## Tags

- [[JWT - JSON Web Token]]
- [[JWT Signature]]
- [[JWT Signature - Null Signature Attack (CVE-2020-28042)]]
