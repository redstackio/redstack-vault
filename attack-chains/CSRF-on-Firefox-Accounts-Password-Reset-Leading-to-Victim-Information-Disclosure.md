---
tags:
  - csrf
  - information-disclosure
  - web-vulnerability
  - phishing
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-Password-Reset-Endpoint-for-CSRF]]'
  - '[[procedures/Craft-CSRF-Proof-of-Concept-HTML]]'
  - '[[procedures/Distribute-Malicious-CSRF-Link-to-Victim]]'
  - '[[procedures/Trigger-CSRF-Submission-for-Information-Disclosure]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.275Z'
description: >-
  A multi-stage CSRF attack exploiting the lack of token validation in Mozilla's
  password reset endpoint to forge requests and disclose victim details like IP
  address, location, and browser information via reset emails.
id: adf48480-679b-4352-b457-9922093a7dde
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF on Firefox Accounts Password Reset Leading to Victim Information Disclosure

Multi-stage attack chain demonstrating a complete CSRF exploitation workflow on Mozilla's accounts.firefox.com to disclose sensitive victim information without authentication.

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
    A[Analyze Endpoint] --> B[Craft PoC]
    B --> C[Distribute Link]
    C --> D[Trigger Submission]
    D --> E[Receive Disclosed Info]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Service: accounts.firefox.com (password reset endpoint)
- No specific ports required (HTTPS/443 implied)
- Network access: Internet connectivity for hosting and sending links

### Initial Access Requirements

- Attacker account on accounts.firefox.com
- Victim's email or social engineering vector for link delivery
- No prior credentials on victim side; exploits unauthenticated endpoint

## Detailed Attack Procedures

### Step 1: Analyze Password Reset Endpoint
procedure: [[procedures/Analyze-Password-Reset-Endpoint-for-CSRF]]

**Objective**: Identify the lack of CSRF protection in the password reset functionality to enable forged requests.

**Instructions**: Register an account on accounts.firefox.com and inspect the /reset_password endpoint using browser developer tools or a proxy to confirm no anti-CSRF tokens are required for the email parameter.

**Expected Output**: Confirmation that requests to https://accounts.firefox.com/reset_password?email=... succeed without tokens, sending reset emails with user details.

**Success Indicators**:
- Endpoint accepts email parameter without CSRF validation
- Test reset email received containing IP and browser info

### Step 2: Craft CSRF Proof-of-Concept
procedure: [[procedures/Craft-CSRF-Proof-of-Concept-HTML]]

**Objective**: Create a malicious HTML page that auto-submits a form to the vulnerable endpoint using the attacker's email.

**Instructions**: Use Burp Suite to generate the CSRF PoC form targeting the endpoint with hidden fields for email, reset_password_confirm, and UTM parameters, then add JavaScript for auto-submission.

**Expected Output**: A self-contained HTML file that, when loaded, submits the form cross-origin.

**Success Indicators**:
- HTML page loads and auto-submits without errors
- Local test triggers a reset email to attacker

### Step 3: Distribute Malicious Link
procedure: [[procedures/Distribute-Malicious-CSRF-Link-to-Victim]]

**Objective**: Deliver the PoC link to the victim via phishing or social engineering to lure them into opening it.

**Instructions**: Host the HTML page on a controllable server (e.g., GitHub Pages or personal domain) and send the URL to the victim disguised as a legitimate link, such as a Firefox update notification.

**Expected Output**: Victim receives and clicks the link, loading the malicious page in their browser.

**Success Indicators**:
- Victim accesses the hosted page
- No direct confirmation; monitor for subsequent reset email

### Step 4: Trigger CSRF Submission for Disclosure
procedure: [[procedures/Trigger-CSRF-Submission-for-Information-Disclosure]]

**Objective**: Exploit the victim's browser to forge the reset request, resulting in an email to the attacker with the victim's sensitive details.

**Instructions**: Once the victim opens the link, their browser auto-submits the form to the endpoint using their session context, initiating the reset process.

**Expected Output**: Attacker receives email from accounts.firefox.com containing victim's IP address, geolocation, and browser details.

**Success Indicators**:
- Reset email arrives in attacker's inbox
- Email includes unauthorized victim information

## Attack Chain Summary

### Key Achievements

1. Identified and exploited CSRF in unauthenticated password reset
2. Crafted and delivered cross-site request forgery payload
3. Achieved information disclosure without victim consent or authentication

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
