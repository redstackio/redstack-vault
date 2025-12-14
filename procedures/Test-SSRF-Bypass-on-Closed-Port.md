---
id: proc-ssrf-closed-port
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
  - '[[commands/ssrf-localhost-21-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:53:38.667Z'
sub_techniques:
  - '[[T1190.001]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
---
# Test-SSRF-Bypass-on-Closed-Port

## Summary

This procedure exploits the SSRF vulnerability by injecting a localhost URL for a closed port (21) using %0A to bypass protections, observing quick response times to confirm the bypass without connection delays.

## Description

The /help_docs endpoint protects against direct internal URLs but allows bypass via line feed (%0A) appended after the internal target. Targeting 127.0.0.1:21 (closed FTP port) results in a fast failure, indicating the server attempted the internal request. This aids in port scanning for closed services.

## Requirements

1. Authenticated session from prior steps
2. Proxy for request modification
3. Timer to measure response times

## Defense

Defensive measures and detection strategies:

- Sanitize URL parameters to block line feeds and internal IPs
- Disable internal fetches or use network segmentation
- Monitor response times for anomalies indicating scans

## Objectives

1. Verify SSRF bypass mechanism
2. Detect closed ports via short response times
3. Collect error messages for further analysis

## Instructions

### Step 1: Modify URL Parameter

**Context**: Prepend internal URL with query and %0A to legitimate URL.

In proxy, edit 'url' to http://127.0.0.1:21/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html.

### Step 2: Send Injected Request

**Context**: Replay the modified request and time the response.

**Command** ([[commands/ssrf-localhost-21-test]]):
```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://127.0.0.1:21/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "Cookie: [your_session_cookies]"
```

> Expect ~450ms response with error for the full injected URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Vulnerability Scanning]] Scanning IP Blocks

### Sub-Techniques

- [[T1190.001]] Exploit Application Deployment Logic

## Commands Used

- [[commands/ssrf-localhost-21-test]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]
- [[tools/ZAP]]

## Tags

- ssrf
- port-scan
- bypass
