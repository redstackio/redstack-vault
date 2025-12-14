---
tags:
  - replay
  - flood
  - dos
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Burp-Suite]]'
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
updated_at: '2025-12-14T17:28:36.268Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ca76aa89-b880-452f-93c7-1cf82b6ff29a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Replay-Modified-Request-Multiple-Times

## Summary

Repeat the tampered PUT request to generate unlimited approval entries, overwhelming the review system and triggering infinite email notifications.

## Description

With the bypass active, each replay creates a new entry visible in the admin dashboard, sending emails to reviewers. The flaw allows any old or invalid token since validation ignores the response body. In a WordPress/PHP setup, this leads to resource exhaustion and potential harassment via spoofed sender emails.

## Requirements

1. Successful modified PUT request
2. Proxy with repeater functionality
3. Access to dashboard for verification (if available)

## Defense

Defensive measures and detection strategies:

- Rate-limit requests per IP/session
- Expire CAPTCHA tokens immediately after use
- Alert on high-volume submissions
- Sanitize sender fields to prevent spoofing

## Objectives

1. Flood system with requests
2. Trigger excessive emails
3. Demonstrate DoS impact

## Instructions

### Step 1: Send to Repeater

**Context**: Load the modified request into repeater for easy replay.

In Burp, right-click intercepted request > Send to Repeater.

> Expected output: Request loaded in Repeater tab.

### Step 2: Execute Multiple Times

**Context**: Replay to create duplicates.

Click Send repeatedly (e.g., 10+ times); observe responses.

Check dashboard at https://en.instagram-brand.com/ for new entries.

> Expected output: Multiple 200 responses; accumulating requests and emails sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Burp-Suite]]

## Tags

- [[replay]]
- [[dos]]
