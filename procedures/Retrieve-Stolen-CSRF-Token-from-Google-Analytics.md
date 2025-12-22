---
id: proc-uuid-4
tags:
  - token-retrieval
  - analytics
  - exfiltration
type: procedure
tools:
  - '[[tools/Google-Analytics]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:27:57.293Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Retrieve-Stolen-CSRF-Token-from-Google-Analytics

## Summary

This procedure involves accessing the attacker's Google Analytics dashboard to view real-time reports and extract the victim's CSRF token from the captured full referral URL.

## Description

GA's real-time analytics displays active users and their page URLs. Since the embedded code sends the complete redirect URL (including ?authenticity_token=...), the attacker can immediately spot and copy the token from the dashboard, enabling quick exploitation before the token expires.

## Requirements

1. Access to GA account linked to the app's tracking ID
2. Real-time reporting enabled in GA
3. Timing: Monitor shortly after victim interaction

## Defense

Defensive measures and detection strategies:

- Review and audit embedded analytics code for data leakage
- Implement URL parameter stripping in tracking scripts
- Alert on unusual real-time spikes from partner domains

## Objectives

1. Access real-time GA data
2. Identify and extract the token from URL
3. Prepare token for use in forged requests

## Instructions

### Step 1: Log into Google Analytics Dashboard

**Context**: Navigate to the GA interface to access reports.

No specific command; open browser to https://analytics.google.com/analytics/web/ and sign in with attacker's credentials.

> Expected output: Dashboard loads with property for the tracking ID.

### Step 2: View Real-Time Analytics

**Context**: Check active users section for the leaked URL.

No specific command; select 'Real Time' from the left menu, then view 'Active users' or 'Events' to see referral URLs from the app page.

> Expected output: Entry showing https://apps.shopify.com/[app_id]?authenticity_token=[stolen_token]; copy the token value.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Analytics]]

## Tags

- token-retrieval
- analytics
- exfiltration
