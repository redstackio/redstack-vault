---
id: proc-build-cosmos-sdk
tags:
  - cosmos-sdk
  - build
  - go-compile
type: procedure
tools:
  - '[[tools/make]]'
  - '[[tools/Go]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/make-build]]'
verified: false
platforms:
  - Blockchain
  - Cosmos SDK
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:30:46.790Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
---

# Build-Cosmos-SDK-Binaries

## Summary

This procedure compiles the latest version of the Cosmos SDK from source, ensuring the vulnerable lockup module is built for local testing and exploitation in a proof-of-concept environment.

## Description

In the context of exploiting the improper access control in the lockup module, building the SDK locally allows reproduction of the vulnerability on a controlled chain. The process involves checking out the repository and using Make to compile Go binaries, focusing on the lockup.go file where sender validation is bypassed.

## Requirements

1. Git access to Cosmos SDK repository
2. Go development environment installed
3. Make tool available

## Defense

Defensive measures and detection strategies:

- Use pre-built, audited SDK versions from trusted sources
- Monitor build pipelines for unauthorized source modifications
- Implement code signing for binaries

## Objectives

1. Obtain vulnerable SDK binaries for local chain
2. Verify compilation includes lockup module
3. Prepare for chain initialization

## Instructions

### Step 1: Clone and Build SDK

**Context**: Retrieve and compile the Cosmos SDK to include the vulnerable lockup module.

**Command** ([[commands/make-build]]):
```bash
make build
```

> This command compiles the Go-based SDK binaries. Expected output includes successful build logs and binaries in the build directory. Update the binary path in the setup_chain script post-build.

### Step 2: Verify Build

**Context**: Confirm binaries are ready for use.

**Command** (ls build):
```bash
ls build/
```

> Lists compiled files; success if cosmos-sdk binary is present.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (adapted for Unix Make/Go build)

### Sub-Techniques


## Commands Used

- [[commands/make-build]]
- [[commands/ls-build]]

## Tools Used

- [[tools/make]]
- [[tools/Go]]

## Tags

- [[cosmos-sdk]]
- [[build-procedure]]
