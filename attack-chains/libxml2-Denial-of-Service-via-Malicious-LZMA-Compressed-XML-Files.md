---
id: ac-libxml2-dos-lzma
tags:
  - dos
  - memory-exhaustion
  - libxml2
  - lzma
  - xml-parsing
  - fuzzing
type: attack_chain
tools:
  - '[[tools/xmllint]]'
  - '[[tools/od]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-libxml2-Vulnerability-via-Fuzzing]]'
  - '[[procedures/Inspect-Malicious-LZMA-File]]'
  - '[[procedures/Trigger-libxml2-DoS-with-xmllint]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:37.429Z'
description: >-
  A multi-step attack chain demonstrating the discovery and exploitation of a
  denial of service vulnerability in libxml2, where malicious LZMA-compressed
  XML files cause excessive memory consumption during decompression, leading to
  application crashes.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# libxml2 Denial of Service via Malicious LZMA Compressed XML Files

Multi-stage attack chain demonstrating the discovery, inspection, and exploitation of a denial of service vulnerability in libxml2 using malicious LZMA-compressed XML files. The vulnerability arises from libxml2's integration with liblzma, which fails to limit memory allocation during decompression of crafted inputs, leading to resource exhaustion and crashes.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Fuzzing Discovery] --> B[File Inspection]
    B --> C[DoS Exploitation]
    C --> D[System Crash]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/od]]
- [[tools/xmllint]]

### Target Environment

- Linux platform with libxml2 and liblzma (XZ Utils) installed
- Access to a fuzzing tool for LZMA file generation (e.g., custom fuzzer)
- Malicious LZMA-compressed XML file (e.g., test000)

### Initial Access Requirements

- Local system access to compile or run libxml2 tools like xmllint
- No network access required; this is a local library exploitation

## Detailed Attack Procedures

### Step 1: Vulnerability Discovery
procedure: [[procedures/Discover-libxml2-Vulnerability-via-Fuzzing]]

**Objective**: Identify the denial of service vulnerability in libxml2 by fuzzing LZMA-compressed files to find inputs that cause excessive memory consumption during XML parsing and decompression.

**Instructions**: Use a fuzzer to generate and test specially crafted LZMA files against libxml2's XML parsing functionality. Focus on inputs that trigger the xz_decomp function in xzlib.c, leading to unbounded memory growth in liblzma.

**Expected Output**: Identification of a malicious file (e.g., test000) that causes libxml2 to attempt massive memory allocations, such as billions of bytes, resulting in allocation failures.

**Success Indicators**:
- Fuzzer detects crashes or high memory usage in libxml2
- Malicious LZMA file isolated for further analysis

### Step 2: Inspect Malicious File
procedure: [[procedures/Inspect-Malicious-LZMA-File]]

**Objective**: Examine the structure of the crafted malicious LZMA file to understand the compression artifacts causing the vulnerability.

**Instructions**: Dump the binary contents of the malicious file using [[commands/od-hex-dump]] to reveal the hex structure, such as oversized dictionary sizes or invalid compression headers that mislead the decompressor.

```bash
od -tx1 ./test000
```

**Expected Output**: Hexadecimal dump showing patterns like "20000000 30 ff ff ff ff ff ff ff ff ff ff ff ff 30000015", indicating manipulated LZMA headers that request excessive memory.

**Success Indicators**:
- Binary structure reveals crafted elements (e.g., large dictionary size)
- Confirms the file is a valid LZMA stream with malicious properties

### Step 3: Exploit DoS Vulnerability
procedure: [[procedures/Trigger-libxml2-DoS-with-xmllint]]

**Objective**: Trigger the denial of service by parsing the malicious LZMA-compressed XML file with xmllint, causing liblzma to exhaust system memory and crash the application.

**Instructions**: Run xmllint on the malicious file using [[commands/xmllint-parse-valid]] to initiate decompression via xmlXzfileRead in xmlIO.c and xmlParseDocument in parser.c, leading to failure in lzma_code.

```bash
./xmllint --valid test000
```

**Expected Output**: AddressSanitizer reports allocation failure, e.g., "ERROR: AddressSanitizer failed to allocate 0x100002000 (4294975488) bytes", followed by a stack trace pointing to lzma_code and xmlParseDocument.

**Success Indicators**:
- Application crash due to memory exhaustion
- System resources depleted, confirming DoS impact

## Attack Chain Summary

### Key Achievements

1. Discovered a novel DoS vulnerability in libxml2 through targeted fuzzing of LZMA inputs.
2. Analyzed the malicious file to pinpoint the root cause in liblzma's decompression bounds.
3. Demonstrated reliable exploitation leading to complete application denial of service.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
