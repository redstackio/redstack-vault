---
id: proc-api-key-extract
tags:
  - credential-access
  - api-testing
  - unauthorized-access
type: procedure
tools:
  - '[[tools/Wayback-Machine]]'
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-api-key-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:39.328Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
---
# Extract-and-Validate-Exposed-API-Keys

## Summary

This procedure focuses on identifying API keys from archived web content and testing their validity against live endpoints to confirm unauthorized access capabilities, as seen in the Planet Labs exposure.

## Description

Once historical snapshots are accessed, attackers manually or semi-automatically extract strings resembling API keys (e.g., 32-character hex strings in URLs). Validation involves sending requests to the API with the key; successful responses indicate active credentials, allowing access to resources like satellite mosaics. This low-privilege technique can lead to data exfiltration without further exploits.

## Requirements

1. Extracted potential API keys from snapshots
2. curl or similar HTTP client installed
3. Knowledge of target API endpoints (e.g., /basemaps/v1/mosaics)

## Defense

Defensive measures and detection strategies:

- Enforce short-lived API keys with scoping to limit damage
- Use API gateways to log and rate-limit requests, alerting on key usage from unusual IPs
- Audit public web presence and remove sensitive embeds via robots.txt or archive requests

## Objectives

1. Confirm key validity for resource access
2. Access sensitive data like basemaps and satellite imagery
3. Demonstrate potential for broader exploitation

## Instructions

### Step 1: Identify Keys in Snapshot Content

**Context**: Scan archived pages for API keys embedded in URLs or JavaScript.

**Command** (Manual inspection):

No command; view page source.

> Look for patterns like ?api_key= followed by alphanumeric strings in URLs such as https://api.planet.com/basemaps/v1/mosaics?api_key=afdb1e8a9c8142739553e3942283d6c8.

### Step 2: Test Key Validity with API Request

**Context**: Use curl to query the API and check for successful authentication.

**Command** ([[commands/curl-api-key-test]]):

```bash
curl "https://api.planet.com/basemaps/v1/mosaics?api_key=afdb1e8a9c8142739553e3942283d6c8&_page_size=1000"
```

> A successful response returns JSON with mosaic data; failures yield error codes like 401 Unauthorized.

### Step 3: Test Alternative Endpoints

**Context**: Validate on other resources like WMTS for broader access.

**Command** ([[commands/curl-api-key-test]]):

```bash
curl "https://api.planet.com/basemaps/v1/mosaics/wmts?service=wmts&request=GetCapabilities&format=text%2Fxml&api_key=8fe044edc78c46ba904bb62e550493a3"
```

> Expect XML capabilities document if valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

### Techniques

- [[Unsecured Credentials]] Unprotected Credentials
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-api-key-test]]

## Tools Used

- [[tools/Wayback-Machine]]

## Tags

- [[credential-access]]
- [[api-testing]]
