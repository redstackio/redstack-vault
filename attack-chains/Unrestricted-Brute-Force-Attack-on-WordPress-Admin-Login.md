---
id: ac-uuid-bruteforce-wp-admin
tags:
  - brute-force
  - wordpress
  - authentication
  - rate-limiting
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-WordPress-Admin-Login-Endpoint]]'
  - '[[procedures/Test-Manual-Login-Attempts-for-Rate-Limiting]]'
  - '[[procedures/Intercept-HTTP-Login-Requests-with-Burp-Proxy]]'
  - '[[procedures/Automate-Brute-Force-Attack-with-Burp-Intruder]]'
step_count: 4
techniques:
  - '[[Brute Force]]'
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:29:20.497Z'
description: >-
  Attack chain exploiting the absence of rate limiting on WordPress admin login,
  enabling automated credential brute forcing to gain unauthorized admin access.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Password Guessing]]'
---
# Unrestricted Brute Force Attack on WordPress Admin Login

Multi-stage attack chain demonstrating exploitation of missing rate limiting on a WordPress admin login page, allowing unlimited brute force attempts to guess credentials and compromise the admin panel.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Admin Endpoint] --> B[Test Manual Attempts]
    B --> C[Intercept Requests]
    C --> D[Automate Brute Force]
    D --> E[Gain Admin Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with WordPress CMS
- Exposed admin login at /wp-admin/
- PHP backend

### Initial Access Requirements

- Network access to the target site (e.g., https://www.stellar.org)
- No prior credentials needed
- Browser or proxy tool for testing

## Detailed Attack Procedures

### Step 1: Discover Admin Endpoint

procedure: [[procedures/Discover-WordPress-Admin-Login-Endpoint]]

**Objective**: Identify the WordPress admin login page and confirm basic authentication requirements.

**Instructions**: Navigate to the suspected admin URL in a browser.

**Expected Output**: 401 Authorization Required response indicating basic auth protection.

**Success Indicators**:
- Admin page loads with login form
- HTTP 401 status code observed

### Step 2: Test Manual Attempts

procedure: [[procedures/Test-Manual-Login-Attempts-for-Rate-Limiting]]

**Objective**: Verify the absence of rate limiting by performing multiple failed login attempts.

**Instructions**: Enter invalid credentials repeatedly in the login form, observing server responses.

**Expected Output**: Consistent login failure responses without blocks, delays, or CAPTCHAs.

**Success Indicators**:
- No account lockout after 10+ attempts
- Server continues accepting requests

### Step 3: Intercept Requests

procedure: [[procedures/Intercept-HTTP-Login-Requests-with-Burp-Proxy]]

**Objective**: Capture and analyze HTTP requests to the login endpoint using a proxy.

**Instructions**: Configure browser to route traffic through Burp Proxy and submit a login attempt.

**Expected Output**: Captured POST request to /wp-login.php with form parameters.

**Success Indicators**:
- Requests visible in Burp Proxy history
- No TLS issues or blocks

### Step 4: Automate Brute Force

procedure: [[procedures/Automate-Brute-Force-Attack-with-Burp-Intruder]]

**Objective**: Automate credential guessing to demonstrate unauthorized access potential.

**Instructions**: Send captured request to Intruder, configure payloads for username/password fields, and launch attack.

**Expected Output**: Multiple responses showing failed attempts; potential success if weak credentials.

**Success Indicators**:
- 200 OK on successful login
- Admin dashboard access

## Attack Chain Summary

### Key Achievements

1. Confirmed exposed admin endpoint without protections
2. Validated unlimited login attempts
3. Demonstrated automated brute forcing feasibility
4. Highlighted risk of full site compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
