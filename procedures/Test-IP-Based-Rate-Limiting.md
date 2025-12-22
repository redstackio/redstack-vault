---
tags:
  - nextcloud
  - rate-limit
  - testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:28:28.125Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a125c76a-5ce2-4e37-a89c-c7377fc5a56d
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Test-IP-Based-Rate-Limiting

## Summary

This procedure tests the rate limiting on Nextcloud's password reset endpoint using Burp Repeater to confirm IP-based restrictions after a threshold of requests.

## Description

Forward the intercepted request to Burp Repeater and resend it multiple times (7-8) from the same IP. Initial requests succeed, but exceeding the limit triggers HTTP 429. This validates the vulnerability's root cause: IP-tied limits without per-user or CAPTCHA protections. Expected outcome: Limit observed at ~7-8 requests.

## Requirements

1. Intercepted request from previous procedure
2. Burp Suite Repeater tab open
3. Stable network without external IP changes

## Defense

Defensive measures and detection strategies:

- Implement per-user rate limits in addition to IP
- Alert on 429 responses to detect probing

## Objectives

1. Identify rate limit threshold
2. Confirm IP dependency
3. Set baseline for bypass

## Instructions

### Step 1: Send to Repeater

**Context**: Load the request for manual replay.

Right-click intercepted request > Send to Repeater.

### Step 2: Replay Requests

**Context**: Simulate repeated submissions.

In Repeater, click 'Send' 7-8 times, observing responses.

> Expected output: First 7 responses: 200 OK with reset email; 8th+: 429 Too Many Requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[nextcloud]]
- [[rate-limit]]
