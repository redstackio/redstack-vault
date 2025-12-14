---
id: proc-observe-burp-traffic-001
tags:
  - traffic-intercept
  - oauth
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:24:44.823Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Network Sniffing]]'
---
# Observe-Intercepted-Traffic-in-Proxy

## Summary

This procedure monitors the proxy for captured traffic from the Twitter iOS app, revealing sensitive data like OAuth tokens and enabling further analysis or modification.

## Description

In Burp Suite, view HTTP history for requests to api.twitter.com, including Authorization headers with OAuth 1.0a tokens, client_uuid, and device_id. Responses may include HSTS headers ignored by the app. Outcomes: Data exfiltration proof, potential for injection (e.g., fake settings.json).

## Requirements

1. Burp Suite in transparent mode
2. Traffic redirected and app launched
3. Knowledge of target endpoints

## Defense

Defensive measures and detection strategies:

- Implement token rotation and short-lived OAuth
- Log proxy detections in network security tools
- App crash reports for MITM attempts

## Objectives

1. Capture sensitive requests
2. Analyze headers and payloads
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Monitor Proxy History

**Context**: Check for incoming requests post-app launch.

In Burp: Proxy > HTTP history > Filter for api.twitter.com

> Expected: Entries like GET /1.1/help/settings.json with OAuth headers.

### Step 2: Inspect and Modify

**Context**: View details and optionally drop/modify.

Select request > Inspect in Repeater

> Reveals tokens; test injection by altering response to 200 with malicious JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- traffic-intercept
- oauth
