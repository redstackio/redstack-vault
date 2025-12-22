---
tags:
  - ssrf
  - impact
  - localhost
type: procedure
tools:
  - '[[tools/cURL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fetch-internal-resource]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:53:38.243Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ff29f30a-7c8d-43b8-9396-751abb25a4c8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
---
# Verify-Impact-with-Localhost-Access

## Summary

This procedure confirms SSRF exploitation by accessing and retrieving content from localhost services.

## Description

Using a successful octal payload, execute cURL to a dummy localhost page (e.g., port 80), verifying information disclosure. Monitor separate terminal logs for server-side requests to internal IPs, demonstrating potential for exposing server internals or chaining to RCE via vulnerable services.

## Requirements

1. Localhost HTTP service (e.g., python -m http.server 8000)
2. Test script with cURL
3. Logging enabled on local server

## Defense

Defensive measures and detection strategies:

- Disable unnecessary localhost services
- Use network segmentation to isolate internal endpoints
- Monitor for unexpected internal traffic

## Objectives

1. Retrieve internal content via SSRF
2. Validate logs for request confirmation
3. Assess escalation potential

## Instructions

### Step 1: Set Up Localhost Target

**Context**: Create a simple endpoint for testing.

```bash
python -m http.server 8000
```

> Expected: Server listening on localhost:8000.

### Step 2: Execute SSRF Payload

**Context**: Use octal to fetch content.

Execute [[commands/curl-fetch-internal-resource]] with ?host=http://0177.0.0.1:8000/:

```bash
php test.php?host=http://0177.0.0.1:8000/
```

> Expected: HTML or page content echoed.

### Step 3: Check Logs

**Context**: Confirm server-side execution.

Monitor terminal running the local server.

> Expected: Log entry showing request from PHP script to internal IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-internal-resource]]

## Tools Used

- [[tools/cURL]]

## Tags

- ssrf
- impact
