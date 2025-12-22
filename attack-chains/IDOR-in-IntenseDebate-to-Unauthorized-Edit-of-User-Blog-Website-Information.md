---
id: ac-idor-intensedebate-blog-edit
tags:
  - idor
  - web
  - authorization-bypass
  - account-tampering
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
  - '[[procedures/Create-Test-Accounts-for-IDOR]]'
  - '[[procedures/Add-and-Extract-Victim-Blog-ID]]'
  - '[[procedures/Prepare-Attacker-Profile-for-Interception]]'
  - '[[procedures/Intercept-and-Modify-Request-for-Unauthorized-Edit]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.123Z'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in
  IntenseDebate's user profile editing to allow unauthorized modification of any
  user's blog or website details.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in IntenseDebate to Unauthorized Edit of User Blog/Website Information

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in the IntenseDebate platform's user profile editing feature. An attacker creates test accounts, extracts a unique blog ID from a victim's profile, and uses a proxy tool to modify HTTP requests, enabling unauthorized changes to the victim's blog or website information. This leads to account tampering without authentication checks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Setup] --> B[Extract ID] --> C[Intercept Request] --> D[Unauthorized Edit]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (IntenseDebate at https://www.intensedebate.com)
- No specific ports or services beyond standard HTTPS (443)
- Internet access to the target site

### Initial Access Requirements

- Ability to register new accounts on IntenseDebate
- No prior credentials needed beyond creating test accounts
- Burp Suite configured as a proxy for browser traffic

## Detailed Attack Procedures

### Step 1: Account Setup
procedure: [[procedures/Create-Test-Accounts-for-IDOR]]

**Objective**: Establish victim and attacker accounts to simulate the IDOR scenario.

**Instructions**: Navigate to the signup page and register two separate accounts, one acting as the victim and one as the attacker. This provides the necessary authenticated sessions for subsequent steps.

**Expected Output**: Two active accounts with login credentials.

**Success Indicators**:
- Successful registration and login for both accounts
- Access to user profile editing pages

### Step 2: Victim Profile Preparation and ID Extraction
procedure: [[procedures/Add-and-Extract-Victim-Blog-ID]]

**Objective**: Add a blog to the victim's profile and extract the unique hidBlogID for later exploitation.

**Instructions**: Log in as the victim, navigate to the profile editor, add a blog/website entry, save it, then inspect the page source to locate and copy the hidBlogID value associated with 'radMainSite'.

**Expected Output**: A unique hidBlogID value (e.g., a numeric or hashed identifier) copied from the page source.

**Success Indicators**:
- Blog added successfully to victim's profile
- hidBlogID extracted without errors

### Step 3: Attacker Profile Preparation
procedure: [[procedures/Prepare-Attacker-Profile-for-Interception]]

**Objective**: Log in as the attacker and initiate a blog addition to generate an interceptable save request.

**Instructions**: Switch to the attacker's account, go to the profile editor, start adding a new blog/website, but do not save yet—prepare to intercept the save action with the proxy tool.

**Expected Output**: Profile page loaded with the 'Add Blog / Website' form ready for submission.

**Success Indicators**:
- Attacker logged in successfully
- Form for adding blog accessible

### Step 4: Request Interception and Unauthorized Modification
procedure: [[procedures/Intercept-and-Modify-Request-for-Unauthorized-Edit]]

**Objective**: Intercept the save request, replace the hidBlogID with the victim's, and forward to perform the unauthorized edit.

**Instructions**: With Burp Suite proxying traffic, submit the save request as the attacker, intercept it, modify the 'hidBlogID' parameter to the victim's value, forward the request, then verify changes by logging back into the victim's account.

**Expected Output**: Victim's blog/website information updated with attacker's changes.

**Success Indicators**:
- Modified request forwarded without errors
- Victim's profile shows unauthorized edits upon re-login

## Attack Chain Summary

### Key Achievements

1. Successful creation and management of test accounts
2. Extraction of sensitive object identifier (hidBlogID)
3. Unauthorized modification of victim data via request tampering
4. Demonstration of IDOR leading to account tampering

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
