---
id: proc-dod-create-test-accounts
tags:
  - account-creation
  - dod
  - web
  - setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:25:33.774Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Accounts-in-DoD-JOINOnline

## Summary

This procedure outlines the creation and login to two test accounts in the DoD JOINOnline web application, providing the foundation for testing IDOR vulnerabilities by establishing attacker and target profiles with known IDs.

## Description

In the context of exploiting IDOR in the DoD JOINOnline application, initial setup involves creating authenticated test accounts. Access the board introduction page at https://www.████████/JOINOnline/Board/BoardIntro/1021/<ID>/False, submit required form data for demographics, and log in. This simulates real users and assigns sequential numeric IDs (e.g., 1328 for attacker, 1327 for target). No tools are strictly needed beyond a browser, but a proxy like Burp Suite can monitor traffic. Prerequisites include internet access and basic knowledge of web forms. Expected outcome: Two functional accounts ready for profile manipulation testing.

## Requirements

1. Internet access to the DoD JOINOnline domain (https://www.████████/)
2. Valid registration credentials or ability to create new accounts
3. Browser for form submission (e.g., Chrome with proxy configured if using Burp)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation endpoints to prevent abuse
- Monitor for unusual sequential ID usage or rapid account setups from the same IP
- Use CAPTCHA or multi-factor authentication during registration

## Objectives

1. Establish authenticated sessions for attacker and target simulations
2. Obtain known user IDs for IDOR parameter manipulation
3. Prepare environment for request interception and modification

## Instructions

### Step 1: Access Board Introduction Endpoint

**Context**: Navigate to the account setup page and prepare to submit initial data.

No specific command; use a browser to visit https://www.████████/JOINOnline/Board/BoardIntro/1021/1328/False for User-A and https://www.████████/JOINOnline/Board/BoardIntro/1021/1327/False for User-B.

> Fill in basic required fields and submit to create accounts. Expected output: Account confirmation and login prompt.

### Step 2: Log In and Verify Access

**Context**: Authenticate each account to confirm access to profile sections.

No command; log in via the application's login form.

> Upon success, navigate to Biographical-Info to ensure profile editing is available. Expected output: Dashboard access with user ID visible in requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[account-creation]]
- [[dod]]
- [[web]]
- [[setup]]
