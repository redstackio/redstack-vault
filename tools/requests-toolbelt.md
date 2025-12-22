---
id: 123e4567-e89b-12d3-a456-426614174010
name: requests-toolbelt
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.186Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - multipart
  - python
url: 'https://requests-toolbelt.readthedocs.io/en/latest/'
validated: true
submitted: true
---

# requests-toolbelt

**Status**: Unverified

## Overview

Requests-Toolbelt is an extension for the Requests library, providing utilities like MultipartEncoder for handling complex file uploads in security testing scenarios.

## Description

It enhances Requests with tools for multipart form data, essential for uploading files like the malicious HTML in Dust's API. Used here for encoding file fields with custom content types.

## Features

- Feature 1: MultipartEncoder for file uploads
- Feature 2: Boundary generation for forms
- Feature 3: Integration with Requests sessions

## Installation

### Requirements

- Python 3.x and requests library

### Install Commands

```bash
pip install requests-toolbelt
```

## Basic Usage

```bash
python -c "from requests_toolbelt import MultipartEncoder; print(MultipartEncoder(fields={'key': 'value'}))"
```

### Common Options

| Option | Description |
|--------|-------------|
| fields= | Dictionary of form fields including files |
| boundary= | Custom boundary string |

## Examples

### Example 1: Basic Usage

```python
from requests_toolbelt.multipart.encoder import MultipartEncoder
m = MultipartEncoder(fields={'file': ('test.txt', b'content', 'text/plain')})
print(m.content_type)
```

### Example 2: Advanced Usage

With file open:

```python
with open('file.html', 'rb') as f:
    m = MultipartEncoder(fields={'file': ('poc.png', f, 'text/html')})
    # Use in requests.post(data=m)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Logs of multipart POSTs with mismatched MIME types
- Python imports of MultipartEncoder in scripts

## Related Procedures


## Related Tools

- [[tools/requests]]
- [[tools/postman]]

## References

- Official documentation: https://requests-toolbelt.readthedocs.io
- Related resources: HTTP file upload testing
