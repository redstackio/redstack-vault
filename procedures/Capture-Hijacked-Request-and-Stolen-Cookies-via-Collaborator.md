---
tags:
  - cookie-theft
  - oob
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:34.491Z'
sub_techniques: []
id: e2b9779f-4273-4afa-a64d-7cf2202dc5bf
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Capture-Hijacked-Request-and-Stolen-Cookies-via-Collaborator

## Summary

This procedure polls Burp Collaborator to capture the out-of-band HTTP request from the hijacked redirect, extracting victim details and Slack session cookies like 'd'.

## Description

After hijacking, the backend's redirect to the collaborator server sends the victim's cookies in the request headers. This targets session-based apps like Slack; requires Collaborator setup. Outcome is stolen credentials for takeover.

## Requirements

1. Active Collaborator client
2. Hijacked request triggered
3. Access to poll interface

## Defense

Defensive measures and detection strategies:

- Sanitize redirects to prevent OOB leaks
- Monitor for unexpected external HTTP requests
- Use secure cookies with HttpOnly and Secure flags

## Objectives

1. Receive OOB callback
2. Extract session cookies
3. Identify victim metadata

## Instructions

### Step 1: Poll Collaborator

**Context**: Check for incoming interactions.

No command; in Burp Collaborator Client, click 'Poll now' or monitor live.

> Look for HTTP requests from slackb.com IP, including headers with 'd' cookie.

### Step 2: Analyze Captured Data

**Context**: Parse the request for sensitive info.

No command; review headers for User-Agent, IP, and cookies.

> Expected: Full request log with stolen 'd' session token.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- session-cookie
- exfiltration
