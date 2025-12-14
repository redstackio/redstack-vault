---
tags:
  - coldfusion
  - endpoint-recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-endpoint]]'
verified: false
platforms:
  - Web
  - Adobe ColdFusion
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.678Z'
sub_techniques: []
id: d3dba24e-20d0-4fb7-9d50-66749626d4b7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-ColdFusion-Admin-Login-Endpoint

## Summary

This procedure involves navigating to the login page of an Adobe ColdFusion administrator interface to identify the authentication endpoint, setting the stage for exploiting unprotected methods.

## Description

In Adobe ColdFusion applications, the administrator API is often exposed via CFC components. This procedure targets the login endpoint at /adminapi/administrator.cfc on a DoD domain, allowing reconnaissance of the auth structure without credentials. Successful execution reveals the endpoint for further exploitation, such as salt leakage, leading to potential authentication bypass.

## Requirements

1. Public internet access to the target URL
2. Web browser or curl tool
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement authentication on all admin endpoints
- Use web application firewalls (WAF) to block direct CFC method access
- Monitor access logs for unauthorized endpoint hits

## Objectives

1. Confirm existence of admin login endpoint
2. Gather details on authentication mechanism
3. Prepare for salt retrieval

## Instructions

### Step 1: Navigate to Login Endpoint

**Context**: Access the CFC file to inspect the login interface and confirm it's a ColdFusion admin component.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl -i https://█████████/████████/adminapi/administrator.cfc
```

> This command sends a GET request and returns headers and body, showing the login form or CFC details. Expect a 200 OK with HTML content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-endpoint]]

## Tools Used


## Tags

- [[coldfusion]]
- [[endpoint-recon]]
