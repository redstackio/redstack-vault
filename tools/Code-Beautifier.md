---
url: ''
tags:
  - code-analysis
type: tool
platforms:
  - Web
description: Tool for beautifying minified code to aid in analysis.
id: 03e749f3-c2af-45ec-88cf-985906ef58e9
created_at: '2025-12-13T23:56:03.982Z'
updated_at: '2025-12-13T23:56:03.982Z'
verified: false
validated: true
submitted: true
---
# Code Beautifier

**Status**: Unverified

## Overview

Code beautifier tools reformat minified JavaScript or other code for readability, essential for vulnerability hunting in SDKs and scripts.

## Description

These tools take compressed code and add indentation, spacing, and line breaks to make it analyzable. Used in security research to find sinks like navigation functions.

## Features

- Indentation and formatting
- Syntax highlighting
- Online or offline options

## Installation

### Requirements

- Web access or local install

### Install Commands

```bash
# Use online tools or npm install js-beautify
```

## Basic Usage

```bash
js-beautify input.js > output.js
```

### Common Options

| Option | Description |
|--------|-------------|
| -o | Output file |
| --type | Code type |

## Examples

### Example 1: Basic Usage

```bash
js-beautify app.js
```

### Example 2: Advanced Usage

```bash
js-beautify --indent-size 2 app.js
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[User Execution]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- File access patterns to minified JS
- Beautified code in temp files

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Browser-DevTools]]

## References

- js-beautify documentation
