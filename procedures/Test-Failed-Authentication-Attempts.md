---
id: proc-uuid-002
tags:
  - brute-force
  - testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:30:58.757Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Test-Failed-Authentication-Attempts

## Summary

This procedure tests the login endpoint by sending multiple invalid credential attempts to confirm no rate limiting or throttling is enforced, highlighting the vulnerability in LinkedIn's authentication system.

## Description

Targeting the web-based login, this involves replaying POST requests with wrong passwords for a fixed username. Using Burp Suite, rapid requests reveal no delays, enabling brute-force risks. The scenario assumes public endpoint access; outcomes include logs proving unlimited tries, as in invalid response attachments.

## Requirements

1. Burp Suite installed and configured
2. Target username (e.g., a test account)
3. List of invalid passwords for testing

## Defense

Defensive measures and detection strategies:

- Enforce account lockout after 5 failures
- Use IP-based throttling with tools like Fail2Ban
- Log and alert on repeated 401/403 responses

## Objectives

1. Validate absence of attempt limits
2. Measure response consistency under load
3. Collect evidence of vulnerability

## Instructions

### Step 1: Setup Invalid Credentials

**Context**: Prepare payloads for failed logins.

**Instructions**: In Burp Suite Repeater, load the captured login request and modify password to invalid values.

> Send 20-50 requests sequentially. Expected output: Each returns error like 'Invalid credentials' without increasing latency.

### Step 2: Observe Responses

**Context**: Check for any security triggers.

**Instructions**: Monitor timings and headers in Burp. Look for absence of 'Retry-After' or CAPTCHA redirects.

> Expected output: Uniform fast responses, confirming no restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[authentication]]
