---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - session-hijacking
  - valid-accounts
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.746Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Hijack Session and Navigate to Password Change

## Summary

Using stolen session cookies, impersonate the victim to access the password change feature on Twitter Flight School.

## Description

After obtaining cookies via XSS, import them into the attacker's browser to hijack the session. Navigate to the profile settings to reach the password update form, which triggers a POST request vulnerable to brute-forcing. This step assumes Burp Suite is proxying traffic for interception.

## Requirements

1. Stolen session cookies from XSS
2. Browser configured with proxy (Burp)
3. Victim's account active

## Defense

Defensive measures and detection strategies:

- Bind sessions to IP or user-agent
- Implement session token rotation on suspicious activity
- Log and alert on multiple failed password change attempts from same session

## Objectives

1. Gain authenticated access as victim
2. Reach password change endpoint
3. Prepare for brute-force exploitation

## Instructions

### Step 1: Import Cookies

**Context**: Load stolen cookies into browser dev tools or extension to hijack session.

In Firefox DevTools (F12) > Storage > Cookies, add the stolen auth cookies.

> Expected output: Browser now shows victim's logged-in state.

### Step 2: Navigate to Password Change

**Context**: Access the change password form to trigger the vulnerable POST.

Go to My Profile > Edit Profile > Change Password. Enter random new password and click Next.

> Expected output: POST request to password endpoint intercepted if proxied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- session-hijacking
