---
tags:
  - ssrf
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-identify-ssrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.467Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fce49cd5-9e16-4d91-8ba5-8e8e4712f9ce
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-SSRF-Vulnerable-Endpoint

## Summary

This procedure identifies a Server-Side Request Forgery (SSRF) vulnerability in a web form's URL parameter by submitting arbitrary external URLs and observing if the server fetches them without validation, setting the stage for internal resource access.

## Description

In the context of the APITest.IO application, the form at https://www.apitest.io/request processes the 'url' parameter without proper validation, allowing attackers to force the server to make requests to arbitrary destinations. This procedure tests basic functionality to confirm the vulnerability before escalating to internal targets. Expected outcomes include echoed or fetched content from the submitted URL, indicating SSRF potential.

## Requirements

1. Public access to the target endpoint (https://www.apitest.io/request)
2. Tool for HTTP POST requests (curl or browser)
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting or validation to restrict to external, trusted domains
- Monitor server logs for requests to internal IPs (127.0.0.1, 169.254.169.254)
- Use web application firewalls (WAF) to block suspicious URL patterns

## Objectives

1. Confirm arbitrary URL fetching capability
2. Establish baseline for SSRF exploitation
3. Identify lack of input sanitization

## Instructions

### Step 1: Submit Test URL

**Context**: Send a harmless external URL to verify the form fetches and returns content.

**Command** ([[commands/curl-identify-ssrf]]):
```bash
curl -X POST -d 'url=http://example.com' https://www.apitest.io/request
```

> This command posts to the form endpoint. Successful execution returns content from example.com, confirming the server acts as a proxy without restrictions.

### Step 2: Analyze Response

**Context**: Check the response for fetched content to validate SSRF.

No specific command; inspect output manually.

> Look for HTML or text from the target URL in the response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-identify-ssrf]]

## Tools Used


## Tags

- ssrf
- reconnaissance
