---
id: proc-nextcloud-replay-spam-001
tags:
  - nextcloud
  - email-bombing
  - dos
type: procedure
tools:
  - '[[tools/Chrome-Developer-Tools]]'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.691Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Replay-XHR-Request-to-Spam-Emails

## Summary

This procedure exploits the rate-limit-free password reset API in Nextcloud by replaying captured XHR requests to flood the admin's email inbox, achieving denial-of-service.

## Description

After triggering a reset, the API endpoint `/lostpassword/email` lacks protections, allowing unlimited POST requests. Using browser tools, attackers replay the request rapidly, sending dozens or hundreds of emails. This targets demo instances but applies to any unprotected Nextcloud setup, causing inbox overload and potential email service exhaustion. Prerequisites include a captured request from a legitimate trigger.

## Requirements

1. Captured XHR request from password reset (via Developer Tools)
2. Chrome or similar browser with Network panel
3. Target instance with admin email configured

## Defense

Defensive measures and detection strategies:

- Add rate limiting (e.g., via nginx or application code) to reset endpoints
- Log and block IPs sending >3 requests in 5 minutes
- Use email service throttling or sinkhole suspicious volumes
- Enable web application firewall (WAF) rules for repeated POSTs to auth paths

## Objectives

1. Flood admin inbox with reset emails
2. Cause DoS to email delivery and management
3. Demonstrate API abuse potential across instances

## Instructions

### Step 1: Capture the Initial Request

**Context**: Use Developer Tools to inspect the reset API call for replay.

Open Chrome Developer Tools (F12), navigate to Network tab, filter XHR/Fetch. Trigger reset and locate POST to `/lostpassword/email`.

> Request details include payload (e.g., email address) and headers; copy as cURL if needed.

### Step 2: Replay the Request Manually

**Context**: Send multiple requests to bypass limits.

Right-click the captured request in Network tab and select "Replay XHR". Repeat 10-50 times, or paste cURL into console and loop (e.g., via JavaScript setInterval).

> Each replay results in a 200 OK and new email sent.

### Step 3: Scale to Other Instances

**Context**: Apply the technique to additional targets.

Visit new instance (e.g., `https://demo.nextcloud.com/test`), trigger once, capture, and replay as above.

> Successful if requests complete without 429 errors, confirming spam delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Developer-Tools]]

## Tags

- nextcloud
- email-bombing
- dos
