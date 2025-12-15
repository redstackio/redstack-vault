---
tags:
  - information-disclosure
  - path-disclosure
  - web
  - php
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-User-Account-on-Airship-CMS]]'
  - '[[procedures/Access-My-Cabins-Endpoint]]'
  - '[[procedures/Trigger-Path-Disclosure-Error]]'
step_count: 3
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:00.639Z'
description: >-
  A simple information disclosure attack that reveals the server's full file
  system path through an unhandled error in the Airship CMS cabins management
  endpoint.
skill_level: beginner
impact_level: low
id: 6ba71307-5965-4d36-90e1-c5862855e391
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Full Path Disclosure via Unhandled Error in Airship CMS

Multi-stage attack chain demonstrating a complete attack workflow for information disclosure in Airship CMS.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Registration] --> B[Endpoint Access]
    B --> C[Error Trigger and Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Web platform
- Airship CMS application
- PHP-based web server
- No specific ports or services required beyond standard HTTP/HTTPS

### Initial Access Requirements

- Internet access to the target site (airship.paragonie.com)
- No prior credentials needed
- Public-facing web application

## Detailed Attack Procedures

### Step 1: Account Registration
procedure: [[procedures/Register-User-Account-on-Airship-CMS]]

**Objective**: Gain authenticated access to the application to reach protected endpoints.

**Instructions**: Navigate to the registration page and create a new user account using valid email and password.

**Expected Output**: Successful account creation and login prompt.

**Success Indicators**:
- Confirmation email received (if enabled)
- Redirect to login page

### Step 2: Access Cabins Endpoint
procedure: [[procedures/Access-My-Cabins-Endpoint]]

**Objective**: Log in and navigate to the cabins management page to set up for error triggering.

**Instructions**: Log in with the newly created credentials and directly access the /my/cabins URL.

**Expected Output**: Page load attempt, potentially leading to error.

**Success Indicators**:
- Successful login
- URL navigation to https://airship.paragonie.com/my/cabins

### Step 3: Trigger Error and Observe Disclosure
procedure: [[procedures/Trigger-Path-Disclosure-Error]]

**Objective**: Induce an unhandled error that exposes the server's full file system path.

**Instructions**: Interact with the page or simply load it to trigger the error message displaying the installation directory path.

**Expected Output**: Error page with visible server path, such as a PHP warning or exception revealing the file system location.

**Success Indicators**:
- Full server path visible in error message
- Confirmation of information disclosure

## Attack Chain Summary

### Key Achievements

1. Successful registration and authentication
2. Access to internal management endpoint
3. Disclosure of server file system path for reconnaissance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
