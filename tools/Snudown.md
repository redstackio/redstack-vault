---
id: uuid6
url: 'https://github.com/reddit/snudown'
tags:
  - markdown-parser
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:49.030Z'
validated: true
submitted: true
---
# Snudown

**Status**: Unverified

## Overview

Snudown is Reddit's custom markdown parser written in C, used for rendering user comments and posts, vulnerable to hash collision DoS in reference links.

## Description

It processes markdown inputs into HTML, employing a hash table for reference definitions. Commonly used in web applications for secure parsing, but flaws allow algorithmic DoS via collisions and duplicates in offensive security testing.

## Features

- Fast C-based parsing
- Support for reference links [text][ref]: url
- Hash table for efficient lookups (flawed in older versions)

## Installation

### Requirements

- GCC compiler
- Make

### Install Commands

```bash
# Clone and build
git clone https://github.com/reddit/snudown.git
cd snudown
make
```

## Basic Usage

```bash
./snudown < input.md > output.html
```

### Common Options

| Option | Description |
|--------|-------------|
| No CLI options; stdin/stdout based |

## Examples

### Example 1: Basic Usage

```bash
./snudown < sample.md > rendered.html
```

### Example 2: Advanced Usage

For testing, pipe malicious input:

```bash
echo "[test]: /url" | ./snudown > out.html
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for gcc builds of markdown.c
- High CPU during markdown rendering

## Related Procedures


## Related Tools

- [[tools/HighwayHash]]
- [[tools/SipHash]]

## References

- GitHub repo: https://github.com/reddit/snudown
