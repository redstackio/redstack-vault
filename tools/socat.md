---
url: ''
tags:
  - networking
  - proxy
type: tool
platforms:
  - Linux
description: Multi-purpose relay for bidirectional data transfer between endpoints
id: 72cbb2cb-548f-4fec-a8e3-bb319dee61b0
created_at: '2025-12-14T04:08:47.988Z'
updated_at: '2025-12-14T04:08:47.988Z'
verified: false
validated: true
submitted: true
---
# socat

**Status**: Unverified

## Overview

Socat (socket cat) extends nc for complex relaying, used here to forward Docker port to external malicious server.

## Description

Supports TCP listening/forwarding with options like reuseaddr for port binding after kill.

## Features

- Feature 1: Address type relaying
- Feature 2: Forking for multiple connections
- Feature 3: Error redirection

## Installation

### Requirements

- Build essentials

### Install Commands

```bash
apt install socat
```

## Basic Usage

```bash
socat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| tcp-listen | Listen on TCP |
| reuseaddr | Reuse address |
| fork | Handle multiple clients |

## Examples

### Example 1: Basic Usage

```bash
socat tcp-listen:2376,reuseaddr,fork tcp:1.2.3.4:1111
```

### Example 2: Advanced Usage

Add 2> /log for errors.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[DLL Search Order Hijacking]]

### Tactics

- [[Lateral Movement]]

## Detection

Indicators and methods for detecting this tool's usage:

- Socat processes binding to privileged ports

## Related Procedures


## Related Tools

- [[tools/nc]]

## References

- Socat homepage
