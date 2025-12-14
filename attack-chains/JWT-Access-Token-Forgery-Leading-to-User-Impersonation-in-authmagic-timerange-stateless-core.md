---
id: ac-736522-jwt-forgery
tags:
  - jwt
  - authentication-bypass
  - impersonation
  - npm-vulnerability
  - token-forgery
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/JSON-Web-Tokens-JWT4B]]'
  - '[[tools/authmagic-cli]]'
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
  - '[[procedures/Setup-Testing-Environment-for-Authmagic]]'
  - '[[procedures/Initialize-and-Install-Authmagic-Example-App]]'
  - '[[procedures/Perform-Initial-User-Authentication]]'
  - '[[procedures/Intercept-and-Modify-JWT-Token-Refresh-Request]]'
  - '[[procedures/Forward-Modified-Request-and-Verify-Impersonation]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:10.866Z'
description: >-
  Multi-stage attack exploiting improper JWT validation in the
  authmagic-timerange-stateless-core npm module (v0.0.9) to forge access tokens
  and impersonate users via the token reissuance endpoint.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# JWT Access Token Forgery Leading to User Impersonation in authmagic-timerange-stateless-core

Multi-stage attack chain demonstrating exploitation of improper JWT token validation in the authmagic-timerange-stateless-core npm module (version 0.0.9). The vulnerability allows attackers to modify the access token payload during reissuance at the POST /token endpoint, as only the refresh token is verified, enabling user impersonation and unauthorized access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Initialize App]
    B --> C[Authenticate User]
    C --> D[Intercept & Modify Token]
    D --> E[Forge Identity & Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/JSON-Web-Tokens-JWT4B]]
- [[tools/authmagic-cli]]

### Target Environment

- Node.js runtime (v14+ recommended)
- npm package manager
- Local web server on port 3000
- Burp Suite proxy configured for browser traffic

### Initial Access Requirements

- No prior credentials needed; starts with local setup
- Network access to localhost:3000
- Email client or console to view authorization links

## Detailed Attack Procedures

### Step 1: Setup Testing Environment
procedure: [[procedures/Setup-Testing-Environment-for-Authmagic]]

**Objective**: Isolate the testing environment to avoid conflicts during vulnerability reproduction.

**Instructions**: Create a dedicated directory for the proof-of-concept using [[commands/create-poc-directory]] and navigate into it with [[commands/change-to-poc-directory]].

```bash
mkdir poc
cd poc/
```

**Expected Output**: A new 'poc' directory is created, and the current working directory is changed to it.

**Success Indicators**:
- Directory 'poc' exists
- Shell prompt shows '/poc' path

### Step 2: Initialize and Install Authmagic Example App
procedure: [[procedures/Initialize-and-Install-Authmagic-Example-App]]

**Objective**: Install the vulnerable module and set up the example application to simulate a production authentication flow.

**Instructions**: Install the authmagic CLI globally using [[commands/install-authmagic-cli-globally]], initialize a new npm project with [[commands/init-npm-project-default]], set up the example app with [[commands/init-authmagic-example]], install dependencies via [[commands/install-authmagic-dependencies]], and start the server using [[commands/start-authmagic-server]]. Ensure the package.json name is not 'authmagic' to prevent dependency issues.

```bash
npm install -g authmagic-cli
npm init -y
authmagic init -e
authmagic install
authmagic
```

**Expected Output**: Dependencies installed, server running on http://localhost:3000.

**Success Indicators**:
- authmagic-cli available in PATH
- package.json created
- Server logs show 'Server running on http://localhost:3000'

### Step 3: Perform Initial User Authentication
procedure: [[procedures/Perform-Initial-User-Authentication]]

**Objective**: Authenticate a legitimate user to obtain initial access and refresh tokens.

**Instructions**: Access the app at http://localhost:3000, enter an email (e.g., test@example.com), and click 'Send authorization link'. Check the console for the preview URL (e.g., a magic link), open it in the browser, and click the authorization link to complete login.

No specific commands; browser-based interaction.

**Expected Output**: Access and refresh tokens displayed in the app after clicking the link.

**Success Indicators**:
- Authorization email/link received
- Tokens visible in the app interface
- User session established

### Step 4: Intercept and Modify JWT Token Refresh Request
procedure: [[procedures/Intercept-and-Modify-JWT-Token-Refresh-Request]]

**Objective**: Capture the token refresh request and tamper with the access token payload to forge user identity.

**Instructions**: Configure Burp Suite as a proxy. In the app, click 'Refresh token' to trigger a POST to /token. Intercept the request in Burp, then use the JWT4B extension to decode and edit the 'token' field's payload (e.g., change 'u' from 'test@example.com' to 'admin@target.com'). Re-encode the JWT.

No CLI commands; tool-based interception.

**Expected Output**: Modified request with altered JWT payload ready to forward.

**Success Indicators**:
- Request intercepted showing original tokens
- Payload edited successfully without signature invalidation

### Step 5: Forward Modified Request and Verify Impersonation
procedure: [[procedures/Forward-Modified-Request-and-Verify-Impersonation]]

**Objective**: Submit the tampered request to obtain a new signed token with the forged identity, confirming unauthorized access.

**Instructions**: In Burp Suite, forward the modified POST /token request. Observe the response, which should include a new access token reflecting the changed user email (e.g., 'admin@target.com').

No CLI commands; tool-based forwarding.

**Expected Output**: Response with new tokens where the user identity matches the forged payload.

**Success Indicators**:
- New token signed and accepted
- App or response shows impersonated user (different email)
- Unauthorized access granted

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable authmagic environment
2. Initial authentication to obtain tokens
3. JWT payload modification bypassing validation
4. Reissuance of forged token enabling impersonation
5. Demonstration of high-impact unauthorized access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
