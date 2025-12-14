---
tags:
  - csrf
  - oauth
  - twitter
  - login-csrf
  - account-takeover
  - session-hijacking
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-and-Capture-Twitter-OAuth-Tokens-in-Factlink]]'
  - '[[procedures/Craft-Malicious-OAuth-Completion-URL]]'
  - '[[procedures/Trick-Victim-into-Visiting-Crafted-URL]]'
  - '[[procedures/Complete-OAuth-Flow-as-Victim]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:29.270Z'
description: >-
  A multi-stage attack exploiting the absence of state parameters in Factlink's
  Twitter OAuth 1.0A flow, allowing an attacker to force a victim to
  authenticate as the attacker without consent, resulting in session hijacking.
skill_level: intermediate
impact_level: high
id: 5b1e0762-f083-4832-903a-4df8d2cabb57
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Login CSRF via Twitter OAuth in Factlink Leading to Attacker Account Impersonation

Multi-stage attack chain demonstrating a complete attack workflow exploiting the lack of state maintenance in Factlink's Twitter OAuth integration.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate OAuth Flow] --> B[Capture Tokens]
    B --> C[Craft Malicious URL]
    C --> D[Trick Victim]
    D --> E[Force Login as Attacker]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for token capture)
- Attacker's Twitter account

### Target Environment

- Factlink application with Twitter OAuth integration
- Web platform accessible via browser
- No specific ports; uses standard HTTPS (443)

### Initial Access Requirements

- Attacker must have a Twitter account
- Victim must be tricked via social engineering (e.g., email, link sharing)
- No prior credentials needed beyond attacker's Twitter access

## Detailed Attack Procedures

### Step 1: Initiate Twitter OAuth Process
procedure: [[procedures/Initiate-and-Capture-Twitter-OAuth-Tokens-in-Factlink]]

**Objective**: Start the OAuth flow to obtain temporary tokens for later use in the CSRF attack.

**Instructions**: Navigate to Factlink's Twitter login endpoint and begin the authentication process. Monitor the callback for tokens.

**Expected Output**: oauth_token and oauth_verifier extracted from the callback URL.

**Success Indicators**:
- OAuth flow initiated successfully
- Tokens captured without completing login

### Step 2: Grant Access and Capture Tokens
procedure: [[procedures/Initiate-and-Capture-Twitter-OAuth-Tokens-in-Factlink]]

**Objective**: Authorize the Factlink app on behalf of the attacker and intercept the verifier.

**Instructions**: During the Twitter authorization page, grant permissions, then use browser dev tools or proxy to capture and halt the redirect to Factlink.

**Expected Output**: Full set of oauth_token and oauth_verifier parameters.

**Success Indicators**:
- Permissions granted
- Redirection interrupted, tokens saved

### Step 3: Craft Malicious URL
procedure: [[procedures/Craft-Malicious-OAuth-Completion-URL]]

**Objective**: Construct a URL that injects the attacker's tokens into the victim's browser session.

**Instructions**: Build the URL in the format `/auth/login/twitter:twitter.com/?oauth_token={attacker_token}&oauth_verifier={attacker_verifier}` and host or share it via phishing.

**Expected Output**: A clickable link ready for distribution.

**Success Indicators**:
- URL correctly formatted with tokens
- Tokens remain unconsumed

### Step 4: Direct Victim to Crafted URL
procedure: [[procedures/Trick-Victim-into-Visiting-Crafted-URL]]

**Objective**: Socially engineer the victim to visit the malicious URL, completing the OAuth flow unwittingly.

**Instructions**: Send the crafted URL to the victim via email, chat, or malicious site, disguising it as a legitimate Factlink login prompt.

**Expected Output**: Victim's browser processes the URL and authenticates.

**Success Indicators**:
- Victim clicks and visits the URL
- No suspicion raised

### Step 5: Victim Logs in as Attacker
procedure: [[procedures/Complete-OAuth-Flow-as-Victim]]

**Objective**: Leverage the CSRF to bind the victim's session to the attacker's Twitter identity in Factlink.

**Instructions**: Upon visit, the victim's browser automatically completes the OAuth exchange using the provided tokens.

**Expected Output**: Victim's Factlink session is now authenticated as the attacker.

**Success Indicators**:
- Victim sees attacker's Factlink dashboard
- Unauthorized actions possible on attacker's behalf

## Attack Chain Summary

### Key Achievements

1. Successful token capture without state binding
2. Forced authentication via CSRF
3. Attacker account access by victim, enabling potential data exfiltration or actions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
