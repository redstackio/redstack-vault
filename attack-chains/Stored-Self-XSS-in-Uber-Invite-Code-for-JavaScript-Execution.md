---
id: ac-uber-self-xss-134124
name: Stored Self-XSS in Uber Invite Code for JavaScript Execution
tags:
  - xss
  - stored-xss
  - self-xss
  - uber
  - javascript-injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Malicious-Invite-Code-Payload]]'
  - '[[procedures/Trigger-XSS-via-m-uber-Login]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.610Z'
description: >-
  A stored self-XSS vulnerability in Uber's invite code feature allows injection
  of malicious JavaScript that executes upon login to m.uber.com, enabling
  potential session data theft via social engineering.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored Self-XSS in Uber Invite Code for JavaScript Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored self-XSS in Uber's invite code feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Malicious Payload] --> B[Trigger Execution on Login]
    B --> C[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Uber.com and m.uber.com (mobile site)
- Authenticated Uber account

### Initial Access Requirements

- Valid Uber credentials
- Ability to access uber.com personal area

## Detailed Attack Procedures

### Step 1: Set Malicious Invite Code
procedure: [[procedures/Set-Malicious-Invite-Code-Payload]]

**Objective**: Inject a malicious JavaScript payload into the user's invite code field on uber.com, which syncs to m.uber.com.

**Instructions**: Log into uber.com, navigate to the personal area, and enter a payload like `<script>alert(document.domain)</script>` or an obfuscated version such as `EMPLOYEE_2016_04_oidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjn<script>eval(atob('YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ=='))</script>oidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjn` into the invite code field. Save the changes.

**Expected Output**: The payload is stored and synced across Uber's platforms.

**Success Indicators**:
- Payload accepted without validation errors
- Invite code updated in profile

### Step 2: Trigger XSS Execution
procedure: [[procedures/Trigger-XSS-via-m-uber-Login]]

**Objective**: Log into m.uber.com to display the unsanitized invite code, executing the injected JavaScript.

**Instructions**: Open m.uber.com in a browser, sign in with the affected account. The invite code will be rendered without escaping, triggering the script on the main page.

**Expected Output**: Alert or JavaScript execution confirming the XSS, such as an alert box showing the domain.

**Success Indicators**:
- JavaScript payload executes on login
- Potential access to session data or cookies via console

## Attack Chain Summary

### Key Achievements

1. Successful injection of arbitrary JavaScript via user-controlled invite code
2. Execution of payload on m.uber.com without additional interaction
3. Demonstration of self-XSS impact, mitigable via social engineering for broader attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
