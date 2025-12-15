---
id: proc-test-double-slash-uber
tags:
  - open-redirect
  - url-testing
  - uber
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-domain-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.924Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Double-Slash-Redirection

## Summary

This procedure tests URL path handling on Uber.com using double slashes followed by an external domain to identify potential open redirection flaws, resulting in a 404 error that hints at improper validation.

## Description

In the context of web vulnerability assessment, this step involves crafting malformed URLs like https://www.uber.com//google.com/cities to probe how the server parses paths with double slashes. The target environment is Uber's public-facing website, expecting a 404 response due to unrecognized paths, but revealing mishandling that can be exploited further. Prerequisites include browser access or curl for HTTP requests; no authentication is needed.

## Requirements

1. Internet access to uber.com
2. Browser or curl tool for URL testing
3. Basic understanding of HTTP redirects and status codes

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to canonicalize paths and block double slashes
- Use web application firewalls (WAF) to detect and log anomalous URL patterns like //external-domain
- Monitor access logs for 404s on malformed paths followed by successful redirects

## Objectives

1. Confirm improper URL path parsing leading to potential redirection
2. Identify baseline error responses for further exploitation
3. Gather evidence of vulnerability for reporting

## Instructions

### Step 1: Craft and Access Malformed URL

**Context**: Construct a URL with double slashes after the domain to test path resolution.

**Command** ([[commands/curl-test-domain-redirect]]):
```bash
curl -L -I "https://www.uber.com//google.com/cities"
```

> This command follows redirects (-L) and shows headers (-I), expecting a 404 status from Uber, indicating the path is not properly sanitized but doesn't redirect yet.

### Step 2: Verify Response in Browser

**Context**: Manually access the URL to observe the 404 page and confirm no unintended redirect.

No command needed; paste https://www.uber.com//google.com/cities into a browser and check for Uber's error page.

> Expected: Page Not Found on Uber website, no navigation to google.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-test-domain-redirect]]

## Tools Used


## Tags

- open-redirect
- url-testing
