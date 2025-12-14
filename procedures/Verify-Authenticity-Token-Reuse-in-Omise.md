---
tags:
  - csrf
  - token-reuse
  - verification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/omise-add-email-relay-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.200Z'
sub_techniques: []
id: fa4c0aee-7309-481b-8f42-3545bc6a9f8a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Authenticity-Token-Reuse-in-Omise

## Summary

Test the Omise authenticity token by replaying the captured request with a different email to confirm it does not expire after single use.

## Description

The core vulnerability lies in the Rails authenticity token being session-bound but not regenerated post-use, allowing multiple CSRF-vulnerable submissions. This procedure replays the request in Burp Repeater to demonstrate reuse, confirming the exploitability for unauthorized actions like adding email relays.

## Requirements

1. Captured request in Burp Repeater
2. Active session cookies
3. Second test email address

## Defense

Defensive measures and detection strategies:

- Regenerate CSRF tokens after each state-changing request
- Implement token expiration timers

## Objectives

1. Replay request with same token
2. Observe successful validation
3. Confirm no invalidation

## Instructions

### Step 1: Modify and Replay Request

**Context**: Change only the email parameter to test token validity.

In Burp Repeater, edit email_relay[address] to a new value (e.g., test2@gmail.com) and send.

Execute [[commands/omise-add-email-relay-post]] with modified param:

```bash
curl -X POST https://dashboard.omise.co/test/subscriptions \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=...' \
  -d 'utf8=%E2%9C%93&authenticity_token=...&email_relay%5Baddress%5D=test2%40gmail.com&...&button='
```

> Expected: 302 redirect on success; failure would be 403 or dashboard redirect.

### Step 2: Check Token on Form Reload

**Context**: Verify no new token generation.

Reload the form page and inspect the new authenticity_token; it should match the original.

> Token remains the same, confirming reuse vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/omise-add-email-relay-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[token-reuse]]
