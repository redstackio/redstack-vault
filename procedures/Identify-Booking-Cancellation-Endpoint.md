---
tags:
  - recon
  - web
  - api
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:33.875Z'
sub_techniques: []
id: de20b8ef-9a17-4032-b3de-33b86a41894c
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Booking-Cancellation-Endpoint

## Summary

This procedure involves inspecting legitimate booking cancellation requests in the Eternal application to identify the API endpoint and parameters used, setting the stage for IDOR exploitation.

## Description

In the context of testing the table booking system, authenticate as a user, create a booking, and monitor the cancellation process to capture the HTTP request. The endpoint typically includes a booking ID parameter that is directly referenced without ownership checks, enabling subsequent IDOR attacks. Expected outcomes include understanding the request format for tampering.

## Requirements

1. Authenticated access to the Eternal web application
2. Browser with developer tools or an intercepting proxy (e.g., Burp Suite)
3. Ability to create and cancel personal bookings

## Defense

Defensive measures and detection strategies:

- Implement request logging to monitor unusual API calls
- Use rate limiting on booking endpoints to detect enumeration

## Objectives

1. Locate the exact API endpoint for booking cancellation
2. Document the booking ID parameter location and format
3. Confirm the request method (e.g., POST) and required headers (e.g., Authorization)

## Instructions

### Step 1: Authenticate and Create Booking

**Context**: Gain legitimate access to observe normal behavior.

Log in to the application and book a table to generate a valid booking ID.

### Step 2: Monitor Cancellation Request

**Context**: Capture the network traffic during cancellation.

Open developer tools (F12), navigate to Network tab, cancel the booking, and inspect the request for endpoint URL, method, and parameters.

**Expected Output**: Details like POST /api/v1/bookings/cancel with {"booking_id": "your_id"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[api]]
