---
id: proc-omise-intercept-burp-001
tags:
  - interception
  - proxy
  - request-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.227Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept Invitation Request with Burp Suite

## Summary

This procedure uses Burp Suite to capture, modify, and prepare the team invitation POST request for concurrent replay in a race condition attack.

## Description

Burp Suite acts as a proxy to intercept HTTP traffic from the Omise dashboard. The target endpoint /team/memberships is modified to HTTP/1.1 with a custom header for Turbo Intruder compatibility. This enables rapid concurrent sending to exploit the lack of atomic checks, leading to duplicates. Requires proxy setup; outcomes include a ready-to-replay request.

## Requirements

1. Burp Suite installed and running (Community edition)
2. Browser proxy configured to 127.0.0.1:8080
3. Authenticated Omise session

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to complicate proxy interception
- Detect unusual headers like 'x-request' in WAF rules
- Monitor for proxy-like traffic patterns

## Objectives

1. Capture the POST /team/memberships request
2. Modify protocol and add Turbo Intruder header
3. Preserve parameters for replay

## Instructions

### Step 1: Configure Proxy and Intercept

**Context**: Set up Burp to catch the invitation submission.

Start Burp, enable intercept in Proxy tab, submit form in browser.

> Request appears in Intercept tab with POST data.

### Step 2: Modify Request

**Context**: Update for race exploitation.

Change to HTTP/1.1, add header 'x-request: %s', verify params: authenticity_token, email, membership[admin]=1, membership[technical]=0, commit=Send invitation.

> Modified request ready; forward to Repeater or Intruder.

### Step 3: Send to Turbo Intruder

**Context**: Prepare for concurrent attack.

Right-click and send to Turbo Intruder.

> Request loaded in Turbo Intruder interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- interception
- proxy
- request-modification
