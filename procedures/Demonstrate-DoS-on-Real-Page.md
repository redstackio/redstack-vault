---
tags:
  - web-cache-poisoning
  - http
  - dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7ca45a78-b373-4783-9730-06400958d3ae
created_at: '2025-12-13T09:00:34.360Z'
updated_at: '2025-12-13T09:00:34.360Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Demonstrate DoS on Real Page

## Summary

This procedure extends cache poisoning to a legitimate page by sending a malformed request with a large header, caching a 400 error and making the page unavailable.

## Description

Targeting a real page like https://www.████████/████████.htm, the attack poisons the cache, causing subsequent accesses to return errors, effectively denying service. This was shown to disrupt user access on the target site.

## Requirements

1. Identified cacheable real page on target
2. Ability to send requests with large headers
3. Verified poisoning on test paths

## Defense

Defensive measures and detection strategies:

- Limit header sizes in server configuration
- Exclude caching for pages with dynamic content
- Monitor for large or malformed requests

## Objectives

1. Achieve DoS on production pages
2. Demonstrate real-world impact
3. Test cache duration (up to 24 hours)

## Instructions

### Step 1: Target Real Page with Malformed Request

**Context**: Send request with large header to trigger 400 and poison cache.

> Use a tool like curl to send a GET request with oversized headers to the target URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[web-cache-poisoning]]
- [[dos]]
