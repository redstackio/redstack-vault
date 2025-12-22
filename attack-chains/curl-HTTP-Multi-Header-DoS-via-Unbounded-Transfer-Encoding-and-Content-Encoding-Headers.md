---
tags:
  - dos
  - curl
  - http
  - memory-exhaustion
  - vulnerability
type: attack_chain
tools:
  - '[[tools/runtests.pl]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - Unix
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Extract-curl-Test-Case-from-Patch]]'
  - '[[procedures/Run-curl-DoS-Reproduction-Test]]'
step_count: 2
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:48.594Z'
description: >-
  Demonstrates a denial-of-service attack on curl clients by sending an HTTP
  response with an unbounded number of Transfer-Encoding and Content-Encoding
  headers, leading to memory exhaustion without bounds checking.
skill_level: intermediate
impact_level: high
id: f6d42317-1111-48f2-9459-1e6bafc42410
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# curl HTTP Multi-Header DoS via Unbounded Transfer-Encoding and Content-Encoding Headers

Multi-stage attack chain demonstrating the reproduction of CVE-2023-23916, a denial-of-service vulnerability in curl where a malicious server sends an HTTP response with multiple Transfer-Encoding and Content-Encoding headers, each allocating a buffer and exhausting client memory.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Extract Test Case] --> B[Run Reproduction Test]
    B --> C[Memory Exhaustion DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/runtests.pl]]

### Target Environment

- Linux or Unix-like system with curl source code and test suite
- Access to curl development environment
- Perl installed for test execution

### Initial Access Requirements

- Local access to a machine with curl built from source
- No network credentials needed; reproduction is local

## Detailed Attack Procedures

### Step 1: Extract Test Case
procedure: [[procedures/Extract-curl-Test-Case-from-Patch]]

**Objective**: Obtain the custom test case (test418) from the vulnerability patch to simulate the malicious HTTP response.

**Instructions**: Review the provided patch file for the curl project, which includes test418 demonstrating multiple Transfer-Encoding and Content-Encoding headers. Manually extract or apply the patch to generate the test file in the curl test directory.

**Expected Output**: A test file (test418) containing the crafted HTTP response with unbounded headers.

**Success Indicators**:
- Test file test418 is present in the curl/tests directory
- File contents show multiple encoding header instances

### Step 2: Run Reproduction Test
procedure: [[procedures/Run-curl-DoS-Reproduction-Test]]

**Objective**: Execute the test to trigger memory exhaustion in curl's HTTP response parsing.

**Instructions**: Use the curl test suite to run test case 418, which sends the malicious response and observes the allocation failures.

Execute [[commands/runtests.pl-418]]:

```bash
runtests.pl 418
```

**Expected Output**: Test failure indicating memory exhaustion or buffer allocation errors during header processing.

**Success Indicators**:
- Curl process consumes excessive memory
- Test logs show unbounded buffer allocations for headers

## Attack Chain Summary

### Key Achievements

1. Successful extraction of the vulnerability test case from the patch
2. Reproduction of DoS via multiple encoding headers in curl
3. Demonstration of client-side memory exhaustion without header count limits

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion (Memory)

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
