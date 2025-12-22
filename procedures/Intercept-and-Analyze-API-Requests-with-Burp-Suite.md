---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - intercept
  - proxy
  - api-analysis
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:29:29.111Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept-and-Analyze-API-Requests-with-Burp-Suite

## Summary

This procedure uses Burp Suite to proxy and inspect HTTP traffic during listing creation, identifying the vulnerable /api/listings/{id}/product_bundle endpoint.

## Description

With the browser proxied through Burp Suite, the listing creation process is repeated to capture the exact API request. Analysis focuses on the GET request structure, parameters, and headers. In the Reverb.com sandbox, this reveals the lack of auth checks. Expected outcomes: Logged request with ID parameter, ready for modification.

## Requirements

1. Burp Suite installed and running
2. Browser proxy configured to 127.0.0.1:8080
3. Authenticated session active

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning to block proxy interception
- Monitor for proxy-like traffic patterns (e.g., via WAF)
- Encrypt API payloads end-to-end

## Objectives

1. Capture the legitimate API request
2. Analyze endpoint and parameters
3. Prepare for request modification

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept traffic.

Launch Burp Suite and configure browser proxy settings.

> No command; UI-based setup in Burp.

### Step 2: Trigger and Intercept

**Context**: Perform listing creation to capture the request.

Repeat listing creation while proxied.

In Burp Proxy tab:

- Filter to show Reverb.com traffic
- Intercept the /api/listings/{own_id}/product_bundle GET request

> Expected: Request details visible, including auth headers and ID.

### Step 3: Analyze Request

**Context**: Examine the captured request.

Review URL, method (GET), and body (empty).

> Note the {own_id} parameter for later replacement.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[api-analysis]]
- [[tools/Burp-Suite]]
