---
tags:
  - web-access
  - preparation
type: procedure
tools:
  - '[[tools/Browser-Developer-Console]]'
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
updated_at: '2025-12-14T17:30:17.966Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 6e126e2f-532b-4593-9793-ba126b9f0fd7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Target-and-Prepare-Console

## Summary

This procedure establishes initial access to the target web application and sets up the browser environment for subsequent JavaScript injections to test CSP configurations.

## Description

In the context of exploiting CSP misconfigurations on public-facing websites like https://portswigger.net/, this step involves navigating to the site and opening the developer tools console. It requires no authentication and serves as the foundation for dynamic payload execution. Expected outcomes include a loaded page session where CSP is active but vulnerable to dynamic manipulations due to missing directives like img-src.

## Requirements

1. Modern web browser (e.g., Chrome, Firefox) with developer tools enabled.
2. Network connectivity to https://portswigger.net/.
3. No special credentials; public access suffices.

## Defense

Defensive measures and detection strategies:

- Implement strict CSP with comprehensive directives (e.g., img-src 'self').
- Monitor browser console access via client-side logging or session analytics.

## Objectives

1. Gain a valid session on the target site.
2. Prepare for JavaScript-based testing.
3. Validate initial page load without anomalies.

## Instructions

### Step 1: Navigate to Target

**Context**: Access the vulnerable endpoint to establish the attack surface.

No command required; manually enter https://portswigger.net/ in the browser address bar.

> The page should load fully, establishing an HTTP session.

### Step 2: Open Developer Console

**Context**: Enable the interface for injecting and executing JavaScript payloads.

Use browser shortcut (F12) or right-click > Inspect > Console tab.

> Console opens without errors, ready for input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Console]]

## Tags

- web-access
- preparation
