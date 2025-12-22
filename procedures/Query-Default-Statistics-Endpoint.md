---
id: proc-mapbox-default-query
tags:
  - api-query
  - baseline
  - dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-mapbox-default-stats]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.055Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Query-Default-Statistics-Endpoint

## Summary

This procedure queries the Mapbox account statistics endpoint with default parameters to establish a baseline response size and confirm functionality before exploitation.

## Description

The Mapbox statistics endpoint at https://www.mapbox.com/core/statistics/v1/{username}/account provides user metrics like countries, browsers, and services. Using default 'interval=day' and a short 'period', the response is small (~2.5 KB). This step verifies access in an authenticated session and measures normal behavior. Expected outcomes include a JSON response with aggregated data over the specified period.

## Requirements

1. Authenticated session cookies
2. Knowledge of username
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Rate limit API endpoints
- Log query parameters for anomalies

## Objectives

1. Confirm endpoint accessibility
2. Measure baseline response size
3. Identify default parameter behavior

## Instructions

### Step 1: Send Default Request

**Context**: Use default parameters to query recent data.

**Command** ([[commands/curl-mapbox-default-stats]]):
```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=day&period=1461766083142,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155" -o default_response.json
```

> Response is ~2.5 KB JSON with metrics for the short period (e.g., one day).

### Step 2: Analyze Response Size

**Context**: Check file size to baseline.

**Command** ([[commands/curl]]):
```bash
ls -lh default_response.json
```

> Expected: Size around 2.5 KB, confirming normal operation.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-mapbox-default-stats]]

## Tools Used


## Tags

- api-query
- baseline
- dos
