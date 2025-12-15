---
tags:
  - api-access
  - unauthenticated
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3c09347e-3b9b-4394-91f7-7214a37ec8d7
created_at: '2025-12-14T17:32:01.672Z'
updated_at: '2025-12-14T17:32:01.672Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Semrush-API-Endpoints

## Summary

This procedure involves directly accessing discovered Semrush API endpoints in a browser to confirm unauthenticated retrieval of domain rank data.

## Description

Targeting Semrush's regional API subdomains, this step loads the endpoints identified via dorking to inspect responses. The web platform allows straightforward HTTP requests, with no authentication required on subdomains. Prerequisites: Valid endpoint URLs from reconnaissance. Outcomes include viewing paid analytics data, highlighting the authentication gap.

## Requirements

1. Discovered API URLs from prior dorking
2. Web browser like Firefox
3. Basic URL navigation skills

## Defense

Defensive measures and detection strategies:

- Enforce API key checks on all endpoints, including subdomains
- Redirect or block direct browser access to APIs with 403 errors
- Log and alert on anomalous direct accesses without keys

## Objectives

1. Load API responses without authentication
2. Verify data exposure for default domains
3. Confirm endpoint functionality and structure

## Instructions

### Step 1: Navigate to Endpoint

**Context**: Use the browser to fetch the API response directly from the search result link.

No specific command; in Firefox, click the Google result URL.

> This sends a GET request to the endpoint. Expected output: A page or raw response showing domain rank data, e.g., JSON with fields like rank, organic traffic.

### Step 2: Inspect Response Data

**Context**: Examine the loaded content to understand the data format and available metrics.

No specific command; view source or use browser dev tools (F12) to parse the response.

> Look for unencrypted data exposure. Expected output: Detailed analytics for the queried domain, confirming no key prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[unauthenticated-access]]
- [[api-exploit]]
