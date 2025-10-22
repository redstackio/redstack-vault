---
id: a81cb7ab-7f72-47d2-935e-e82d1a36eb1a
name: JWT Signature Disclosure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.574439+00:00'
updated_at: '2023-04-10T20:22:32.412703+00:00'
tags:
- '[[JWT - JSON Web Token]]'
- '[[JWT Signature]]'
- '[[JWT Signature - Disclosure of a correct signature (CVE-2019-7644)]]'
---

# JWT Signature Disclosure

## Summary

JWT Signature Disclosure attack involves sending a JWT with an incorrect signature to the endpoint. If the endpoint is vulnerable, it might respond with an error message disclosing the correct signature. This vulnerability is tracked as CVE-2019-7644. Attackers can use this information to craft a v

## Description

# Description

JWT Signature Disclosure attack involves sending a JWT with an incorrect signature to the endpoint. If the endpoint is vulnerable, it might respond with an error message disclosing the correct signature. This vulnerability is tracked as CVE-2019-7644. Attackers can use this information to craft a valid JWT and gain unauthorized access to the system. This vulnerability can be exploited if the JWT implementation uses a symmetric key to sign the tokens and the secret key is not properly protected.

## Requirements

1. Access to a JWT protected endpoint

1. Knowledge of the JWT implementation details

## Defense

1. Use asymmetric encryption to sign JWT tokens

1. Protect the secret key used to sign JWT tokens

1. Implement proper input validation and error handling mechanisms to prevent information disclosure

## Objectives

1. To obtain the correct JWT signature from the server

1. To use the disclosed JWT signature to craft a valid JWT token

# Instructions

1. Send a JWT with an incorrect signature to the endpoint and observe the error response.

**Code**: [[Invalid signature. Expected SflKxwRJSMeKKF2QT4fwpM]]

> To exploit this vulnerability, the attacker needs to send a JWT with an incorrect signature to the endpoint. The attacker can use various tools to craft the JWT token with an incorrect signature. If the endpoint is vulnerable, it might respond with an error message disclosing the correct signature. The attacker can use this information to craft a valid JWT token and gain unauthorized access to the system.

## Tags

- [[JWT - JSON Web Token]]
- [[JWT Signature]]
- [[JWT Signature - Disclosure of a correct signature (CVE-2019-7644)]]
