---
id: tool-python-http-cookies
url: 'https://docs.python.org/3/library/http.cookies.html'
tags:
  - library
  - python
  - web
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.485Z'
validated: true
submitted: true
---
# Python-http-cookies

**Status**: Unverified

## Overview

Python's http.cookies module provides the SimpleCookie class for parsing HTTP cookies, demonstrating vulnerabilities like delimiter injection in Django contexts.

## Description

The module's load() method uses a lax regex allowing ']', space, tab, etc., as separators, enabling attacks. Used in code snippets to replicate server-side parsing flaws for PoCs.

## Features

- Feature 1: SimpleCookie for Morsel-based parsing
- Feature 2: Support for quoted values and attributes
- Feature 3: Lax delimiter handling (vulnerable pre-patches)

## Installation

### Requirements

- Python 3.6+

### Install Commands

```bash
# Included in stdlib, no install needed
python3 -c "from http import cookies; print('OK')"
```

## Basic Usage

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('cookie=value')
print(C)
```

### Common Options

N/A (library methods)

## Examples

### Example 1: Basic Usage

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah]csrftoken=x')
print(C)
```

### Example 2: Advanced Usage

Test delimiters as in commands.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]]
- [[Pass the Hash]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python traces in logs
- Anomalous cookie parses
- Version < fixed (pre-3.5?)

## Related Procedures


## Related Tools

- [[tools/Google-Chrome]]

## References

- Official documentation: https://docs.python.org/3/library/http.cookies.html
- Vulnerability reports: HackerOne #26647
