---
id: proc-002
tags:
  - waf-bypass
  - cloudflare
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:31.333Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Cloudflare-WAF-with-Staging-Domain

## Summary

This procedure bypasses CloudFlare WAF blocking of suspicious search queries by targeting the staging domain secnews.wpengine.com instead of the production www.secnews.gr.

## Description

CloudFlare WAF on the production site blocks payloads with encoded quotes and tags, but the staging domain lacks this protection. Switch endpoints for testing and exploitation. Requires knowledge of hosting provider (wpengine.com) to identify staging URLs.

## Requirements

1. Knowledge of target's hosting provider
2. Access to staging domain (publicly accessible)
3. No special tools needed

## Defense

Defensive measures and detection strategies:

- Secure staging environments with equivalent WAF rules
- Monitor traffic to staging domains
- Use internal-only staging if possible

## Objectives

1. Avoid WAF blocks on payloads
2. Enable vulnerability testing
3. Proceed to exploitation

## Instructions

### Step 1: Identify and Use Staging Domain

**Context**: Replace the production URL with the staging one for all subsequent requests to evade WAF.

**Command**:
```bash
# Example: Use staging in curl tests
curl -s 'https://secnews.wpengine.com?s=%27%3E%3Ctest%3E%3C' | egrep -o ".{47}?<test>.*?>"
```

> Adapt previous commands by changing the host to secnews.wpengine.com. Expected output is the same injection confirmation without blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[waf-bypass]]
- [[cloudflare]]
