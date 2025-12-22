---
tags:
  - cdn
  - verification
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-url]]'
platforms:
  - Web
techniques:
  - '[[Scanning IP Blocks]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 48248745-b2a7-417a-b94f-c50b6048a229
created_at: '2025-12-14T04:38:39.955Z'
updated_at: '2025-12-14T04:38:39.955Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Scanning IP Blocks]]'
---
# Verify-Fastly-Unregistered-Status

## Summary

This procedure verifies if a subdomain pointing to Fastly is unregistered by attempting access, resulting in an error that confirms vulnerability to takeover.

## Description

After discovering a CNAME to Fastly, access the subdomain via HTTP to trigger Fastly's error handling. An 'unknown domain' response indicates the domain is not configured in any Fastly account, allowing the attacker to claim it. This applies to web-based CDN misconfigurations and precedes actual takeover.

## Requirements

1. HTTP client like curl
2. Target subdomain URL
3. Basic networking knowledge

## Defense

Defensive measures and detection strategies:

- Claim all subdomains in CDN providers promptly
- Set up monitoring for access errors on subdomains
- Use automated scanners for dangling DNS records

## Objectives

1. Confirm unclaimed status
2. Validate error response
3. Prepare for registration

## Instructions

### Step 1: Access Subdomain

**Context**: Send a HEAD request to check server response without downloading content.

**Command** ([[commands/curl-access-url]]):
```bash
curl -I http://addons-preview-cdn.mozilla.net
```

> Expect a 404 or custom Fastly error page indicating 'unknown domain'. This confirms the subdomain is available for takeover.

### Step 2: Inspect Response

**Context**: Analyze headers for Fastly signatures.

**Command** (Manual):
No command; review curl output for error details.

> Look for Fastly-specific error messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Scanning IP Blocks]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[cdn]]
- [[verification]]
- [[subdomain-takeover]]
