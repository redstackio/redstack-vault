---
id: proc-paypal-dos-induce
tags:
  - dos
  - web-cache-poisoning
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-simulate-user]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:27:02.990Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Induce-Denial-of-Service-via-Poisoned-Cache

## Summary

This procedure demonstrates the impact of cache poisoning by simulating user access to the affected site, confirming that poisoned JS files cause functional breakdowns leading to denial of service.

## Description

After poisoning, regular user requests hit the cache and receive 501 errors for JS files, breaking interactive elements on paypal.com. This DoS affects all cached clients until the cache is purged. The scenario targets high-traffic sites; outcomes include widespread usability issues without direct server overload.

## Requirements

1. Successful cache poisoning from previous steps
2. Ability to simulate or observe user traffic
3. Browser or tool to inspect network failures

## Defense

Defensive measures and detection strategies:

- Implement cache TTL limits and proactive purging for errors
- Monitor client-side errors (e.g., JS load failures) via analytics
- Use content security policies to mitigate broken script impacts

## Objectives

1. Confirm DoS through failed resource loads
2. Demonstrate core functionality disruption
3. Validate attack persistence

## Instructions

### Step 1: Simulate User Access

**Context**: Request the main site to trigger cache hits on poisoned JS.

**Command** ([[commands/curl-simulate-user]]):
```bash
curl https://www.paypal.com/ -v
```

> This mimics a user visit. Check verbose output for references to JS files; in a browser, inspect for 501 fetches.

### Step 2: Validate Impact

**Context**: Test specific features reliant on JS, like login, to observe breakage.

**Command** ([[commands/curl-simulate-user]]):
```bash
curl https://www.paypal.com/signin -v
```

> Expected: Page loads but JS-dependent actions fail. Success if errors correlate to poisoned resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-simulate-user]]

## Tools Used

- [[tools/curl]]

## Tags

- dos
- web-cache-poisoning
