---
id: proc-001
tags:
  - open-redirect
  - twitter
  - web
type: procedure
tools:
  - '[[tools/site24x7-ip-finder]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:23.235Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Discover Open Redirect in Twitter Mobile URL Path

## Summary

This procedure identifies an open redirect vulnerability in Twitter's mobile web interface by manipulating URL paths with double slashes, allowing redirection to arbitrary endpoints during message form submissions and potential leakage of the CSRF authenticity_token.

## Description

The attack targets the messages endpoint at mobile.twitter.com, where a double slash (//) followed by a path segment causes the form to submit to an unintended location. Dots are blocked in paths to prevent direct domain specification, but numeric paths (simulating IPs) succeed. This enables testing redirects to sites like example.com, where the authenticity_token is POSTed upon submission. Prerequisites include a browser with mobile emulation and access to Twitter without authentication for initial testing.

## Requirements

1. Browser supporting mobile user-agent emulation (e.g., Chrome DevTools).
2. Access to mobile.twitter.com.
3. Developer tools to inspect network requests.

## Defense

Defensive measures and detection strategies:

- Implement strict URL path validation to canonicalize double slashes and block numeric IP-like paths.
- Use same-site cookies and robust CSRF token binding to prevent leakage exploitation.
- Monitor for anomalous POST requests to external domains from internal forms.

## Objectives

1. Confirm open redirect behavior in URL handling.
2. Observe authenticity_token transmission to redirected endpoints.
3. Validate vulnerability for further exploitation.

## Instructions

### Step 1: Construct Vulnerable URL

**Context**: Build a URL with double slash to test basic redirection.

No command required; manually construct https://mobile.twitter.com//example/messages and load in browser.

> Load the page in Chrome with mobile emulation. Observe that the messages form appears to load from Twitter but prepares to submit elsewhere.

### Step 2: Test Form Submission

**Context**: Submit the form to confirm token leakage.

No command; fill a dummy message and click send while monitoring Network tab in DevTools.

> Inspect the POST request; it should target https://example.com with authenticity_token in the payload.

### Step 3: Test Numeric Path Redirection

**Context**: Verify bypass of dot blocking using numbers.

Construct https://mobile.twitter.com//0/messages and submit form.

> This redirects to 0.0.0.0; extend with longer numbers (e.g., 2130706433 for 127.0.0.1) to confirm IP simulation works.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/site24x7-ip-finder]]

## Tags

- open-redirect
- twitter-mobile
- url-manipulation
