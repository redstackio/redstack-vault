---
tags:
  - idor
  - web
  - access-control
  - yelp
  - reservation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Obtain-Reservation-ID-from-Public-Shares]]'
  - '[[procedures/Cancel-Reservation-via-IDOR-Without-Authentication]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.091Z'
description: >-
  A simple two-step attack exploiting an Insecure Direct Object Reference (IDOR)
  in Yelp's reservation cancellation feature, allowing anyone with a reservation
  ID to cancel bookings without authentication.
skill_level: beginner
impact_level: medium
id: d4b4ed79-b8e0-473c-9392-48012bdba929
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Reservation Cancellation via IDOR in Yelp Booking System

Multi-stage attack chain demonstrating a complete attack workflow exploiting IDOR in Yelp's reservation system.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Obtain Reservation ID] --> B[Cancel Reservation]
    B --> C[Disrupt Booking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Web platform
- Access to Yelp's reservation cancellation feature
- Publicly shared reservation URLs from social media

### Initial Access Requirements

- No credentials required
- Internet access to Yelp's web application
- No prior access needed

## Detailed Attack Procedures

### Step 1: Obtain Reservation ID
procedure: [[procedures/Obtain-Reservation-ID-from-Public-Shares]]

**Objective**: Identify and extract a target reservation ID from publicly shared URLs on social media.

**Instructions**: Search social media platforms like Twitter or Facebook for posts where users share their Yelp reservation links. These URLs typically contain the reservation ID as a parameter (e.g., https://yelp.com/reservation? id=12345). Copy the ID from the URL.

**Expected Output**: A valid reservation ID (e.g., a numeric or alphanumeric string).

**Success Indicators**:
- Reservation ID extracted from a public share
- ID format matches expected pattern (e.g., integer sequence)

### Step 2: Cancel Reservation via IDOR
procedure: [[procedures/Cancel-Reservation-via-IDOR-Without-Authentication]]

**Objective**: Use the obtained reservation ID to access and trigger the cancellation endpoint without any authentication, resulting in unauthorized booking disruption.

**Instructions**: In a web browser, navigate directly to the Yelp reservation cancellation URL using the known ID, such as https://www.yelp.com/reservations/cancel?id=12345 (replace 12345 with the actual ID). The feature does not prompt for login, allowing immediate cancellation if the ID is valid.

**Expected Output**: Confirmation page or message indicating the reservation has been canceled.

**Success Indicators**:
- Cancellation succeeds without login prompt
- Reservation status changes to canceled (verifiable if original owner checks)

## Attack Chain Summary

### Key Achievements

1. Easy acquisition of reservation IDs from public social media shares
2. Bypassing authentication to cancel any targeted reservation
3. Potential for widespread disruption of user bookings without detection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
