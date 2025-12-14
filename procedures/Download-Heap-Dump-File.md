---
id: proc-002
tags:
  - heapdump
  - download
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-download]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.363Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Download-Heap-Dump-File

## Summary

This procedure retrieves the complete JVM heap dump file from the exposed actuator endpoint, capturing all in-memory server data for offline analysis.

## Description

The /actuator/heapdump endpoint in Spring Boot triggers the JVM to create a snapshot of the heap memory, which includes loaded classes, objects, and strings. Due to misconfiguration, this file is downloadable without credentials, exposing runtime data from multiple domains like plugin.stripo.email.

## Requirements

1. Valid endpoint URL confirmed accessible
2. Sufficient local storage for large files (GBs)
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Disable heapdump endpoint in production or require authentication
- Implement rate limiting on actuator paths to prevent abuse
- Log and monitor large file downloads from management endpoints

## Objectives

1. Obtain raw heap memory data from the target server
2. Prepare file for detailed forensic analysis
3. Avoid detection by using direct HTTP requests

## Instructions

### Step 1: Initiate Download

**Context**: Use curl to fetch the heap dump, handling potential large file sizes.

**Command** ([[commands/curl-download]]):
```bash
curl -O https://my.stripo.email/cabinet/stripeapi/actuator/heapdump
```

> The -O flag saves the file with its original name; expect a binary .hprof file.

### Step 2: Verify Download Integrity

**Context**: Check file size and completeness post-download.

**Command** ([[commands/curl-download]]):
```bash
ls -lh heapdump.hprof
```

> Confirms the file is substantial (e.g., >1GB), indicating successful capture of memory contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-download]]

## Tools Used


## Tags

- [[heapdump]]
- [[java]]
