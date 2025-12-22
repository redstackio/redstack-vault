---
id: proc-identify-turbonomic-endpoint
name: Identify Vulnerable Turbonomic Endpoint
tags:
  - ssrf
  - reconnaissance
  - web
  - cloud
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-basic-probe]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:09.581Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Turbonomic Endpoint

## Summary

This procedure involves reconnaissance to identify endpoints in IBM Turbonomic that are susceptible to Server-Side Request Forgery (SSRF) by testing for URL parameter handling without proper validation, setting the stage for internal resource access.

## Description

In the context of IBM Turbonomic, a cloud optimization platform, public-facing endpoints often process user-supplied URLs for integrations or webhooks. An SSRF vulnerability arises when these endpoints make server-side HTTP requests to the provided URLs without restricting internal or metadata services. This procedure uses basic HTTP probing to detect such endpoints, typically in unauthenticated scenarios, leading to potential secret disclosure in cloud environments like AWS or Azure.

## Requirements

1. Network access to the Turbonomic public URL (HTTPS on port 443)
2. curl or similar HTTP client installed
3. Optional: Web proxy (e.g., Burp Suite) for request inspection

## Defense

Defensive measures and detection strategies:

- Implement URL whitelisting to restrict requests to trusted domains
- Use network segmentation to isolate internal metadata endpoints
- Monitor application logs for anomalous internal requests (e.g., to 169.254.169.254)

## Objectives

1. Confirm endpoint accepts and processes user-controlled URLs
2. Identify lack of SSRF protections like IP blacklisting
3. Prepare for payload crafting in subsequent exploitation

## Instructions

### Step 1: Probe for URL-Processing Endpoints

**Context**: Enumerate and test Turbonomic API endpoints that handle URL inputs, such as integration setup APIs.

**Command** ([[commands/curl-basic-probe]]):
```bash
curl -X POST https://turbonomic.example.com/api/integrations -d 'url=http://example.com' -v
```

> This sends a test POST request with a benign external URL. Look for verbose output indicating the server fetched the URL (e.g., connection resets or content reflection). Success confirms potential SSRF.

### Step 2: Validate SSRF Susceptibility

**Context**: Escalate testing by attempting an internal URL to check for blind SSRF or response leakage.

**Command** ([[commands/curl-basic-probe]]):
```bash
curl -X POST https://turbonomic.example.com/api/integrations -d 'url=http://localhost/admin' -v
```

> Observe for delays, errors, or leaked internal data in the response, indicating the server made the request internally.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-basic-probe]]

## Tools Used


## Tags

- [[ssrf]]
- [[Reconnaissance]]
