---
url: null
tags:
  - poc
  - ps4
  - ipv6
type: tool
platforms:
  - PS4
description: >-
  Adjusted proof-of-concept C program for PS4 to trigger IPv6 double free from
  WebKit.
id: 271d5268-2fe5-4b09-b595-33f37c9e7857
created_at: '2025-12-11T03:47:39.435Z'
updated_at: '2025-12-11T03:47:39.435Z'
verified: false
validated: true
submitted: true
---
# ps4.c

**Status**: Unverified

## Overview

Adjusted proof-of-concept C program for PS4 to trigger the double free vulnerability from WebKit process.

## Description

This tool is modified from poc.c to run in PS4's WebKit context, sending fragmented IPv6 packets without root, exploiting the kernel double free.

## Features

- Runs in unprivileged WebKit process
- Triggers double free on PS4 kernel
- ~20% reliability

## Installation

### Requirements

- PS4 SDK or custom framework
- Compilation in PS4 development environment

### Install Commands

```bash
# Compile with PS4 SDK
```

## Basic Usage

Run from WebKit context on PS4.

## Examples

### Example 1: Basic Usage

Execute in WebKit process.

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

- Monitor WebKit process for raw socket usage
- Kernel logs for mbuf corruption

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/poc.c]]

## References

- HackerOne Report: https://hackerone.com/reports/943231
