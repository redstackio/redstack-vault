---
tags:
  - http-request-smuggling
  - recon
type: procedure
tools:
  - '[[tools/smuggler]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/smuggler-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:33:34.510Z'
sub_techniques: []
id: bb6751c5-bae8-4f23-9943-55a6bf489d74
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-HTTP-Request-Smuggling-with-Smuggler

## Summary

This procedure uses the custom smuggler tool to scan for HTTP Request Smuggling vulnerabilities, specifically the CL.TE variant, by testing malformed headers like spaces in Transfer-Encoding to detect frontend/backend desynchronization.

## Description

In this attack scenario, the procedure targets web applications like slackb.com that may mishandle HTTP headers, leading to request smuggling. The smuggler tool runs exhaustive tests, identifying issues such as the 'space1' test where a space before the colon in 'Transfer-Encoding : chunked' causes the frontend to ignore chunking and use Content-Length, while the backend parses as chunked. Prerequisites include network access to the target and the smuggler tool installed. Expected outcome is confirmation of a smuggling vector for further exploitation.

## Requirements

1. Network access to target URL over HTTPS
2. Installed smuggler tool
3. Basic understanding of HTTP protocols

## Defense

Defensive measures and detection strategies:

- Normalize HTTP headers to remove spaces and enforce strict parsing
- Use request queuing or buffering to prevent desync
- Monitor for anomalous Transfer-Encoding headers in logs

## Objectives

1. Identify smuggling vulnerabilities
2. Confirm CL.TE desync
3. Gather payload details for exploitation

## Instructions

### Step 1: Run Smuggler Scan

**Context**: Launch the tool to test the target for various smuggling payloads.

**Command** ([[commands/smuggler-test]]):
```bash
smuggler -u https://slackb.com
```

> This command specifies the target URL and runs tests like 'space1', outputting failures indicating vulnerabilities such as CL.TE desync.

### Step 2: Analyze Output

**Context**: Review results for failed tests.

No command; parse the tool's output for details on the 'space1' test, noting the payload with space in Transfer-Encoding.

> Expected: Report showing desync in parsing, e.g., "space1: vulnerable".

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/smuggler-test]]

## Tools Used

- [[tools/smuggler]]

## Tags

- http-request-smuggling
- cl.te
