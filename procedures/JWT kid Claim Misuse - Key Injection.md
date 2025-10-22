---
id: 48aba475-54cd-4d9d-8511-09797debabd2
name: JWT kid Claim Misuse - Key Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.766036+00:00'
updated_at: '2023-04-10T20:22:38.422933+00:00'
tags:
- '[[JWT Claims]]'
- '[[JWT - JSON Web Token]]'
- '[[JWT kid Claim Misuse]]'
commands:
- '[[Sign JWT with malicious key]]'
---

# JWT kid Claim Misuse - Key Injection

## Summary

JWT is a widely used standard for authentication and authorization in web applications. The 'kid' claim is a header parameter that identifies the key used to sign the JWT. An attacker can modify the 'kid' claim to inject a malicious key and gain access to sensitive data or perform unauthorized acti

## Description

# Description

JWT is a widely used standard for authentication and authorization in web applications. The 'kid' claim is a header parameter that identifies the key used to sign the JWT. An attacker can modify the 'kid' claim to inject a malicious key and gain access to sensitive data or perform unauthorized actions. This technique can be used to bypass authentication and authorization controls and escalate privileges. By modifying the 'kid' claim, an attacker can change the key used to sign the JWT, allowing them to craft their own tokens and impersonate legitimate users. This can lead to data theft, privilege escalation, and other malicious activities.

## Requirements

1. Access to a JWT

1. Knowledge of the 'kid' claim

## Defense

1. Use a secure key management system to store and manage cryptographic keys

1. Ensure that the 'kid' claim is validated and verified during JWT processing

1. Monitor and analyze JWT usage for anomalies and suspicious activity

## Objectives

1. Inject a malicious key into the 'kid' claim of a JWT

1. Bypass authentication and authorization controls

1. Escalate privileges

# Instructions

1. Use the following command to extract the header and payload from a JWT: 

`echo <JWT> | cut -d. -f1,2 | base64 -d`

This will output the header and payload in JSON format.

**Code**: [[eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJzdWIiO]]

> The `cut` command is used to split the JWT into two parts: the header and the payload. The `-d.` option specifies that the delimiter is a period. The `-f1,2` option specifies that we want to extract the first and second fields. The `base64 -d` command is used to decode the base64-encoded header and payload.

2. Use the following command to generate a malicious private key: 

`openssl genrsa -out malicious.key 2048`

This will generate a 2048-bit RSA private key and save it to the file `malicious.key`.

**Code**: [[
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9]]

> The `openssl genrsa` command is used to generate an RSA private key. The `-out` option specifies the output file name. The `2048` argument specifies the key size in bits.

3. Use the following code to sign a JWT with a malicious key: 

```
jwt.sign({
  data: 'test'
}, maliciousKey, { algorithm: 'HS256', header: { kid: 'malicious.key' } })
```

This will sign a JWT with the `malicious.key` key and the `HS256` algorithm.

**Code**: [[
jwt.sign({
  data: 'test'
}, maliciousKey, { algo]]

> The `jwt.sign` function is used to sign a JWT. The first argument is the payload data. The second argument is the key used to sign the JWT. The third argument is an options object that specifies the algorithm and the header parameters. The `kid` parameter is set to the `malicious.key` value to inject the malicious key into the JWT.

**Command** ([[Sign JWT with malicious key]]):

```bash
jwt.sign({
  data: 'test'
}, maliciousKey, { algorithm: 'HS256', header: { kid: 'malicious.key' } })

```

## Commands Used

- [[Sign JWT with malicious key]]

## Tags

- [[JWT Claims]]
- [[JWT - JSON Web Token]]
- [[JWT kid Claim Misuse]]
