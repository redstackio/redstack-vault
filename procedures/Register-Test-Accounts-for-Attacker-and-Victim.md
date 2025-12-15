---
id: proc-register-test-accounts-001
name: Register Test Accounts for Attacker and Victim
tags:
  - setup
  - test-accounts
  - authentication-bypass
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.692Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Register Test Accounts for Attacker and Victim

## Summary

This procedure sets up a controlled environment by registering two test accounts on the target web application—one for the attacker and one simulating a victim—to facilitate testing the authentication bypass without affecting real users.

## Description

In the context of exploiting an authentication bypass vulnerability, initial setup involves creating legitimate accounts to capture baseline login behavior and simulate impersonation. This is done via the application's registration endpoint, typically a web form or API call. No special tools are required beyond browser access, though Burp Suite can monitor the process. Expected outcome: Two active accounts ready for login testing, enabling safe reproduction of the vulnerability.

## Requirements

1. Network access to the target web application registration page
2. Valid email addresses for registration (e.g., attacker@test.com, victim@test.com)
3. No prior authentication needed

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on registration endpoints to prevent abuse
- Monitor for unusual registration patterns from the same IP
- Use CAPTCHA on signup forms to deter automated account creation

## Objectives

1. Establish attacker account for capturing legitimate requests
2. Create victim account to target for impersonation
3. Ensure accounts are verifiable for post-exploitation testing

## Instructions

### Step 1: Access Registration Page

**Context**: Navigate to the application's signup functionality to create accounts.

No specific command; use a web browser to visit the registration URL (e.g., https://████████/register) and fill in details for the attacker account first.

> Submit the form with email (e.g., attacker+test@domain.com), password, and any required fields. Confirm via email if needed.

### Step 2: Register Victim Account

**Context**: Repeat for the victim to simulate a target user.

No specific command; use the browser to register the second account with a different email (e.g., victim+test@domain.com).

> Ensure both accounts are active and can log in normally before proceeding to capture requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[setup]]
- [[test-accounts]]
