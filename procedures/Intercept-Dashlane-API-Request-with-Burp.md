---
id: uuid-intercept-request
tags:
  - interception
  - proxy
  - api-discovery
  - burp
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
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:28:59.266Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Intercept-Dashlane-API-Request-with-Burp

## Summary

This procedure uses Burp Suite to intercept HTTP requests during user management actions in the Dashlane console, capturing legitimate API calls for later modification in IDOR exploitation.

## Description

By proxying traffic through Burp while interacting with the Manage Users feature, attackers can identify sensitive API endpoints like teamPlans/getTeamLastUpdateTs. This reveals authentication parameters and enables tampering. Applicable to any web app with unaudited API parameters.

## Requirements

1. Active Burp Suite proxy session
2. Authenticated Dashlane console access
3. Knowledge of target feature (Manage Users)

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to complicate interception
- Log and alert on proxied traffic signatures (e.g., Burp UA)
- Rate-limit API calls from suspicious clients

## Objectives

1. Capture baseline API request
2. Identify exploitable parameters
3. Enable request replay and modification

## Instructions

### Step 1: Navigate to Manage Users

**Context**: Trigger API calls by accessing the feature.

**Instructions**: In the console dashboard, click on 'Manage Users' while Burp is intercepting.

### Step 2: Capture Specific Request

**Context**: Filter for the team plans endpoint.

**Instructions**: In Burp Proxy > HTTP history, search for POST to https://ws1.dashlane.com/1/teamPlans/getTeamLastUpdateTs and intercept it.

> The request body will contain parameters like login and uki.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- interception
- api
