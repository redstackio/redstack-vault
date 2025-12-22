---
tags:
  - xss
  - trigger
  - admin-dashboard
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 389da605-c1f8-470c-9dbd-5c528a32d17e
created_at: '2025-12-14T17:30:27.345Z'
updated_at: '2025-12-14T17:30:27.345Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Admin-Dashboard

## Summary

This procedure triggers the blind XSS by having an administrator access the vulnerable marketplace-admin-production page, where the injected User-Agent is reflected unencoded in an <option> tag, executing the malicious script.

## Description

Once the payload is stored via the login endpoint, an admin logging into sentry-test.mopub.com and navigating to the production dashboard causes the User-Agent to be inserted into HTML without escaping. The payload closes the <option> context and injects a script tag, loading external JS that runs with admin privileges, potentially stealing session data.

## Requirements

1. Valid administrative credentials for sentry-test.mopub.com
2. Payload already injected from prior procedure
3. Browser access to the admin interface

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs in admin views, particularly headers like User-Agent
- Use strict CSP to prevent script src from external domains
- Monitor admin page loads for unexpected JS execution via browser dev tools or WAF

## Objectives

1. Cause reflection of the stored payload in the admin context
2. Escape the <option> tag to inject and execute script
3. Load arbitrary JS for further exploitation

## Instructions

### Step 1: Admin Login

**Context**: Authenticate to the admin dashboard to establish a high-privilege session.

Log in at http://sentry-test.mopub.com/ using admin credentials. No command needed; use browser.

### Step 2: Navigate to Vulnerable Page

**Context**: Visit the page that reflects the User-Agent, triggering execution.

Navigate to http://sentry-test.mopub.com/exchange-marketplace/marketplace-admin-production/. The payload executes silently in the background.

> Expected: No visible alert, but script loads from attacker.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[admin-dashboard]]
