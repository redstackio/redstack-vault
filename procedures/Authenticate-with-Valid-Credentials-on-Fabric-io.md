---
id: proc-uuid-002
tags:
  - authentication
  - phishing
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:23.525Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Authenticate-with-Valid-Credentials-on-Fabric-io

## Summary

This procedure simulates or induces victim authentication on the manipulated Fabric.io login page, using valid credentials to trigger the open redirect after successful login.

## Description

Once the victim clicks the phishing link, they encounter the standard Fabric.io login form with the embedded malicious 'redirect_url'. Entering valid username and password completes authentication, causing the server to process the redirect to the attacker's site. This step relies on social engineering to get the victim to log in, exploiting the lack of parameter validation during the authentication flow. Expected outcome: Seamless login followed by unintended navigation.

## Requirements

1. Valid Fabric.io credentials (provided by victim)
2. The manipulated URL from the prior procedure
3. Web browser access for the victim

## Defense

Defensive measures and detection strategies:

- Add client-side warnings for suspicious redirect parameters before form submission
- Log and alert on login attempts with non-standard redirect URLs
- Educate users on verifying URLs before entering credentials

## Objectives

1. Complete user authentication to activate the redirect mechanism
2. Ensure the malicious parameter persists through the login process
3. Transition the victim to the attacker's controlled site

## Instructions

### Step 1: Access the Manipulated Login Page

**Context**: Victim navigates to the crafted URL, loading the login form.

Direct the victim to the URL (e.g., via email). No command needed; browser handles navigation.

> The page loads the Fabric.io login interface. Expected output: Form fields for username and password appear.

### Step 2: Submit Credentials

**Context**: Enter and submit valid credentials to authenticate.

Fill in the username and password fields and click submit.

> The form submits via POST to the endpoint, including the query parameter. Expected output: Authentication success message, then automatic redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[authentication]]
- [[Phishing]]
