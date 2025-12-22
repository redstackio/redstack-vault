---
url: ''
tags:
  - encoding
  - xss
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Python script to convert JS to char codes for XSS payloads
id: 4db28b93-64ba-4674-9721-2f40ef7944b2
created_at: '2025-12-14T00:11:16.547Z'
updated_at: '2025-12-14T00:11:16.547Z'
verified: false
validated: true
submitted: true
---
# Python Char Code Converter

**Status**: Unverified

## Overview

A Python script designed to convert JavaScript code into character code arrays, useful for obfuscating XSS payloads to bypass restrictions like spaces in src attributes.

## Description

The tool takes JS input and outputs an array of char codes, which can be used in eval(String.fromCharCode()) constructs. It includes PoC for various exploits like changing usernames or site settings.

## Features

- Converts JS strings to numerical char codes
- Handles spaces and quotes for iframe src compatibility
- Supports custom PoC payloads

## Installation

### Requirements

- Python 3.x

### Install Commands

```bash
# No installation needed; run as script
```

## Basic Usage

```bash
python char_converter.py 'let test = 123; alert(test);'
```

### Common Options

| Option | Description |
|--------|-------------|
| input | JS code to convert |

## Examples

### Example 1: Basic Usage

```bash
python char_converter.py 'alert(1)'
```

### Example 2: Advanced Usage

```bash
python char_converter.py 'complex js here'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unusual char code arrays in inputs
- Log eval usage in JS contexts

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

- HackerOne Report #487081
