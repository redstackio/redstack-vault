---
url: ''
tags:
  - monitoring
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.276Z'
id: 30a7b181-7298-4e45-ad51-f633f90c7404
validated: true
submitted: true
---
# Task-Manager

**Status**: Unverified

## Overview

Built-in Windows GUI tool for monitoring processes, performance, and resource usage, used to track memory during PoC.

## Description

Provides tabs for processes, performance (including memory), allowing sorting and real-time views of leak effects.

## Features

- Feature 1: Process memory sorting
- Feature 2: CPU and disk graphs
- Feature 3: End task functionality

## Installation

### Requirements

- Windows OS

### Install Commands

Built-in; no installation needed.

## Basic Usage

```bash
# Ctrl+Shift+Esc
```

### Common Options

| Option | Description |
|--------|-------------|
| Processes tab | View and sort by memory |
| Performance tab | Memory usage overview |

## Examples

### Example 1: Basic Usage

Launch and select Processes > Sort Memory.

### Example 2: Advanced Usage

Use Details tab for PID-specific monitoring.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Taskmgr.exe process

## Related Procedures

- [[procedures/Monitor-Memory-Consumption]]

## Related Tools

- [[Resource-Monitor]]

## References

- Microsoft Docs: Windows Task Manager
