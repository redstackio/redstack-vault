---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - csrf
  - privilege-escalation
  - router
  - ubiquiti
  - edgeos
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
  - Router
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Gain-Operator-Access-to-Ubiquiti-EdgeOS]]'
  - '[[procedures/Craft-Malicious-CSRF-Page-for-Backup-Replacement]]'
  - '[[procedures/Lure-Admin-and-Execute-Privilege-Escalation]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:27:36.128Z'
description: >-
  A multi-stage attack exploiting a CSRF vulnerability in the Ubiquiti EdgeOS
  router's configuration backup feature to bypass Referer whitelist protection,
  allowing an operator user to escalate privileges to admin level by luring a
  root user to an attacker-controlled page.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# CSRF Bypass in Ubiquiti EdgeOS Configuration Backup for Operator to Admin Privilege Escalation

Multi-stage attack chain demonstrating a complete attack workflow exploiting a CSRF protection bypass in Ubiquiti EdgeOS version 1.9.1 and prior.

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
    A[Gain Operator Access] --> B[Craft Malicious CSRF Page]
    B --> C[Lure Admin and Execute]
    C --> D[Privilege Escalation Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for hosting and accessing the malicious page
- Basic HTML editor or text editor for crafting the CSRF payload

### Target Environment

- Ubiquiti EdgeOS router version 1.9.1 or prior
- Web interface accessible (typically port 80 or 443)
- Operator-level credentials required

### Initial Access Requirements

- Valid operator (read-only) account credentials
- Network access to the router's web interface
- Ability to host a malicious webpage (e.g., via free hosting service)

## Detailed Attack Procedures

### Step 1: Gain Operator Access
procedure: [[procedures/Gain-Operator-Access-to-Ubiquiti-EdgeOS]]

**Objective**: Obtain read-only operator access to the Ubiquiti EdgeOS web interface to prepare for CSRF exploitation.

**Instructions**: Log in to the router's web interface using operator credentials. Verify access by navigating to read-only sections like status or monitoring pages. No specific commands are needed; use the browser to authenticate.

**Expected Output**: Successful login to the web UI with operator privileges, displaying read-only dashboard.

**Success Indicators**:
- Operator dashboard accessible without admin features
- No errors on login

### Step 2: Craft Malicious CSRF Page
procedure: [[procedures/Craft-Malicious-CSRF-Page-for-Backup-Replacement]]

**Objective**: Create an HTML page that submits a forged request to the router's configuration backup endpoint, bypassing the Referer whitelist by spoofing or omitting the header.

**Instructions**: Develop a simple HTML form that auto-submits to the vulnerable backup endpoint (e.g., /api/config/backup). Include fields for uploading a malicious configuration file that grants admin privileges. Host the page on an attacker-controlled server. Test the form locally to ensure it posts correctly without triggering Referer checks.

**Expected Output**: A hosted HTML page that, when visited, automatically triggers the CSRF request to replace the router config.

**Success Indicators**:
- Form submission succeeds in a test environment
- Malicious config file prepared and referenced in the form

### Step 3: Lure Admin and Execute Privilege Escalation
procedure: [[procedures/Lure-Admin-and-Execute-Privilege-Escalation]]

**Objective**: Trick the admin (root) user into visiting the malicious page, triggering the CSRF to replace the configuration and escalate the attacker's privileges to admin level.

**Instructions**: Send a phishing link or lure the admin via email/social engineering to visit the hosted CSRF page while logged into the router as root. Upon visit, the page auto-submits the request, bypassing CSRF protections due to the Referer whitelist flaw. Monitor for successful config replacement by checking operator access post-execution.

**Expected Output**: Router configuration updated, granting admin privileges to the operator account.

**Success Indicators**:
- Admin visits the page and config is replaced
- Attacker can now access admin-only features

## Attack Chain Summary

### Key Achievements

1. Bypassed CSRF Referer whitelist protection in the backup feature
2. Escalated from operator to admin privileges without direct root access
3. Demonstrated social engineering integration for real-world exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T12:00:00Z*
