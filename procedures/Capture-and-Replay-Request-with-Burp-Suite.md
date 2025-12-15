---
id: proc-uuid-2
tags:
  - rate-limit-bypass
  - request-replay
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.701Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-and-Replay-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept a legitimate money request POST from Coinbase, then replays it with modified email parameters to exploit the lack of rate limiting, allowing unlimited requests to arbitrary emails for spam or enumeration.

## Description

The Coinbase /transactions/request_money endpoint processes POST requests without rate limits, enabling attackers to replay captured requests. The procedure involves proxy interception, parameter modification (e.g., transaction[from]=arbitrary@email.com), and repeated sending. This leads to unlimited email notifications and sets up enumeration by observing response differences. Requires Burp Suite configured as a proxy and a captured baseline request.

## Requirements

1. Burp Suite installed and running as a proxy (default port 8080).
2. Browser traffic routed through the proxy.
3. Captured baseline POST request from a legitimate submission.

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on sensitive endpoints like request_money (e.g., 5 requests per minute per IP).
- Log and alert on repeated POSTs from the same session or IP.

## Objectives

1. Capture the exact request structure including tokens and headers.
2. Bypass rate limits by replaying without restrictions.
3. Test arbitrary emails to trigger notifications and observe effects.

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception for HTTPS traffic to Coinbase.

In Burp, go to Proxy > Options, ensure Intercept is on, and configure browser to use 127.0.0.1:8080.

**Expected Output**: Traffic from browser routed through Burp.

### Step 2: Intercept the POST Request

**Context**: Submit a legitimate money request to capture it.

With Intercept on, submit the form; forward the request in Burp Repeater.

**Expected Output**: Request details in Repeater, including POST /transactions/request_money with body like transaction[from]=test@email.com&transaction[amount]=0.001&transaction[notes]=Test, headers X-CSRF-Token, Cookie, Content-Type: application/x-www-form-urlencoded.

### Step 3: Modify and Replay

**Context**: Alter the email parameter and send repeatedly.

In Repeater, change transaction[from] to arbitrary@email.com, click Send; repeat for multiple emails without limits.

**Expected Output**: 200 OK responses for each, no throttling observed.

### Step 4: Verify No Rate Limiting

**Context**: Test scale by sending 10+ requests quickly.

Replay rapidly; monitor for errors.

**Expected Output**: All requests succeed, demonstrating bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- rate-limit-bypass
- request-replay
- burp-suite
