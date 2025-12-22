---
id: 9db7b9a8-9cdc-480d-b205-c2a817cd33ba
type: tool
verified: true
created_at: '2019-08-28T21:17:39.629470+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - evasion
  - ids-testing
  - false-positives
url: 'https://github.com/trimstray/inundator'
validated: true
---

# inundator

**Status**: Unverified

## Overview

Inundator is a multi-threaded, queue-driven tool designed to generate anonymous false positives for intrusion detection systems (IDS). It supports multiple targets and is commonly used in red teaming to test IDS configurations by simulating non-malicious traffic that triggers alerts, helping to tune detection rules without real attacks.

## Description

Inundator operates by queuing and dispatching requests to specified targets, mimicking patterns that could falsely trigger IDS signatures, such as high-volume benign probes or anomalous but legitimate behaviors. It emphasizes anonymity through optional proxy support or IP rotation, making it suitable for evasion testing and security validation in controlled environments.

## Features

- Multi-threaded request generation for high performance
- Queue-driven architecture to manage request bursts
- Support for multiple targets in a single run
- Anonymous mode with proxy chaining or spoofing
- Configurable request methods, rates, and payloads
- Logging for alert simulation verification

## Installation

### Requirements

- Go 1.16+ (built with Go)
- Linux environment (primary support)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/trimstray/inundator.git
cd inundator

# Build the binary
go build -o inundator .

# For Kali/Ubuntu, ensure Go is installed first
sudo apt update && sudo apt install golang-go
```

## Basic Usage

```bash
./inundator --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --version | Display version information |
| -t, --targets | Specify targets (IPs/hosts) |
| -r, --rate | Set request rate per second |
| --anonymous | Enable anonymous request mode |

## Examples

### Example 1: Basic Usage

Generate false positives against a single target at default rate.

```bash
./inundator -t 192.168.1.100
```

### Example 2: Advanced Usage

Target multiple hosts with custom rate and threads in anonymous mode.

```bash
./inundator -t 192.168.1.100,192.168.1.101 -r 50 -th 10 --anonymous
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual high-volume benign traffic patterns to IDS-monitored hosts
- Multi-threaded connections from single source with proxy artifacts
- Log entries showing queued request bursts without malicious payloads
- Process monitoring for 'inundator' binary or Go runtime signatures

## Related Procedures

- [[procedures/Generate-IDS-False-Positives]]
- [[procedures/Test-IDS-Evasion-Techniques]]

## Related Tools

- [[tools/hping3]]
- [[tools/scapy]]

## References

- Official GitHub: https://github.com/trimstray/inundator
- Go documentation for building: https://golang.org/doc/
