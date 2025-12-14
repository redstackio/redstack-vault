---
id: ac-uber-xss-app-name-001
name: >-
  Stored XSS in Uber Developer Portal Application Name Leading to Arbitrary
  JavaScript Execution
tags:
  - xss
  - stored-xss
  - uber
  - developer-portal
  - javascript-execution
type: attack_chain
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
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
  - '[[procedures/Inject-Malicious-Payload-into-Uber-App-Name]]'
  - '[[procedures/Trigger-XSS-via-Uber-App-Deletion]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.814Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in the Uber
  developer portal's application name field, allowing arbitrary JavaScript
  execution in an administrator's browser during app deletion, potentially
  enabling session hijacking or data theft.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Uber Developer Portal Application Name Leading to Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating a complete stored XSS workflow in Uber's developer portal at https://login.uber.com/applications.

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
    A[Payload Injection] --> B[Trigger Execution]
    B --> C[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]
- [[tools/Chrome]]

### Target Environment

- Web platform
- Access to Uber developer portal at https://login.uber.com/applications
- Valid Uber developer account credentials

### Initial Access Requirements

- Authenticated session as a developer
- No special privileges beyond standard app creation/deletion
- Network access to Uber's login domain

## Detailed Attack Procedures

### Step 1: Payload Injection
procedure: [[procedures/Inject-Malicious-Payload-into-Uber-App-Name]]

**Objective**: Create a new application with a stored XSS payload in the name field to persist malicious JavaScript.

**Instructions**: Log in to the Uber developer portal and navigate to the applications section. Enter the payload "><img src=x onerror=prompt(1)> as the application name while creating a new app. Save the application to store the payload.

**Expected Output**: Application created successfully with the malicious name reflected in the list without immediate execution.

**Success Indicators**:
- Application appears in the list with the injected payload visible in the name field
- No errors during creation

### Step 2: Trigger Execution
procedure: [[procedures/Trigger-XSS-via-Uber-App-Deletion]]

**Objective**: Interact with the malicious application (e.g., via deletion) to trigger the XSS payload in the victim's browser context.

**Instructions**: From the applications list, select the maliciously named app and initiate deletion. The payload executes during the rendering of the app name in the deletion confirmation or list view.

**Expected Output**: A JavaScript alert or prompt (e.g., prompt(1)) appears in the browser, confirming execution.

**Success Indicators**:
- Arbitrary JavaScript runs, such as a prompt dialog
- Potential for further exploitation like cookie theft if payload is escalated

## Attack Chain Summary

### Key Achievements

1. Successful injection of stored XSS payload into application metadata
2. Triggering of payload execution in an authenticated user's browser
3. Demonstration of high-impact client-side attack potential, including session hijacking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
