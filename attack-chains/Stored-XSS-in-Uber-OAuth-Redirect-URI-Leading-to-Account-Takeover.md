---
tags:
  - xss
  - stored-xss
  - oauth
  - account-takeover
  - uber
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Stored-XSS-in-OAuth-Redirect-URI]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:34.222Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in the OAuth v2
  authorize endpoint's redirect_uri parameter to execute arbitrary JavaScript
  and achieve account takeover on Uber's authentication domains.
skill_level: intermediate
impact_level: high
id: 50df6512-05cb-49d9-8e07-ec4d38f6f0b7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---
id: attack-chain-stored-xss-uber-oauth
name: Stored XSS in Uber OAuth Redirect URI Leading to Account Takeover
type: attack_chain
description: A multi-stage attack exploiting a stored XSS vulnerability in the OAuth v2 authorize endpoint's redirect_uri parameter to execute arbitrary JavaScript and achieve account takeover on Uber's authentication domains.
verified: false
submitted: false
step_count: 3
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Exploit-Stored-XSS-in-OAuth-Redirect-URI]]
techniques: [[Exploit Public-Facing Application]], [[JavaScript]]
tactics: [[Initial Access]], [[Execution]], [[Collection]]
tags: xss, stored-xss, oauth, account-takeover, uber
platforms: Web
tools: []
---

# Stored XSS in Uber OAuth Redirect URI Leading to Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting insufficient sanitization of the redirect_uri parameter in Uber's OAuth v2 authorize endpoint at auth.uber.com.

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
    A[Craft Malicious Redirect URI Payload] --> B[Trick Authenticated Victim into Visiting Link]
    B --> C[Execute JavaScript for Account Takeover]
    C --> D[Steal Session or Manipulate Login]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for payload crafting
- No specialized tools required beyond web access

### Target Environment

- Web platform
- OAuth v2 services on auth.uber.com
- Authenticated user session on login.uber.com or auth.uber.com

### Initial Access Requirements

- Ability to craft and distribute links (e.g., via email or social engineering)
- Victim must be authenticated to Uber
- No prior network access beyond public internet

## Detailed Attack Procedures

### Step 1: Craft Malicious Payload
procedure: [[procedures/Exploit-Stored-XSS-in-OAuth-Redirect-URI]]

**Objective**: Create a redirect_uri parameter containing a JavaScript payload that will be stored and executed upon victim interaction with the OAuth authorize endpoint.

**Instructions**: Construct a URL targeting https://auth.uber.com/oauth/v2/authorize with a malicious redirect_uri, such as javascript:alert(document.cookie) encoded to bypass basic validation. For storage, leverage the endpoint's handling to persist the payload in a way that triggers on subsequent visits.

**Expected Output**: A crafted link like https://auth.uber.com/oauth/v2/authorize?client_id=...&redirect_uri=javascript%3Aalert%28document.cookie%29&response_type=code&scope=...

**Success Indicators**:
- Payload URL generated without immediate rejection
- Basic testing shows JS execution in a non-auth context

### Step 2: Distribute Link to Victim
procedure: [[procedures/Exploit-Stored-XSS-in-OAuth-Redirect-URI]]

**Objective**: Use social engineering to get an authenticated victim to visit the malicious link, triggering the stored XSS.

**Instructions**: Send the crafted link via phishing email, messaging, or other means, impersonating a legitimate Uber communication. The victim must be logged in for the JS to execute in the authentication domain context.

**Expected Output**: Victim accesses the link, and the OAuth flow attempts to redirect, storing and executing the payload.

**Success Indicators**:
- Victim reports clicking the link or session anomaly
- Attacker observes payload execution via callback or exfil channel in payload

### Step 3: Execute Takeover via JavaScript
procedure: [[procedures/Exploit-Stored-XSS-in-OAuth-Redirect-URI]]

**Objective**: Leverage the executed JS to steal session cookies, manipulate login forms, or exfiltrate data for account takeover.

**Instructions**: The payload, once executed in the context of login.uber.com or auth.uber.com, can access document.cookie to steal sessions or alter DOM elements to capture credentials during login.

**Expected Output**: Attacker receives stolen session data or gains control of the victim's account.

**Success Indicators**:
- JS alert or exfil confirms execution
- Attacker logs in with stolen session

## Attack Chain Summary

### Key Achievements

1. Bypassed redirect_uri validation to inject and store XSS payload
2. Achieved arbitrary JS execution in high-privilege authentication domains
3. Enabled full account takeover by stealing or manipulating user sessions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
