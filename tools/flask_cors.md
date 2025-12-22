---
id: 0f534cac-e2f6-4039-b557-4ba416960930
name: flask_cors
type: tool
verified: false
created_at: '2025-12-11T06:10:15.556Z'
updated_at: '2025-12-11T06:10:15.556Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web
  - cors
url: 'https://flask-cors.readthedocs.io/'
description: Flask extension for handling Cross-Origin Resource Sharing.
validated: true
submitted: true
---

# flask_cors

**Status**: Unverified

## Overview

flask_cors is an extension for Flask to enable Cross-Origin Resource Sharing, allowing cross-domain requests in web applications.

## Description

It simplifies handling CORS headers, useful in attack servers where cross-origin logging is needed, such as in DNS rebinding scenarios.

## Features

- Feature 1: Automatic CORS header addition
- Feature 2: Configurable for specific routes
- Feature 3: Supports multiple origins

## Installation

### Requirements

- Flask installed
- pip

### Install Commands

```bash
pip install flask-cors
```

## Basic Usage

```python
from flask_cors import CORS
CORS(app)
```

### Common Options

| Option | Description |
|--------|-------------|
| `origins` | Allowed origins |
| `methods` | Allowed HTTP methods |

## Examples

### Example 1: Basic Usage

```python
CORS(app)
```

### Example 2: Advanced Usage

```python
CORS(app, origins='*')
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Check for CORS headers in responses
- Monitor cross-origin requests

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Flask]]
- [[tools/XMLHttpRequest]]

## References

- https://flask-cors.readthedocs.io/
- CORS documentation
