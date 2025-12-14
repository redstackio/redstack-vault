---
id: tool-xmllint
url: 'https://xmlsoft.org/xmllint.html'
tags:
  - xml-parsing
  - vulnerability-testing
  - dos
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.396Z'
configuration: '--valid for DTD validation'
validated: true
submitted: true
---
# xmllint

**Status**: Unverified

## Overview

xmllint is a command-line tool from the libxml2 library for parsing, validating, and querying XML documents, often used in security testing to trigger vulnerabilities in XML handling, such as DoS via compressed inputs.

## Description

In offensive operations, xmllint simulates application behavior to exploit libxml2 flaws, like LZMA decompression issues, by processing malicious files and observing crashes from resource exhaustion.

## Features

- Feature 1: XML validation against DTDs or schemas.
- Feature 2: Support for compressed formats like LZMA via liblzma.
- Feature 3: Debugging output and error reporting with stack traces.

## Installation

### Requirements

- libxml2 and liblzma development packages.

### Install Commands

```bash
# Ubuntu/Debian
sudo apt install libxml2-utils
# Or compile from source
./configure --with-lzma && make && make install
```

## Basic Usage

```bash
xmllint --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--valid` | Validate against DTD |
| `--debug` | Enable debug output |
| `--noout` | Suppress document output |

## Examples

### Example 1: Basic Usage

```bash
xmllint --valid malicious.xml
```

### Example 2: Advanced Usage

```bash
./xmllint --valid --debug test000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for xmllint processes handling unexpected files.
- Alert on memory spikes correlated with XML parsing.

## Related Procedures

- [[procedures/Trigger-libxml2-DoS-with-xmllint]]

## Related Tools

- [[xmlstarlet]]
- [[libxml2]]

## References

- Official documentation: https://xmlsoft.org/xmllint.html
