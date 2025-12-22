---
id: ac-csrf-dod-deletion-001
tags:
  - csrf
  - web
  - account-deletion
  - dod
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Test-Account-on-Target]]'
  - '[[procedures/Exploit-CSRF-for-Account-Deletion]]'
  - '[[procedures/Verify-Account-Deletion]]'
step_count: 3
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.125Z'
description: >-
  A multi-stage attack exploiting CSRF vulnerability to delete user accounts on
  a DoD website without authentication tokens.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# CSRF Account Deletion on DoD Website

Multi-stage attack chain demonstrating a complete attack workflow exploiting a CSRF vulnerability on a U.S. Department of Defense website to delete authenticated user accounts.

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
    A[Create and Authenticate Account] --> B[Trigger CSRF via Malicious Page]
    B --> C[Verify Account Deletion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses basic HTML and browser)

### Target Environment

- Web platform
- Access to the DoD website (e.g., https://redacted-dod-site.com)
- No special services or ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to register a new account on the target website
- Authenticated session as the victim user
- Victim must visit the attacker's malicious page while authenticated

## Detailed Attack Procedures

### Step 1: Create and Authenticate Test Account
procedure: [[procedures/Create-Test-Account-on-Target]]

**Objective**: Establish a test authenticated session to demonstrate the vulnerability.

**Instructions**: Register a new user account on the target DoD website and log in to create an active session.

**Expected Output**: Successful login with an active session cookie.

**Success Indicators**:
- User account created and login confirmed
- Access to account dashboard visible

### Step 2: Trigger CSRF Attack
procedure: [[procedures/Exploit-CSRF-for-Account-Deletion]]

**Objective**: Trick the authenticated user into submitting a forged delete request via a malicious HTML page.

**Instructions**: Create a local HTML file with a form that POSTs to the account deletion endpoint. While authenticated on the target site, open the HTML file in a browser and click the POC button to submit the request.

**Expected Output**: Silent submission of the delete request without user interaction on the target site.

**Success Indicators**:
- Form submission completes without errors
- No CSRF token validation blocks the request

### Step 3: Verify Account Deletion
procedure: [[procedures/Verify-Account-Deletion]]

**Objective**: Confirm the impact by checking for loss of access.

**Instructions**: Refresh the target website page after triggering the CSRF. Attempt to log back in to verify permanent deletion.

**Expected Output**: User is logged out and unable to re-authenticate with the same credentials.

**Success Indicators**:
- Session terminated
- Account no longer exists, requiring new registration

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of missing CSRF protections on account deletion endpoint
2. Demonstrated account takeover and deletion without direct authentication
3. Highlighted high-impact risk to authenticated users via social engineering (e.g., phishing links to malicious page)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
