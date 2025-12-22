---
id: 2173f50f-826c-449f-864b-b1097abb8b00
name: >-
  Stored XSS in User Profile City Field Leading to Cookie Theft and Account
  Takeover
type: attack_chain
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in the City field
  of user profiles on devicelock.com to inject payloads, trigger execution on
  profile views, and steal cookies for potential account takeover.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.097Z'
procedures:
  - '[[procedures/Create-User-Account-for-XSS-Injection]]'
  - '[[procedures/Inject-XSS-Payload-into-City-Field]]'
  - '[[procedures/Trigger-Stored-XSS-by-Viewing-Profile]]'
  - '[[procedures/Escalate-XSS-to-Cookie-Stealing]]'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
tags:
  - xss
  - stored-xss
  - cookie-theft
  - account-takeover
  - web-vulnerability
platforms:
  - Web
tools:
  - '[[tools/xsshunter]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---

# Stored XSS in User Profile City Field Leading to Cookie Theft and Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting stored XSS on devicelock.com to steal user cookies and enable account takeover.

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
    A[Create Account] --> B[Inject XSS Payload]
    B --> C[View Profile to Trigger]
    C --> D[Steal Cookies]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/xsshunter]]

### Target Environment

- Web platform using PHP and Bitrix CMS
- Access to devicelock.com forum and admin user edit pages
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- No prior credentials needed; public registration available
- Attacker must host a server for cookie grabbing (e.g., grabber.php)
- Network access to the target site

## Detailed Attack Procedures

### Step 1: Create User Account
procedure: [[procedures/Create-User-Account-for-XSS-Injection]]

**Objective**: Establish a user account to access profile editing features for payload injection.

**Instructions**: Navigate to the registration page and complete the signup process with basic details.

**Expected Output**: Successful account creation with a user ID assigned.

**Success Indicators**:
- Confirmation email or login success
- User ID visible in profile URL

### Step 2: Inject XSS Payload
procedure: [[procedures/Inject-XSS-Payload-into-City-Field]]

**Objective**: Store a malicious JavaScript payload in the City field via the admin user edit interface.

**Instructions**: Access the user edit page, locate the Personal Information section, and insert the payload into the City input before applying changes.

**Expected Output**: Payload saved without errors, stored in the database.

**Success Indicators**:
- No validation errors on apply
- Profile updates successfully

### Step 3: Trigger Stored XSS
procedure: [[procedures/Trigger-Stored-XSS-by-Viewing-Profile]]

**Objective**: Execute the stored payload by rendering the profile page, demonstrating arbitrary JavaScript execution.

**Instructions**: Visit the profile view URL with the user ID to load and execute the injected script.

**Expected Output**: Alert or script execution in the browser console.

**Success Indicators**:
- JavaScript alert pops up
- Document cookies displayed

### Step 4: Escalate to Cookie Theft
procedure: [[procedures/Escalate-XSS-to-Cookie-Stealing]]

**Objective**: Redirect victim browsers to an attacker-controlled server to exfiltrate session cookies for account takeover.

**Instructions**: Replace the basic payload with a redirecting script, host the grabber on your server, and have a victim view the profile.

**Expected Output**: Cookies logged on attacker's server.

**Success Indicators**:
- Cookies appended to grabber.php log file
- Potential session hijacking confirmed

## Attack Chain Summary

### Key Achievements

1. Successful injection and storage of XSS payload in user profile
2. Arbitrary JavaScript execution on profile views
3. Cookie exfiltration leading to session theft
4. Potential full account takeover via stolen credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
