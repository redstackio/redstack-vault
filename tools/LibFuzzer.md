---
url: 'https://llvm.org/docs/LibFuzzer.html'
tags:
  - fuzzer
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:30.889Z'
id: a004904e-5e78-4f92-8fff-48bcb5b1082f
validated: true
submitted: true
---
# LibFuzzer

**Status**: Unverified

## Overview

In-process fuzzer for libraries, integrated with sanitizers.

## Description

Complements AFL for faster fuzzing of parsers like qpdf.

## Features

- Feature 1: In-process execution
- Feature 2: Sanitizer synergy
- Feature 3: Corpus evolution

## Installation

### Requirements

- Clang

### Install Commands

```bash
# Via LLVM build
clang++ -fsanitize=fuzzer code.cc
```

## Basic Usage

```bash
./fuzzer corpus_dir
```

### Common Options

| Option | Description |
|--------|-------------|
| None specific | Uses env vars |

## Examples

### Example 1: Basic Usage

```bash
./qpdf_fuzzer /path/to/seeds
```

### Example 2: Advanced Usage

Compile with -fsanitize=address,fuzzer.

## MITRE ATT&CK Mapping

### Techniques

- [[Develop Capabilities]] Develop Capabilities

### Tactics

- [[Resource Development]] Resource Development

## Detection

- Fuzzer binary runs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/American-Fuzzy-Lop-AFL]]

## References

- https://llvm.org/docs/LibFuzzer.html
