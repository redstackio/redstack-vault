---
id: tool-sleep-2023
url: 'https://www.gnu.org/software/coreutils/sleep'
tags:
  - delay
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.842Z'
validated: true
submitted: true
---
# sleep

**Status**: Unverified

## Overview

Sleep pauses execution for a specified time, used here to wait for Squid startup before sending the payload.

## Description

Built-in for scripting delays, preventing race conditions in automated exploits.

## Features

- Feature 1: Second granularity
- Feature 2: Fractional seconds
- Feature 3: Signal handling

## Installation

### Requirements

- Coreutils package

### Install Commands

Pre-installed.

## Basic Usage

```bash
sleep --help
```

### Common Options

None; argument is duration.

## Examples

### Example 1: Basic Usage

```bash
sleep 1
```

### Example 2: Advanced Usage

```bash
sleep 0.5 && echo "done"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]] Windows Command Shell (analogous)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Minimal; part of normal scripting

## Related Procedures

- [[procedures/Trigger-Squid-Host-Header-Buffer-Overflow]]

## Related Tools

- [[tools/usleep]]

## References

- Man page: sleep(1)
