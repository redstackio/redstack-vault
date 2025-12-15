---
id: ac-twitter-remember-me-persistence-37822
tags:
  - authentication
  - cookies
  - persistence
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/FireBug]]'
tactics:
  - '[[Persistence]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-with-Remember-Me-Enabled]]'
  - '[[procedures/Inspect-Authentication-Cookies]]'
step_count: 2
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:20.593Z'
description: >-
  Demonstrates the vulnerability in Twitter's 'Remember Me' feature where
  authentication cookies are set with a 10-year expiration, enabling long-term
  unauthorized access if cookies are stolen via device compromise or XSS.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Persistence]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
---
# Twitter Remember Me Functionality Abuse for Persistent Account Access

Multi-stage attack chain demonstrating the identification and potential exploitation of long-lived authentication cookies in Twitter's login process, leading to persistent unauthorized access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login with Remember Me] --> B[Inspect Cookies]
    B --> C[Potential Cookie Theft and Reuse]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/FireBug]]

### Target Environment

- Web platform (Twitter login page at https://twitter.com/login)
- Browser with developer tools (Firefox with FireBug extension)
- Valid Twitter credentials for testing

### Initial Access Requirements

- Network access to Twitter's login page
- No prior access needed; public-facing web application
- User account credentials

## Detailed Attack Procedures

### Step 1: Login with Remember Me Enabled
procedure: [[procedures/Login-with-Remember-Me-Enabled]]

**Objective**: Authenticate to Twitter while enabling the 'Remember Me' feature to trigger the setting of long-lived authentication cookies.

**Instructions**: Navigate to the Twitter login page, enter credentials, check the 'Remember Me' checkbox, and submit the login form.

**Expected Output**: Successful login with cookies 'auth_token' and 'remember_checked_on' set in the browser.

**Success Indicators**:
- User is redirected to the Twitter dashboard
- Cookies are present in browser storage

### Step 2: Inspect Authentication Cookies
procedure: [[procedures/Inspect-Authentication-Cookies]]

**Objective**: Examine the set cookies to identify their excessively long expiration dates, highlighting the persistence risk.

**Instructions**: Use browser developer tools to view cookie details post-login, focusing on expiration timestamps.

**Expected Output**: Cookies with expiration around November 2024 (from a 2014 login), indicating ~10 years validity.

**Success Indicators**:
- 'auth_token' cookie expiration is ~3651 days
- Confirmation of persistent storage without short-term limits

## Attack Chain Summary

### Key Achievements

1. Successful authentication with persistent cookies enabled
2. Identification of long expiration dates on auth cookies
3. Demonstration of risk for cookie theft scenarios leading to decade-long access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Persistence]] Persistence
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
