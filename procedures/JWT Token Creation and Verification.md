---
id: ddc4c4fe-3811-435e-a873-dc3165502314
name: JWT Token Creation and Verification
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.436398+00:00'
updated_at: '2023-04-10T20:22:36.884514+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]'
sub_techniques:
- '[[Password Cracking|T1110.002 - Password Cracking]]'
tags:
- '[[JWT Format]]'
- '[[JWT - JSON Web Token]]'
commands:
- '[[Encode Header, Data, and Signature in Base64]]'
---

# JWT Token Creation and Verification

## Summary

JSON Web Tokens (JWTs) are a compact, URL-safe means of representing claims to be transferred between two parties. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA. This procedure involves creating and verifying JWT tokens. The creation of 

## Description

# Description

JSON Web Tokens (JWTs) are a compact, URL-safe means of representing claims to be transferred between two parties. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA. This procedure involves creating and verifying JWT tokens. The creation of tokens requires a secret key while verification requires the public key. Attackers can use brute force or credential stuffing to obtain the secret key and create their own tokens. The business value of using JWT tokens is that it allows for secure and efficient transfer of claims between parties.

## Requirements

1. Access to a JWT token generation and verification tool

1. Knowledge of the secret key

## Defense

1. Keep the secret key used to sign the token secure

1. Use strong passwords and two-factor authentication to prevent brute force and credential stuffing attacks

1. Use a JWT library that has been audited and is actively maintained to prevent vulnerabilities in the token generation and verification process.

## Objectives

1. Create JWT tokens

1. Verify JWT tokens

# Instructions

1. To create a JWT token, first create a header specifying the algorithm used to sign the token. Then create a payload containing the claims to be transferred. Finally, sign the header and payload using the secret key to create the signature. Concatenate the header, payload, and signature with periods to create the JWT token.

**Code**: [[Base64(Header).Base64(Data).Base64(Signature)]]

> The header typically consists of two parts: the type of token, which is JWT, and the signing algorithm being used, such as HMAC SHA256 or RSA. The payload contains claims, which are statements about an entity (typically, the user) and additional data. For example, a token could contain a claim stating that the user is an admin ("admin": true). The signature is used to verify that the sender of the JWT is who it says it is and to ensure that the message wasn't changed along the way.

**Command** ([[Encode Header, Data, and Signature in Base64]]):

```bash
Base64(Header).Base64(Data).Base64(Signature)
```

2. To verify a JWT token, first split the token into its three components (header, payload, and signature) using periods. Then, decode the header and payload from base64. Finally, verify the signature using the public key. If the signature is valid, the token is considered verified.

**Code**: [[eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxM]]

> The verified token can then be used to transfer claims between parties. It is important to ensure that the secret key used to sign the token is kept secure to prevent attackers from creating their own tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]

### Sub-Techniques

- [[Password Cracking|T1110.002 - Password Cracking]]

## Commands Used

- [[Encode Header, Data, and Signature in Base64]]

## Tags

- [[JWT Format]]
- [[JWT - JSON Web Token]]
