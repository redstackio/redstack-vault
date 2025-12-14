---
url: ''
tags:
  - vm
  - testing
type: tool
verified: false
platforms:
  - Windows
  - macOS
  - Linux
id: 2072fceb-697d-49c9-8681-4256b870ddeb
created_at: '2025-12-13T23:55:06.730Z'
updated_at: '2025-12-13T23:55:06.730Z'
validated: true
submitted: true
---
# VirtualBox

**Status**: Unverified

## Overview

Oracle VM for running Windows VMs to test RCE and debug offsets.

## Description

Hypervisor for local Windows environments to reproduce Electron/V8 exploits.

## Features

- Feature 1: Guest OS support
- Feature 2: Snapshot/restore
- Feature 3: USB passthrough

## Installation

### Requirements

- Host OS

### Install Commands

```bash
download from oracle.com
# Or: brew install --cask virtualbox (macOS)
```

## Basic Usage

```bash
VBoxManage startvm "Windows11"
```

### Common Options

| Option | Description |
|--------|-------------|
| --type | headless/gui |

## Examples

### Example 1: Basic Usage

Create and start Windows VM.

### Example 2: Advanced Usage

```bash
VBoxManage snapshot "VM" take "test"
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

- Monitor VM process

## Related Tools

- [[tools/AWS-EC2]]

## References

- VirtualBox Docs
