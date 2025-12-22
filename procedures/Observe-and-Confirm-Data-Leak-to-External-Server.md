---
tags:
  - leak
  - observation
  - server-logs
type: procedure
tools: []
tactics:
  - '[[Exfiltration]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
updated_at: '2025-12-14T17:24:45.115Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 465146da-d5e6-4abd-b332-ccbcb62f54fd
validated: true
mitre_tactics:
  - '[[Exfiltration]]'
mitre_techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
---
# Observe-and-Confirm-Data-Leak-to-External-Server

## Summary

This procedure details how to monitor and verify the leakage of search queries and server IP to the external Nextcloud lookup server, confirming the vulnerability's impact.

## Description

Upon receiving the incomplete API request, the Nextcloud server at ShareesAPIController.php (line 144) defaults the 'lookup' parameter to true, initiating a query to the external lookup server (e.g., lookup.nextcloud.com). This leaks sensitive data like the search term and originating IP without user awareness. Observation can be done via server logs, proxy tools, or external server access.

## Requirements

1. Access to Nextcloud server logs (e.g., via tail -f on log files)
2. Network monitoring capability (e.g., tcpdump or Wireshark)
3. Optional: Access to Nextcloud lookup server for confirmation

## Defense

Defensive measures and detection strategies:

- Patch server to handle missing parameters securely
- Implement API request validation and logging
- Use firewalls to restrict outbound connections to lookup servers

## Objectives

1. Capture the server's response to the API request
2. Identify outbound query to external server
3. Validate leaked data contents

## Instructions

### Step 1: Monitor Server Logs

**Context**: Watch for incoming API requests.

Tail the Nextcloud log file (e.g., data/nextcloud.log) during the search step. Look for entries related to ShareesAPIController and the absence of 'lookup' parameter.

### Step 2: Inspect Network Traffic

**Context**: Capture outbound requests.

Use a tool like Wireshark to filter traffic to the external lookup server domain. Confirm the request includes the search term and source IP.

### Step 3: Verify Leak

**Context**: Cross-check data.

Compare the captured query with the entered search term to confirm unintended transmission.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration]] Exfiltration

### Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol]] Exfiltration Over Unencrypted Non-C2 Protocol

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[leak]]
- [[observation]]
- [[server-logs]]
