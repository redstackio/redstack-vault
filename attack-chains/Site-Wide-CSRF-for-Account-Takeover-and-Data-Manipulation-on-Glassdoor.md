---
id: ac-glassdoor-csrf-takeover-001
tags:
  - csrf
  - web
  - account-takeover
  - data-manipulation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Obtain-Reusable-CSRF-Token-from-Glassdoor]]'
  - '[[procedures/Craft-Forged-CSRF-Requests-for-Unauthorized-Actions]]'
  - '[[procedures/Exploit-CSRF-for-Account-Takeover-and-Data-Manipulation]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.834Z'
description: >-
  A multi-stage CSRF attack exploiting missing token validation on Glassdoor to
  perform unauthorized actions on job seeker and employer accounts, leading to
  takeovers and data manipulation.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Site-Wide CSRF for Account Takeover and Data Manipulation on Glassdoor

Multi-stage attack chain demonstrating a complete CSRF workflow on glassdoor.com, allowing attackers to forge requests on behalf of logged-in victims without proper token validation.

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
    A[Obtain CSRF Token] --> B[Craft Forged Requests]
    B --> C[Exploit for Takeover/Manipulation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for inspecting requests

### Target Environment

- Web platform: www.glassdoor.com
- Victim must be logged in as job seeker or employer
- Attacker needs to host malicious HTML page or use social engineering to trick victim into visiting it

### Initial Access Requirements

- No prior credentials needed for attacker
- Victim's active session on glassdoor.com
- Network access to glassdoor.com

## Detailed Attack Procedures

### Step 1: Obtain Reusable CSRF Token
procedure: [[procedures/Obtain-Reusable-CSRF-Token-from-Glassdoor]]

**Objective**: Retrieve a valid CSRF token from the Glassdoor server that can be reused in forged requests.

**Instructions**: Use browser developer tools to inspect a legitimate request to Glassdoor while logged in, or simulate a GET request to an endpoint that exposes the token. For example, navigate to a profile page and extract the token from the response headers or form fields.

**Expected Output**: A CSRF token value, such as a string like "csrf_token=abc123def456".

**Success Indicators**:
- Token retrieved without authentication challenges
- Token is present in server responses and can be copied for reuse

### Step 2: Craft Forged CSRF Requests
procedure: [[procedures/Craft-Forged-CSRF-Requests-for-Unauthorized-Actions]]

**Objective**: Create malicious POST requests incorporating the stolen CSRF token to mimic legitimate actions on the victim's behalf.

**Instructions**: Host a malicious HTML page on an attacker-controlled server that includes a form submitting to Glassdoor endpoints (e.g., /employer/invite-admin). Include the CSRF token in the form data. Trick the victim into visiting the page via phishing or malicious link, causing their browser to submit the request using their session cookies.

**Expected Output**: Successful HTTP 200 response from Glassdoor indicating the action was processed.

**Success Indicators**:
- Forged request accepted without validation errors
- Victim's account shows changes, like a new invite sent

### Step 3: Exploit for Account Takeover and Data Manipulation
procedure: [[procedures/Exploit-CSRF-for-Account-Takeover-and-Data-Manipulation]]

**Objective**: Use forged requests to achieve account takeover on employer accounts or manipulate data on job seeker accounts.

**Instructions**: Target specific endpoints: For employers, forge a request to invite an attacker-controlled email as admin; for job seekers, forge requests to edit profiles, add reviews/salaries/photos, or delete CVs. Repeat Step 2 for each action, using the same token.

**Expected Output**: Confirmation of admin invite, profile updates, or CV deletion in the victim's account.

**Success Indicators**:
- Attacker gains admin access to employer account
- Unauthorized changes visible in job seeker profile or reviews

## Attack Chain Summary

### Key Achievements

1. Bypassed CSRF protections site-wide on glassdoor.com
2. Enabled full account actions without victim interaction beyond visiting a malicious page
3. Achieved employer account takeover and job seeker data compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
