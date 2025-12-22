---
tags:
  - xss-capture
  - data-exfiltration
  - notification
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 74053664-2ebb-4680-b6b2-29cea4eae35f
created_at: '2025-12-13T23:52:55.553Z'
updated_at: '2025-12-13T23:52:55.553Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Capture-XSS-Executions-with-XSS-Hunter

## Summary

This procedure uses XSS Hunter to monitor and capture executions of injected XSS payloads, receiving notifications with details like triggering IP addresses and exfiltrated data from affected admin sessions.

## Description

After injection and triggering, XSS Hunter sends email alerts for each execution, revealing sensitive information such as emails, locations, store names, IDs, and usernames from dashboard views (up to 25 accounts per page, across 10+ pages). This enables ongoing data collection as multiple admins interact with the search functionality over time.

## Requirements

1. Active XSS Hunter account and generated payload script
2. Email access for notifications
3. Injected payloads using XSS Hunter

## Defense

Defensive measures and detection strategies:

- Block outbound requests to known XSS tracking domains (e.g., xsshunter.com)
- Monitor network traffic for beaconing to external C2-like services
- Educate admins on phishing risks and anomalous browser prompts

## Objectives

1. Collect proof of exploitation from multiple triggers
2. Exfiltrate sensitive user data visible to admins
3. Assess vulnerability scope through repeated executions

## Instructions

### Step 1: Deploy XSS Hunter Payload

**Context**: Ensure the injected payload includes the XSS Hunter script for remote capture.

During profile injection (from prior procedure), embed the unique XSS Hunter payload script provided in your dashboard.

> Payload activation sends data to XSS Hunter upon execution.

### Step 2: Monitor Executions

**Context**: Receive and analyze notifications as admins trigger the XSS.

Check your email for alerts from XSS Hunter, detailing IP addresses, timestamps, and stolen data (e.g., user emails, store IDs).

> Alerts continue for hours, showing data from various sources; compile for impact assessment.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[xss-capture]]
- [[data-exfiltration]]
