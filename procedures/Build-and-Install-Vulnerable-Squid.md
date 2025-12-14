---
id: proc-build-squid-2023
tags:
  - build
  - compile
  - squid
type: procedure
tools:
  - '[[tools/autoreconf]]'
  - '[[tools/configure]]'
  - '[[tools/make]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mkdir-squid-install]]'
  - '[[commands/cd-squid-source]]'
  - '[[commands/autoreconf-regenerate]]'
  - '[[commands/configure-squid-build]]'
  - '[[commands/make-compile-squid]]'
  - '[[commands/make-install-squid]]'
  - '[[commands/cd-to-squid-sbin]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:33.009Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Build-and-Install-Vulnerable-Squid

## Summary

This procedure compiles Squid 4.8 from source in a local installation to create a vulnerable instance for testing the Host header buffer overflow, ensuring no mitigations interfere with reproduction.

## Description

Targeting Linux build environments, this builds Squid without stack protectors (default in source) to enable RCE potential. It uses autoconf tools for configuration and installs to a custom prefix. Outcomes include a runnable `squid` binary ready for reverse proxy setup, with the overflow exploitable via crafted inputs.

## Requirements

1. Installed build tools: gcc, autoconf, automake, libtool
2. Access to the extracted Squid source directory
3. Sufficient disk space (~100MB) and CPU for compilation

## Defense

Defensive measures and detection strategies:

- Scan for custom compilations of proxy software in logs
- Use compiler flags like -fstack-protector-strong in production builds
- Monitor for make/autoconf processes on endpoints

## Objectives

1. Produce a vulnerable Squid binary for local testing
2. Install in isolated path to avoid system pollution
3. Verify build integrity for reliable exploitation

## Instructions

### Step 1: Create Install Directory

**Context**: Prepares the target path for compiled binaries.

**Command** ([[commands/mkdir-squid-install]]):
```bash
mkdir squid-install
```

> Creates `squid-install`. Expected output: Silent success.

### Step 2: Navigate to Source

**Context**: Enters the Squid source for build commands.

**Command** ([[commands/cd-squid-source]]):
```bash
cd squid-SQUID_4_8/
```

> Updates working directory. Expected output: Path change.

### Step 3: Regenerate Build Files

**Context**: Prepares autoconf environment.

**Command** ([[commands/autoreconf-regenerate]]):
```bash
autoreconf -if
```

> Generates configure script. Expected output: Build files created.

### Step 4: Configure Build

**Context**: Sets installation prefix.

**Command** ([[commands/configure-squid-build]]):
```bash
./configure --prefix=$(realpath ../squid-install)
```

> Configures with local prefix. Expected output: Summary ready for make.

### Step 5: Compile Squid

**Context**: Builds the binaries in parallel.

**Command** ([[commands/make-compile-squid]]):
```bash
make -j$(nproc)
```

> Compiles using CPU cores. Expected output: Compiled objects.

### Step 6: Install Squid

**Context**: Deploys to prefix.

**Command** ([[commands/make-install-squid]]):
```bash
make install
```

> Installs files. Expected output: Files in `squid-install/`.

### Step 7: Navigate to Binaries

**Context**: Positions for execution.

**Command** ([[commands/cd-to-squid-sbin]]):
```bash
cd ../squid-install/sbin/
```

> Enters sbin. Expected output: Path update.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/mkdir-squid-install]]
- [[commands/cd-squid-source]]
- [[commands/autoreconf-regenerate]]
- [[commands/configure-squid-build]]
- [[commands/make-compile-squid]]
- [[commands/make-install-squid]]
- [[commands/cd-to-squid-sbin]]

## Tools Used

- [[tools/autoreconf]]
- [[tools/configure]]
- [[tools/make]]

## Tags

- build
- compile
- squid
