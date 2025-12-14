---
id: p4c5d6e7-f8g9-0123-defg-4567890123
tags:
  - indrive
  - pii-leak
  - data-exposure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Mobile App
  - Web API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:25:17.853Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
---
# Access-Revealed-Passenger-PII

## Summary

Following forced acceptance, this procedure retrieves unauthorized passenger PII (e.g., phone number) exposed due to the access control flaw, along with enforcement of the ride at potentially inflated prices.

## Description

Post-acceptance, the server treats the driver as authorized for the ride, revealing details in the app dashboard or API responses. This leads to privacy violations and financial impacts. Prerequisites: Successful force-accept. Outcomes: PII collection and ride progression without consent.

## Requirements

1. Completed force-acceptance with valid ride status
2. Access to driver's app session or follow-up API
3. No additional auth beyond initial token

## Defense

Defensive measures and detection strategies:

- Restrict PII visibility until mutual confirmation
- Encrypt and log PII access attempts
- Implement data loss prevention for sensitive fields

## Objectives

1. Extract passenger phone and details
2. Confirm financial enforcement
3. Realize full impact of chain

## Instructions

### Step 1: Query Ride Details

**Context**: Use app UI or API to view accepted ride info post-acceptance.

No specific command; poll /api/order or similar endpoint, or check app dashboard for PII.

### Step 2: Validate Exposure

**Context**: Confirm PII visibility and price lock.

Monitor response: Expected PII in JSON or UI; success if phone revealed without passenger action.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Unsecured Credentials]] Unprotected Storage of Credentials (adapted for PII)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[indrive]]
- [[pii-leak]]
- [[data-exposure]]
