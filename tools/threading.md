---
url: 'https://docs.python.org/3/library/threading.html'
tags:
  - concurrency
  - python-module
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.963Z'
id: faf1035f-8b4a-4d53-940c-4c8f9410b9b0
validated: true
submitted: true
---
# threading

**Status**: Unverified

## Overview

threading is a Python module for creating and managing threads, used to run the HTTPS server in the background during the PoC execution.

## Description

Creates a daemon thread to serve requests asynchronously, allowing the main script to proceed with attack steps.

## Features

- Feature 1: Thread creation
- Feature 2: Daemon threads
- Feature 3: Join and synchronization

## Installation

### Requirements

- Python 3 standard library

### Install Commands

```bash
# Built-in
```

## Basic Usage

```python
import threading
thread = threading.Thread(target=func)
```

### Common Options

| Option | Description |
|--------|-------------|
| `daemon=True` | Background thread |
| `start()` | Begin execution |

## Examples

### Example 1: Basic Usage

```python
thread = threading.Thread(target=httpd.serve_forever)
thread.start()
```

### Example 2: Advanced Usage

```python
thread = threading.Thread(target=func, daemon=True)
thread.join(timeout=5)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Multiple Python threads in process lists

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/python3]]

## References

- Official documentation: https://docs.python.org/3/library/threading.html
