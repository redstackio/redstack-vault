---
id: ac-uber-xss-citysource-001
tags:
  - xss
  - javascript-uri
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-XSS-in-citySource-Parameter]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.867Z'
description: >-
  A cross-site scripting attack exploiting the lack of validation on the
  citySource URL parameter in the Uber Movement community page, allowing
  execution of arbitrary JavaScript via javascript: URIs upon user interaction.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS via javascript: URI in citySource Parameter on Uber Movement Community Page

Multi-stage attack chain demonstrating a complete XSS workflow on the Uber Movement community page.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Vulnerable Page] --> B[Inject Payload]
    B --> C[Trigger Execution]
    C --> D[Observe Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to http://ubermovement.com/community/daniel
- No special services or ports required

### Initial Access Requirements

- Public internet access
- No credentials needed
- Direct navigation to the target URL

## Detailed Attack Procedures

### Step 1: Access Vulnerable Page with Payload
procedure: [[procedures/Exploit-XSS-in-citySource-Parameter]]

**Objective**: Inject the malicious javascript: URI into the citySource parameter to set up the payload.

**Instructions**: Navigate to the target URL with the appended payload in your web browser.

**Expected Output**: The page loads with the injected parameter, but no immediate execution.

**Success Indicators**:
- Page loads without errors
- URL reflects the citySource parameter with javascript: payload

### Step 2: Trigger Payload Execution
procedure: [[procedures/Exploit-XSS-in-citySource-Parameter]]

**Objective**: Interact with the page element to execute the injected JavaScript.

**Instructions**: On the loaded page, locate and click the 'Back to community' link.

**Expected Output**: The JavaScript payload executes upon click.

**Success Indicators**:
- No page navigation errors
- Payload ready for execution

### Step 3: Validate XSS Execution
procedure: [[procedures/Exploit-XSS-in-citySource-Parameter]]

**Objective**: Confirm arbitrary JavaScript execution by observing the alert popup.

**Instructions**: After clicking the link, watch for the alert dialog to appear.

**Expected Output**: An alert box displays 'XSSED'.

**Success Indicators**:
- Alert popup appears
- Confirms XSS vulnerability

## Attack Chain Summary

### Key Achievements

1. Successful injection of javascript: URI via citySource parameter
2. Triggered execution through user interaction on the community page
3. Demonstrated potential for phishing or CSRF via arbitrary JS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T12:00:00Z*
