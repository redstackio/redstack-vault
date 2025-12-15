---
id: uuid-verify-unauth-1
tags:
  - recon
  - unauth-access
type: procedure
tools:
  - '[[tools/curl]]'
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
updated_at: '2025-12-14T17:29:19.876Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Unauthenticated Access to Target Site

## Summary

This procedure confirms that the target web application allows anonymous browsing without enforcing authentication, setting the stage for exploiting public API endpoints.

## Description

In the context of tmss.gsa.gov, this involves navigating to the main site and verifying no login is required, which exposes the improper authorization in API paths. The target environment is a public-facing web app on HTTPS, with no prerequisites beyond internet access. Expected outcome is confirmation of open access, enabling further enumeration without credentials.

## Requirements

1. Web browser or HTTP client like curl
2. Direct internet access to https://tmss.gsa.gov
3. No authentication artifacts (cookies, tokens)

## Defense

Defensive measures and detection strategies:

- Implement authentication middleware for all endpoints
- Monitor for anomalous unauthenticated API calls via WAF logs
- Use rate limiting on public endpoints

## Objectives

1. Establish baseline unauthenticated access
2. Verify no redirects to login pages
3. Identify exposed public paths

## Instructions

### Step 1: Navigate to Main Site

**Context**: Load the primary domain to check for authentication enforcement.

No specific command; use browser to visit https://tmss.gsa.gov/ or curl HEAD request:

```bash
curl -I https://tmss.gsa.gov/
```

> Returns HTTP 200 without auth challenges; inspect headers for no Set-Cookie requiring login.

### Step 2: Inspect Request Headers

**Context**: Ensure requests are sent without auth tokens.

Use browser dev tools or curl verbose:

```bash
curl -v https://tmss.gsa.gov/
```

> Confirms no Authorization header needed; successful if page loads fully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[recon]]
- [[unauth-access]]
