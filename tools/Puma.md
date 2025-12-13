---
url: ''
tags:
  - web-server
  - ruby
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Web server for Ruby applications
id: 2483fcb5-7f3a-4531-9eb6-50ac799c13d2
created_at: '2025-12-13T09:01:16.834Z'
updated_at: '2025-12-13T09:01:16.834Z'
verified: false
validated: true
submitted: true
---
# Puma

**Status**: Unverified

## Overview

Puma is a high-performance web server for Ruby, used to host applications like the Rails UJS test server.

## Description

It runs in single or clustered mode, here used in development with version 4.3.1 for the vulnerable endpoint.

## Features

- Threaded execution
- Configurable workers

## Installation

### Requirements

- Ruby installed

### Install Commands

```bash
gem install puma
```

## Basic Usage

```bash
puma --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | Port to bind |

## Examples

### Example 1: Basic Usage

```bash
puma
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network listening on ports
- Process monitoring for puma

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools



## References

- https://puma.io
