---
tags:
  - cache-poisoning
  - dos
  - varnish
  - gcp
  - web
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Cloud (GCP)
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Send-Normal-GET-Request-to-Static-Asset]]'
  - '[[procedures/Send-Poisoned-GET-with-X-Http-Method-Override]]'
  - '[[procedures/Verify-Poisoned-Cache-Entry]]'
  - '[[procedures/Purge-and-Poison-Live-Cache-for-DoS]]'
step_count: 4
techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.063Z'
description: >-
  Multi-stage attack exploiting cache poisoning in GitLab's Varnish CDN on GCP
  to cause widespread DoS by serving empty JS and CSS files.
skill_level: intermediate
impact_level: high
id: f9d8bc51-01db-4757-ad3c-2ecc23090ec9
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Cache Poisoning Denial of Service on GitLab Static Assets CDN

Multi-stage attack chain demonstrating a complete attack workflow exploiting cache poisoning in GitLab's static asset CDN at assets.gitlab-static.net, hosted on GCP with Varnish caching, to cause denial of service by serving empty responses for critical JS and CSS files, rendering GitLab.com and about.gitlab.com unusable.

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
    A[Normal Request] --> B[Poison Cache with HEAD Override]
    B --> C[Verify Poisoning]
    C --> D[Purge and Live Poison for DoS]
    D --> E[Impact: Empty Assets Served]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl or browser)

### Target Environment

- Web platform with Varnish CDN on GCP
- Static asset endpoints like https://assets.gitlab-static.net/
- No authentication required

### Initial Access Requirements

- Public internet access to the CDN
- No credentials needed
- Ability to send custom HTTP headers

## Detailed Attack Procedures

### Step 1: Send Normal GET Request to Static Asset
procedure: [[procedures/Send-Normal-GET-Request-to-Static-Asset]]

**Objective**: Establish baseline behavior by requesting a static JS file and confirming it is cached by Varnish.

**Instructions**: Use a standard HTTP GET request to fetch a webpack chunk JS file from the CDN. Observe the response includes the full JS content and Varnish cache headers.

**Expected Output**: Full JS file content with headers like X-Varnish-Cache: MISS or HIT.

**Success Indicators**:
- JS file loads correctly
- Cache headers present indicating Varnish involvement

### Step 2: Send Poisoned GET with X-Http-Method-Override
procedure: [[procedures/Send-Poisoned-GET-with-X-Http-Method-Override]]

**Objective**: Test cache poisoning by overriding the GET method to HEAD, which returns an empty body, without affecting the live cache using a cache buster parameter.

**Instructions**: Send a GET request with the X-Http-Method-Override: HEAD header and a query parameter like ?cb=unique to isolate the test. The GCP backend processes the override, returning an empty response, which Varnish caches due to the header not being in the cache key.

**Expected Output**: Empty HTTP response body.

**Success Indicators**:
- Empty response received
- No errors from the server

### Step 3: Verify Poisoned Cache Entry
procedure: [[procedures/Verify-Poisoned-Cache-Entry]]

**Objective**: Confirm the poisoning effect by requesting the resource with the cache buster and observing the empty response from cache.

**Instructions**: Access the URL with the cache buster parameter in a browser or via HTTP client to check if the cached empty response is served.

**Expected Output**: Empty content for the JS file.

**Success Indicators**:
- Browser shows blank or broken page due to empty JS
- Response body is empty

### Step 4: Purge and Poison Live Cache for DoS
procedure: [[procedures/Purge-and-Poison-Live-Cache-for-DoS]]

**Objective**: Evict the existing cache entry and poison the live cache to affect all users, causing widespread DoS.

**Instructions**: First, send a PURGE request to the target URL to clear the cache. Then, immediately send the poisoning GET request without the cache buster and with X-Http-Method-Override: HEAD to cache the empty response for the main resource.

**Expected Output**: PURGE succeeds with 200 or 204, followed by empty responses on subsequent normal GET requests.

**Success Indicators**:
- Normal requests now return empty bodies
- GitLab.com assets fail to load, breaking functionality

## Attack Chain Summary

### Key Achievements

1. Demonstrated cache poisoning via method override header
2. Verified impact on isolated and live cache entries
3. Achieved DoS affecting all users of GitLab.com by breaking JS/CSS delivery
4. Exploited lack of authorization on PURGE for amplification

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
