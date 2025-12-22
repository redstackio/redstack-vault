---
tags:
  - open-redirect
  - moodle
  - lti
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-moodle-open-redirect-with-curl]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fee0e42d-6b86-4750-b8c6-34bedc436fd4
created_at: '2025-12-13T23:52:39.023Z'
updated_at: '2025-12-13T23:52:39.023Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Open Redirect in Moodle LTI redirect_uri Parameter

## Summary

This procedure tests the Moodle LTI authentication endpoint for an open redirect vulnerability by injecting an arbitrary external URL into the redirect_uri parameter, allowing attackers to redirect users to phishing or malicious sites.

## Description

The /mod/lti/auth.php endpoint in Moodle processes the redirect_uri parameter without proper validation, permitting redirects to any external domain. This was identified on evolve.glovoapp.com, where appending an external URL like https://example.com causes an unvalidated redirect. The vulnerability enables phishing attacks by tricking users into visiting controlled domains, potentially leading to credential theft or further exploitation.

## Requirements

1. Network access to the target Moodle instance on port 443
2. curl installed for HTTP request testing
3. Web browser to verify redirect behavior

## Defense

Defensive measures and detection strategies:

- Implement a whitelist of allowed redirect domains in the application code
- Log all redirect attempts and monitor for external URLs in redirect_uri
- Use Content Security Policy (CSP) headers to restrict navigation

## Objectives

1. Confirm the endpoint allows arbitrary redirects
2. Document the vulnerable parameter for escalation
3. Assess potential for phishing

## Instructions

### Step 1: Craft and Send Test Request

**Context**: Simulate an LTI authentication request with an external redirect_uri to check for unvalidated redirection.

**Command** ([[commands/test-moodle-open-redirect-with-curl]]):
```bash
curl -i -L "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=https://example.com"
```

> This command follows redirects (-L) and displays headers (-i). Look for a 3xx status and Location header matching the external URL, indicating no validation.

### Step 2: Verify in Browser

**Context**: Confirm the redirect executes in a real browser session, as some validations may be client-side.

Visit the URL directly: https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=https://example.com

> The browser should navigate to example.com without warnings. Use developer tools to inspect network requests for redirect confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/test-moodle-open-redirect-with-curl]]

## Tools Used


## Tags

- open-redirect
- moodle
- lti
