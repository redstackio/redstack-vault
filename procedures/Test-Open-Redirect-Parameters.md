---
tags:
  - open-redirect
  - testing
  - revive-adserver
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: a869fe66-bc82-4f59-9210-6d25d8c36c11
created_at: '2025-12-14T17:24:23.019Z'
updated_at: '2025-12-14T17:24:23.019Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Open Redirect Parameters

## Summary

This procedure tests the dest, oadest, and ct0 parameters in Revive Adserver's ck.php and lg.php for open redirect behavior by supplying arbitrary external URLs and observing unvalidated redirection.

## Description

The vulnerability stems from a design feature allowing third-party ad servers to track metrics via redirects, but without validation or allowlisting, any URL can be injected. Testing involves crafting requests to these endpoints and following the redirect chain to confirm exploitation potential in a web environment.

## Requirements

1. Accessible Revive Adserver instance
2. HTTP client like curl for redirect testing
3. A test external URL (e.g., benign site like example.com)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize redirect parameters against a whitelist
- Log all redirect attempts for anomaly detection
- Deploy Content Security Policy (CSP) to restrict navigation

## Objectives

1. Verify redirect without validation
2. Confirm parameter acceptance
3. Assess redirect chain

## Instructions

### Step 1: Craft Test Request

**Context**: Build a URL with an arbitrary dest parameter to initiate redirect.

Execute [[commands/curl-test-open-redirect]] to test:

```bash
curl -L -v "http://target.com/ck.php?dest=http://example.com/test" -o /dev/null
```

> This follows (-L) the redirect and shows verbose (-v) headers to reveal the Location.

**Expected Output**: Redirect header pointing to http://example.com/test.

### Step 2: Test Alternative Parameters

**Context**: Repeat for oadest and ct0 to identify all vulnerable vectors.

Use similar curl command: curl -L -v "http://target.com/lg.php?oadest=http://example.com/test"

**Expected Output**: Successful redirect to the test URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-open-redirect]]

## Tools Used


## Tags

- [[open-redirect]]
- [[testing]]
