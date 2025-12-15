---
url: 'http://lcamtuf.coredump.cx/afl/'
tags:
  - fuzzer
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:30.903Z'
id: cd151321-ab5b-4dcc-9246-38b37eea437a
validated: true
submitted: true
---
# American Fuzzy Lop (AFL)

**Status**: Unverified

## Overview

Coverage-guided fuzzer for discovering crashes in binaries/parsers.

## Description

Mutates inputs to find edges like overflows/DoS in open-source software.

## Features

- Feature 1: Code coverage
- Feature 2: Crash minimization
- Feature 3: Parallel fuzzing

## Installation

### Requirements

- Linux kernel
- QEMU for binaries

### Install Commands

```bash
# Download and make
make
```

## Basic Usage

```bash
afl-fuzz -i in -o out target @@
```

### Common Options

| Option | Description |
|--------|-------------|
| -i | Input dir |
| -o | Output dir |
| -m none | No mem limit |

## Examples

### Example 1: Basic Usage

```bash
afl-fuzz -i seeds -o findings ./parser @@
```

### Example 2: Advanced Usage

```bash
afl-fuzz -i in -o out -m none -f input.txt target
```

## MITRE ATT&CK Mapping

### Techniques

- [[T1587.001]] Malware Development

### Tactics

- [[Resource Development]] Resource Development

## Detection

- afl-fuzz processes
- High CPU usage

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/LibFuzzer]]

## References

- http://lcamtuf.coredump.cx/afl/
