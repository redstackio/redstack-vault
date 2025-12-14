---
url: 'http://misaka.61924.nl/api/'
tags:
  - markdown
  - xss-vuln
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:31.079Z'
id: 5d53c58a-925f-4967-af53-51c927e77db1
validated: true
submitted: true
---
# mikasa

**Status**: Unverified

## Overview

Mikasa is a wrapper library for processing Markdown input using the Sundown library, commonly used in web applications for rendering user-generated content.

## Description

In the Gratipay Stored XSS vulnerability, mikasa was misconfigured by missing the HTML_SAFELINK flag, allowing unsafe protocols like javascript: in links. This enables Stored XSS attacks via Markdown inputs. It's typically integrated in Python-based apps for safe Markdown handling, but requires proper flags for security.

## Features

- Markdown parsing via Sundown
- HTML output generation
- Configurable flags for sanitization

## Installation

### Requirements

- Python environment
- Sundown library dependencies

### Install Commands

```bash
pip install mikasa
```

## Basic Usage

```python
import mikasa
html = mikasa.markdown_to_html("[link](javascript:alert(1))", flags=0)  # Unsafe without HTML_SAFELINK
```

### Common Options

| Option | Description |
|--------|-------------|
| `flags` | Bitmask for Sundown options, e.g., HTML_SAFELINK to block unsafe links |
| `extensions` | Enable Markdown extensions |

## Examples

### Basic Usage

```python
html = mikasa.markdown_to_html("Hello [world](http://example.com)")
print(html)
```

### Advanced Usage (Unsafe)

```python
# Without HTML_SAFELINK, allows XSS
html = mikasa.markdown_to_html("[xss](javascript:alert('XSS'))")
```

## Expected Output

HTML string with rendered Markdown; unsafe configs output executable links.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Review app code for mikasa imports without HTML_SAFELINK
- Scan rendered HTML for javascript: links
- Audit Markdown inputs for URI schemes

## Related Procedures


## Related Tools

- [[tools/Sundown]]
- [[tools/Hoedown]]

## References

- http://misaka.61924.nl/api/
- Sundown documentation
