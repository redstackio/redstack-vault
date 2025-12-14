---
url: 'https://prettier.io/playground/'
tags:
  - code-formatting
  - analysis
type: tool
platforms:
  - Web
  - Linux
  - Windows
  - macOS
description: >-
  An opinionated code formatter for JavaScript and other languages, used here to
  beautify minified JS from the Polaris demo for vulnerability analysis.
id: 5ed2864a-fae7-4051-a8d2-0d888a6ee8b2
created_at: '2025-12-14T03:16:02.493Z'
updated_at: '2025-12-14T03:16:02.493Z'
verified: false
validated: true
submitted: true
---
# prettier

**Status**: Unverified

## Overview

Prettier is a code formatter that enforces consistent styling for JavaScript, JSX, and other formats. In security testing, it's commonly used to deobfuscate or beautify minified production JS files, like the Polaris demo's script, to identify vulnerabilities such as unsafe postMessage handling.

## Description

Prettier automatically formats code based on its rules, making it easier to read and analyze complex or minified scripts. For this XSS exploit, paste the contents of demo-3801177f8c9e2fc96d7fbd9b73f76b32a8aa35fee26bee5aa0964e71955cf960.js into the online playground to reveal the handleMessage function's lack of validation.

## Features

- Feature 1: Automatic formatting of JS/JSX with one click
- Feature 2: Online playground for quick analysis without installation
- Feature 3: Supports embedding and parsing of React components

## Installation

### Requirements

- Node.js (for CLI version)

### Install Commands

```bash
# Global install
npm install -g prettier
```

## Basic Usage

```bash
prettier --write file.js
```

### Common Options

| Option | Description |
|--------|-------------|
| `--write` | Overwrite file with formatted version |
| `--parser babel` | Parse JSX/JS files |
| `--check` | Check if code is formatted |

## Examples

### Example 1: Basic Usage

```bash
prettier --parser babel demo.js
```

### Example 2: Advanced Usage

```bash
prettier --write --single-quote --trailing-comma es5 demo.js
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript (for analysis)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network requests to prettier.io/playground
- Installed npm packages including prettier

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://prettier.io/docs/en/
- Related resources: JS beautifiers like js-beautify
