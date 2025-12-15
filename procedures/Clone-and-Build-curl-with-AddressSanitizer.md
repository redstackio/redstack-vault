---
tags:
  - build
  - asan
  - curl
type: procedure
tools:
  - '[[tools/Git]]'
  - '[[tools/Clang]]'
  - '[[tools/Make]]'
  - '[[tools/AddressSanitizer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-clone-curl]]'
  - '[[commands/cd-curl]]'
  - '[[commands/export-cc-clang]]'
  - '[[commands/export-cxx-clang++]]'
  - '[[commands/export-cflags-asan]]'
  - '[[commands/export-cxxflags-asan]]'
  - '[[commands/export-ldflags-asan]]'
  - '[[commands/configure-curl]]'
  - '[[commands/make-parallel]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:22.112Z'
sub_techniques: []
id: 8915c688-26cb-4217-a3d6-8beb426418b0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Clone-and-Build-curl-with-AddressSanitizer

## Summary

This procedure clones the curl source code from GitHub and builds it with Clang and AddressSanitizer enabled to detect memory errors like the out-of-bounds read in cookie handling for CVE-2025-9086 reproduction.

## Description

In a Linux environment, clone the curl repository, configure Clang as the compiler with ASan flags for runtime memory checking, enable OpenSSL support, disable shared libraries, and compile in debug mode. This setup allows triggering and detecting the vulnerability without production impacts. Prerequisites include Git, Clang, and Make installed.

## Requirements

1. Linux system with development tools
2. Clang and Make installed
3. Internet access for cloning
4. Sufficient disk space (~100MB)

## Defense

Defensive measures and detection strategies:

- Use static analysis tools like Coverity in CI/CD
- Enable ASan in development builds
- Monitor for memory errors in logs

## Objectives

1. Prepare vulnerable curl binary with instrumentation
2. Enable detection of buffer over-reads
3. Verify build integrity for reproduction

## Instructions

### Step 1: Clone Repository

**Context**: Fetch the curl source code to local machine.

**Command** ([[commands/git-clone-curl]]):
```bash
git clone https://github.com/curl/curl
```

> Clones the repository; expected output is a new 'curl' directory with source files.

### Step 2: Navigate to Directory

**Context**: Enter the cloned directory for build setup.

**Command** ([[commands/cd-curl]]):
```bash
cd curl
```

> Changes working directory; prompt updates to curl/.

### Step 3: Set Compilers

**Context**: Configure Clang for C and C++ compilation with ASan support.

**Command** ([[commands/export-cc-clang]] and [[commands/export-cxx-clang++]]):
```bash
export CC=clang
export CXX=clang++
```

> Sets environment variables; verify with echo $CC.

### Step 4: Enable ASan Flags

**Context**: Add sanitization flags to detect memory issues.

**Command** ([[commands/export-cflags-asan]], [[commands/export-cxxflags-asan]], [[commands/export-ldflags-asan]]):
```bash
export CFLAGS="-fsanitize=address"
export CXXFLAGS="-fsanitize=address"
export LDFLAGS="-fsanitize=address"
```

> Applies flags; no output, but affects subsequent builds.

### Step 5: Configure Build

**Context**: Prepare build with OpenSSL and debug options.

**Command** ([[commands/configure-curl]]):
```bash
./configure --with-openssl --disable-shared --enable-debug --enable-maintainer-mode
```

> Outputs configuration summary; ends with 'ready to make'.

### Step 6: Compile

**Context**: Build the binary using all CPU cores.

**Command** ([[commands/make-parallel]]):
```bash
make -j$(nproc)
```

> Compiles; expected output is binaries in src/, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/git-clone-curl]]
- [[commands/cd-curl]]
- [[commands/export-cc-clang]]
- [[commands/export-cxx-clang++]]
- [[commands/export-cflags-asan]]
- [[commands/export-cxxflags-asan]]
- [[commands/export-ldflags-asan]]
- [[commands/configure-curl]]
- [[commands/make-parallel]]

## Tools Used

- [[tools/Git]]
- [[tools/Clang]]
- [[tools/Make]]
- [[tools/AddressSanitizer]]

## Tags

- build
- asan
- curl
