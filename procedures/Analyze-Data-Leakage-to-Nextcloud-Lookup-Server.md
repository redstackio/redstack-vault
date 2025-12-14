---
id: proc-nextcloud-leak-analyze-001
tags:
  - data-leak
  - nextcloud
  - server-log
  - privacy-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:24:39.955Z'
skill_level: low
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Automated Collection]]'
---
# Analyze-Data-Leakage-to-Nextcloud-Lookup-Server

## Summary

This procedure examines server-side processing and network traffic to confirm the leakage of search terms and server IP to the external Nextcloud lookup server due to the default 'lookup=true' interpretation.

## Description

Following a sharee search, the Nextcloud server's ShareesAPIController.php (line 144) defaults missing 'lookup' parameters to true, prompting a query to the central lookup server. This sends sensitive data externally without consent, compromising user privacy by exposing search intents and infrastructure details.

## Requirements

1. Access to Nextcloud server logs (e.g., via SSH or dashboard)
2. Network monitoring tool (e.g., tcpdump or proxy) for traffic capture
3. Knowledge of PHP code in ShareesAPIController.php

## Defense

Defensive measures and detection strategies:

- Patch server to require explicit 'lookup' parameter or disable global search
- Implement logging alerts for lookup server connections
- Regularly audit API requests for parameter anomalies

## Objectives

1. Capture and inspect leaked data
2. Verify root cause in server code
3. Quantify privacy impact

## Instructions

### Step 1: Monitor Server Logs

**Context**: Check for query initiation.

Access Nextcloud logs (e.g., data/nextcloud.log) after performing a search and look for entries related to ShareesAPIController and lookup queries.

> Expected: Log shows default to lookup=true and external request details.

### Step 2: Capture Network Traffic

**Context**: Observe transmission to external server.

Use a tool like Wireshark or server-side tcpdump to filter traffic to lookup.nextcloud.com, noting payloads with search terms and source IP.

> Expected: Requests reveal leaked data, confirming no user consent.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Automated Collection]] Automated Collection

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[data-leak]]
- [[nextcloud]]
- [[server-log]]
- [[privacy-leak]]
