---
tags:
  - host-header-injection
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-host-header-injection-test]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: bba99780-becd-4c60-8444-b0effd80f88a
created_at: '2025-12-13T09:01:17.465Z'
updated_at: '2025-12-13T09:01:17.465Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test for Host Header Injection

## Summary

This procedure tests for host header injection vulnerabilities by modifying the Host header in an HTTP request to an external domain, observing the server's response to identify potential issues like misdirected requests that could lead to password reset poisoning or cache poisoning.

## Description

Host header injection occurs when an application fails to properly validate the Host header in incoming HTTP requests, allowing attackers to inject arbitrary values. This can be exploited in scenarios where the header is used to generate links, redirects, or cache keys. In this case, the test involves sending a GET request to the /contact/ endpoint with a spoofed Host header set to an external domain like www.google.com. The server may respond with a 421 Misdirected Request, indicating partial handling, but further exploitation could enable access to internal hosts, XSS, or other attacks on Apache-based web servers.

## Requirements

1. Access to the target web application's endpoint (e.g., /contact/)
2. Tool for sending custom HTTP requests, such as curl
3. Knowledge of the target's domain and basic HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement strict validation of the Host header against a whitelist of allowed domains
- Monitor server logs for unusual Host header values or 421 response codes

## Objectives

1. Identify if the server accepts and processes spoofed Host headers
2. Check for potential impacts like misdirected requests or injection points
3. Document server response for further analysis

## Instructions

### Step 1: Craft and Send Modified Request

**Context**: Modify the Host header in a standard GET request to test for injection.

**Command** ([[commands/curl-host-header-injection-test]]):
```bash
curl -H "Host: www.google.com" -H "User-Agent: Mozilla/5.0" -H "Accept: */*" https://target.com/contact/
```

> This command sends a GET request to /contact/ with the Host header set to www.google.com. Expect a 421 Misdirected Request if the server detects the mismatch.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-host-header-injection-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[host-header-injection]]
- [[web]]
