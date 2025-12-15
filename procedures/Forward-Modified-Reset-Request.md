---
id: proc-004
tags:
  - request-forwarding
  - exploit-submission
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.521Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Forward-Modified-Reset-Request

## Summary

This procedure forwards the tampered JSON request to the GitLab server, triggering the sending of password reset emails to both the victim's and attacker's addresses due to the injected email array.

## Description

With the payload modified, releasing the request simulates a legitimate submission but exploits the vulnerability. The server processes the array and dispatches links accordingly. Requires Burp Suite; outcome: Receipt of reset email by attacker.

## Requirements

1. Modified request held in Burp Suite
2. Valid GitLab instance endpoint
3. Email access for attacker

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to reset forms to prevent intercepted modifications
- Monitor for JSON payloads on form endpoints and flag anomalies
- Rate-limit reset emails per email domain or IP

## Objectives

1. Submit the exploited request successfully
2. Trigger dual reset emails
3. Avoid detection during transmission

## Instructions

### Step 1: Release the Request

**Context**: Send the modified payload to the server from the proxy.

In Burp's Intercept or Repeater tab, click 'Forward' or 'Send'.

> Expected: Server responds with 200 OK or redirect; emails queued.

### Step 2: Verify Server Response

**Context**: Check for success without errors.

Inspect the response body for confirmation messages.

> Look for 'Password reset instructions sent' or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

None

## Commands Used

None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-forwarding]]
- [[exploit-submission]]
- [[web]]
