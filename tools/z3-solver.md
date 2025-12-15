---
url: 'https://github.com/Z3Prover/z3'
tags:
  - solver
  - smt
  - lcg
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.194Z'
id: e93d4af8-9286-4b5b-8d3e-df1885dd3e78
validated: true
submitted: true
---
# z3-solver

**Status**: Unverified

## Overview

Z3 SMT solver library for Python, used to solve constraints and reverse-engineer the state of V8's LCG from observed Math.random() boundary values.

## Description

Z3 proves theorems and solves equations; in the exploit, it models the LCG parameters (multiplier, increment, modulus) to predict future random outputs from a few samples extracted from multipart boundaries.

## Features

- Feature 1: Satisfiability modulo theories
- Feature 2: Constraint solving
- Feature 3: Optimization support

## Installation

### Requirements

- Python 3

### Install Commands

```bash
pip3 install z3-solver
```

## Basic Usage

```bash
python -c "from z3 import *; print(Solver())")
```

### Common Options

N/A for library; used programmatically.

## Examples

### Example 1: Basic Usage

```python
from z3 import *
s = Solver()
# Add constraints for LCG
```

### Example 2: Advanced Usage

Integrated in predict.py for LCG state solving.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Develop Capabilities]] Develop Capabilities

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- z3 process or Python imports
- Unusual constraint-solving computations

## Related Procedures

- [[procedures/Exploit-Predictable-Randomness-for-Request-Tampering]]

## Related Tools

- [[tools/predict.py]]

## References

- Official documentation: https://github.com/Z3Prover/z3
