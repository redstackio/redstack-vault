---
tags:
  - http-smuggling
  - header-conflicts
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-conflicting-headers]]'
platforms:
  - Linux
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4d3dd608-e2d1-4641-9cf5-70044027474b
created_at: '2025-12-13T09:01:21.807Z'
updated_at: '2025-12-13T09:01:21.807Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Test Request with Conflicting Headers

## Summary

This procedure crafts an HTTP request using cURL with conflicting Transfer-Encoding and Content-Length headers to test for HTTP Request Smuggling vulnerability, allowing smuggling of malicious payloads.

## Description

The procedure involves sending a POST request via cURL that includes both chunked Transfer-Encoding and a fixed Content-Length, which can lead to inconsistent parsing by intermediaries like proxies. This is based on a manual code review of cURL's http_req_set_reader() function. The target environment includes proxies or load balancers that may interpret headers differently, potentially enabling authentication bypass or cache poisoning.

## Requirements

1. Installed cURL version 8.4.0 or affected
2. Access to a test HTTP server (e.g., example.com)
3. Network access for sending requests

## Defense

Defensive measures and detection strategies:

- Update cURL to a version that rejects conflicting headers
- Configure proxies to strictly validate HTTP headers and reject ambiguities

## Objectives

1. Test if cURL allows sending conflicting headers
2. Prepare a smuggled payload for further exploitation
3. Confirm potential for smuggling attacks

## Instructions

### Step 1: Craft and Send Test Request

**Context**: Create a POST request with both headers and a smuggled payload to check if cURL processes it.

**Command** ([[commands/curl-test-conflicting-headers]]):
```bash
curl -v -X POST -H "Transfer-Encoding: chunked" -H "Content-Length: 100" -d "0\r\n\r\nSMUGGLED_PAYLOAD" http://example.com/test
```

> This command sends the request with verbose output, including a chunked ending followed by the smuggled content. Expected output includes confirmation of both headers in the request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-test-conflicting-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- [[http-smuggling]]
- [[header-conflicts]]
