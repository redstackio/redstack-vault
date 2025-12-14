---
id: proc-trigger-curl-exhaustion
tags:
  - dos
  - memory-exhaustion
  - curl
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-fetch-malicious-response]]'
  - '[[commands/check-exit-status]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:37.300Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Trigger-curl-Memory-Exhaustion-with-Malicious-Response

## Summary

This procedure uses curl to fetch a malicious HTTP response from a local server, processing repeated compression headers that cause unbounded memory allocation, resulting in application termination or system unresponsiveness.

## Description

Curl versions prior to 7.84.0 do not limit resource allocation when handling multiple Transfer-Encoding or Content-Encoding headers with repeated 'gzip' values, or large numbers of Set-Cookie headers. Fetching such a response leads to indefinite memory growth, invoking the OOM killer on Unix-like systems (exit code 137) or causing black screens and reboots on Windows 11. This demonstrates client-side DoS via crafted HTTP responses.

## Requirements

1. Running malicious server on localhost:9999 (from prior procedure)
2. Vulnerable curl installation
3. Sufficient system resources to observe exhaustion (e.g., limited RAM for quicker effect)
4. Shell access to check exit codes

## Defense

Defensive measures and detection strategies:

- Patch curl to mitigate header processing flaws
- Limit HTTP client memory usage via ulimit or container resource caps
- Log and alert on curl processes exceeding memory thresholds
- Scan for and block servers sending anomalous header patterns

## Objectives

1. Force curl to process malicious headers and allocate excessive memory
2. Achieve DoS through application crash or system impact
3. Verify exhaustion via exit code or system behavior

## Instructions

### Step 1: Fetch Malicious Response

**Context**: Connect to the local server and request the response, triggering curl's header parsing and decompression logic.

**Command** ([[commands/curl-fetch-malicious-response]]):
```bash
curl http://localhost:9999
```

> Curl will attempt to decompress the repeated gzip encodings, leading to memory exhaustion. The process may hang or be killed by the OS.

### Step 2: Verify Termination

**Context**: Check the exit status to confirm OOM kill.

**Command** ([[commands/check-exit-status]]):
```bash
echo $?
```

> Expected output is 137, indicating SIGKILL from OOM killer on Unix-like systems.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-malicious-response]]
- [[commands/check-exit-status]]

## Tools Used

- [[tools/curl]]

## Tags

- [[dos]]
- [[memory-exhaustion]]
- [[tools/curl]]
