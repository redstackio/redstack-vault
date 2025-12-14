---
id: p-discover-open-redirect
tags:
  - open-redirect
  - endpoint-enumeration
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.528Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Open Redirect Endpoint

## Summary

This procedure focuses on enumerating and testing common redirect endpoints on a third-party web service to identify open redirect vulnerabilities, where URL parameters accept arbitrary external destinations without validation.

## Description

Open redirects occur when web applications fail to validate redirect targets, allowing attackers to chain them with trusted domains for phishing. After identifying a third-party domain via CNAME, test paths like '/redirect' with parameters such as 'url=' using browser requests or tools. The target environment is a public web service; prerequisites include the vendor domain from DNS recon. Successful discovery confirms unrestricted redirects, enabling phishing simulations.

## Requirements

1. Identified third-party domain from DNS
2. Web browser or HTTP client for testing
3. Knowledge of common redirect parameter names (e.g., url, next, redirect)

## Defense

Defensive measures and detection strategies:

- Implement URL validation with allowlists for redirects
- Log and monitor unusual redirect patterns
- Use Content Security Policy (CSP) to restrict navigation

## Objectives

1. Locate vulnerable redirect endpoints
2. Confirm lack of parameter validation
3. Assess potential for domain spoofing

## Instructions

### Step 1: Enumerate Common Endpoints

**Context**: Probe the third-party domain for redirect paths by accessing likely URLs.

Navigate to or request:

```http
http://third-party-domain/redirect
```

> Inspect the page or response for parameter inputs like 'url='. Expected output: A form or endpoint that processes redirect requests.

### Step 2: Test Arbitrary URL Parameter

**Context**: Append an external test URL to the parameter and observe behavior.

Construct and access:

```http
http://third-party-domain/redirect?url=http://example.com
```

> If redirected without checks, vulnerability confirmed. Expected output: 302 status with Location header to the test URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[redirect-testing]]
- [[parameter-fuzzing]]
