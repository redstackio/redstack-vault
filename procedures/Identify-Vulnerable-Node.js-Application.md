---
tags:
  - http-request-smuggling
  - node.js
  - recon
type: procedure
tools:
  - '[[tools/Curl]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-scan-for-hrs-vulnerability]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3759cd31-8883-4246-887a-1e4666a5831c
created_at: '2025-12-13T09:01:17.690Z'
updated_at: '2025-12-13T09:01:17.690Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Node.js Application

## Summary

This procedure involves scanning a target web application to detect if it is running a vulnerable version of Node.js with the llhttp parser susceptible to HTTP Request Smuggling via flawed Transfer-Encoding header handling.

## Description

The vulnerability (CVE-2022-32213) affects the http module in Node.js, allowing attackers to smuggle requests due to improper parsing. This procedure uses probing requests to identify desynchronization between request parsers, targeting web environments with Node.js backends. Expected outcomes include confirmation of vulnerability for further exploitation.

## Requirements

1. Network access to the target's HTTP endpoint
2. Tools like Curl or Burp Suite installed
3. Knowledge of the target's domain or IP

## Defense

Defensive measures and detection strategies:

- Update Node.js and llhttp to patched versions
- Monitor for anomalous Transfer-Encoding headers in logs

## Objectives

1. Confirm presence of Node.js and llhttp
2. Detect smuggling vulnerability
3. Prepare for exploitation

## Instructions

### Step 1: Probe for Vulnerability

**Context**: Send a test request to check for parsing flaws in Transfer-Encoding.

**Command** ([[commands/curl-scan-for-hrs-vulnerability]]):
```bash
curl -v -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET / HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com
```

> This command tests if the server misinterprets chunked encoding, potentially smuggling a GET request. Look for unexpected responses.

### Step 2: Analyze Response

**Context**: Use Burp Suite to intercept and verify if the request causes desynchronization.

> Inspect headers and body for signs of smuggling success, such as echoed content or errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-scan-for-hrs-vulnerability]]

## Tools Used

- [[tools/Curl]]
- [[tools/Burp-Suite]]

## Tags

- [[http-request-smuggling]]
- [[node.js]]
