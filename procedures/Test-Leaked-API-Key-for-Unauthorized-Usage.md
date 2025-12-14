---
id: proc-002-test-api-key
tags:
  - api-abuse
  - dos
  - google-api
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-test-google-geocode]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:48.553Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Cloud Instance Metadata API]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Network Denial of Service]]'
---
# Test-Leaked-API-Key-for-Unauthorized-Usage

## Summary

This procedure tests a leaked API key by sending requests to the associated service (e.g., Google Geocode API) to confirm its validity and unrestricted nature, demonstrating potential for unauthorized queries that could incur costs ($5 per 1000 requests) or enable DoS through flooding.

## Description

Once an API key is obtained from exposed endpoints, attackers validate it by crafting requests to the target API, such as Google's Geocoding service. In the FetLife case, a simple latlng query reveals if the key works without referrer checks. Successful tests confirm the key's power for abuse, like geolocating arbitrary coordinates or overwhelming the quota. This targets web-based APIs; outcomes include proof-of-concept responses and risk assessment for billing/DoS.

## Requirements

1. Extracted API key
2. curl or similar HTTP client
3. Knowledge of the API endpoint (e.g., Geocode API)

## Defense

Defensive measures and detection strategies:

- Enable API key restrictions (e.g., HTTP referrers, API scopes) in provider console
- Set up billing alerts and quotas to detect spikes
- Log and monitor for high-volume requests from unexpected IPs

## Objectives

1. Verify key functionality with a test request
2. Demonstrate unauthorized access potential
3. Highlight abuse vectors like cost escalation or DoS

## Instructions

### Step 1: Construct Test Request

**Context**: Build a basic API call using the leaked key to check for valid responses.

Use the Geocode endpoint with sample coordinates.

**Command** ([[commands/curl-test-google-geocode]]):
```bash
curl "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=AIza████████DM"
```

> This sends a GET request; expected output is JSON with 'status': 'OK' and location details, confirming the key works.

### Step 2: Simulate Abuse

**Context**: Repeat requests to test rate limits and potential DoS.

Loop the command multiple times.

**Command** ([[curl-loop-abuse]]):
```bash
for i in {1..100}; do curl "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=AIza████████DM"; done
```

> This floods the API; monitor for quota errors or continued success, indicating vulnerability to excessive usage.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- [[Cloud Instance Metadata API]] Unsecured Stored Credentials

## Commands Used

- [[commands/curl-test-google-geocode]]

## Tools Used


## Tags

- [[api-abuse]]
- [[dos]]
