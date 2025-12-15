---
id: proc-test-browser-crash-001
tags:
  - browser-dos
  - png
  - end-user-impact
type: procedure
tools:
  - '[[tools/Browser-Chrome]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.932Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Test-Browser-Crash-with-Large-Image

## Summary

This procedure loads the White Label page in a browser to trigger proxy fetch of the large valid PNG (big_valid.php), observing browser instability or crash due to memory overload.

## Description

When the page loads, the proxy fetches the 457MB PNG, which browsers like Chrome attempt to render, leading to crashes. The CDN caches it, reducing repeat attacker load but amplifying distribution.

## Requirements

1. Embedded big_valid.php ([[procedures/Embed-Malicious-Images-in-Chaturbate-White-Label]])
2. Modern browser like Chrome

## Defense

Defensive measures and detection strategies:

- Browser extensions for image size limits
- Proxy pre-caching and size checks
- User education on suspicious pages

## Objectives

1. Demonstrate end-user impact beyond server DoS
2. Validate valid content evasion
3. Test caching behavior

## Instructions

### Step 1: Load White Label Page

**Context**: Visit the page with embedded img.

Open https://white-label.chaturbate.com in [[tools/Browser-Chrome]].

> Expected output: Page loads, but image fetch causes high memory use; Chrome may crash or tab freeze.

### Step 2: Monitor Network and Memory

**Context**: Use dev tools to observe.

F12 > Network tab; watch for proxy PNG request.

> Expected output: 457MB download; memory spikes to GBs, potential crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Chrome]]

## Tags

- browser-crash
- end-user
