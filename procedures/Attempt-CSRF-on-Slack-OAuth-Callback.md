---
id: proc-004
tags:
  - csrf
  - oauth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/slack-oauth-callback-attempt]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:30.203Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Attempt-CSRF-on-Slack-OAuth-Callback

## Summary

This procedure attempts a CSRF attack on the Slack OAuth callback endpoint using the traversal, but encounters blocking due to the appended .json suffix.

## Description

By setting report_id to traverse to /auth/slack/callback with code and state parameters, the internal GET simulates an OAuth completion. However, the .json suffix causes the server to treat parameters as part of the path, blocking processing. This targets OAuth2 flows in HackerOne's integration setup.

## Requirements

1. Valid OAuth code and state from a prior Slack auth initiation
2. Encoded parameters
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Validate state parameter strictly against session
- Require CSRF tokens on all OAuth callbacks
- Reject requests with .json in query paths

## Objectives

1. Trigger OAuth callback via traversal
2. Observe parameter blocking
3. Identify need for suffix bypass

## Instructions

### Step 1: Target Callback Path

**Context**: Use traversal to hit /auth/slack/callback with params.

**Command** ([[commands/slack-oauth-callback-attempt]]):
```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=..%2F..%2F..%2Fauth%2Fslack%2Fcallback%3Fcode%3D14582397537.14583911921.010c282773%26state%3Dc802bcef4532f0122d0f06088a2eaea890d746f0cb4d39b2%3F&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

> Expected output: 302 to /auth/failure?message=csrf_detected due to .json blocking params.

### Step 2: Analyze Failure

**Context**: Note the suffix issue for next bypass.

**Command** (Inspect response):
```bash
# Check redirect location
```

> Failure confirms .json interferes with query parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/slack-oauth-callback-attempt]]

## Tools Used


## Tags

- csrf
- oauth
- callback
