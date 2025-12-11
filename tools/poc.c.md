---
url: null
tags:
  - poc
  - freebsd
  - ipv6
type: tool
platforms:
  - FreeBSD
description: Proof-of-concept C program for FreeBSD to trigger IPv6 double free.
id: 67d8975e-d387-484c-8d2c-6f3926f021cf
created_at: '2025-12-11T03:47:39.437Z'
updated_at: '2025-12-11T03:47:39.437Z'
verified: false
validated: true
submitted: true
---
# poc.c

**Status**: Unverified

## Overview

Proof-of-concept C program to demonstrate privilege escalation on FreeBSD 9 by triggering the double free with fragmented IPv6 packets.

## Description

This tool crafts and sends fragmented IPv6 packets to loopback, exploiting the double free in IP6_EXTHDR_CHECK for memory corruption and escalation.

## Features

- Packet crafting for IPv6 fragments
- Triggers kernel double free
- ~80% reliability on FreeBSD

## Installation

### Requirements

- GCC compiler
- Root privileges on FreeBSD

### Install Commands

```bash
gcc poc.c -o poc
```

## Basic Usage

```bash
./poc
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | No options; direct execution |

## Examples

### Example 1: Basic Usage

```bash
./poc
```

### Example 2: Advanced Usage

N/A - Standalone PoC

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[procedures/Trigger-Double-Free-for-Privilege-Escalation]]
- [[Exploitation for Client Execution]]

### Tactics

- [[Privilege Escalation]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for anomalous IPv6 traffic on loopback
- Kernel crash logs indicating double free

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/ps4.c]]

## References

- HackerOne Report: https://hackerone.com/reports/943231
