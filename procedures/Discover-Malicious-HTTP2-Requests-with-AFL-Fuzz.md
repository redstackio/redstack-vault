---
id: proc-discover-http2-fuzz
tags:
  - dos
  - fuzzing
  - http2
  - discovery
type: procedure
tools:
  - '[[tools/afl-fuzz]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.465Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-Malicious-HTTP2-Requests-with-AFL-Fuzz

## Summary

This procedure uses the AFL-Fuzz tool to identify specially crafted HTTP/2 requests that exploit a flaw in Apache's mod_http2 module (CVE-2018-1333), causing worker threads to hang while waiting for incomplete data until a timeout, enabling resource exhaustion attacks.

## Description

In a controlled environment, such as a local Apache server with mod_http2 and h2c enabled, AFL-Fuzz is employed to mutate sample HTTP/2 frames (e.g., PRIORITY, HEADERS, DATA). The fuzzer monitors server behavior for anomalies like prolonged thread blocking without resource release. This reveals requests that bypass validation, tricking the module into indefinite waits. Prerequisites include compiling Apache with debugging symbols and running under AFL's instrumentation for crash detection. Expected outcomes: reproducible request payloads that hold resources for up to 1 minute per worker.

## Requirements

1. AFL-Fuzz installed and configured for network fuzzing (e.g., via AFL-Net extension)
2. Test Apache HTTP Server 2.4.x with mod_http2 enabled on localhost:8080 (h2c mode)
3. Sample HTTP/2 corpus (e.g., valid frames from Wireshark captures)
4. Monitoring tools like strace or gdb to observe thread hangs

## Defense

Defensive measures and detection strategies:

- Disable HTTP/2 or use strict frame validation in mod_http2 configuration
- Implement request rate limiting and timeout reductions (e.g., <30 seconds)
- Monitor worker process CPU/memory spikes and anomalous connection patterns via tools like Apache's mod_status or ELK stack

## Objectives

1. Uncover HTTP/2 requests causing uncontrolled resource consumption in mod_http2
2. Validate hangs exceed typical timeouts without crashing the server
3. Prepare payloads for low-rate DoS exploitation

## Instructions

### Step 1: Setup AFL-Fuzz Environment

**Context**: Prepare the fuzzing target by instrumenting Apache to handle HTTP/2 inputs via a fuzzer harness.

No specific command; configure AFL with a seed corpus of HTTP/2 binaries and point to the local Apache instance.

> Run AFL-Fuzz: afl-fuzz -i input_corpus -o findings -- /path/to/http2_harness @@. This mutates inputs and tests against mod_http2, logging hangs as 'persistent' faults.

### Step 2: Execute Fuzzing Session

**Context**: Launch fuzzing to discover problematic requests that trigger resource holds.

No command; monitor output for sessions where server threads block >30 seconds on incomplete DATA frames.

> Expected: AFL identifies mutations like truncated HEADERS (e.g., incomplete PRIORITY updates) causing waits. Extract hex payloads from findings/crashes directory for later use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/afl-fuzz]]

## Tags

- [[dos]]
- [[fuzzing]]
- [[http2]]
