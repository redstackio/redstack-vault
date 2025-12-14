---
tags:
  - endpoint-discovery
  - http-analysis
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.770Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c99b1ccb-61b6-4ace-bc0c-365354761499
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Attachment-Download-Endpoint

## Summary

This procedure analyzes captured traffic to pinpoint the attachment download endpoint, revealing the /attachments/{ID} structure vulnerable to IDOR.

## Description

After sending an attachment, review Burp logs for the GET request to download it. The endpoint uses a simple numeric ID without path traversal protections, and headers like X-Signal-Agent indicate the client. This identifies the target for manipulation.

## Requirements

1. Captured traffic from previous attachment send
2. Burp Suite Proxy history accessible
3. Knowledge of HTTP request formats

## Defense

Defensive measures and detection strategies:

- Add endpoint logging to track access patterns and anomalous IDs
- Implement IP-based access controls for download endpoints
- Use request signing to validate ID ownership

## Objectives

1. Locate the exact download request in traffic logs
2. Document endpoint URL and headers
3. Confirm ID parameterization

## Instructions

### Step 1: Filter Burp History

**Context**: Isolate relevant requests.

In Burp Proxy > HTTP history, filter for GET /attachments/.

> GUI filter. Expected: Request like GET /attachments/938540538 visible.

### Step 2: Inspect Request Details

**Context**: Note structure and headers.

Examine the full request: Host: ameim.bs2dl.yy.com, X-Signal-Agent: OWA.

> Review. Expected: Endpoint confirmed as /attachments/{ID}.

### Step 3: Test Download

**Context**: Verify functionality.

Replay the request in Proxy to ensure file serves.

> Replay. Expected: Attachment content returned.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[endpoint-discovery]]
- [[idor]]
