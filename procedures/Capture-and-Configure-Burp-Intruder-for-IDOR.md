---
id: proc-capture-config-burp-idor
tags:
  - burp-intruder
  - idor
  - request-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:34.970Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-and-Configure-Burp-Intruder-for-IDOR

## Summary

This procedure captures a vulnerable GET request from the DoD portal in Burp Suite and configures the Intruder tool to target the numeric parameter susceptible to IDOR, enabling brute-force testing for unauthorized data access.

## Description

The DoD portal uses predictable numeric IDs in URL paths (e.g., /61/124948002) without proper authorization checks, leading to IDOR. By sending the request to Intruder and marking the parameter, attackers can inject payloads to access other users' records. Prerequisites include an active authenticated session. Outcomes include a configured attack ready for payload execution, revealing PII on successful hits.

## Requirements

1. Active Burp Suite session with captured HTTP History
2. Authenticated portal access from previous procedure
3. Knowledge of the target URL path (e.g., /SelfService/Home/dynamicdata/section/...)
4. Burp Suite Professional or Community edition with Intruder enabled

## Defense

Defensive measures and detection strategies:

- Enforce server-side authorization checks on all dynamic endpoints
- Rate-limit requests to /dynamicdata/ paths to detect brute-forcing
- Log and alert on parameter manipulations in access logs

## Objectives

1. Isolate the IDOR-vulnerable parameter in the request
2. Prepare Intruder for automated payload insertion
3. Validate configuration before launching the attack

## Instructions

### Step 1: Select and Send Request to Intruder

**Context**: Identify the successful GET request in history for transfer to Intruder.

In Burp Proxy > HTTP History, right-click the 200-status GET (e.g., https://█████████/SelfService/Home/dynamicdata/section/██████████/██████████%20TPU/61/124948002) and select 'Send to Intruder'.

> The request loads into the Intruder tab, ready for position marking.

### Step 2: Clear and Mark Positions

**Context**: Ensure only the vulnerable numeric is targeted to focus the attack.

In Intruder Positions, click 'Clear §' to remove defaults. Highlight the '61' in the path and click 'Add §'.

> A single § appears on the numeric parameter, confirming the injection point.

### Step 3: Verify Configuration

**Context**: Double-check the marked position matches the IDOR vector.

Review the request preview to ensure the § is on the correct path segment (e.g., /61/).

> No errors in positioning; proceed to payloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[intruder]]
- [[url-manipulation]]
