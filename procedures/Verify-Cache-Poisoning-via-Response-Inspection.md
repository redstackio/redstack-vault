---
tags:
  - web-cache-poisoning
  - verification
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/grep]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-verify-poisoned-cache]]'
platforms:
  - Web
techniques:
  - '[[Network Denial of Service]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 24201933-b6a4-4361-9665-73f1a4322edd
created_at: '2025-12-14T17:26:55.916Z'
updated_at: '2025-12-14T17:26:55.916Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Verify-Cache-Poisoning-via-Response-Inspection

## Summary

This procedure checks for successful cache poisoning by sending requests to the target homepage and inspecting responses for injected elements like invalid ports in canonical links.

## Description

After poisoning, the cache serves tainted content to new requests. This step uses grep to filter for the poison string (:1337) in responses from https://themes.shopify.com/, confirming that links and resources now reference the non-existent port. It relies on the prior poisoning step and default browser/curl headers that trigger cached responses.

## Requirements

1. Prior execution of cache poisoning
2. Access to the target homepage
3. curl and grep available

## Defense

Defensive measures and detection strategies:

- Log and alert on unexpected ports in generated URLs
- Implement cache invalidation on suspicious activity
- Use content security policies to block invalid resource loads

## Objectives

1. Confirm poison propagation to cache
2. Identify affected elements (e.g., links, resources)
3. Validate setup for DoS observation

## Instructions

### Step 1: Run Verification Loop

**Context**: Send repeated requests to the homepage and filter for poison indicators.

**Command** ([[commands/curl-verify-poisoned-cache]]):
```bash
while true; do curl -ik "https://themes.shopify.com/" | grep ":1337"; done
```

> This loops HTTPS requests to the root path, includes headers (-i) and insecure SSL (-k), and greps for ':1337'. Expected output: Matches like <link rel="canonical" href="https://themes.shopify.com:1337/">, indicating cache hit on poisoned entry.

### Step 2: Analyze Output

**Context**: Review grep results to ensure consistent poisoning.

**Command** (Use grep from Step 1):
```bash
grep ":1337"
```

> Successful if multiple iterations show the poison; failure if clean responses appear, suggesting cache miss or eviction.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-poisoned-cache]]

## Tools Used

- [[tools/curl]]
- [[tools/grep]]

## Tags

- [[web-cache-poisoning]]
- [[verification]]
