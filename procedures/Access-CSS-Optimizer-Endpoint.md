---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - ssrf
  - endpoint
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.595Z'
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
# Access-CSS-Optimizer-Endpoint

## Summary

This procedure accesses the unauthenticated test interface in the cerdic/csstidy module to confirm exposure of the SSRF vulnerability.

## Description

The css_optimiser.php file serves as a public demo for CSS tidying, allowing URL-based input without any authentication or validation. Accessing it directly reveals the form for 'CSS from URL', which can be manipulated for SSRF. This step validates the attack surface before triggering requests.

## Requirements

1. Publicly accessible Nextcloud instance
2. Mail extension enabled
3. HTTP client like curl or browser

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to /vendor/ paths via .htaccess or nginx rules
- Implement authentication on all app endpoints
- Log and alert on accesses to debug/test files

## Objectives

1. Confirm unauthenticated access
2. Inspect the interface for URL input
3. Prepare for parameter injection

## Instructions

### Step 1: Direct Access

**Context**: Hit the endpoint to load the interface.

**Command** ([[commands/curl-request]]):
```bash
curl http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php
```

> Displays HTML form with CSS input options. Success if no auth redirect.

### Step 2: Inspect Response

**Context**: Check for the URL parameter field.

**Command** ([[commands/curl-with-verbose]]):
```bash
curl -v http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php
```

> Verbose output shows headers; look for form action pointing to self.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-request]]
- [[commands/curl-with-verbose]]

## Tools Used


## Tags

- ssrf
- endpoint

