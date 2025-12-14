---
id: proc-test-open-redirect
tags:
  - open-redirect
  - phishing
  - url-injection
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:21.038Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Test-Open-Redirect-Payload-in-Attach-Html

## Summary

This procedure tests the open redirect vulnerability by appending a malicious domain to the URL search parameter, demonstrating how attackers can lure users to phishing sites via the trusted domain.

## Description

Open redirects abuse URL handling to bypass same-origin checks, often chained with social engineering. Here, the unsanitized document.location.replace allows any URL in the search param to trigger a redirect, impacting user trust in informatica.com and enabling phishing campaigns.

## Requirements

1. Vulnerable endpoint access
2. Web browser
3. A test domain (e.g., evil.com placeholder)

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against a whitelist of allowed domains
- Log and monitor unexpected redirects in server-side analytics
- Educate users on verifying URLs before clicking

## Objectives

1. Confirm redirect functionality without validation
2. Show potential for phishing attacks
3. Measure redirect speed and reliability

## Instructions

### Step 1: Construct Payload URL

**Context**: Append a simple domain to the search parameter to test basic redirect.

Navigate to: https://iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html?evil.com

> The ? initiates the search param, and evil.com is treated as the redirect target.

### Step 2: Observe Redirect Behavior

**Context**: Verify the browser follows the injected URL.

Monitor the address bar and network tab in dev tools.

> Expected output: Page redirects to http://evil.com immediately.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
- [[url-injection]]
