---
tags:
  - csrf
  - authentication
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
updated_at: '2025-12-14T17:33:06.100Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 29537aa7-e541-4597-815c-b557147fcf37
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Login-and-Obtain-Fixed-fkey

## Summary

This procedure authenticates an attacker account on Khan Academy to establish a session and acquire the fixed CSRF 'fkey' token, which does not change across sessions.

## Description

In the context of CSRF token fixation, logging into the target web application generates a session-bound token that remains static even after logout. This procedure targets Khan Academy's login flow at https://www.khanacademy.org, where the fkey is embedded in forms for CSRF protection but fails to regenerate, enabling later exploitation. Prerequisites include valid attacker credentials and a standard web browser.

## Requirements

1. Valid Khan Academy account credentials
2. Web browser with developer tools enabled
3. Internet access to https://www.khanacademy.org

## Defense

Defensive measures and detection strategies:

- Implement dynamic CSRF tokens tied to sessions that regenerate on login/logout
- Monitor for anomalous login patterns from shared IPs/devices
- Use browser fingerprinting to detect session sharing

## Objectives

1. Gain authenticated access to observe the fixed fkey
2. Verify token persistence for exploitation
3. Prepare for token extraction in subsequent steps

## Instructions

### Step 1: Navigate and Authenticate

**Context**: Access the login page and submit credentials to create a session with the fixed fkey.

Open https://www.khanacademy.org in a browser and enter attacker credentials in the login form. Submit to authenticate.

> Upon success, the dashboard loads, and the fkey is set in the browser's local storage or forms.

### Step 2: Verify Session and Token Presence

**Context**: Confirm the session is active and inspect for the fkey.

Use browser developer tools (F12) to inspect network requests or form elements on the dashboard page.

> Look for 'fkey' parameter in POST requests or hidden form fields; note its value as it will remain fixed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-login]]
