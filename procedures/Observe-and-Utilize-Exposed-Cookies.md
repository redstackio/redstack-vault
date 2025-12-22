---
id: proc-uuid-006
tags:
  - account-takeover
  - credential-replay
  - impact
type: procedure
tools:
  - '[[tools/Custom-Attacker-App]]'
tactics:
  - '[[Collection]]'
  - '[[Command and Control]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:06.346Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Observe-and-Utilize-Exposed-Cookies

## Summary

This procedure captures the displayed cookies and uses them to hijack the victim's Exness account for unauthorized actions.

## Description

The WebView writes document.cookie to the page, exposing JWT tokens and session IDs from shared storage. These can be copied and replayed in tools like Postman or a browser to access my.exness.asia, allowing portfolio modifications, position views, or withdrawals.

## Requirements

1. Cookies visible from prior step
2. Network access to exness.asia
3. Tools for cookie replay (e.g., browser dev tools)

## Defense

Defensive measures and detection strategies:

- Use HttpOnly and Secure flags on cookies
- Implement token binding or short-lived JWTs
- Monitor for anomalous logins from unusual IPs/devices

## Objectives

1. Validate stolen credentials
2. Achieve account takeover
3. Perform impact actions like unauthorized trades

## Instructions

### Step 1: Capture Output

**Context**: Record the exposed data.

Screenshot or copy the WebView content showing cookies.

**Expected Output**: Full cookie string captured.

### Step 2: Replay for Takeover

**Context**: Use cookies to impersonate user.

Set cookies in browser and navigate to my.exness.asia; perform actions like view positions.

**Expected Output**: Successful login without credentials; access to account features.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection
- [[Command and Control]] Command and Control (implied replay)

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Attacker-App]]

## Tags

- account-takeover
- credential-replay
- impact
