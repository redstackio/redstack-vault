---
tags:
  - booking-creation
  - api-request
type: procedure
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/bykea-create-trip]]'
verified: false
platforms:
  - Web
  - Mobile (iOS)
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:46.874Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d564ac79-f841-4275-a61b-647926edeb9f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Victim-Booking

## Summary

This procedure simulates a legitimate booking creation by the victim user on Bykea, generating a booking_id and trip_id that can later be exploited via IDOR to access sensitive data.

## Description

Using the victim's authenticated session, send a POST request to the /api/v1/trips/create endpoint with location details, service code 23 (specific ride type), and a customer bid of 75. The response provides the necessary IDs for exploitation. This step requires the victim's access_token and user_id, obtained from app authentication. The target environment is Bykea's REST API, inferred to use MongoDB for ID generation.

## Requirements

1. Victim's user_id and access_token from authentication
2. Coordinates for pickup/dropoff (e.g., Quetta, Pakistan locations)
3. curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Validate input coordinates and addresses for geographic relevance
- Log all booking creations with user_id for audit trails
- Implement CAPTCHA or additional verification for high-frequency requests

## Objectives

1. Generate a valid booking with exploitable IDs
2. Capture trip_id and booking_id from response
3. Ensure booking includes sensitive details like locations for later disclosure testing

## Instructions

### Step 1: Prepare Request Data

**Context**: Gather victim's credentials and location info for the booking payload.

Use placeholders: {{user_id}} for victim's ID, {{access_token}} for token, and hardcoded locations (pickup: lat 29.5500097, lng 67.883339799999931; dropoff: lat 29.573396420702664, lng 67.898040153086185).

### Step 2: Execute Booking Creation

**Context**: Send the POST request to create the trip.

**Command** ([[commands/bykea-create-trip]]):
```bash
curl -X POST "https://api.bykea.net/api/v1/trips/create" \
  -H "User-Agent: BYKEA/1.0.169 (com.bykea.pk; build:21; iOS 15.8.0) Alamofire/1.0.169" \
  -H "X-App-Version:1.0.169" \
  -d '{"advertisement_id":"REDACTED","token_id":"{{access_token}}","pickup_info":{"lng":67.883339799999931,"lat":29.5500097,"address":"Ø³Ø¨Û, ØªØØµÛÙ Ø³Ø¨Û, Ø¶ÙØ¹ Ø³Ø¨Û, Ø³Ø¨Û ÚÙÛÚÙ, Ø¨ÙÙÚØ³ØªØ§Ù, 82000, Ù¾Ø§Ú©Ø³ØªØ§Ù"},"trip":{"creator":"iOS","service_code":23,"lng":67.883339799999931,"lat":29.5500097,"customer_bid":75},"dropoff_info":{"address":"Kurak, ØªØØµÛÙ Ø³Ø¨Û, Ø¶ÙØ¹ Ø³Ø¨Û, Ø³Ø¨Û ÚÙÛÚÙ, Ø¨ÙÙÚØ³ØªØ§Ù, Ù¾Ø§Ú©Ø³ØªØ§Ù","lat":29.573396420702664,"lng":67.898040153086185},"_id":"{{user_id}}"}'
```

> This command creates a booking and returns {"code":200,"success":true,"data":{"trip_id":"███████","trip_no":"PKX████████","passenger_id":"██████████"}}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/bykea-create-trip]]

## Tools Used

- curl

## Tags

- [[api]]
- [[booking]]
