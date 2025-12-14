---
id: ac-stored-xss-airship-author
tags:
  - xss
  - stored-xss
  - cms-airship
  - php
  - twig
  - docker
type: attack_chain
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-CMS-Airship-via-Docker]]'
  - '[[procedures/Register-and-Login-to-Airship]]'
  - '[[procedures/Create-Malicious-Author-Profile]]'
  - '[[procedures/Trigger-Stored-XSS-as-Admin]]'
step_count: 7
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.825Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in CMS Airship's
  author name field to inject and execute malicious JavaScript when an admin
  views the edit page, potentially leading to session theft.
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in CMS Airship Author Profiles for Admin JavaScript Execution

Multi-stage attack chain demonstrating exploitation of a stored Cross-Site-Scripting (XSS) vulnerability in CMS Airship version 1.1.0's author profiles feature. The attack involves installing the CMS, registering an account, injecting a malicious script into an author name, and tricking an admin into viewing the edit page to trigger JavaScript execution, which could lead to session theft or other client-side attacks, though partially mitigated by CSP.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install CMS Airship] --> B[Register Account]
    B --> C[Login and Create Author]
    C --> D[Inject Malicious Payload]
    D --> E[Share Edit Link]
    E --> F[Admin Views Edit Page]
    F --> G[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#e67e22
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Docker]]

### Target Environment

- Web platform running CMS Airship 1.1.0
- Ports 8080 (main app) and 8081 (bridge)
- PHP with Twig templating
- Docker for installation

### Initial Access Requirements

- Local network access to the target instance
- No prior credentials needed; registration must be enabled

## Detailed Attack Procedures

### Step 1: Install CMS Airship
procedure: [[procedures/Install-CMS-Airship-via-Docker]]

**Objective**: Set up a vulnerable instance of CMS Airship using Docker to enable registration and exploration.

**Instructions**: Use Docker to pull and run the CMS Airship image with default settings.

**Expected Output**: CMS Airship accessible at http://localhost:8080 and bridge at http://localhost:8081.

**Success Indicators**:
- Application loads without errors
- Registration feature is enabled

### Step 2: Register a New Account
procedure: [[procedures/Register-and-Login-to-Airship]]

**Objective**: Create a low-privilege user account to access author creation features.

**Instructions**: Navigate to the registration page and submit valid user details.

**Expected Output**: Successful account creation with login prompt.

**Success Indicators**:
- User registered
- Able to access login page

### Step 3: Login with New Account
procedure: [[procedures/Register-and-Login-to-Airship]]

**Objective**: Authenticate as the registered user to gain access to author management.

**Instructions**: Enter credentials at the login endpoint.

**Expected Output**: Dashboard or main interface loads.

**Success Indicators**:
- Session established
- Navigation to author creation possible

### Step 4: Navigate to Create New Author
procedure: [[procedures/Create-Malicious-Author-Profile]]

**Objective**: Access the form for creating a new author profile.

**Instructions**: From the authenticated session, go to the author creation URL.

**Expected Output**: Author creation form displayed.

**Success Indicators**:
- Form fields visible, including name input

### Step 5: Create Author with Malicious Name
procedure: [[procedures/Create-Malicious-Author-Profile]]

**Objective**: Inject a stored XSS payload into the author name field.

**Instructions**: Submit the form with payload `<script>alert(1)</script>` in the name field.

**Expected Output**: Author created successfully; payload stored.

**Success Indicators**:
- Author profile saved
- No immediate errors on submission

### Step 6: Share Author Edit Link
procedure: [[procedures/Trigger-Stored-XSS-as-Admin]]

**Objective**: Obtain and distribute the edit link to a privileged user.

**Instructions**: Copy the edit URL for the created author (e.g., http://localhost:8080/bridge/author/edit/3).

**Expected Output**: Valid edit link generated.

**Success Indicators**:
- Link accessible and points to the vulnerable page

### Step 7: Open Edit Link as Admin
procedure: [[procedures/Trigger-Stored-XSS-as-Admin]]

**Objective**: Trigger the XSS by having an admin view the edit page, executing the payload.

**Instructions**: As admin, access the shared link; observe script execution or CSP violation.

**Expected Output**: Alert box or console warning indicating XSS attempt.

**Success Indicators**:
- JavaScript executes in admin's browser context
- Potential for session theft if CSP bypassed

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of vulnerable CMS Airship instance
2. Injection of stored XSS payload via author name without sanitization
3. Triggering of JavaScript execution in admin context, demonstrating impact on privileged users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
