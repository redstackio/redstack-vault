---
tags:
  - http-smuggling
  - request-crafting
  - bypass
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-smuggling-request]]'
platforms:
  - Cloud
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0df84c65-c373-41eb-a2a8-937b554cfcba
created_at: '2025-12-13T09:01:26.054Z'
updated_at: '2025-12-13T09:01:26.054Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform HTTP Request Smuggling with Crafted POST Request

## Summary

This procedure involves sending a specially crafted POST request to exploit the injected headers from Cloudflare Transform Rules, smuggling a secondary GET request to access internal servers and bypass Cloudflare Access.

## Description

After setting up the header injection, a POST request with a chunked body is sent, ending with a zero chunk followed by a smuggled GET request. This leverages TE.CL smuggling to reach internal origin servers. The target must have the vulnerable rule active.

## Requirements

1. Vulnerable Cloudflare Transform Rule active on the target domain
2. Tool like curl to send HTTP requests
3. Knowledge of internal hostnames (e.g., internal.example.com)

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous chunked requests and smuggling patterns in logs
- Patch Cloudflare rules to sanitize hex escapes and validate headers

## Objectives

1. Smuggle secondary request through the proxy
2. Access restricted internal content
3. Demonstrate bypass of security controls

## Instructions

### Step 1: Craft the POST Body

**Context**: Prepare the smuggling payload in the POST body.

Construct the body as "0\r\n\r\nGET / HTTP/1.1\r\nHost: internal.example.com\r\n\r\n" to end the chunk and append the GET request.

> This creates the smuggling effect when combined with chunked encoding.

### Step 2: Send the Request

**Context**: Transmit the request to the target endpoint.

Execute [[commands/curl-http-smuggling-request]]:

```bash
curl -X POST https://target.example.com/ -H "Content-Type: text/plain" --data "0\r\n\r\nGET / HTTP/1.1\r\nHost: internal.example.com\r\n\r\n"
```

> This sends the crafted request, triggering the smuggling.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-http-smuggling-request]]

## Tools Used

- [[tools/curl]]

## Tags

- [[http-smuggling]]
- [[bypass]]
