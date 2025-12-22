---
id: proc-login-non-admin-error
tags:
  - path-traversal
  - initial-access
  - saba-lms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:00.486Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Login with Non-Admin Account to Trigger Error

## Summary

This procedure authenticates a standard user to the Saba LMS login page, triggering an error page that serves as an entry point for path traversal exploitation, allowing subsequent unauthorized access without admin credentials.

## Description

In the Saba LMS web application, logging in with a non-admin account redirects to a custom error page due to privilege checks. This error state exposes a vulnerable session context where URL manipulation can traverse to admin paths. The target is a public-facing web app, and the procedure requires only basic user credentials. Expected outcomes include session establishment and error page access, paving the way for privilege escalation and data exfiltration such as IPs, passwords, and configurations.

## Requirements

1. Valid non-admin username and password for the Saba LMS
2. Network access to the target URL (e.g., https://target.com/)
3. Web browser for manual navigation

## Defense

Defensive measures and detection strategies:

- Implement strict authentication checks on all post-login redirects
- Use web application firewalls (WAF) to detect anomalous URL patterns
- Log and monitor login errors for unusual follow-on requests to /home or admin paths

## Objectives

1. Establish an authenticated session with restricted privileges
2. Reach the error page to identify vulnerable navigation points
3. Prepare for path traversal to admin resources

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the application's login endpoint to initiate authentication.

No command required; use browser to visit https://target.com/ and enter non-admin credentials.

> Upon submission, the application processes the login and redirects to https://target.com/Saba/[custom-context]/CustomLogin.jsp with an error message.

### Step 2: Verify Error Page

**Context**: Confirm the error state, which indicates successful but restricted login.

Inspect the page for the error text: "There was an error while processing your request. Please try again. If the problem persists, please contact the help desk at [email]."

> This confirms the session is active but non-admin, ready for traversal.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[path-traversal]]
- [[initial-access]]
