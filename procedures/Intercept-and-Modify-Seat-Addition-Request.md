---
id: uuid-intercept-modify-seats
tags:
  - api-interception
  - request-modification
  - input-validation-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.423Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Seat-Addition-Request

## Summary

This procedure uses Burp Suite to intercept, modify, and forward the PUT /v2/seats API request in Krisp's billing system, exploiting decimal input acceptance to allocate more seats than paid for via inconsistent Math.ceil and Math.floor application.

## Description

The Krisp backend fails to validate integer-only inputs for the 'seats' parameter, allowing decimals like 1.9. This results in 2 seats added (ceil(1.9)) but only $60 charged (floor(1.9)*$60), enabling financial manipulation. The procedure targets authenticated users in the web app's billing section, with outcomes including verified over-allocation. Prerequisites: Active Krisp team and Burp Suite configured as proxy.

## Requirements

1. Authenticated Krisp session with team access.
2. Burp Suite installed and proxy active (e.g., browser set to 127.0.0.1:8080).
3. Knowledge of HTTP request structure (JSON body with auth tokens).

## Defense

Defensive measures and detection strategies:

- Enforce strict integer validation on 'seats' parameter (e.g., regex or type checks).
- Log and alert on decimal inputs to billing APIs.
- Use consistent rounding (e.g., always ceil for both seats and price) or reject decimals.
- Monitor for proxy-intercepted traffic patterns.

## Objectives

1. Capture and alter the seat addition request.
2. Exploit rounding discrepancy for free seats.
3. Confirm impact via dashboard and billing review.

## Instructions

### Step 1: Initiate Seat Addition and Intercept

**Context**: Trigger the API call to capture the request.

Navigate to billing > add seats in Krisp app. Burp intercepts the PUT /v2/seats request.

> Inspect body: {"seats": 1, ...} with auth headers.

### Step 2: Modify Seats to Decimal

**Context**: Change input to trigger the flaw.

In Burp Interceptor, edit JSON body to {"seats": 1.9, ...}. Preserve all other fields.

> Ensure request method PUT, endpoint /v2/seats, and valid auth.

### Step 3: Forward and Observe Response

**Context**: Execute and validate the exploit.

Click Forward in Burp. Check response (200 OK expected) and refresh Krisp dashboard.

> Expected: Seats +2, price +$60. Note 30-day cycle limits full payment test.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[api-interception]]
- [[request-modification]]
