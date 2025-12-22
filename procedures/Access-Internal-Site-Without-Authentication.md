---
tags:
  - auth-bypass
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:21.947Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 90872ef2-0412-431d-9ebe-d20f7c84c85b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Internal-Site-Without-Authentication

## Summary

This procedure exploits missing authentication enforcement on internal web pages of a target site, allowing unauthenticated users to access content intended only for logged-in personnel. In the Uber lab.usuppliers.uber.com scenario, this enables direct navigation to sensitive areas without credentials.

## Description

The target site, such as lab.usuppliers.uber.com, is designed for authenticated internal users but fails to enforce login requirements on certain pages. An attacker can simply visit the URL in a browser or via HTTP request, gaining immediate access to internal interfaces. This broken access control leads to potential further exploitation, such as file access, and exposes the organization's internal structure. Prerequisites include public resolvability of the domain; no special tools or privileges are needed.

## Requirements

1. Internet access to resolve and reach the target domain (e.g., lab.usuppliers.uber.com)
2. A web browser or HTTP client like curl
3. No authentication credentials

## Defense

Defensive measures and detection strategies:

- Implement strict authentication checks on all internal endpoints using frameworks like OAuth or session-based auth
- Use web application firewalls (WAF) to block unauthenticated requests to sensitive paths
- Monitor access logs for anomalous unauthenticated traffic from external IPs
- Conduct regular access control audits with tools like OWASP ZAP

## Objectives

1. Bypass authentication to enter the internal site
2. Confirm access to restricted pages
3. Set stage for deeper information gathering

## Instructions

### Step 1: Resolve and Access the Target Site

**Context**: Verify the site's availability and attempt direct access without login.

Navigate to https://lab.usuppliers.uber.com in a web browser. If using curl for scripting:

```bash
curl -i https://lab.usuppliers.uber.com
```

> This command sends a GET request and displays headers. Expect a 200 OK status and HTML content indicating internal pages, without any redirect to a login form.

### Step 2: Verify Internal Content

**Context**: Confirm that sensitive or internal elements are visible, indicating successful bypass.

Inspect the loaded page for Uber-specific internal links or data. Look for elements like dashboard interfaces or file directories that should require auth.

**Expected Output**: Page loads with internal navigation options, no auth prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- web
