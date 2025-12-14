---
url: 'https://www.npmjs.com/package/blamer'
tags:
  - vulnerable-module
  - vcs
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.772Z'
id: 2ddc536c-ab7e-4677-9852-6482ab110850
validated: true
submitted: true
---
# blamer

**Status**: Unverified

## Overview

Blamer is a Node.js module for retrieving code author information from version control systems like Git and Subversion; version 0.1.13 is vulnerable to RCE via command injection.

## Description

Blamer executes VCS commands to fetch blame data but insecurely interpolates filenames into shell strings, allowing injection. Used in security testing to demonstrate supply chain risks in Node.js dependencies.

## Features

- Feature 1: Support for Git and Subversion
- Feature 2: Blame by file or hash methods
- Feature 3: Callback-based asynchronous operations

## Installation

### Requirements

- Node.js >= 0.10

### Install Commands

```bash
npm i blamer@0.1.13
```

## Basic Usage

```bash
# In JavaScript
const Blamer = require('blamer');
const blamer = new Blamer('git');
blamer.blameByFile('file.js', callback);
```

### Common Options

| Option | Description |
|--------|-------------|
| VCS type | 'git' or 'svn' |

## Examples

### Example 1: Basic Usage

```javascript
blamer.blameByFile('safe.js', (err, blame) => { console.log(blame); });
```

### Example 2: Advanced Usage (Vulnerable)

```javascript
blamer.blameByFile('test; touch HACKED;#', (err, blame) => {});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of blamer@0.1.13 in package.json or node_modules
- Logs of Git blame commands with unsanitized inputs

## Related Procedures


## Related Tools

- [[tools/node]]

## References

- npm page: https://www.npmjs.com/package/blamer
- HackerOne report: https://hackerone.com/reports/772448
