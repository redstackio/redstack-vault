---
url: 'https://github.com/PwnFunction/v8-randomness-predictor/tree/main'
tags:
  - prediction
  - v8
  - random
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.191Z'
id: 143ba4a9-af04-4ddd-91a7-ce3a8f620a75
validated: true
submitted: true
---
# predict.py

**Status**: Unverified

## Overview

Modified Python script for predicting V8 Math.random() values using Z3, integrated into the Node.js exploit workflow to forecast multipart boundaries.

## Description

Based on a GitHub repo, this script analyzes observed random floats from boundaries, sets up Z3 constraints for the LCG (state = (state * 16807 + 0) % 2^48), and solves for the internal state to generate future values, enabling precise tampering.

## Features

- Feature 1: LCG state recovery
- Feature 2: Random value prediction
- Feature 3: Integration with Node.js via child_process

## Installation

### Requirements

- z3-solver
- Python 3

### Install Commands

```bash
# Clone and modify
git clone https://github.com/PwnFunction/v8-randomness-predictor
# Integrate into exp.js
```

## Basic Usage

```bash
python predict.py
```

### Common Options

N/A; script-based.

## Examples

### Example 1: Basic Usage

```python
# Input observed values, output predicted
```

### Example 2: Advanced Usage

Called from exp.js with boundary samples.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Python scripts with Z3 imports
- Boundary value logging

## Related Procedures

- [[procedures/Exploit-Predictable-Randomness-for-Request-Tampering]]

## Related Tools

- [[tools/z3-solver]]

## References

- GitHub: https://github.com/PwnFunction/v8-randomness-predictor
