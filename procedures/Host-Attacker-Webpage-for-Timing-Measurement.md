---
id: proc-uuid-002
tags:
  - webpage-hosting
  - javascript-timing
type: procedure
tools:
  - '[[tools/Resource-Timing-API]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/calculate-load-times-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:50.107Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Host-Attacker-Webpage-for-Timing-Measurement

## Summary

This procedure involves creating and hosting a malicious webpage that uses JavaScript and `<img>` tags to load HackerOne endpoints cross-origin, measuring response times via the Resource Timing API for side-channel data inference.

## Description

Targeted at web browsers, the attacker sets up an HTML page on their server with embedded PHP to generate dynamic `<img>` elements pointing to vulnerable endpoints. JavaScript captures load timings post-page load, distinguishing successful responses (200 OK) from errors. This enables stealthy measurement without direct API access, exploiting the victim's authenticated session.

## Requirements

1. Attacker-controlled web server supporting PHP
2. Modern browser environment for Resource Timing API
3. Victim logged into HackerOne

## Defense

Defensive measures and detection strategies:

- Enforce strict CORS policies on API endpoints
- Rate-limit cross-origin requests
- Educate users on phishing risks for malicious pages

## Objectives

1. Enable cross-origin resource loads from victim browser
2. Capture precise timing data for baseline and target queries
3. Avoid detection by mimicking benign image loads

## Instructions

### Step 1: Create HTML with JS Function

**Context**: Embed the timing calculation function in the page head.

**Command** ([[commands/calculate-load-times-js]]):
```javascript
function calculate_load_times() { if (performance === undefined) { console.log('= Calculate Load Times: performance NOT supported'); return; } var resources = performance.getEntriesByType('resource'); if (resources === undefined || resources.length <= 0) { console.log('= Calculate Load Times: there are NO `resource` performance records'); return; } console.log('= Calculate Load Times'); for (var i=0; i < resources.length; i++) { t = resources[i].responseEnd - resources[i].responseStart; console.log(t); } }
```

> Add to `<head>`; call after page load to log deltas in ms.

### Step 2: Generate Dynamic Img Tags

**Context**: Use PHP to create multiple tags for parallel loading.

**Command** (PHP Embed):
Include PHP loops in body for `<img>` src to endpoints.

> Outputs HTML triggering requests; random params prevent caching.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/calculate-load-times-js]]

## Tools Used

- [[tools/Resource-Timing-API]]
- [[tools/PHP]]

## Tags

- [[drive-by-compromise]]
- [[timing-leak]]
