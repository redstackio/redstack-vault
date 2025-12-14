---
id: tool-python
url: 'https://www.python.org/'
tags:
  - scripting
  - automation
  - poc
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.413Z'
validated: true
submitted: true
---
# Python

**Status**: Unverified

## Overview

Python is a high-level programming language used for scripting, automation, and developing proof-of-concept exploits in security testing, such as HTTP request automation for API vulnerabilities.

## Description

In this context, Python runs a custom poc.py script leveraging the requests library to interact with the Flink API, sending crafted parameters for RCE. It's ideal for rapid prototyping of web exploits due to its simplicity and extensive libraries.

## Features

- Feature 1: Rich standard library including http.client and requests for API calls
- Feature 2: Cross-platform scripting for PoC development
- Feature 3: Easy integration with gadgets like JavaScript loaders

## Installation

### Requirements

- OS with package manager

### Install Commands

```bash
# On Linux
apt install python3 python3-pip
pip3 install requests

# On macOS
brew install python
```

## Basic Usage

```bash
python3 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-V` | Version info |

## Examples

### Example 1: Basic Usage

```bash
python3 script.py
```
(Run a PoC script.)

### Example 2: Advanced Usage

```bash
python3 -m requests.get https://target/api
```
(Direct module use for HTTP.)

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for python3 processes spawning HTTP connections to internal APIs
- Log anomalous script executions with requests library
- Behavioral analysis for PoC-like file runs

## Related Procedures


## Related Tools

- [[Related Tool: curl]]
- [[Related Tool: requests library]]

## References

- Official documentation: https://www.python.org/
- Related resources: PyPI requests
