---
id: ac-csrf-password-change-coinbase
tags:
  - csrf
  - web
  - account-takeover
  - password-change
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Intercept-Password-Change-Request-with-Burp-Suite]]'
  - '[[procedures/Generate-Malicious-CSRF-HTML-Form]]'
  - '[[procedures/Deliver-and-Trigger-CSRF-POC]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.122Z'
description: >-
  Demonstrates a CSRF attack vector targeting a password change endpoint to
  enable unauthorized password updates, potentially leading to account takeover,
  though reported as non-reproducible in the specific case.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# CSRF Attack on Password Change Endpoint for Unauthorized Account Takeover

Multi-stage attack chain demonstrating a CSRF workflow targeting a web application's password change functionality to forge unauthorized requests.

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
    A[Intercept Legitimate Request] --> B[Craft Malicious Form]
    B --> C[Deliver and Trigger POC]
    C --> D[Unauthorized Password Change]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application with password change endpoint (e.g., POST /password_reset)
- No specific ports required beyond standard HTTPS (443)
- Attacker needs ability to host or deliver HTML content to victim

### Initial Access Requirements

- Victim must be authenticated to the target site
- Attacker requires network access to intercept or observe legitimate requests (e.g., via proxy)
- No prior credentials needed, but social engineering may be used to lure victim to malicious page

## Detailed Attack Procedures

### Step 1: Intercept Password Change Request
procedure: [[procedures/Intercept-Password-Change-Request-with-Burp-Suite]]

**Objective**: Capture the legitimate password change request to understand the endpoint, parameters, and any CSRF protections.

**Instructions**: Configure Burp Suite as a proxy and initiate a password change on the target site to intercept the POST request. Analyze the form data including old_password, password, password_confirmation, and check for CSRF tokens.

**Expected Output**: Captured HTTP request details, including endpoint URL and parameters.

**Success Indicators**:
- Request intercepted successfully
- Parameters and endpoint identified
- CSRF token presence noted (or absence exploited)

### Step 2: Generate Malicious CSRF HTML Form
procedure: [[procedures/Generate-Malicious-CSRF-HTML-Form]]

**Objective**: Craft a self-submitting HTML form that mimics the password change request but omits CSRF protections to forge the action from an external site.

**Instructions**: Use the intercepted data from Burp Suite to create an HTML page with a hidden form targeting the password_reset endpoint. Set the form to auto-submit via JavaScript, excluding any CSRF token field.

**Expected Output**: A functional HTML POC file that, when loaded by the victim, submits the forged request.

**Success Indicators**:
- HTML form generated without CSRF token
- Form submission tested in a controlled environment
- Request structure matches intercepted legitimate request

### Step 3: Deliver and Trigger CSRF Attack
procedure: [[procedures/Deliver-and-Trigger-CSRF-POC]]

**Objective**: Deliver the malicious HTML to the victim while they are authenticated, triggering the unauthorized password change.

**Instructions**: Host the HTML POC on an attacker-controlled site or send via email/phishing. Modify form values (e.g., new password) as needed. When victim visits, the form auto-submits to change their password.

**Expected Output**: Successful POST to the target endpoint, potentially resulting in password update if CSRF validation is absent.

**Success Indicators**:
- Victim loads the page and form submits
- Target endpoint receives and processes the request (monitor via proxy if possible)
- Account password changed without user interaction

## Attack Chain Summary

### Key Achievements

1. Intercepted and analyzed password change mechanics
2. Created a bypass for alleged CSRF protections via forged form
3. Enabled potential account takeover through unauthorized password reset

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
