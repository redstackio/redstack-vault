---
tags:
  - sentry
  - endpoint-discovery
  - web
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:25:18.303Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: df86bc58-2d89-4e64-95b7-4938b0cd4c8f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Identify-and-Target-Sentry-Store-Endpoint

## Summary

This procedure involves monitoring intercepted traffic to detect Sentry error tracking usage and targeting the /api/20/store endpoint, which may be misconfigured for public access.

## Description

Sentry is commonly integrated into web applications for error logging, but misconfigurations can expose endpoints like /api/20/store. By inspecting requests in Burp Suite, attackers identify these integrations. This step assumes prior interception setup and focuses on reconnaissance of the error tracking surface. Outcomes include confirmation of endpoint exposure, setting up for exploitation.

## Requirements

1. Active Burp Suite interception from previous setup
2. Access to application traffic that may trigger errors
3. Knowledge of common Sentry paths (e.g., /api/20/store)

## Defense

Defensive measures and detection strategies:

- Restrict Sentry endpoints with authentication (e.g., API keys)
- Disable public error tracking in production
- Use WAF rules to block probes to internal paths like /api/

## Objectives

1. Detect Sentry integration via traffic analysis
2. Confirm accessibility of the store endpoint
3. Gather baseline response for modification

## Instructions

### Step 1: Monitor for Sentry References

**Context**: Review intercepted requests and responses for Sentry indicators.

In Burp Proxy > HTTP history, search for 'sentry' in responses or JS files. Look for error events or DSN (Data Source Name) references.

> Identification of Sentry usage confirms potential exposure.

### Step 2: Probe the Store Endpoint

**Context**: Send an initial GET request to test the endpoint.

In Burp Repeater, paste a request to https://target.com/api/20/store. Send as GET with default headers.

> Response may include metadata; no auth required indicates misconfig.

### Step 3: Document Endpoint Details

**Context**: Note the exact path and any parameters for next steps.

Capture screenshots or export the request. Verify it's the /api/20/store variant used for event storage.

> Endpoint details ready for modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[sentry]]
- [[Reconnaissance]]
- [[endpoint]]
