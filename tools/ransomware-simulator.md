---
url: null
tags:
  - simulation
  - ransomware
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.564Z'
id: 38dd4b96-7710-461e-bb69-0cd2a2f6a301
validated: true
submitted: true
---
# ransomware-simulator

**Status**: Unverified

## Overview

A custom Go-based executable that simulates ransomware by attempting file encryption in a target directory, designed to trigger detection by security tools like Acronis without causing real harm.

## Description

ransomware_sim.exe mimics ransomware behavior (e.g., renaming/encrypting files) but can be configured to execute arbitrary payloads when copied to quarantine. It's placed in ProgramData for easy execution and detection in this exploit chain.

## Features

- Feature 1: Simulate file encryption
- Feature 2: Target specific directories
- Feature 3: Non-destructive mode for testing

## Installation

### Requirements

- Go compiler if building from source
- Windows environment

### Install Commands

```cmd
# Assume pre-built; otherwise go build ransomware_sim.go
copy ransomware_sim.exe C:\ProgramData\ransomware_sim.exe
```

## Basic Usage

```cmd
ransomware_sim.exe <target_dir>
```

### Common Options

| Option | Description |
|--------|-------------|
| <target_dir> | Directory to simulate on |

## Examples

### Example 1: Basic Usage

```cmd
ransomware_sim.exe C:\Users\UNPRIVILIEGEDUSER\"
```

### Example 2: Advanced Usage

Run with logging for debugging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Execution from ProgramData
- File access patterns mimicking encryption

## Related Procedures

- [[procedures/Prepare-and-Trigger-Ransomware-Simulation]]

## Related Tools

- [[tools/symboliclink-testing-tools]]

## References

- Custom tool for this exploit; based on Go ransomware simulations
