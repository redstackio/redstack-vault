---
tags:
  - traffic-interception
  - jwt
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Credentials In Files]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 7000e234-e7d0-489b-ad11-ccb4c2278599
created_at: '2025-12-13T09:01:26.696Z'
updated_at: '2025-12-13T09:01:26.696Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Intercept Traffic to Capture JWT

## Summary

This procedure captures the JWT token by intercepting network traffic during the SSO flow to Zendesk.

## Description

Using browser tools or a proxy, the attacker intercepts the HTTP request containing the JWT. This reveals the token used for authentication, which can then be analyzed. The scenario targets web applications with client-side auth, expecting to capture a valid JWT for further tampering.

## Requirements

1. Browser with network inspection capabilities (e.g., Chrome DevTools)
2. Active SSO flow from previous step
3. No proxy detection on target site

## Defense

Defensive measures and detection strategies:

- Use HTTPS and certificate pinning to prevent interception
- Log and alert on suspicious traffic patterns to auth endpoints

## Objectives

1. Obtain the raw JWT token
2. Enable decoding and analysis
3. Identify token structure for exploitation

## Instructions

### Step 1: Monitor Network Traffic

**Context**: Capture the specific JWT request.

Open developer tools, navigate to the network tab, and capture the request to https://trintsupport.zendesk.com/access/jwt?jwt=[JWT_TOKEN].

> Copy the JWT token from the request parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[traffic-interception]]
- [[jwt]]
