---
id: proc-trigger-redirect-001
tags:
  - open-redirect
  - phishing
  - firefox
type: procedure
tools:
  - '[[tools/Firefox-Browser-for-Redirect-Testing]]'
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:23.262Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Trigger-Open-Redirect-with-Crafted-URL

## Summary

This procedure exploits the open redirect by accessing a crafted URL in Firefox, causing a 301 redirect to an arbitrary external site due to the plugin's failure to validate // prefixed paths.

## Description

In the vulnerable setup, requesting //google.com/%2e%2e results in a redirect location of //google.com/%2e%2e/, which Firefox interprets as https://www.google.com/. This differs from other browsers (Chrome, Edge, etc.), which block or handle it differently. Impacts include phishing, SSRF gadget usage, and OAuth token stealing.

## Requirements

1. Running vulnerable server on localhost:3000
2. Firefox browser installed
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Normalize paths to remove leading // and validate against allowed domains
- Use Content-Security-Policy headers to restrict navigations
- Detect anomalous redirects in WAF logs or browser dev tools

## Objectives

1. Send GET request to trigger 301 redirect
2. Achieve redirection to external malicious site
3. Validate exploit success via browser navigation

## Instructions

### Step 1: Open Browser and Navigate

**Context**: Use Firefox to access the crafted path, as it uniquely follows the // redirect.

No command; manually enter URL: http://localhost:3000//google.com/%2e%2e

> Browser sends GET / /google.com/%2e%2e. Server responds with 301 Location: //google.com/%2e%2e/. Expected output: Automatic redirect to https://www.google.com/.

### Step 2: Verify Redirect

**Context**: Inspect network tab to confirm 301 and location header.

Use browser dev tools (F12) to check response.

> Success if redirected without error; failure in other browsers shows blocked redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Phishing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser-for-Redirect-Testing]]

## Tags

- [[open-redirect]]
- [[Phishing]]
- [[firefox]]
