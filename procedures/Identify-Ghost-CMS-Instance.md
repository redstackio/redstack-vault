---
id: proc-uuid-2
tags:
  - reconnaissance
  - ghost-cms
  - fingerprinting
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-ghost-detection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.460Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Ghost CMS Instance

## Summary

This procedure fingerprints a target website to confirm it runs Ghost CMS, focusing on oEmbed endpoints and headers to identify potential SSRF vulnerabilities.

## Description

Ghost CMS instances can be detected via unique API paths, headers, or oEmbed responses. This reconnaissance step is essential before attempting SSRF exploitation, ensuring the target uses the vulnerable oEmbed functionality in a Node.js web environment.

## Requirements

1. Public access to the target website
2. Basic HTTP client (e.g., curl)
3. Knowledge of common Ghost CMS paths (e.g., /ghost/api/)

## Defense

Defensive measures and detection strategies:

- Remove or obscure server headers indicating Ghost CMS
- Implement WAF rules to block probing requests to admin paths
- Use content security policies to limit endpoint exposure

## Objectives

1. Confirm Ghost CMS deployment
2. Identify oEmbed endpoint availability
3. Gather version info for vulnerability assessment

## Instructions

### Step 1: Probe for Ghost Headers

**Context**: Send a HEAD request to check for Ghost-specific headers.

**Command** ([[commands/curl-ghost-detection]]):
```bash
curl -I https://target.com/ | grep -i ghost
```

> Expected output: Headers like 'X-Powered-By: Ghost' or similar.

### Step 2: Test oEmbed Endpoint

**Context**: Verify oEmbed processing with a safe external URL.

**Command** ([[commands/curl-ghost-detection]]):
```bash
curl -s "https://target.com/ghost/api/oembed/?url=https://example.com"
```

> Expected output: JSON oEmbed structure if vulnerable endpoint is present.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ghost-detection]]

## Tools Used


## Tags

- reconnaissance
- ghost-cms
- fingerprinting
