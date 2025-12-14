---
tags:
  - idor
  - exploit
  - access-bypass
type: procedure
tools: []
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
updated_at: '2025-12-14T17:30:35.080Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: e913f8ed-0cd7-4e48-8399-2ba7ffcbe294
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Cancel-Reservation-via-IDOR-Without-Authentication

## Summary

This procedure exploits an IDOR vulnerability in Yelp's reservation cancellation feature by directly accessing the cancellation endpoint with a known reservation ID, bypassing all authentication and authorization checks.

## Description

Yelp's system allows cancellation requests via a web endpoint that references reservations solely by ID without verifying user ownership or login status. An attacker with a valid ID can trigger cancellation, disrupting the original user's booking. This targets the web-based reservation management system and assumes IDs are predictable or leaked. Prerequisites include a valid ID from public sources; outcomes include successful cancellation and potential notification to the owner.

## Requirements

1. Valid reservation ID
2. Web browser or HTTP client
3. Access to Yelp's public web application

## Defense

Defensive measures and detection strategies:

- Enforce server-side authorization checks for all object references
- Require JWT or session tokens for sensitive actions like cancellation
- Log and alert on cancellation attempts from unauthenticated sessions

## Objectives

1. Bypass access controls to cancel targeted reservations
2. Disrupt user bookings without detection
3. Demonstrate impact of IDOR on business operations

## Instructions

### Step 1: Construct Cancellation URL

**Context**: Build the direct link to the cancellation feature using the ID.

Format the URL as https://www.yelp.com/reservations/cancel?id=[ID] (replace [ID] with the obtained reservation ID, e.g., 12345).

### Step 2: Access and Execute Cancellation

**Context**: Submit the request without login to exploit the lack of checks.

Open the URL in a web browser. The page should load the cancellation interface directly. Confirm the action by clicking the cancel button if prompted; no authentication dialog will appear due to the IDOR flaw.

**Expected Output**: A success message like "Reservation canceled successfully" or redirection to a confirmation page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- web-exploit
