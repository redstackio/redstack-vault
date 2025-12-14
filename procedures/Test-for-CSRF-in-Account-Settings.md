---
tags:
  - csrf
  - testing
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 63fb1dfe-4b4b-49f2-81ab-8d0ad7644089
created_at: '2025-12-14T17:32:58.048Z'
updated_at: '2025-12-14T17:32:58.048Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Test-for-CSRF-in-Account-Settings

## Summary

This procedure tests the account settings update functionality of a web application for missing CSRF token validation, allowing unauthorized changes to user details like email.

## Description

In the FanFootage application, the account settings endpoint lacks verification of session tokens during updates, enabling attackers to forge requests from external sites. This procedure involves inspecting and simulating form submissions to confirm the vulnerability, typically in a testing environment or with permission. Prerequisites include access to a test account and knowledge of the update endpoint (e.g., POST to /account/update).

## Requirements

1. Authenticated session in the target web application
2. Browser with developer tools or a proxy like Burp Suite for request inspection
3. Knowledge of the form parameters (e.g., email field)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Enforce same-origin policy and validate referer headers
- Monitor for anomalous account changes from unexpected IPs

## Objectives

1. Confirm absence of CSRF protection in account update endpoint
2. Identify exploitable parameters like email
3. Assess potential for account manipulation

## Instructions

### Step 1: Inspect Account Settings Form

**Context**: Log in to the application and navigate to account settings to examine the update form.

Use browser developer tools to view the HTML form and note the action URL and parameters. Look for absence of a CSRF token input field.

### Step 2: Simulate Forged Request

**Context**: Attempt an update without the session token to verify vulnerability.

Craft a simple HTML form on a local file or external site targeting the endpoint:

```html
<form action="https://target.com/account/update" method="POST">
    <input type="hidden" name="email" value="test@example.com">
    <input type="submit" value="Update">
</form>
```

Submit while logged in from a different origin. If successful, the vulnerability is confirmed.

> Expected output: Email updates without token errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-testing]]
