---
tags:
  - open-redirect
  - web
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
id: 26b1e14f-9aeb-422c-9fef-aaf06f64094c
created_at: '2025-12-14T17:24:34.778Z'
updated_at: '2025-12-14T17:24:34.778Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Redirect

## Summary

This procedure activates the modified link to confirm the open redirect, observing navigation to the external malicious URL.

## Description

After modification, clicking the link tests if the browser follows the external HREF without restrictions. On sites like xnxx.com, this succeeds due to no validation, allowing phishing vectors. The outcome is redirection, validating the exploit.

## Requirements

1. Modified HREF in place
2. Browser ready for navigation
3. Test external URL (non-malicious for verification)

## Defense

Defensive measures and detection strategies:

- Add redirect confirmation dialogs for external links
- Log and alert on unexpected redirects

## Objectives

1. Execute the link click
2. Observe redirection
3. Confirm vulnerability

## Instructions

### Step 1: Activate Link

**Context**: Simulate user interaction to trigger the exploit.

No specific command; perform manually:

In [[tools/Web-Browser]], click the modified link on the page.

> The browser should redirect to the external URL (e.g., https://google.com) without warnings, confirming the open redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[open-redirect]]
- [[web]]
