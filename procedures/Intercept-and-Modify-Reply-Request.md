---
id: proc-003
tags:
  - interception
  - modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Postman]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:27.366Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Reply-Request

## Summary

This procedure captures a legitimate BuddyPress reply request and modifies the thread_id to target an unauthorized thread, setting up the IDOR exploitation.

## Description

Using proxy tools, intercept AJAX requests to messages_send_reply and alter the thread_id parameter while preserving nonce and cookies. This exploits the lack of participation checks; targets web AJAX endpoints in WordPress. Prerequisites: Authenticated session and known thread_id.

## Requirements

1. Running proxy like Burp Suite
2. Legitimate reply action to intercept
3. Valid _wpnonce from a real request

## Defense

Defensive measures and detection strategies:

- Validate user participation in thread before processing replies
- Monitor for mismatched thread_id and user IDs in logs

## Objectives

1. Alter request to inject into unauthorized thread
2. Maintain request validity (nonce, cookies)
3. Test for server-side acceptance

## Instructions

### Step 1: Set Up Proxy

**Context**: Configure browser to proxy through Burp Suite.

Intercept traffic to /wp-admin/admin-ajax.php.

> Expected output: Requests visible in Burp proxy.

### Step 2: Perform Legitimate Reply

**Context**: Trigger a reply in a owned thread to capture base request.

Send a test reply via UI; intercept in Burp.

> Explanation: Copy parameters like action, _wpnonce, content, thread_id (modify this last one).

### Step 3: Modify and Forward

**Context**: Change thread_id to target.

In Burp Repeater, update thread_id=1 (unauthorized) and forward.

> Expected output: Modified request in tool interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Postman]]

## Tags

- interception
- modification
