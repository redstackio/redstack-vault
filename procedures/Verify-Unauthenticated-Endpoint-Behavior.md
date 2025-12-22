---
tags:
  - verification
  - http-status
  - privacy-check
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-private-profile-status]]'
  - '[[commands/curl-check-public-profile-status]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:13.224Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d8878bc7-d01a-4ae0-86dd-cbd057207fc6
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-Unauthenticated-Endpoint-Behavior

## Summary

This procedure uses curl to test the HTTP status of the charts.json endpoint without authentication, confirming 403 for private profiles and 200 for public ones, to contrast with the authenticated XSSI bypass.

## Description

To validate the vulnerability's scope, send HEAD requests to the JSONP endpoint for both private (e.g., EdOverflow) and public (e.g., Liberapay) profiles. This checks that privacy enforcement works correctly for unauthenticated access but fails for credentialed cross-origin scenarios. Use silent mode to fetch only headers. This reconnaissance step highlights the information disclosure risk.

## Requirements

1. curl installed on system
2. Internet access to Liberapay
3. Target usernames (private and public)

## Defense

Defensive measures and detection strategies:

- Ensure consistent privacy checks across all authentication states
- Rate-limit or block suspicious HEAD/GET requests to JSON endpoints
- Log unauthenticated access attempts to private resources
- Use automated scanners to verify endpoint behaviors

## Objectives

1. Confirm 403 for private unauthenticated requests
2. Confirm 200 for public unauthenticated requests
3. Validate differential privacy enforcement

## Instructions

### Step 1: Test Private Profile

**Context**: Check status for a profile with hide_receiving enabled.

**Command** ([[commands/curl-check-private-profile-status]]):
```bash
curl -Is https://liberapay.com/EdOverflow/charts.json?callback=rip | head -1
```

> This fetches headers silently; expect HTTP/2 403 indicating privacy block.

### Step 2: Test Public Profile

**Context**: Check status for a profile without privacy restrictions.

**Command** ([[commands/curl-check-public-profile-status]]):
```bash
curl -Is https://liberapay.com/Liberapay/charts.json?callback=rip | head -1
```

> Expect HTTP/2 200, showing successful access.

### Step 3: Compare Results

**Context**: Analyze outputs to confirm behavior.

No command; review headers for status codes.

> This underscores the authenticated bypass vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-private-profile-status]]
- [[commands/curl-check-public-profile-status]]

## Tools Used

- [[tools/curl]]

## Tags

- verification
- http-status
- privacy-check
