---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Stored XSS Injection in Autodesk Admin Panel Custom Integration
tags:
  - xss
  - stored-xss
  - web
  - injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Inject-Stored-XSS-Payload-in-Custom-Integration]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.694Z'
description: >-
  Demonstrates exploitation of a stored XSS vulnerability in the Custom
  Integration feature of Autodesk's admin panel, allowing injection of malicious
  JavaScript that executes for other users viewing the content.
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS Injection in Autodesk Admin Panel Custom Integration

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Admin Panel] --> B[Inject Payload]
    B --> C[Execution on View]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools (e.g., Chrome DevTools)

### Target Environment

- Web platform
- Access to Autodesk admin panel at https://admin.b360.autodesk.com
- Authenticated session as admin user

### Initial Access Requirements

- Valid admin credentials for Autodesk B360
- Network access to the admin portal

## Detailed Attack Procedures

### Step 1: Inject Malicious Payload
procedure: [[procedures/Inject-Stored-XSS-Payload-in-Custom-Integration]]

**Objective**: Inject a stored XSS payload into the Custom Integration feature, which persists and executes JavaScript when other users view the integration settings.

**Instructions**: Authenticate to the admin panel, navigate to the Custom Integration section, and submit a form field with a malicious JavaScript payload such as `<script>alert('XSS');</script>`. Use browser developer tools to intercept and modify the request if needed, ensuring the payload bypasses any basic filters.

**Expected Output**: The payload is stored successfully without errors, and upon viewing the integration by another user, the JavaScript executes (e.g., alert popup appears).

**Success Indicators**:
- Payload submission succeeds without validation errors
- JavaScript executes in the victim's browser session when viewing the affected content

## Attack Chain Summary

### Key Achievements

1. Successful injection of persistent JavaScript code into the admin panel's Custom Integration feature
2. Execution of the payload in the context of other authenticated users' sessions
3. Potential for data theft, session hijacking, or further exploitation depending on payload

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T12:00:00Z*
