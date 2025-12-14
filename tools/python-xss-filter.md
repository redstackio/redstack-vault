---
url: 'https://github.com/phith0n/python-xss-filter'
tags:
  - xss-filter
  - sanitization
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:31.067Z'
id: 1055d811-f805-4b03-98bb-649e01956c4d
validated: true
submitted: true
---
# python-xss-filter

**Status**: Unverified

## Overview

Python-xss-filter is a Python library designed to filter and sanitize inputs to prevent XSS attacks, suitable as a fix for vulnerabilities like the Gratipay Stored XSS.

## Description

This tool scans and removes malicious HTML/JS from user inputs, including script tags and unsafe attributes. Suggested as a remediation for Gratipay's Markdown issue, it can be applied post-Markdown rendering or on raw inputs to block javascript: URIs and other vectors.

## Features

- XSS pattern detection and removal
- Customizable rules
- Integration with web frameworks

## Installation

### Requirements

- Python 2/3

### Install Commands

```bash
pip install xssfilter
```

## Basic Usage

```python
from xssfilter import XSSFilter
xf = XSSFilter()
clean = xf.filter("<script>alert(1)</script>")
```

### Common Options

| Option | Description |
|--------|-------------|
| `rules` | Custom XSS evasion rules |
| `mode` | Strict or lenient filtering |

## Examples

### Basic Usage

```python
clean_html = xf.filter("[xss](javascript:alert(1))")
print(clean_html)  # Sanitized output
```

### Advanced Usage

Chain with Markdown processors for full sanitization.

## Expected Output

Cleaned string without executable code.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- Defensive against [[JavaScript]]

### Tactics

- Mitigates [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Code reviews for xssfilter imports
- Absence indicates potential vuln

## Related Procedures


## Related Tools

- [[tools/mikasa]]

## References

- https://github.com/phith0n/python-xss-filter
- OWASP XSS Prevention Cheat Sheet
