---
id: proc-parse-url
tags:
  - url-parsing
  - libcurl
  - zone-id
type: procedure
tools:
  - '[[tools/libcurl]]'
  - '[[tools/trurl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/compile-parserbatch-test]]'
  - '[[commands/run-parserbatch-test]]'
  - '[[commands/trurl-parse-url]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:29:36.075Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Cloud Instance Metadata API]]'
---
# Parse-URL-with-libcurl-Omitting-Zone-ID

## Summary

This procedure tests and exploits libcurl's URL parsing to omit IPv6 zone identifiers, altering the effective hostname and enabling bypass of interface restrictions.

## Description

libcurl's CURLU API (curl_url_get for CURLUPART_HOST) strips zone IDs from IPv6 literals like `[fe80::1%eth0]`, parsing as `[fe80::1]` instead of preserving per RFC 6874. This affects applications using libcurl for validation. Test in a controlled environment to confirm behavior against other libraries (Rust, Go, Python).

## Requirements

1. Compiled libcurl test program (e.g., parserbatch)
2. Input file with test URLs (seed_tmp.txt containing `http://[fe80::1%25eth0]/`)
3. trurl installed for API frontend testing

## Defense

Defensive measures and detection strategies:

- Parse URLs with compliant libraries (e.g., Go net/url) and compare outputs
- Disable IPv6 zone ID support or validate post-parsing
- Audit libcurl usage and update to patched versions if available

## Objectives

1. Confirm zone ID omission in parsing
2. Extract parsed components for verification
3. Highlight deviation from RFC 6874

## Instructions

### Step 1: Compile Test Program

**Context**: Build C code to invoke libcurl's parsing.

**Command** ([[commands/compile-parserbatch-test]]):
```bash
gcc parserbatch.c -o parserbatch -lcurl
```

> Successful compilation links libcurl; no output on success.

### Step 2: Run Parsing Test

**Context**: Execute to parse URLs and observe omission.

**Command** ([[commands/run-parserbatch-test]]):
```bash
./parserbatch
```

> Outputs: 'Hostname: [fe80::1]' without zone ID from seed_tmp.txt.

### Step 3: Use trurl for Component Extraction

**Context**: Verify separate host and zoneid handling.

**Command** ([[commands/trurl-parse-url]]):
```bash
trurl --get 'Host: {host} Zone: {zoneid}' 'http://[fe80::1%25eth0]/'
```

> Outputs: 'Host: [fe80::1] Zone: eth0', but zone ignored in connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Cloud Instance Metadata API]] Unsecured Web Services

### Sub-Techniques


## Commands Used

- [[commands/compile-parserbatch-test]]
- [[commands/run-parserbatch-test]]
- [[commands/trurl-parse-url]]

## Tools Used

- [[tools/libcurl]]
- [[tools/trurl]]

## Tags

- url-parsing
- libcurl
- zone-id
