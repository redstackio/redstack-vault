---
tags:
  - csrf
  - execute
  - verify
  - web
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
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
updated_at: '2025-12-14T17:27:15.975Z'
sub_techniques: []
id: 16607d2a-3f31-43f3-bfe7-f03585b211f5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-POC-and-Verify

## Summary

This procedure runs the CSRF POC to alter stats parameters and confirms the vulnerability's impact on the legitimate site.

## Description

With an active login, loading the POC triggers a cross-site request that modifies the stats form without user interaction. Verification involves checking the Chaturbate page for unauthorized changes, highlighting the risk of data manipulation or forced actions.

## Requirements

1. Active Chaturbate session in browser
2. Local Csrf.html file
3. Access to the stats endpoint

## Defense

Defensive measures and detection strategies:

- Deploy Content Security Policy (CSP) to restrict form submissions
- Monitor for unexpected parameter changes in user sessions

## Objectives

1. Trigger the forged request
2. Observe state change on target site
3. Validate lack of consent

## Instructions

### Step 1: Open POC in Browser

**Context**: Initiate the cross-site request.

Ensure logged into Chaturbate, then open file:// path to Csrf.html in the same browser.

### Step 2: Monitor Network

**Context**: Confirm request transmission.

Use developer tools to watch for the POST to /affiliates/stats with modified params.

### Step 3: Verify Changes

**Context**: Check impact.

Navigate back to https://chaturbate.com/affiliates/stats and observe if filters (e.g., dates) have updated to POC values.

> The stats form reflects the alterations, proving CSRF success without direct input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- csrf
- execute
