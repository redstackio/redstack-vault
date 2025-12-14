---
tags:
  - open-redirect
  - web
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
id: 064ed009-851e-4270-8201-52817ab6c27b
created_at: '2025-12-14T17:24:34.783Z'
updated_at: '2025-12-14T17:24:34.783Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-HREF-for-Redirect

## Summary

This procedure alters the identified HREF attribute from an internal path to an external URL, enabling the open redirect to a malicious site.

## Description

Editing the HREF in dev tools simulates how an attacker could craft phishing links or exploit the site. For xnxx.com, changing '/todays-selection/2' to 'https://google.com' tests the lack of validation. This client-side change doesn't affect the server but demonstrates the vulnerability when triggered.

## Requirements

1. Located HREF in dev tools
2. External URL ready (e.g., for testing or phishing)
3. Browser allowing DOM edits

## Defense

Defensive measures and detection strategies:

- Validate all URLs server-side against a whitelist
- Use JavaScript to enforce internal links only

## Objectives

1. Replace internal HREF with external
2. Save the modification
3. Verify change in inspector

## Instructions

### Step 1: Edit Attribute

**Context**: Directly modify the DOM element.

No specific command; perform manually:

In [[tools/Browser-Developer-Tools]] Elements panel, double-click the HREF value and replace '/todays-selection/2' with 'https://google.com'.

> Press Enter to apply; the attribute updates in real-time without page reload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[open-redirect]]
- [[web]]
