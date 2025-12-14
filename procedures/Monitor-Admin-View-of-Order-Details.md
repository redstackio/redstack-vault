---
id: proc-zomato-xss-monitor-2
tags:
  - xss
  - monitoring
  - zomato
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:58.383Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Monitor Admin View of Order Details

## Summary

This procedure monitors for the triggering of a Blind XSS payload by waiting for an admin to view the injected order details in the Zomato backend dashboard, leading to script execution.

## Description

After payload injection, the attack relies on normal business processes where admins review orders. The lack of sanitization causes the payload to render and execute in the admin's browser. This step is passive, requiring patience based on order volume and admin activity. Expected outcomes include remote script loading if successful.

## Requirements

1. Previously injected order with XSS payload
2. Access to XSS Hunter dashboard for real-time monitoring
3. Awareness of typical admin review timelines (e.g., minutes to hours)

## Defense

Defensive measures and detection strategies:

- Log and audit admin dashboard views for suspicious inputs
- Implement rate-limiting or anomaly detection on order reviews
- Use web application firewalls (WAF) to scan for XSS patterns in logs

## Objectives

1. Trigger payload execution via admin interaction
2. Confirm blind nature of the attack
3. Prepare for detection in the next step

## Instructions

### Step 1: Initiate Monitoring

**Context**: Set up observation on the XSS Hunter interface to watch for incoming callbacks.

Log into XSS Hunter and navigate to the active hunt dashboard. Refresh periodically or enable notifications for new hits.

> Expected output: Dashboard showing no activity initially.

### Step 2: Await Admin Trigger

**Context**: Wait for the order to be processed and viewed by an admin.

Monitor order status in the Zomato app for updates. The payload fires when the special instructions are rendered in the dashboard.

> Expected output: Potential callback if triggered; otherwise, continued waiting.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- xss
- monitoring
- blind-xss
