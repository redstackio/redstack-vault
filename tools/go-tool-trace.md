---
url: 'https://pkg.go.dev/runtime/trace'
tags:
  - tracing
  - go
  - analysis
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.127Z'
id: 4ebbca4e-ebe5-4962-af38-bd13ad81b1ba
validated: true
submitted: true
---
# go-tool-trace

**Status**: Unverified

## Overview

Command-line tool for analyzing Go execution traces to debug concurrency and runtime behavior in applications.

## Description

Processes trace files from runtime/trace, displaying goroutine schedules, syscalls, and blocking events in a viewer. Essential for analyzing downloaded traces from exposed pprof endpoints to understand program flow.

## Features

- Feature 1: Timeline visualization of execution events
- Feature 2: Filtering by goroutine or process
- Feature 3: Export to SVG for reports

## Installation

### Requirements

- Go 1.18+ installed

### Install Commands

```bash
# Included with Go
go version
```

## Basic Usage

```bash
go tool trace --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p | Filter by goroutine |
| -s | Save view as SVG |

## Examples

### Example 1: Basic Usage

```bash
go tool trace trace.out
```

### Example 2: Advanced Usage

```bash
go tool trace -p=1 trace.out
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]] System Information Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Execution of "go tool trace"
- Local viewer launches

## Related Procedures


## Related Tools

- [[tools/go-tool-pprof]]

## References

- Official documentation: https://pkg.go.dev/runtime/trace
