---
tags:
  - misconfiguration
  - initial-access
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.367Z'
sub_techniques: []
id: 54424c7c-2e63-4ecc-bbcc-68f6d4c13110
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Cortex-Home-Endpoint

## Summary

This procedure accesses the home endpoint of an exposed Cortex metrics server to confirm unauthorized access without authentication, serving as the initial entry point for further reconnaissance.

## Description

In scenarios where a Cortex instance is misconfigured and publicly exposed, navigating to the root URL reveals the server interface, including API details and status, without any login requirements. This is common in cloud environments like Shopify where internal tools are accidentally left open, enabling attackers to map the attack surface and proceed to sensitive endpoints.

## Requirements

1. Public network access to the target URL (e.g., https://cortex-ingest.shopifycloud.com/)
2. HTTP client like curl or a web browser
3. No credentials due to lack of authentication

## Defense

Defensive measures and detection strategies:

- Implement authentication (e.g., API keys or OAuth) on all public-facing endpoints
- Use web application firewalls (WAF) to block unauthorized access to admin/debug paths
- Monitor access logs for anomalous requests to root or config endpoints

## Objectives

1. Verify exposure of the Cortex interface
2. Confirm no authentication barriers
3. Identify available sub-endpoints for escalation

## Instructions

### Step 1: Request Home Endpoint

**Context**: Send an HTTP GET to the root URL to retrieve the server interface.

**Command** ([[commands/curl-access-url]]):
```bash
curl -i https://cortex-ingest.shopifycloud.com/
```

> This command fetches the response headers and body, expecting a 200 OK with Cortex UI elements. Success indicates full exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used

- [[tools/curl]]

## Tags

- [[misconfiguration]]
- [[initial-access]]
