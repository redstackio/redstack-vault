---
tags:
  - jwt
  - auth-bypass
  - jitsi-meet
  - prosody
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Obtain-Jitsi-Meet-JWT-Public-Key]]'
  - '[[procedures/Forge-JWT-Token-with-HS256-Algorithm]]'
  - '[[procedures/Submit-Forged-JWT-to-Access-Protected-Conferences]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack exploiting JWT validation flaw in Jitsi Meet to forge
  tokens and gain unauthorized access to protected conferences.
skill_level: intermediate
impact_level: high
id: c8b6053b-7bdb-4f71-9297-25fcac1c4246
created_at: '2025-12-14T17:31:42.673Z'
updated_at: '2025-12-14T17:31:42.673Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Jitsi Meet Authentication Bypass via JWT Algorithm Confusion

## Overview

This attack chain exploits a vulnerability in Jitsi Meet versions prior to 2.0.5963, where the Prosody module fails to enforce asymmetric JWT validation when public keys are configured. An attacker can forge a JWT by switching the algorithm to a symmetric one (HS256) and using the public key as the HMAC secret, bypassing authentication to start conferences or enter protected rooms. Discovered by researcher plokta and reported on May 27, 2021, via HackerOne, this allows unauthorized access without known real-world incidents but high potential for conference disruption.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Obtain Public Key] --> B[Forge JWT Token]
    B --> C[Access Protected Resources]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- JWT library or tool (e.g., Python's PyJWT for forging)
- Browser or curl for submission

### Target Environment

- Jitsi Meet instance (versions < 2.0.5963)
- Prosody module with JWT authentication enabled using asymmetric signatures (e.g., RS256)
- Web platform access

### Initial Access Requirements

- Network access to the Jitsi Meet server
- Knowledge of the public key (often exposed in config)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Obtain Public Key
procedure: [[procedures/Obtain-Jitsi-Meet-JWT-Public-Key]]

**Objective**: Retrieve the public key used for JWT validation to enable forgery.

**Instructions**: Inspect the Jitsi Meet configuration files or network responses where the public key is typically exposed for asymmetric authentication. Look for PEM-formatted keys in Prosody config or API endpoints.

**Expected Output**: A public key in PEM or raw format, e.g., -----BEGIN PUBLIC KEY----- ... -----END PUBLIC KEY-----.

**Success Indicators**:
- Public key retrieved successfully
- Key confirmed as used for JWT signing

### Step 2: Forge JWT Token
procedure: [[procedures/Forge-JWT-Token-with-HS256-Algorithm]]

**Objective**: Create a malicious JWT by altering the algorithm to HS256 and signing with the public key as secret.

**Instructions**: Use a JWT library to set the header to {'alg': 'HS256'}, craft a payload with desired claims (e.g., moderator access), and sign using the public key bytes as the HMAC secret. Encode the result as a valid JWT string.

**Expected Output**: A forged JWT token, e.g., eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0In0.signature.

**Success Indicators**:
- Token generated without errors
- Token decodes correctly with HS256

### Step 3: Submit Forged JWT
procedure: [[procedures/Submit-Forged-JWT-to-Access-Protected-Conferences]]

**Objective**: Use the forged token to authenticate and access protected Jitsi Meet resources.

**Instructions**: Include the forged JWT in the Authorization header of requests to Jitsi Meet endpoints, such as starting a new conference or joining a protected room via the web interface or API.

**Expected Output**: Successful access to the conference room without authentication prompts.

**Success Indicators**:
- Unauthorized entry granted
- Ability to start or join protected conferences

## Attack Chain Summary

### Key Achievements

1. Bypassed JWT authentication using algorithm confusion
2. Gained unauthorized access to protected Jitsi Meet conferences
3. Demonstrated potential for conference hijacking or disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
