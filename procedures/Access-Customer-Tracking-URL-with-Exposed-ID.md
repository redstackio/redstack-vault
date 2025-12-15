---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - url-access
  - unauthorized-disclosure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:17.309Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Customer-Tracking-URL-with-Exposed-ID

## Summary

This procedure constructs a customer tracking URL using the leaked trip_no and accesses it without authorization, resulting in disclosure of excessive customer information in Bykea's system.

## Description

By leveraging the exposed trip_no, attackers can bypass access controls by directly navigating to tracking endpoints. The URL format exposes customer details like location and contacts upon visit, highlighting IDOR-like issues in web tracking features. Resolution involves hashing IDs in URLs.

## Requirements

1. Extracted trip_no from prior step
2. Active browser session with driver authentication
3. Knowledge of Bykea tracking URL pattern (e.g., /track?trip_no=ID)

## Defense

Defensive measures and detection strategies:

- Add server-side validation for trip_no ownership before rendering tracking pages
- Implement URL parameter obfuscation or short-lived tokens
- Detect direct URL access via referer checks or anomaly monitoring

## Objectives

1. Construct exploitable tracking URL
2. Gain unauthorized view of customer data
3. Demonstrate information disclosure impact

## Instructions

### Step 1: Build URL

**Context**: Format the tracking endpoint with the leaked ID.

Use the base URL https://bykea.com/track and append ?trip_no=TRIP123456 (replace with actual ID).

### Step 2: Navigate and View

**Context**: Access the URL to retrieve data.

Paste the URL into the browser address bar while logged in as the unauthorized driver. The page should load without errors, showing customer info.

**Expected Output**: Tracking page with customer details (e.g., map, phone, route).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-access]]
- [[unauthorized-disclosure]]
