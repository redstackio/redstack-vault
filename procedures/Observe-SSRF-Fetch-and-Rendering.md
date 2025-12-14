---
id: proc-observe-ssrf
tags:
  - ssrf
  - observation
  - verification
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/netcat-listen-on-port]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T05:32:10.493Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Active Scanning]]'
---
# Observe-SSRF-Fetch-and-Rendering

## Summary

This procedure monitors and validates the SSRF exploitation by observing server fetches to public URLs (via rendering), private endpoints (via logs), or local files (via display).

## Description

Post-upload, Shopify's parser attempts to load the referenced resource, which can be verified through image rendering for public tests, netcat captures for private, or direct file content display for local. This confirms the vulnerability's impact, such as information disclosure. Requires setup from prior steps; outcomes provide proof of exploitation.

## Requirements

1. Uploaded SVG and active session
2. Netcat listener for private tests
3. Browser for rendering checks

## Defense

Defensive measures and detection strategies:

- Log all resource fetches during image processing
- Use content security policies to restrict rendering sources
- Scan for local file access attempts in server logs

## Objectives

1. Capture evidence of server-side requests
2. Verify resource loading success
3. Assess potential for further exploitation

## Instructions

### Step 1: Check Rendering

**Context**: For public URLs, view the product image.

Refresh the product page and inspect the uploaded image.

> Expected: Image renders with fetched content, e.g., Google logo.

### Step 2: Monitor Logs

**Context**: For private/local, review netcat or server output.

**Command** ([[commands/netcat-listen-on-port]]):
```bash
netcat -l -p 3001 -v
```

> Explanation: Logs show GET /?evil=var from Shopify IP. For local, image displays ubuntu_logo.png content.

### Step 3: Validate Impact

**Context**: Confirm SSRF by checking for internal access.

Compare logs against expected requests.

> Expected: Evidence of arbitrary fetch, e.g., internal file rendered.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[File and Directory Discovery]]
- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/netcat-listen-on-port]]

## Tools Used

- [[tools/netcat]]

## Tags

- ssrf
- verification
