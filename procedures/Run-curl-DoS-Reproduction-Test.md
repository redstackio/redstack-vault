---
tags:
  - dos
  - curl
  - reproduction
type: procedure
tools:
  - '[[tools/runtests.pl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/runtests.pl-418]]'
verified: false
platforms:
  - Linux
  - Unix
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.578Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[OS Exhaustion Flood]]'
id: 30c6ab91-1aee-4a3e-a700-0a4882351df4
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Run-curl-DoS-Reproduction-Test

## Summary

This procedure reproduces the CVE-2023-23916 DoS vulnerability in curl by executing test case 418, which triggers memory exhaustion through unbounded allocations for multiple Transfer-Encoding and Content-Encoding headers in HTTP responses.

## Description

In the curl test environment, this procedure uses the runtests.pl script to simulate a malicious server response parsed by curl, highlighting the lack of bounds on header occurrences. Each header instance causes a buffer allocation, exhausting available memory and causing a denial of service. This is ideal for verifying the vulnerability in unpatched curl versions and understanding the fix in subsequent patches.

## Requirements

1. Curl source code with tests directory containing test418
2. Perl environment for runtests.pl
3. Sufficient system resources to observe memory exhaustion (vulnerable curl build)

## Defense

Defensive measures and detection strategies:

- Patch curl to version fixing CVE-2023-23916 (bounds check on header counts)
- Monitor HTTP client processes for high memory usage
- Use resource limits (e.g., ulimit) on curl invocations

## Objectives

1. Trigger and observe memory exhaustion in curl
2. Confirm DoS impact from multi-header processing
3. Validate reproduction for vulnerability reporting

## Instructions

### Step 1: Prepare Test Environment

**Context**: Ensure the curl test suite is set up with the extracted test418 file.

Navigate to the curl source directory and verify test418 exists in tests/.

> No command; manual check to confirm setup.

### Step 2: Execute Test

**Context**: Run the specific test case to reproduce the vulnerability, simulating the HTTP response parsing failure.

**Command** ([[commands/runtests.pl-418]]):
```bash
runtests.pl 418
```

> This command invokes the Perl script to execute test 418, which sends a crafted response with multiple encoding headers. Expected output includes test failure logs showing buffer allocations leading to memory exhaustion or process crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion (Memory)

## Commands Used

- [[commands/runtests.pl-418]]

## Tools Used

- [[tools/runtests.pl]]

## Tags

- [[dos]]
- [[curl]]
- [[reproduction]]
