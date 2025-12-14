---
url: null
tags:
  - scripting
  - socket
type: tool
verified: false
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.217Z'
id: 3759bad5-6715-47bc-b01d-9ab5c9e158a9
validated: true
submitted: true
---
# Perl

**Status**: Unverified

## Overview

Perl is a versatile scripting language with strong text processing and networking capabilities, ideal for quick PoC tools like TCP listeners in pentesting.

## Description

Used here to create a one-liner TCP server for capturing SSRF traffic in constrained environments like Docker containers, leveraging modules like IO::Socket::INET.

## Features

- Feature 1: One-liner scripting for rapid prototyping
- Feature 2: Built-in socket support
- Feature 3: Cross-platform compatibility

## Installation

### Requirements

- Most Linux/Docker images include Perl

### Install Commands

```bash
apt install perl -y
```

## Basic Usage

```bash
perl -e 'print "Hello";'
```

### Common Options

| Option | Description |
|--------|-------------|
| -MModule | Load module |
| -e | Execute code |

## Examples

### Example 1: Basic Usage

```bash
perl -e 'print "Test";'
```

### Example 2: Advanced Usage

TCP listener as in command.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell (adapted for Perl)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Perl processes binding to ports
- One-liner executions in logs
- IO::Socket usage

## Related Procedures

- [[procedures/Setup-Perl-TCP-Listener-in-Container]]

## Related Tools

- [[tools/Python]]

## References

- perl.org
