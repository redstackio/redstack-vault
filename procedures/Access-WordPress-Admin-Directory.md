---
id: proc-uuid-1
tags:
  - reconnaissance
  - wordpress
type: procedure
tools:
  - '[[tools/Burp-Intruder]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:59.240Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Access-WordPress-Admin-Directory

## Summary

This procedure involves navigating to the WordPress wp-admin directory to identify the authentication mechanism and confirm the absence of protective measures like CAPTCHAs or rate limiting, setting the stage for brute force exploitation.

## Description

In a typical WordPress deployment, the /wp-admin endpoint handles administrative logins. This procedure targets sites where authentication relies on Basic Auth or simple form submissions without defenses, allowing attackers to probe for vulnerabilities. The expected outcome is confirmation of an unprotected login interface, enabling subsequent brute force attempts. Prerequisites include direct network access to the target URL.

## Requirements

1. Web browser or HTTP client like curl
2. Network connectivity to the target (e.g., https://target.com/wp-admin)
3. No authentication credentials required for initial access

## Defense

Defensive measures and detection strategies:

- Implement IP-based rate limiting on wp-admin endpoints
- Enable CAPTCHA or multi-factor authentication for logins
- Monitor access logs for repeated failed attempts from single IPs

## Objectives

1. Verify the existence and accessibility of the wp-admin login form
2. Observe the authentication method (e.g., Basic Auth)
3. Confirm no immediate blocking mechanisms are in place

## Instructions

### Step 1: Navigate to wp-admin Endpoint

**Context**: Use a browser or HTTP tool to load the admin directory and inspect the response.

**Command** (Manual browser access or curl):
```bash
curl -v https://my.stripo.email/wp-admin
```

> This command sends a GET request and displays verbose output, including headers. Expected output includes a 200 OK with HTML login form or a 401 prompting Basic Auth, without any rate limit warnings.

### Step 2: Inspect for Protections

**Context**: Manually attempt a few invalid logins to test for lockouts.

**Instructions**: Enter incorrect credentials 5-10 times and observe if the server responds consistently without delays or blocks.

**Expected Output**: Consistent error messages (e.g., "Invalid username or password") without session termination.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Intruder]]

## Tags

- [[Reconnaissance]]
- [[wordpress]]
