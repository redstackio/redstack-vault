---
tags:
  - session-hijacking
  - broken-auth
  - cookies
  - web-auth
type: attack_chain
tools:
  - '[[tools/EditThisCookie-Extension]]'
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-to-Establish-Session]]'
  - '[[procedures/Extract-Session-Cookies]]'
  - '[[procedures/Logout-Without-Invalidation]]'
  - '[[procedures/Reuse-Cookies-for-Hijacking]]'
step_count: 4
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.655Z'
description: >-
  Demonstrates exploitation of broken session management where logout does not
  invalidate cookies, enabling indefinite session reuse for hijacking.
skill_level: beginner
impact_level: high
id: 15105965-4949-41cd-af7b-81b7f0c50ed5
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
---
# Session Hijacking via Persistent Cookies After Logout in HackerOne

Multi-stage attack chain demonstrating exploitation of broken session management in the HackerOne web application, where session cookies persist after logout, allowing attackers to hijack sessions indefinitely if cookies are stolen (e.g., via XSS).

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login and Establish Session] --> B[Extract Cookies]
    B --> C[Logout]
    C --> D[Reuse Cookies for Hijack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/EditThisCookie-Extension]]

### Target Environment

- Web platform (https://www.hackerone.com/)
- Browser with cookie management extension (e.g., Chrome)
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid HackerOne account credentials
- Direct network access to the target web application
- No prior access needed beyond account creation/login

## Detailed Attack Procedures

### Step 1: Login to Establish Session
procedure: [[procedures/Login-to-Establish-Session]]

**Objective**: Authenticate to the target application to create an active session with valid cookies.

**Instructions**: Navigate to https://www.hackerone.com/ and perform standard login using an existing or new account.

**Expected Output**: Successful login, redirect to dashboard with authenticated session.

**Success Indicators**:
- User is logged in and can access protected pages
- Session cookies are present in browser developer tools

### Step 2: Extract Session Cookies
procedure: [[procedures/Extract-Session-Cookies]]

**Objective**: Capture the session cookies while authenticated for later reuse.

**Instructions**: With the session active, use the [[tools/EditThisCookie-Extension]] to export cookies. Open the extension, select the HackerOne domain, and use the 'Export' or 'Copy' function to save cookies as JSON or text.

**Expected Output**: Cookies saved to a file (e.g., notepad.txt) containing session identifiers like _h1_session.

**Success Indicators**:
- Cookies extracted without errors
- File contains key-value pairs for session tokens

### Step 3: Logout Without Invalidation
procedure: [[procedures/Logout-Without-Invalidation]]

**Objective**: Terminate the session from the user's perspective while preserving cookie validity.

**Instructions**: Click the logout button in the HackerOne application to end the session.

**Expected Output**: User is redirected to login page, appearing logged out.

**Success Indicators**:
- Application shows login prompt
- Extracted cookies remain unchanged in the saved file

### Step 4: Reuse Cookies for Hijacking
procedure: [[procedures/Reuse-Cookies-for-Hijacking]]

**Objective**: Restore the session using saved cookies to demonstrate hijacking potential.

**Instructions**: Wait 6-8 hours, then use [[tools/EditThisCookie-Extension]] to import the saved cookies back into the browser for the HackerOne domain. Refresh the page or navigate to a protected area.

**Expected Output**: Automatic authentication without credentials, access to dashboard as the original user.

**Success Indicators**:
- Session restored without re-login
- Access to victim-protected resources post-logout

## Attack Chain Summary

### Key Achievements

1. Established and extracted persistent session cookies
2. Demonstrated logout does not invalidate cookies
3. Regained access after hours, proving hijacking feasibility
4. Highlighted risk when combined with cookie theft vectors like XSS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
