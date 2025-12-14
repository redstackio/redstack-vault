---
tags:
  - business-logic
  - api
  - unauthenticated
  - idor
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-put-forged-bid]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:34.947Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2c3d660c-0baf-4816-9cc6-febf8d0c5be1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Forged-Bid-to-Inflate-Fare-via-Bidding-Endpoint

## Summary

This procedure uses a generated trip hash to submit a forged higher bid via an unauthenticated PUT endpoint, exploiting business logic flaws to inflate the fare displayed to the driver, potentially causing conflicts while the original passenger retains cancellation rights.

## Description

Building on the hash from the config endpoint, the /v1/bidding endpoint in the ride-sharing API allows unauthenticated updates to trip bids without verifying user ownership. This IDOR combined with logic flaws permits impersonation of passengers, altering fare amounts. The attack is web-based, requires the prior hash, and impacts platform trust by displaying incorrect fares to drivers.

## Requirements

1. Valid hash from the config endpoint query
2. Inflated bid amount (e.g., higher than original fare)
3. Network access to the bidding API endpoint

## Defense

Defensive measures and detection strategies:

- Enforce session-based or token authentication for all modification endpoints
- Validate bid ownership by cross-checking user ID with trip ownership
- Log and alert on bid submissions with mismatched hashes or anomalous amounts

## Objectives

1. Submit forged bid to update trip fare
2. Impersonate passenger without credentials
3. Cause inflated fare display and potential disruptions

## Instructions

### Step 1: Submit Inflated Bid

**Context**: Craft and send a PUT request with the hash and higher bid to manipulate the trip's bidding logic.

**Command** ([[commands/curl-put-forged-bid]]):
```bash
curl -X PUT "https://api.example.com/v1/bidding" -H "Content-Type: application/json" -d '{"hash": "EXTRACTED_HASH", "bid_amount": 500}' -H "Accept: application/json"
```

> This updates the bid in the backend. Expected output is a success JSON (e.g., {"status": "updated"}). Verify impact by monitoring the driver's interface for the new fare or attempting to view the trip as an observer. The bid chains with the config hash to bypass checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-put-forged-bid]]

## Tools Used


## Tags

- business-logic
- api
- unauthenticated
- idor
