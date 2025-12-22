---
id: proc-uuid-003
tags:
  - idor
  - manipulation
  - unauthorized-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:30.011Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Manipulate-ID-Parameter-for-Unauthorized-Access

## Summary

This procedure exploits the IDOR vulnerability by modifying the ID parameter in the shot records endpoint to access records of unauthorized individuals, resulting in the server returning their PDF data without checks.

## Description

The application fails to verify if the requested ID belongs to the authenticated user, serving any ID's PDF in the 302 response body. Using Burp Suite, the parameter is incremented or decremented (e.g., own_id +1). This discloses PHI/PII like vaccination details for dependents, retirees, or others. Prerequisites: Active session and intercepted baseline request.

## Requirements

1. Intercepted authorized request in Burp Suite
2. Knowledge of sequential ID structure (assumed incremental)
3. Valid session to avoid re-authentication

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks comparing user ID to requested ID
- Use indirect references (e.g., hashes) instead of direct IDs
- Log and alert on ID parameter mismatches or rapid sequential requests

## Objectives

1. Bypass authorization to retrieve unauthorized record
2. Confirm IDOR by receiving foreign PDF data
3. Enable data extraction for collection

## Instructions

### Step 1: Intercept Baseline Request

**Context**: From Step 2, have the authorized request in Burp Repeater.

No command; copy the request to Repeater tab.

> Ensure session cookies are included.

### Step 2: Modify and Send Request

**Context**: Alter the ID parameter and resend to exploit IDOR.

In Burp Repeater, change [own_id] to [manipulated_id] (e.g., +1) in https://███████=[manipulated_id].

> Send request; expect 302 with unauthorized PDF in body, redirect to █████████.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[manipulation]]
- [[unauthorized-access]]
