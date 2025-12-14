---
id: proc-libcurl-parsing-demo-001
tags:
  - parsing
  - libcurl
  - ipv6
type: procedure
tools:
  - '[[tools/libcurl]]'
  - '[[tools/trurl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/run-libcurl-parsing-test]]'
  - '[[commands/extract-url-components-with-trurl]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.536Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-libcurl-Parsing-Stripping

## Summary

This procedure tests and demonstrates how libcurl strips the zone identifier from IPv6 URL hostnames during parsing, treating it separately and deviating from RFC 6874, which can lead to incorrect network routing.

## Description

Using a compiled test program or trurl (libcurl-based), parse a malformed IPv6 URL to extract host and zone components. The hostname becomes [fe80::1] without %eth0, while the zone is preserved separately, causing connections to use the default interface. Compare with other libraries (Rust, Go, Python) that include the zone in the literal. This highlights the vulnerability in applications relying on parsed hostnames for routing.

## Requirements

1. Compiled libcurl test executable from prior setup.
2. Input file (e.g., seed_tmp.txt) with test URLs.
3. trurl tool installed (post-v0.8).

## Defense

Defensive measures and detection strategies:

- Audit libcurl usage and switch to compliant parsers for IPv6.
- Add post-parsing validation to recombine host and zone.
- Monitor for anomalous interface usage in logs.

## Objectives

1. Verify zone ID stripping in libcurl output.
2. Extract and compare host/zone components.
3. Confirm inconsistency with RFC standards.

## Instructions

### Step 1: Run Compiled Test

**Context**: Execute the custom program to parse URLs and output hostnames.

**Command** ([[commands/run-libcurl-parsing-test]]):
```bash
./parserbatch
```

> Parses URLs from seed_tmp.txt, showing stripped hostnames (e.g., [fe80::1]).

### Step 2: Use trurl for Extraction

**Context**: Directly parse with trurl to see separated fields.

**Command** ([[commands/extract-url-components-with-trurl]]):
```bash
trurl --get 'Host: {host} Zone: {zoneid}' 'http://[fe80::1%25eth0]/'
```

> Outputs Host: [fe80::1] Zone: eth0, demonstrating separation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/run-libcurl-parsing-test]]
- [[commands/extract-url-components-with-trurl]]

## Tools Used

- [[tools/libcurl]]
- [[tools/trurl]]

## Tags

- parsing
- libcurl
- ipv6
