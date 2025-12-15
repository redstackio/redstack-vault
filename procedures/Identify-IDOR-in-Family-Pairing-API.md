---
id: 123e4567-e89b-12d3-a456-426614174001
name: Identify-IDOR-in-Family-Pairing-API
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.410Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - idor
  - api
  - recon
commands:
  - '[[commands/burp-intercept-request]]'
platforms:
  - Web
  - API
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Identify-IDOR-in-Family-Pairing-API

## Summary

This procedure involves intercepting and analyzing API traffic in the TikTok app to identify endpoints vulnerable to Insecure Direct Object Reference (IDOR), specifically those handling family pairing features where user objects are referenced directly without authorization checks.

## Description

In the context of TikTok's Family Pairing API, attackers with a valid account can inspect network traffic to find endpoints like `/v1/family/pair/{user_id}`. These endpoints use predictable identifiers (e.g., numeric user IDs) that can be manipulated. The procedure requires proxying app traffic and examining requests for direct references, enabling discovery of vulnerabilities that allow unauthorized access to other users' data. Expected outcomes include mapping API structure and pinpointing IDOR-prone parameters.

## Requirements

1. Valid TikTok account and authentication token.
2. Burp Suite or similar proxy tool installed and configured on the testing device.
3. Mobile device or browser with TikTok app/web access to family pairing settings.
4. Basic knowledge of HTTP requests and JSON payloads.

## Defense

Defensive measures and detection strategies:

- Implement proper server-side authorization checks for all object references.
- Use indirect references (e.g., UUIDs) instead of predictable IDs.
- Monitor API logs for anomalous parameter manipulations and rate-limit requests.

## Objectives

1. Discover API endpoints related to family pairing.
2. Identify parameters vulnerable to IDOR exploitation.
3. Validate lack of authorization on object access.

## Instructions

### Step 1: Configure Proxy and Intercept Traffic

**Context**: Set up Burp Suite to capture TikTok app requests during interaction with family pairing features.

**Command** ([[commands/burp-intercept-request]]):
```bash
# Configure device proxy to Burp (e.g., via burpsuite --listen 8080)
# No direct command; use Burp UI to intercept
```

> In Burp Suite, enable interception on the Proxy tab. Navigate to TikTok family pairing settings and perform actions like viewing or creating a pair. Inspect captured requests for endpoints containing user IDs.

### Step 2: Analyze Requests for Direct References

**Context**: Examine payloads to find IDOR indicators, such as path parameters like `{user_id}`.

**Command** ([[commands/burp-intercept-request]]):
```bash
# Use Burp Repeater to replay and inspect (manual UI action)
```

> Look for JSON bodies or headers with user-specific data. Note endpoints like POST /v1/family/pair/{id} where {id} is a direct user reference.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/burp-intercept-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[api]]
- [[recon]]
