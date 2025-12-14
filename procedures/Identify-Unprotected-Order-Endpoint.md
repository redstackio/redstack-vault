---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - reconnaissance
  - api-discovery
  - broken-access-control
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:17.901Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
---

# Identify-Unprotected-Order-Endpoint

## Summary

This reconnaissance procedure involves testing a web application to identify API endpoints lacking access controls, specifically those handling sensitive order data.

## Description

In vulnerable applications like Azbuka Vkusa, API endpoints for orders may be exposed without authentication. This procedure uses manual testing or proxy interception to probe for unprotected paths, confirming the vulnerability by observing successful responses to unauthenticated requests. It sets the stage for exploitation by mapping the attack surface.

## Requirements

1. Access to the web application via browser or proxy.
2. Basic knowledge of REST APIs.
3. Tools for inspecting network traffic (e.g., browser dev tools).

## Defense

Defensive measures and detection strategies:

- Document and secure all API endpoints with auth.
- Use API discovery tools to audit exposure.
- Log and monitor probe attempts on sensitive paths.

## Objectives

1. Locate vulnerable endpoints.
2. Confirm lack of access controls.
3. Prepare for deeper exploitation.

## Instructions

### Step 1: Inspect Application Traffic

**Context**: Navigate the app to trigger order-related requests and note endpoints.

**Instructions**: Use browser developer tools (Network tab) while viewing orders. Look for GET/POST to /api/orders or similar. Test by removing auth headers if present.

> Expected: Endpoint responds with data sans auth.

### Step 2: Manual Probing

**Context**: Directly test the suspected endpoint.

**Instructions**: Send a simple GET to the path without cookies or tokens.

> Success: 200 response with order schema.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[api-discovery]]

---
