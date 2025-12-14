---
url: 'https://requests-toolbelt.readthedocs.io/'
tags:
  - multipart
  - library
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.379Z'
id: 9fb2959b-d121-4b46-ab4f-3d2bb81659f1
validated: true
submitted: true
---
# requests_toolbelt

**Status**: Unverified

## Overview

Requests Toolbelt extends the requests library with utilities like MultipartEncoder for handling file uploads in multipart form data.

## Description

Used in this attack to encode the HTML file for upload, ensuring proper content-type and boundaries.

## Features

- Feature 1: Multipart encoding
- Feature 2: Media type utilities
- Feature 3: Structure streaming

## Installation

### Requirements

- requests library

### Install Commands

```bash
pip install requests-toolbelt
```

## Basic Usage

```bash
python -c "from requests_toolbelt.multipart.encoder import MultipartEncoder; print('Imported')"
```

### Common Options

N/A

## Examples

### Example 1: Basic Usage

```python
from requests_toolbelt.multipart.encoder import MultipartEncoder
m = MultipartEncoder(fields={'file': (filename, file, 'text/html')})
```

### Example 2: Advanced Usage

Combined with requests.post(data=m)

## MITRE ATT&CK Mapping

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

- Look for toolbelt imports in Python scripts
- Multipart request patterns in traffic

## Related Procedures


## Related Tools

- [[tools/requests]]

## References

- https://requests-toolbelt.readthedocs.io/
