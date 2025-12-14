---
id: proc-002
tags:
  - build
  - sanitizers
  - curl
type: procedure
tools:
  - '[[tools/git]]'
  - '[[tools/clang]]'
  - '[[tools/make]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-clone-curl]]'
  - '[[commands/cd-curl-dir]]'
  - '[[commands/buildconf-generate]]'
  - '[[commands/export-cc-clang]]'
  - '[[commands/export-cflags-sanitizers]]'
  - '[[commands/export-ldflags-sanitizers]]'
  - '[[commands/configure-curl-build]]'
  - '[[commands/make-parallel-build]]'
  - '[[commands/echo-build-status]]'
  - '[[commands/ls-curl-binary]]'
  - '[[commands/curl-version-check]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:28.094Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Building-cURL-with-Security-Debugging-Flags

## Summary

This procedure clones, configures, and compiles cURL 8.16.1-DEV with Clang, address/undefined sanitizers, and debug flags to enable detection of memory issues during testing.

## Description

To test for buffer overflows, cURL must be built securely with instrumentation. This involves cloning from GitHub, generating build configs, setting compiler/linker flags for sanitizers (-fsanitize=address,undefined), and configuring for WebSockets/OpenSSL/static build. Outcomes include a debug-enabled curl binary ready for Valgrind, verifying no compilation errors.

## Requirements

1. Linux with sudo for dependencies (build-essential, clang, etc.)
2. Internet access for clone and dependency installs
3. Installed dependencies like libssl-dev via apt

## Defense

Defensive measures and detection strategies:

- Integrate sanitizer builds into CI/CD pipelines
- Scan build logs for sanitizer warnings
- Use static linking to avoid shared lib vulnerabilities

## Objectives

1. Produce instrumented cURL binary
2. Enable WebSocket and SSL support
3. Verify build success for testing

## Instructions

### Step 1: Clone Repository

**Context**: Obtain cURL source code.

**Command** ([[commands/git-clone-curl]]):
```bash
git clone https://github.com/curl/curl.git
```

> Clones into curl/ directory.

### Step 2: Prepare Build Environment

**Context**: Navigate and generate configs.

**Command** ([[commands/cd-curl-dir]]):
```bash
cd curl
./buildconf
```

> Generates autoconf scripts.

### Step 3: Set Compiler and Flags

**Context**: Configure for sanitizers.

**Command** ([[commands/export-cc-clang]]):
```bash
export CC=clang
export CFLAGS="-fsanitize=address,undefined -fno-omit-frame-pointer -O1 -g"
export LDFLAGS="-fsanitize=address,undefined"
```

> Sets environment for secure build.

### Step 4: Configure Build

**Context**: Enable features and debug.

**Command** ([[commands/configure-curl-build]]):
```bash
./configure --enable-debug --enable-maintainer-mode --enable-websockets --with-openssl --disable-shared --enable-static
```

> Outputs configuration summary.

### Step 5: Compile

**Context**: Build the project.

**Command** ([[commands/make-parallel-build]]):
```bash
make -j$(nproc)
```

> Compiles in parallel.

### Step 6: Verify Build

**Context**: Check status and binary.

**Command** ([[commands/echo-build-status]]):
```bash
echo $?
ls -la src/curl
./src/curl --version
```

> Confirms exit 0 and version output.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- [[commands/git-clone-curl]]
- [[commands/cd-curl-dir]]
- [[commands/buildconf-generate]]
- [[commands/export-cc-clang]]
- [[commands/export-cflags-sanitizers]]
- [[commands/export-ldflags-sanitizers]]
- [[commands/configure-curl-build]]
- [[commands/make-parallel-build]]
- [[commands/echo-build-status]]
- [[commands/ls-curl-binary]]
- [[commands/curl-version-check]]

## Tools Used

- [[tools/git]]
- [[tools/clang]]
- [[tools/make]]

## Tags

- [[build]]
- [[sanitizers]]
- [[curl]]
