---
id: tool-uuid-002
url: 'https://flask.palletsprojects.com/'
tags:
  - web-framework
  - testing
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.495Z'
validated: true
submitted: true
---
# Flask

**Status**: Unverified

## Overview

Flask is a lightweight Python web framework for building simple HTTP servers, ideal for PoC environments in security testing.

## Description

Used here to quickly set up a listener server for verifying SSRF requests, with minimal routing to respond to root paths.

## Features

- Feature 1: Simple routing for endpoints
- Feature 2: Threaded operation for handling requests
- Feature 3: Built-in development server

## Installation

### Requirements

- Python 3.x

### Install Commands

```bash
pip install flask
```

## Basic Usage

```bash
flask --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `host` | Bind address |
| `port` | Listening port |
| `threaded` | Enable threading |

## Examples

### Example 1: Basic Usage

```python
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello'
app.run()
```

### Example 2: Advanced Usage

```python
app.run(host='0.0.0.0', port=80, threaded=True)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes with flask module loaded
- Local port 80 bindings

## Related Procedures


## Related Tools

- [[tools/Django]]

## References

- Official documentation: https://flask.palletsprojects.com/
