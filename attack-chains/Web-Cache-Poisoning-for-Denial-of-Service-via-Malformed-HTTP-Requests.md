---
tags:
  - web-cache-poisoning
  - dos
  - http
  - nginx
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/get-malformed-http-version-1]]'
  - '[[commands/get-malformed-http-version-2]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Send-Malformed-HTTP-Request-to-Poison-Cache]]'
  - '[[procedures/Verify-Cached-Poisoned-Response]]'
  - '[[procedures/Demonstrate-DoS-on-Real-Page]]'
  - '[[procedures/Extend-and-Automate-DoS-Attack]]'
step_count: 4
techniques:
  - '[[Endpoint Denial of Service]]'
description: >-
  Exploits web cache poisoning on a web server by sending malformed HTTP
  requests to cache error responses, leading to prolonged denial of service on
  targeted pages.
skill_level: intermediate
impact_level: high
id: b0bc4e12-18db-4e9b-8509-be7613a9671d
created_at: '2025-12-13T09:00:34.374Z'
updated_at: '2025-12-13T09:00:34.374Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Web Cache Poisoning for Denial of Service via Malformed HTTP Requests

Multi-stage attack chain demonstrating web cache poisoning on a U.S. Department of Defense website by exploiting the caching of error responses from malformed HTTP requests, resulting in denial of service for targeted pages.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Malformed Request] --> B[Verify Poisoning]
    B --> C[Demonstrate DoS]
    C --> D[Extend Attack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Web platform with caching enabled (e.g., nginx)
- Services: Web Cache
- Network access: Ability to send HTTP requests to the target server

### Initial Access Requirements

- No credentials required
- External network access to the public-facing website
- No prior access needed

## Detailed Attack Procedures

### Step 1: Send Malformed HTTP Request to Poison Cache
procedure: [[procedures/Send-Malformed-HTTP-Request-to-Poison-Cache]]

**Objective**: Trigger a 400 Bad Request response and poison the cache with it.

**Instructions**: Send a GET request with an invalid HTTP version using [[commands/get-malformed-http-version-1]]:

```bash
GET /yeettest?yeettest=1 HTTP/1.1234567
```

**Expected Output**: 400 Bad Request response, which gets cached.

**Success Indicators**:
- Server returns 400 error
- Cache is poisoned for the specified path

### Step 2: Verify Cached Poisoned Response
procedure: [[procedures/Verify-Cached-Poisoned-Response]]

**Objective**: Confirm that the poisoned response is served from cache to subsequent requests.

**Instructions**: Send a similar GET request using [[commands/get-malformed-http-version-2]]:

```bash
GET /yeettest?yeettest=1 HTTP/1.123456
```

**Expected Output**: Cached 400 Bad Request instead of expected 404.

**Success Indicators**:
- Request returns cached 400 error
- Poisoning is verified

### Step 3: Demonstrate DoS on Real Page
procedure: [[procedures/Demonstrate-DoS-on-Real-Page]]

**Objective**: Poison the cache of a legitimate page to cause DoS.

**Instructions**: Send a malicious request with a large header to a real page, such as https://www.████████/████████.htm, to trigger and cache a 400 response.

**Expected Output**: The page returns 400 error when accessed normally.

**Success Indicators**:
- Targeted page becomes unavailable
- Error served from cache

### Step 4: Extend and Automate DoS Attack
procedure: [[procedures/Extend-and-Automate-DoS-Attack]]

**Objective**: Target additional pages and automate requests for prolonged DoS.

**Instructions**: Repeat poisoning on other pages like https://www.██████████/█████ and automate repeated attacks to extend cache duration beyond 24 hours.

**Expected Output**: Multiple pages return 400 errors persistently.

**Success Indicators**:
- DoS extended across multiple pages
- Automation maintains poisoning

## Attack Chain Summary

### Key Achievements

1. Successful cache poisoning with error responses
2. Denial of service on targeted web pages
3. Potential for automated, prolonged disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

*Last updated: [TIMESTAMP]*
