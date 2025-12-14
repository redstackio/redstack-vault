---
tags:
  - dos
  - impact
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Network Denial of Service]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 4b53b8f8-00b3-491e-8b4e-3219f13ff7dd
created_at: '2025-12-14T17:26:55.905Z'
updated_at: '2025-12-14T17:26:55.905Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Observe-Denial-of-Service-Impact

## Summary

This procedure demonstrates the real-world impact of cache poisoning, where tainted cache entries cause resources to reference invalid ports, leading to failed loads and degraded site functionality for users.

## Description

With the cache poisoned, visiting https://themes.shopify.com/ results in canonical links and resources (e.g., images, CSS) pointing to :1337, a non-existent port. This breaks page rendering without server errors, affecting all unauthenticated users until cache expires. Observation can be done via browser or additional curl requests.

## Requirements

1. Successful prior poisoning and verification
2. Browser or curl for impact testing
3. Public access to the site

## Defense

Defensive measures and detection strategies:

- Monitor user error rates for resource 404s or connection failures
- Deploy cache poisoning detection via header anomaly scanning
- Use fallback mechanisms for resource loading

## Objectives

1. Validate DoS through broken resources
2. Assess integrity impact on site usability
3. Highlight risks to unauthenticated traffic

## Instructions

### Step 1: Access Poisoned Page

**Context**: Load the homepage in a browser or via curl to observe failures.

**Command** (Use curl for inspection):
```bash
curl -ik "https://themes.shopify.com/"
```

> Inspect the response for :1337 in URLs. In a browser, attempt to load; images/CSS will fail to load from port 1337, causing visual breakage.

### Step 2: Confirm Resource Failures

**Context**: Check specific resources or use dev tools to verify DoS.

**Command** (No specific; manual inspection):
```bash
# Example: curl a poisoned resource URL
curl -ik "https://themes.shopify.com:1337/some-image.jpg"
```

> Expected: Connection refused or timeout, confirming DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[dos]]
- [[Impact]]
