---
id: p7g8h9i0-j1k2-3456-ghij-789012345678
tags:
  - automation
  - enumeration
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:28.831Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Automate-User-ID-Enumeration-with-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder to automate cycling through user IDs in the IDOR endpoint, enabling bulk enumeration of all user data.

## Description

Manual requests are inefficient for large databases; automation via Burp Intruder brute-forces the USER_ID parameter (e.g., 1-100), collecting responses to identify valid accounts and extract their sensitive information, simulating a full data breach.

## Requirements

1. Burp Suite with proxy/interceptor running
2. Captured base request to the endpoint with JWT
3. Range of IDs to test (1-100)

## Defense

Defensive measures and detection strategies:

- Rate limiting and IP blocking on API endpoints
- Anomaly detection for sequential ID requests
- Web application firewall (WAF) rules for parameter fuzzing

## Objectives

1. Configure payload for ID brute-force
2. Execute and collect responses
3. Aggregate leaked user data

## Instructions

### Step 1: Intercept and Send to Intruder

**Context**: Capture a sample request in Burp Proxy.

Browse or send the GET request, right-click and select "Send to Intruder".

> Prepares for automation. Expected output: Request loaded in Intruder.

### Step 2: Set Payload Position

**Context**: Mark the USER_ID for replacement.

Highlight {USER_ID} in the URL and click "Add §" to set as payload position.

> Targets the parameter. Expected output: Position marked with §.

### Step 3: Configure Payloads

**Context**: Define IDs to cycle through.

In Payloads tab, set type to "Numbers", from 1 to 100, step 1.

> Generates sequence. Expected output: Payload list ready.

### Step 4: Start Attack

**Context**: Run the enumeration.

Click "Start Attack" and monitor responses.

> Fetches data for each ID. Expected output: Table of responses with user info for valid IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- automation
- enumeration
- burp
