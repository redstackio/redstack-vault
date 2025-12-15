---
url: >-
  https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack
tags:
  - fuzzing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.877Z'
id: fd998d51-ba3e-4a0b-9f2c-5e91e7eef81a
validated: true
submitted: true
---
# Turbo Intruder

**Status**: Unverified

## Overview

Burp extension for rapid HTTP fuzzing and brute-forcing.

## Description

Enables high-speed attacks like subdomain and directory enumeration using Python scripts.

## Features

- Feature 1: Billion-request capability
- Feature 2: Custom payloads
- Feature 3: Rate control

## Installation

### Requirements

- Burp Suite Pro

### Install Commands

```bash
# Load .jar in Burp Extensions
```

## Basic Usage

```bash
# Configure in Burp tab
```

### Common Options

| Option | Description |
|--------|-------------|
| Payloads | Wordlist input |
| Threads | Concurrency |

## Examples

### Example 1: Basic Usage

Fuzz subdomains.

### Example 2: Advanced Usage

Custom script for paths.

## MITRE ATT&CK Mapping

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

High request rates to single host.

## Related Procedures

- [[procedures/Enumerate-Subdomains-of-Target-Domain]]

## Related Tools

- [[Burp Suite]]

## References

- PortSwigger research
