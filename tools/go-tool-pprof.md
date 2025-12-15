---
url: 'https://pkg.go.dev/runtime/pprof'
tags:
  - profiling
  - go
  - analysis
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.132Z'
id: f742dd28-3b47-42c5-a990-6e7d7872df70
validated: true
submitted: true
---
# go-tool-pprof

**Status**: Unverified

## Overview

Command-line tool for analyzing Go profiles (CPU, memory, etc.) to identify performance bottlenecks in applications like InfluxDB.

## Description

Part of the Go toolchain, pprof visualizes and interacts with profile data from endpoints, showing call graphs, hotspots, and allocations. Used post-exploitation to dissect downloaded profiles for deeper insights.

## Features

- Feature 1: Interactive text or web-based visualization of profiles
- Feature 2: Support for heap, CPU, goroutine, and contention profiles
- Feature 3: Flame graph generation for bottleneck identification

## Installation

### Requirements

- Go 1.18+ installed

### Install Commands

```bash
# Included with Go installation
go version
```

## Basic Usage

```bash
go tool pprof --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -http | Start HTTP server for UI |
| -top | Show top functions |
| -list | List source code |

## Examples

### Example 1: Basic Usage

```bash
go tool pprof profile.pb.gz
```

### Example 2: Advanced Usage

```bash
go tool pprof -http=:8080 heap.pprof.gz
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]] System Information Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for "go tool pprof" executions
- Network traffic to localhost:8080 for UI

## Related Procedures


## Related Tools

- [[tools/go-tool-trace]]

## References

- Official documentation: https://pkg.go.dev/runtime/pprof
