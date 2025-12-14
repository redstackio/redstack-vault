---
id: proc-leaked-staff-id-access
tags:
  - information-disclosure
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/curl-staff-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:58.112Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Use-Leaked-Staff-ID-for-Unauthorized-Staff-Access

## Summary

Utilize a leaked staff ID from a public badge image to POST to the staff API endpoint, gaining access to the restricted staff.bountypay.h1ctf.com subdomain.

## Description

The staff ID is visible in Sandra's badge image, allowing direct submission to /api/staff without authentication checks. This exposes staff functions and chains to escalation.

## Requirements

1. Access to the badge image
2. Staff ID extraction (e.g., via image analysis)
3. API access

## Defense

Defensive measures and detection strategies:

- Remove sensitive IDs from public images
- Require auth for staff endpoints
- Audit image uploads

## Objectives

1. Submit leaked ID
2. Access staff subdomain
3. Enable further privileges

## Instructions

### Step 1: Extract Staff ID

**Context**: Analyze badge image for ID.

**Command** ([[commands/curl-staff-access]]):
```bash
# Manual: Use image viewer or OCR to find ID, e.g., 'STAFF123'
```

> ID obtained.

### Step 2: POST to Staff Endpoint

**Context**: Send ID to gain access.

**Command** ([[commands/curl-staff-access]]):
```bash
curl -X POST 'https://api.bountypay.h1ctf.com/api/staff' -d 'staff_id=STAFF123'
```

> Response: Access granted to staff site.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-staff-access]]

## Tools Used

- None specific

## Tags

- [[information-disclosure]]
- [[privilege-escalation]]
