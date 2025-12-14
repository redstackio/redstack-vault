---
id: uuid-amxx
url: 'https://www.amxmodx.org/'
tags:
  - compiler
  - pawn-language
  - plugin-build
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.423Z'
validated: true
submitted: true
---
# AMXX-Compiler

**Status**: Unverified

## Overview

The AMXX Compiler (amxxpc) is a tool for compiling Pawn (.sma) scripts into AMX Mod X plugins (.amxx), essential for building custom server-side code in Counter-Strike exploits.

## Description

It translates high-level Pawn scripts into bytecode executable by the AMX runtime, supporting features like net message manipulation for vulnerability exploitation. Used in security testing to create PoC plugins that trigger client-side bugs like array underflows.

## Features

- Feature 1: Syntax checking and optimization
- Feature 2: Include support for AMXX APIs
- Feature 3: Error reporting for debugging

## Installation

### Requirements

- AMX Mod X installed

### Install Commands

```bash
# Included in AMX Mod X; use amxxpc.exe
```

## Basic Usage

```bash
amxxpc poc_calc_pop.sma
```

### Common Options

| Option | Description |
|--------|-------------|
| -i<dir> | Include path |
| -o<output> | Output file name |

## Examples

### Example 1: Basic Usage

```bash
amxxpc script.sma
```

### Example 2: Advanced Usage

```bash
amxxpc -i include/ -o poc.amxx poc.sma
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of .amxx files with suspicious names
- Compilation artifacts in temp directories
- Pawn source code on server

## Related Procedures


## Related Tools

- [[tools/AMX-Mod-X]]

## References

- AMX Mod X docs
