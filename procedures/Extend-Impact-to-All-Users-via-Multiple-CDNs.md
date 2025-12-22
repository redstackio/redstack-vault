---
id: proc-uuid-006
tags:
  - cdn-poisoning
  - global-impact
  - dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:55.822Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Extend-Impact-to-All-Users-via-Multiple-CDNs

## Summary

This procedure scales the cache poisoning attack across multiple CDN nodes, ensuring persistent stored XSS and DoS by refreshing poisoned caches every 10 minutes to target all global users.

## Description

CDNs distribute content worldwide; by hitting various edge locations with poisoning requests and looping before TTL expiry, the attack ensures broad propagation, affecting all users accessing /Award/ or /List/ with XSS execution and potential service disruption.

## Requirements

1. Tools for geolocation spoofing or multi-IP requests
2. Automation script for periodic poisoning
3. Knowledge of CDN topology

## Defense

Defensive measures and detection strategies:

- Deploy cache invalidation on anomaly detection
- Use origin shielding to validate cache requests
- Monitor global cache hit rates for spikes in poisoned content

## Objectives

1. Poison caches across CDN edges
2. Maintain persistence via timed refreshes
3. Maximize user impact with DoS

## Instructions

### Step 1: Target Multiple CDNs

**Context**: Send poisoning requests from different locations.

Use VPNs or proxies to vary origin:

```bash
curl -v --proxy proxy-us "https://target.com/List/../Job/xss-payload"
curl -v --proxy proxy-eu "https://target.com/Award/../survey/xss-payload"
```

> Ensures edges in US/EU cache the payload.

### Step 2: Automate Refresh Loop

**Context**: Script to repeat every 10 minutes.

Use a simple loop (e.g., in bash or Python) to resend before expiry.

**Expected Output**: Continuous poisoned responses globally.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None specific

## Tags

- multi-cdn
- persistence
- global-dos
