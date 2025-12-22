---
tags:
  - xss
  - payload-craft
  - url-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.444Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 0455cea1-7f1a-465a-a37e-971ef0759c18
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-XSS-Callback-URL

## Summary

This procedure constructs a malicious URL by injecting a URL-encoded XSS payload into the OWOX BI Google Analytics callback path, enabling reflection and execution upon victim access.

## Description

Targeting the unsanitized URL path in the /ui/callbacks/google-supervisors/ endpoint, this step modifies the callback after the OAuth flow. The payload <img src=xss onerror=prompt(1)> is encoded as %3Cimg%20src=xss%20onerror=prompt(1)%3E and appended after 'analytics', e.g., https://bi.owox.com/ui/callbacks/google-supervisors/analytics%3Cimg%20src=xss%20onerror=prompt(1)%3E/?state=d159b8264eef78b11afdd016531b128c&code=.... This allows arbitrary JS like session theft when reflected post-login. Requires the callback URL from the prior setup step.

## Requirements

1. Captured callback URL from OWOX BI setup
2. URL encoding knowledge or browser dev tools
3. Browser for testing the crafted URL

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all URL path parameters in callbacks
- Encode outputs to prevent HTML injection
- Log and alert on suspicious query parameters in OAuth flows

## Objectives

1. Inject XSS payload into the callback path
2. Ensure payload survives URL parsing and reflection
3. Prepare URL for phishing delivery

## Instructions

### Step 1: Identify Callback Structure

**Context**: Extract the base callback URL from the setup error link.

In browser dev tools (F12), inspect the redirect or error page to copy the full callback URL including state and code parameters.

> Expected: Base URL like https://bi.owox.com/ui/callbacks/google-supervisors/analytics/?state=...&code=....

### Step 2: Encode and Inject Payload

**Context**: Append the encoded payload to the path segment for reflection.

Modify the URL to insert %3Cimg%20src=xss%20onerror=prompt(1)%3E after 'analytics', then access in a browser to verify reflection in source.

> Expected: Payload visible in HTML without execution (until post-login).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- xss
- payload
- injection
