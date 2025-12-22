---
id: ac-starbucks-idor-account-takeover
tags:
  - idor
  - account-takeover
  - session-hijacking
  - web
  - php
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Shared-Resources-Between-Sites]]'
  - '[[procedures/Exploit-Endpoint-to-Obtain-PHPSESSID-Cookie]]'
  - '[[procedures/Transfer-Cookie-and-Perform-Account-Takeover]]'
step_count: 3
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:34.355Z'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) through
  shared database and PHPSESSID cookies between an alternate site and
  card.starbucks.com.sg, leading to full account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Account Takeover via IDOR on Shared Database and Cookies in Starbucks Singapore

Multi-stage attack chain demonstrating a complete attack workflow exploiting shared resources for account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Shared Resources] --> B[Obtain PHPSESSID Cookie]
    B --> C[Transfer Cookie and Takeover Account]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for cookie inspection
- Proxy tool like Burp Suite for request manipulation

### Target Environment

- Web platform with PHP backend
- Shared database between main site (card.starbucks.com.sg) and alternate site
- Services: Web application, Database

### Initial Access Requirements

- Access to the alternate site
- No prior credentials needed; relies on shared session mechanisms
- Network access to both sites

## Detailed Attack Procedures

### Step 1: Discover Shared Resources
procedure: [[procedures/Discover-Shared-Resources-Between-Sites]]

**Objective**: Identify that the alternate site shares the same database and PHPSESSID cookie credentials with the main site card.starbucks.com.sg.

**Instructions**: Inspect the alternate site's network requests using browser developer tools or a proxy. Look for shared endpoints or cookie usage patterns that match the main site. Verify database interactions by observing response data or error messages indicating common backend resources.

**Expected Output**: Confirmation of shared PHPSESSID usage and database connectivity between sites.

**Success Indicators**:
- Identical cookie names (PHPSESSID) observed on both sites
- Similar response structures or data leaks indicating shared database

### Step 2: Exploit Endpoint to Obtain PHPSESSID Cookie
procedure: [[procedures/Exploit-Endpoint-to-Obtain-PHPSESSID-Cookie]]

**Objective**: Use an endpoint on the alternate site to extract the PHPSESSID cookie value due to the IDOR vulnerability.

**Instructions**: Navigate to the vulnerable endpoint on the alternate site. Trigger a request that exposes session data, such as a profile or login-related API. Capture the PHPSESSID from the response headers or body using developer tools.

**Expected Output**: Valid PHPSESSID cookie value retrieved from the alternate site's endpoint.

**Success Indicators**:
- Cookie value successfully copied without authentication on alternate site
- No access controls preventing endpoint usage

### Step 3: Transfer Cookie and Perform Account Takeover
procedure: [[procedures/Transfer-Cookie-and-Perform-Account-Takeover]]

**Objective**: Inject the stolen PHPSESSID into the main site to access user data, update password, and achieve full control.

**Instructions**: In the browser, set the PHPSESSID cookie for card.starbucks.com.sg using developer tools (Application tab > Cookies). Refresh the page to authenticate with the stolen session. Access user information, navigate to password change endpoint, and submit a new password.

**Expected Output**: Unauthorized access to account details and successful password update.

**Success Indicators**:
- User profile loads with sensitive information
- Password change succeeds, confirming takeover

## Attack Chain Summary

### Key Achievements

1. Identified shared infrastructure leading to IDOR exposure
2. Extracted session cookie from alternate site
3. Achieved full account takeover on main site

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
