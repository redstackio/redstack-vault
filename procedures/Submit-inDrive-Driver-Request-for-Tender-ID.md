---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - indrive
  - api
  - bid-submission
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
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
updated_at: '2025-12-14T17:25:17.882Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-inDrive-Driver-Request-for-Tender-ID

## Summary

This procedure submits a driver bid request to the inDrive API's /api/driverrequest endpoint in response to a passenger's ride order, generating a tender_id and order_id essential for subsequent exploitation steps like force-acceptance.

## Description

In the inDrive ride-bidding process, passengers request rides, and drivers respond with bids including price, location, and timing. This procedure crafts and sends an authenticated HTTP request using the driver's credentials to create a tender. The response provides identifiers needed to impersonate acceptance. Prerequisites include a valid driver account and a pending passenger job_id, obtainable by monitoring app traffic or API polling. Expected outcomes: Successful bid submission and ID extraction, setting up unauthorized access.

## Requirements

1. Valid driver phone number and authentication token from inDrive app login
2. Passenger-initiated ride request providing job_id (intercept via app proxy)
3. HTTP client like curl for API interaction
4. Location coordinates (latitude/longitude) for the bid

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on /api/driverrequest to prevent rapid bidding
- Validate job_id ownership and prevent reuse across sessions
- Log and monitor anomalous bid patterns, such as frequent submissions from single accounts

## Objectives

1. Generate tender_id and order_id for ride impersonation
2. Establish a valid bid context for chaining exploits
3. Prepare for PII access and price manipulation

## Instructions

### Step 1: Prepare Driver Request Parameters

**Context**: Gather necessary parameters including job_id from passenger request, driver's phone/token, and location data to simulate a legitimate bid.

No command; manually collect: job_id (e.g., UUID from passenger flow), phone (redacted), token (from login), stream_id (session timestamp), etc.

### Step 2: Execute Driver Request

**Context**: Send the GET request to /api/driverrequest to create the tender and obtain IDs.

**Command** ([[commands/curl-indrive-driverrequest]]):
```bash
curl "https://terra-akamai.indriverapp.com/api/driverrequest?cid=5957&locale=en_US&job_id=338f72ff-f3c1-4da0-af15-5d1aa720146b&phone=██████████&token=████████&v=7&stream_id=1682279074257167&order_id=██████&client_id=█████████&shield_session_id=██████████&type=indriver&price=63&period=3&geo_arrival_time=1&distance=5&longitude=85.3249627&latitude=27.7390611&sn=1"
```

> This command submits the bid with standard price (63). Parse the JSON response for tender_id and order_id. Expected output: Success status with IDs; errors if auth fails.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

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
- [[api]]
- [[bid-submission]]
