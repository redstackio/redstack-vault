---
tags:
  - brute-force
  - wordpress
  - authentication
  - rate-limiting
type: attack_chain
tools:
  - '[[tools/Wfuzz]]'
  - '[[tools/Burp-Intruder]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-WordPress-Admin-Directory]]'
  - '[[procedures/Brute-Force-WordPress-Admin-Credentials]]'
step_count: 2
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:28:59.242Z'
description: >-
  A multi-step attack exploiting the absence of rate limiting on WordPress
  wp-admin authentication, allowing unrestricted brute force attempts to gain
  administrative access.
skill_level: intermediate
impact_level: high
id: 47c1c788-ce1d-40b6-b23b-0baabc3d7873
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute Force Attack on WordPress wp-admin Due to Missing Rate Limiting

Multi-stage attack chain demonstrating a complete attack workflow exploiting the lack of rate limiting on WordPress admin authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access wp-admin] --> B[Brute Force Credentials]
    B --> C[Gain Admin Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Wfuzz]]
- [[tools/Burp-Intruder]]
- SecLists wordlist (/usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt)

### Target Environment

- WordPress platform
- Web server with wp-admin endpoint exposed
- No rate limiting on authentication

### Initial Access Requirements

- Network access to the target URL (e.g., https://target.com/wp-admin)
- No prior credentials needed
- Kali Linux or similar environment with tools installed

## Detailed Attack Procedures

### Step 1: Access the wp-admin Directory
procedure: [[procedures/Access-WordPress-Admin-Directory]]

**Objective**: Identify and access the WordPress admin login endpoint to confirm the presence of an authorization form vulnerable to brute force.

**Instructions**: Navigate to the target wp-admin URL using a web browser or curl to observe the login form. This step verifies the endpoint is accessible and uses Basic Authentication or form-based login without protections.

**Expected Output**: Display of the wp-admin login page or a Basic Auth prompt.

**Success Indicators**:
- Login form loads without errors
- No immediate blocking or CAPTCHA observed

### Step 2: Perform Brute Force Attack on Authorization
procedure: [[procedures/Brute-Force-WordPress-Admin-Credentials]]

**Objective**: Exploit the lack of rate limiting by attempting multiple password guesses against the admin user to gain unauthorized access.

**Instructions**: Use [[commands/wfuzz-brute-force-wp-admin]] with a common password wordlist to fuzz the Basic Auth header. Alternatively, configure [[tools/Burp-Intruder]] to replay requests with varying passwords and monitor responses for successful logins (e.g., 200 OK vs. 401 Unauthorized).

```bash
wfuzz -c -w /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt -u https://my.stripo.email/wp-admin -d "Authorization: Basic admin:FUZZ"
```

Monitor for responses indicating a successful match, such as redirection to the dashboard or absence of authentication failure.

**Expected Output**: Tool outputs thousands of attempts without server-side blocking, potentially identifying the correct password in ~40 seconds for 3000 attempts.

**Success Indicators**:
- No account lockout or IP blocking after hundreds of failed attempts
- Successful login response (e.g., HTTP 200 with dashboard access)
- Full administrative control over the WordPress backend

## Attack Chain Summary

### Key Achievements

1. Confirmed vulnerability in wp-admin authentication without rate limits
2. Demonstrated rapid brute force capability using common tools
3. Achieved potential full site compromise via admin access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
