---
id: 801967e0-0848-4931-92b5-54204c661f38
name: Login CSRF via Missing State Parameter in Gratipay Bitbucket OAuth
type: attack_chain
description: >-
  A multi-stage attack exploiting the absence of a state parameter in Gratipay's
  Bitbucket OAuth integration, allowing an attacker to force a victim to
  authenticate as the attacker, leading to potential account takeover.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.355Z'
procedures:
  - '[[procedures/Initiate-Bitbucket-OAuth-Authorization-Flow]]'
  - '[[procedures/Grant-Access-and-Preserve-OAuth-Token]]'
  - '[[procedures/Craft-and-Deliver-Malicious-Login-URL]]'
  - '[[procedures/Force-Victim-Authentication-as-Attacker]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Initial Access]]'
tags:
  - csrf
  - oauth
  - login-csrf
  - account-takeover
platforms:
  - Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---

# Login CSRF via Missing State Parameter in Gratipay Bitbucket OAuth

Multi-stage attack chain demonstrating a complete attack workflow exploiting Login CSRF in OAuth flows without state parameters.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate OAuth Flow] --> B[Preserve Token]
    B --> C[Trick Victim with URL]
    C --> D[Complete Login as Attacker]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual browser-based actions)

### Target Environment

- Web platform with Gratipay application
- Bitbucket OAuth integration enabled
- No specific ports; requires internet access to Bitbucket and Gratipay endpoints

### Initial Access Requirements

- Attacker must have a Bitbucket account
- Victim must be tricked into clicking a link (e.g., via phishing or social engineering)
- No prior credentials needed beyond attacker's Bitbucket login

## Detailed Attack Procedures

### Step 1: Initiate OAuth Flow
procedure: [[procedures/Initiate-Bitbucket-OAuth-Authorization-Flow]]

**Objective**: Start the OAuth authorization process to obtain a temporary oauth_token without CSRF protection.

**Instructions**: As the attacker, navigate to the Gratipay Bitbucket OAuth endpoint in your browser to begin the flow. The request lacks a state parameter, making it vulnerable to reuse.

**Expected Output**: Bitbucket prompts for authorization, and an oauth_token is generated in the URL (e.g., https://bitbucket.org/site/oauth1/authorize?oauth_token=ZmCHb7dnyYVYKTYRNt).

**Success Indicators**:
- OAuth_token visible in the browser URL
- No state parameter present in the request

### Step 2: Preserve Token
procedure: [[procedures/Grant-Access-and-Preserve-OAuth-Token]]

**Objective**: Grant permission to the app while preventing the token from being consumed by interrupting the callback.

**Instructions**: Authorize the Gratipay app in Bitbucket, then manually interrupt the redirection back to Gratipay (e.g., by closing the tab or using browser dev tools to block the callback).

**Expected Output**: The oauth_token remains valid and preserved for later use, not invalidated by the callback.

**Success Indicators**:
- Token is still accessible and not expired
- No successful callback to Gratipay occurs

### Step 3: Deliver Malicious URL
procedure: [[procedures/Craft-and-Deliver-Malicious-Login-URL]]

**Objective**: Create a URL embedding the preserved token and trick the victim into accessing it.

**Instructions**: Construct the URL as /auth/login/bitbucket:bitbucket.com/?oauth_token={preserved_token} and send it to the victim via email, chat, or phishing link.

**Expected Output**: Victim receives and clicks the link, initiating the OAuth completion on their browser.

**Success Indicators**:
- Victim accesses the crafted URL
- Gratipay login flow starts without additional prompts

### Step 4: Unauthorized Login
procedure: [[procedures/Force-Victim-Authentication-as-Attacker]]

**Objective**: Complete the OAuth flow on the victim's side, logging them in as the attacker.

**Instructions**: When the victim accesses the URL, the flow proceeds without CSRF validation, authenticating them with the attacker's Bitbucket-linked account.

**Expected Output**: Victim's Gratipay session is established as the attacker's account, allowing unauthorized actions.

**Success Indicators**:
- Victim dashboard shows attacker's account details
- Attacker can observe or exploit the shared session indirectly

## Attack Chain Summary

### Key Achievements

1. Obtained reusable oauth_token due to missing state parameter
2. Forced victim login as attacker without their credentials
3. Enabled potential account takeover or unauthorized transactions in Gratipay

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
