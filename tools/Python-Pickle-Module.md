---
url: 'https://docs.python.org/3/library/pickle.html'
tags:
  - serialization
  - deserialization
  - python
type: tool
platforms:
  - Python
  - Web
description: >-
  Python standard library module for object serialization/deserialization,
  insecurely used in Liberapay for notifications leading to RCE.
id: 162e771b-c70c-4ab7-8a26-2046c7ac61f7
created_at: '2025-12-14T03:46:19.788Z'
updated_at: '2025-12-14T03:46:19.788Z'
verified: false
validated: true
submitted: true
---
# Python-Pickle-Module

**Status**: Unverified

## Overview

The pickle module serializes and deserializes Python objects to/from byte streams, commonly used for data persistence but vulnerable to RCE when untrusted data is deserialized, as in Liberapay's notification contexts.

## Description

Pickle allows reconstruction of arbitrary objects, including code execution gadgets. In this vulnerability, liberapay/utils/__init__.py uses pickle.loads without validation, enabling attacks via crafted payloads injected into database fields.

## Features

- Feature 1: Object serialization with pickle.dumps
- Feature 2: Deserialization with pickle.loads, supporting complex types like functions
- Feature 3: Binary protocol for efficient storage

## Installation

### Requirements

- Python 3.x

### Install Commands

```bash
# Built-in, no installation needed
python -c "import pickle"
```

## Basic Usage

```bash
python -c "import pickle; data = pickle.dumps('test'); print(pickle.loads(data))"
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Pickle is a module, used via import |

## Examples

### Example 1: Basic Usage

```python
import pickle
payload = pickle.dumps(os.system)
print(pickle.loads(payload))
```

### Example 2: Advanced Usage

Craft malicious payload:

```python
import pickle, os
malicious = pickle.dumps((os.system, ('sleep 500000',)))
# Hex encode for SQL: hexlify(malicious)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for pickle.loads calls on untrusted input
- Log deserialization errors or unexpected code execution
- Scan for hex-encoded payloads in database fields

## Related Procedures

- [[procedures/Inject-Malicious-Pickle-Payload-via-SQL-Injection]]
- [[procedures/Trigger-Deserialization-by-Viewing-Notifications]]

## Related Tools

- [[CBOR Library]]

## References

- Official documentation: https://docs.python.org/3/library/pickle.html
- HackerOne Report: https://hackerone.com/reports/361341
