---
id: proc-uuid-mtn-step3-001
name: Access-Offers-Dashboard
tags:
  - dashboard
  - access
  - web
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
updated_at: '2025-12-14T17:30:27.222Z'
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
# Access-Offers-Dashboard

## Summary

This procedure loads the authenticated user's offers dashboard, displaying personalized content and confirming session validity prior to exploitation.

## Description

After OTP validation, the browser redirects to the dashboard endpoint. This step verifies access to user-specific features like offer listings. In the attack chain, it serves as the pivot point for IDOR. Target: https://mtn.ng/offers/list?phone=<authenticated_phone>. Prerequisites: Valid session. Outcomes: Visibility into account offers, setting up for unauthorized parameter changes.

## Requirements

1. Successful OTP validation
2. Persistent browser session
3. Internet connectivity

## Defense

Defensive measures and detection strategies:

- Server-side session validation on every dashboard load
- Log access patterns for anomaly detection (e.g., rapid parameter changes)
- Implement CSRF tokens for dashboard actions

## Objectives

1. Confirm authenticated access
2. Observe dashboard structure for exploitation points
3. Identify the 'phone' parameter in the URL

## Instructions

### Step 1: Load Dashboard Post-Authentication

**Context**: Automatically or manually navigate to the offers list after validation.

The page should load at https://mtn.ng/offers/list?phone=<your_phone>, showing offers.

### Step 2: Verify Content

**Context**: Ensure the dashboard reflects the authenticated user's data.

Inspect the page for personalized elements like current promotions or balance info.

> If content loads correctly, the session is active; note the exact URL for modification in the next step.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dashboard
- session-access
- verification
