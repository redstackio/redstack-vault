---
id: tool-uuid-002
url: 'http://www.bluez.org/'
name: BlueZ
tags:
  - bluetooth
  - stack
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.311Z'
validated: true
submitted: true
---
# BlueZ

**Status**: Unverified

## Overview

BlueZ is the official Linux Bluetooth protocol stack, providing tools for managing Bluetooth adapters, including spoofing, discoverability, and connection handling in security testing scenarios.

## Description

Version 5.55 on Raspberry Pi OS enables configuration of adapters for attacks like device impersonation. It's used for setting discoverable states, restarting services, and capturing Bluetooth traffic.

## Features

- Feature 1: bluetoothctl for interactive control
- Feature 2: Support for SSP and legacy pairing
- Feature 3: Integration with kernel for low-level access

## Installation

### Requirements

- Linux kernel 6.1 or later
- Raspberry Pi OS Bullseye

### Install Commands

```bash
# Usually pre-installed; update if needed
sudo apt update && sudo apt install bluez
```

## Basic Usage

```bash
bluetoothctl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| power on/off | Toggle adapter power |

## Examples

### Example 1: Basic Usage

```bash
bluetoothctl discoverable on
```

### Example 2: Advanced Usage

```bash
bluetoothctl scan on
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- bluetooth.service restarts in logs
- Unusual discoverable states
- Traffic anomalies via btmon

## Related Procedures

- [[procedures/Set-Bluetooth-Adapter-to-Discoverable-State]]

## Related Tools

- [[tools/Golang]]

## References

- Official documentation: http://www.bluez.org/
