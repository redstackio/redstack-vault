---
tags:
  - web-cache-poisoning
  - verification
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/grep]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-verify-poisoned-cache-loop]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4c6bb990-d7c8-4212-99c0-0e70b658ff8a
created_at: '2025-12-13T09:00:34.733Z'
updated_at: '2025-12-13T09:00:34.733Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Verify Cache Poisoning on Homepage

## Summary

This procedure verifies successful web cache poisoning by querying the homepage and checking if the response includes the injected invalid port, confirming that the cache is serving tainted content.

## Description

After attempting to poison the cache, this step uses repeated requests to the root URL to detect the presence of the poisoned Host in elements like canonical links. It's essential for confirming the exploit's effectiveness before observing broader impacts.

## Requirements

1. Prior cache poisoning attempt
2. Tools: curl and grep
3. Access to the target homepage

## Defense

Defensive measures and detection strategies:

- Regularly flush or monitor cache contents
- Detect repeated requests with grepping patterns in access logs

## Objectives

1. Confirm poisoned content in cache
2. Validate exploit success
3. Prepare for impact assessment

## Instructions

### Step 1: Query and Check Homepage

**Context**: Send repeated GET requests to the homepage and grep for the poisoned port to confirm caching of invalid data.

**Command** ([[commands/curl-verify-poisoned-cache-loop]]):
```bash
while true; do curl -ik "https://themes.shopify.com:443/"|grep ":1337"; done
```

> This loop fetches the homepage, ignores cert errors, and filters for :1337 to indicate poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/curl-verify-poisoned-cache-loop]]

## Tools Used

- [[tools/curl]]
- [[tools/grep]]

## Tags

- web-cache-poisoning
- verification
