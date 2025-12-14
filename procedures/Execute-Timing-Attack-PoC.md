---
tags:
  - timing-attack
  - poc
  - curl-exploit
type: procedure
tools:
  - '[[tools/Python]]'
  - '[[tools/requests-module]]'
  - '[[tools/poc-timing-attack-py]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/python3-poc-timing-attack]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-12-14T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Hardware]]'
updated_at: '2025-12-14T17:31:30.974Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 782ca247-4b33-4548-a70e-ed677ab38c57
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Hardware]]'
---
# Execute-Timing-Attack-PoC

## Summary

This procedure runs a Python PoC script to perform a timing attack against curl's Digest Authentication, sending requests with different algorithms and measuring response times to exploit the strcmp() vulnerability.

## Description

The attack targets curl's non-constant-time comparison of server-announced algorithms in digest.c line 360. Using the requests module, the PoC simulates client requests to a test server, iterating over algorithms like MD5, MD5-sess, and SHA-1. Timings are captured to detect discrepancies, allowing fingerprinting of supported configurations. Prerequisites include a running test server; outcomes reveal the vulnerable timing side-channel, though curl maintainers note limited impact due to protocol visibility.

## Requirements

1. Running test server on localhost:8080 with Digest Auth
2. Python 3 with requests module installed
3. poc_timing_attack.py script available

## Defense

Defensive measures and detection strategies:

- Patch curl to use constant-time functions (e.g., Curl_timestrcmp())
- Implement server-side rate limiting on authentication attempts
- Log and alert on high-frequency auth requests with varying parameters

## Objectives

1. Send targeted authentication requests to trigger curl's comparison
2. Capture precise response timings for analysis
3. Confirm exploitation of the timing vulnerability

## Instructions

### Step 1: Prepare the PoC Environment

**Context**: Ensure the script is ready and the target URL is correct for the protected resource.

No command; download or create poc_timing_attack.py if needed.

### Step 2: Run the PoC Script

**Context**: Execute the script to test multiple algorithms and log timings.

**Command** ([[commands/python3-poc-timing-attack]]):
```bash
python3 poc_timing_attack.py http://localhost:8080/protected
```

> The script uses requests to send Digest auth attempts, measuring nanosecond timings for each algorithm. Expected output includes per-algorithm logs like 'Testing algorithm: MD5 - 963236.5 ns' and overall vulnerability confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning
- [[Hardware]] Gather Victim Host Information: Hardware

### Sub-Techniques


## Commands Used

- [[commands/python3-poc-timing-attack]]

## Tools Used

- [[tools/Python]]
- [[tools/requests-module]]
- [[tools/poc-timing-attack-py]]

## Tags

- timing-attack
- poc
- curl-exploit
