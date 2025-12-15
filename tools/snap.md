---
id: tool-snap
url: 'https://snapcraft.io/'
tags:
  - package-manager
  - containerization
type: tool
verified: false
platforms:
  - Linux
  - Ubuntu
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.747Z'
validated: true
submitted: true
---
# snap

**Status**: Unverified

## Overview

Snap is Canonical's package manager for installing sandboxed applications on Linux, vulnerable in versions before 4.4.4 to RCE via library path hijacking.

## Description

Snaps bundle apps with dependencies in containers, using bash wrappers that can be exploited if LD_LIBRARY_PATH is empty, allowing cwd library loads. Used to install vulnerable apps like Chromium or Audacity.

## Features

- Feature 1: Sandboxed app installation
- Feature 2: Automatic updates
- Feature 3: Interface plugs like x11 for GUI

## Installation

### Requirements

- Ubuntu or compatible Linux

### Install Commands

```bash
# Install snapd
sudo apt update && sudo apt install snapd
```

## Basic Usage

```bash
snap --help
```

### Common Options

| Option | Description |
|--------|-------------|
| install | Install snap |
| run | Execute snap app |

## Examples

### Example 1: Basic Usage

```bash
sudo snap install chromium
```

### Example 2: Advanced Usage

```bash
sudo snap install audacity
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Dynamic Linker Hijacking]] Dynamic Linker Search Order Hijacking

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor snap installs of GUI apps
- Audit wrapper scripts for empty paths

## Related Procedures

- [[procedures/Trigger-RCE-in-Snap-Application]]

## Related Tools

- [[tools/docker]]

## References

- Official documentation: https://snapcraft.io/docs
