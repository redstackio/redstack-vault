---
tags:
  - oauth
  - protocol-relative
  - uri
  - error
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-protocol-relative-uri]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.134Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d12ae557-ae3a-433c-88eb-924fdb57c902
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Protocol-Relative-Redirect-URI

## Summary

This procedure exploits improper validation of protocol-relative URLs in the OAuth redirect parameter of Respondly's Twitter integration, triggering an error during authorization without causing an immediate crash.

## Description

The vulnerability stems from the lack of checks for protocol-relative URIs (starting with //) in the requestTokenAndRedirect parameter at the /_oauth/twitter/ endpoint. When processed in the Meteor framework, this leads to unhandled errors during token exchange or state management with Twitter's OAuth. The first attempt reveals error handling flaws, potentially exposing internal details, setting the stage for DoS via repetition.

## Requirements

1. Curl or equivalent HTTP client
2. Knowledge of the target OAuth endpoint
3. Ability to inspect HTTP responses for errors

## Defense

Defensive measures and detection strategies:

- Validate all redirect URIs to enforce absolute protocols (http/https)
- Sanitize inputs to reject protocol-relative formats
- Monitor for error logs containing OAuth-related exceptions

## Objectives

1. Trigger authorization error with malformed URI
2. Observe error response for potential information disclosure
3. Validate vulnerability for escalation to repeated attacks

## Instructions

### Step 1: Send Request with Protocol-Relative URI

**Context**: Craft a request using //hackerone.com to bypass protocol specification, causing parsing issues in the OAuth flow.

**Command** ([[commands/curl-test-protocol-relative-uri]]):
```bash
curl "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com"
```

> The command issues a GET to the endpoint with the malformed parameter. Expected output is an error page or response indicating failure in Twitter authorization, without server disruption on single use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-protocol-relative-uri]]

## Tools Used


## Tags

- [[protocol-relative]]
- [[uri]]
- [[error]]
