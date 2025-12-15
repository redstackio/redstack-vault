---
id: proc-uuid-1
tags:
  - authentication
  - mobile
type: procedure
tools:
  - '[[tools/Google-Chrome-Mobile]]'
  - '[[tools/Microsoft-Edge-Mobile]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:45.181Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-HackerOne-on-Mobile-Browser

## Summary

This procedure logs into a HackerOne account using a mobile browser, setting up the environment to test external link handling features.

## Description

In the context of testing the domain highlighting vulnerability, authentication is required to access areas of the platform where external links may be present, such as report views or notifications. This step uses standard login mechanics on mobile Chrome or Edge, ensuring the session is active for subsequent link interactions. The target environment is the HackerOne web platform, and outcomes include a valid session that triggers platform-specific security features like the External Link Warning.

## Requirements

1. Mobile device with internet access
2. Valid HackerOne account credentials (username/email and password)
3. Latest version of Google Chrome or Microsoft Edge installed on mobile

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) on HackerOne accounts to prevent unauthorized access
- Monitor login attempts from unusual mobile user agents or IP addresses

## Objectives

1. Establish an authenticated session on HackerOne
2. Prepare for interaction with potentially malicious external links
3. Verify mobile browser compatibility with the platform

## Instructions

### Step 1: Launch Mobile Browser and Navigate

**Context**: Open the browser and access the HackerOne login page to begin authentication.

No specific command; manually navigate to https://hackerone.com/login in the mobile browser.

> Expected output: Login form loads, prompting for credentials.

### Step 2: Enter Credentials and Submit

**Context**: Provide account details to authenticate and access the dashboard.

Manually enter username/email and password, then submit the form.

> Expected output: Redirect to the HackerOne dashboard upon successful login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome-Mobile]]
- [[tools/Microsoft-Edge-Mobile]]

## Tags

- authentication
- mobile
