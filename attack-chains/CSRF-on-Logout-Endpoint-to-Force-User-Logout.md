---
id: ac-uuid-12345
name: CSRF on Logout Endpoint to Force User Logout
tags:
  - csrf
  - web
  - session-hijacking
  - denial-of-service
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Generate-CSRF-PoC-for-Logout-Endpoint]]'
  - '[[procedures/Deliver-CSRF-Payload-to-Authenticated-Victim]]'
step_count: 2
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.224Z'
description: >-
  A multi-stage attack exploiting a CSRF vulnerability in the logout endpoint to
  force authenticated users, including admins, to log out by tricking them into
  visiting a malicious page.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# CSRF on Logout Endpoint to Force User Logout

Multi-stage attack chain demonstrating a complete attack workflow exploiting a Cross-Site Request Forgery (CSRF) vulnerability on the logout endpoint of a web application like Courier.

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
    A[Generate PoC] --> B[Deliver Payload]
    B --> C[Force Logout]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application with authenticated sessions (e.g., https://www.trycourier.app)
- No CSRF protection on logout endpoint
- Victim must be authenticated

### Initial Access Requirements

- Ability to host or send HTML files (e.g., via email, phishing site)
- Victim interaction required (visiting malicious page while logged in)

## Detailed Attack Procedures

### Step 1: Generate CSRF PoC
procedure: [[procedures/Generate-CSRF-PoC-for-Logout-Endpoint]]

**Objective**: Create a malicious HTML page that automatically submits a forged logout request to the target endpoint.

**Instructions**: Use Burp Suite to generate the PoC HTML form targeting the logout URL. The form should POST to https://www.trycourier.app/logout without a CSRF token. Include JavaScript to auto-submit and redirect to avoid alerts.

**Expected Output**: An HTML file that, when loaded, sends the logout request.

**Success Indicators**:
- PoC HTML file generated and tested locally to confirm it triggers logout when visited while authenticated.
- No navigation warnings interfere with submission.

### Step 2: Deliver CSRF Payload
procedure: [[procedures/Deliver-CSRF-PoC-to-Authenticated-Victim]]

**Objective**: Trick the victim into loading the PoC page while they are authenticated, forcing the logout request.

**Instructions**: Host the PoC HTML on a controllable server (e.g., GitHub Pages, personal site) or embed in an email. Lure the victim via phishing link, social engineering, or malicious advertisement. Ensure the victim is logged into the target app.

**Expected Output**: Victim's session ends upon page load, requiring re-authentication.

**Success Indicators**:
- Victim visits the page and is logged out.
- Application logs show unexpected logout from the forged request.

## Attack Chain Summary

### Key Achievements

1. Successful generation of CSRF PoC exploiting lack of token validation.
2. Delivery of payload leading to forced logout of authenticated users.
3. Disruption of admin sessions, enabling potential DoS or follow-on attacks.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
