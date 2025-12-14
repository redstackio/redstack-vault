---
id: proc-reddit-intercept-pwchange-001
tags:
  - traffic-interception
  - request-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:32:58.354Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Intercept-Reddit-Password-Change-Request

## Summary

This procedure captures the HTTP request for Reddit's password change endpoint using Burp Suite, preparing for brute-force analysis by simulating a failed update attempt.

## Description

Targeting https://old.reddit.com/prefs/update/?, submit a password change with an incorrect old password to trigger the verification mechanism. Intercept via proxy to analyze the request parameters (old_password, new_password, etc.). This step reveals the lack of protections and sets up for automated attacks, assuming prior session access.

## Requirements

1. Active test account session
2. Burp Suite installed and running as proxy (browser configured to 127.0.0.1:8080)
3. Access to https://old.reddit.com/prefs/update

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and monitor for proxy interception attempts via certificate pinning
- Rate limit request interceptions by logging unusual proxy traffic
- Use client-side validation to complicate request tampering

## Objectives

1. Capture the exact POST request structure for password update
2. Identify parameters vulnerable to brute-forcing
3. Confirm no immediate throttling on failed attempts

## Instructions

### Step 1: Navigate to Password Change Page

**Context**: Log in to the test account and access the update preferences.

Use browser to visit https://old.reddit.com/prefs/update/ and enter incorrect old password (e.g., 'wrong'), new password, and confirm.

> This triggers a submission; do not complete without interception.

### Step 2: Intercept with Burp Suite

**Context**: Route traffic through Burp proxy to capture the request.

Configure browser proxy to Burp, submit the form, and forward the request in Burp Proxy tab.

> Captured request shows POST to /prefs/update with form-encoded parameters; right-click to send to Intruder.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[traffic-interception]]
- [[request-capture]]
