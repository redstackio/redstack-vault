---
tags:
  - recon
  - http
  - baseline
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/normal-http-get-to-target]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:53:38.044Z'
sub_techniques: []
id: c4aea8a7-84c1-4fee-874e-2cae045b75f8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Send-Normal-HTTP-Request-to-Target

## Summary

This procedure sends a standard HTTP GET request to the target DoD website to establish baseline behavior and confirm normal connectivity before attempting exploitation.

## Description

In the context of SSRF testing on a public-facing DoD web application, this initial step simulates legitimate user traffic using common browser headers. It verifies that the target responds correctly without any immediate anomalies, setting the stage for header manipulation. The target environment is a web server on port 80, likely using ASP.NET based on session cookies.

## Requirements

1. Network access to the target website (www.████████)
2. Tool for sending HTTP requests (e.g., curl or Burp Suite)
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement request logging to monitor baseline traffic patterns
- Use WAF rules to flag unusual User-Agent or header combinations

## Objectives

1. Confirm legitimate response from the target server
2. Capture baseline headers for comparison in exploitation steps
3. Validate tool setup for subsequent requests

## Instructions

### Step 1: Craft and Send Baseline Request

**Context**: Prepare a standard GET request mimicking a Firefox browser to interact with the target.

**Command** ([[commands/normal-http-get-to-target]]):
```http
GET / HTTP/1.1
Host: www.████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/-;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: mt=rid=6130; ASPSESSIONIDQABQSQCS=GNPLOPOCDIGPIKHGFMDDBLBG; googtrans=/en/zh-TW
Connection: close
Upgrade-Insecure-Requests: 1
```

> This command sends a normal request and expects a 200 OK response with the website's HTML content. No leakage should occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/normal-http-get-to-target]]

## Tools Used


## Tags

- recon
- http
- baseline
