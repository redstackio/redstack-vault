---
id: tool-curling-001
name: curling
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.387Z'
platforms:
  - Node.js
tags:
  - http-client
  - vulnerable
url: 'https://www.npmjs.com/package/curling'
validated: true
submitted: true
---

# curling

**Status**: Unverified

## Overview

curling is a Node.js module that wraps the curl binary for HTTP requests. Version 1.1.0 is vulnerable to command injection due to poor input sanitization, allowing RCE in applications using it.

## Description

The module's run() function executes curl commands but uses a weak regex to block special characters, failing against payloads like file:// URLs and -o flags. In offensive security, it's exploited to demonstrate supply chain risks in Node.js apps, enabling file read/write on the host.

## Features

- Feature 1: Asynchronous curl execution with callbacks
- Feature 2: Support for various curl options
- Feature 3: Integration with Node.js event loop

## Installation

### Requirements

- Node.js and npm
- curl binary on host

### Install Commands

```bash
npm i curling
```

## Basic Usage

```javascript
const curling = require('curling'); curling.run('http://example.com', callback);
```

### Common Options

| Option | Description |
|--------|-------------|
| `run(command, callback)` | Execute curl with command string |
| `callback(data, payload)` | Handle response |

## Examples

### Example 1: Basic Usage

```javascript
curling.run('http://example.com', function(d, p){ console.log(p); });
```

### Example 2: Advanced Usage (Exploitation)

```javascript
curling.run('file:///etc/passwd -o ./file.txt', function(d, p){ console.log(p); });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]] Unix Shell
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous curl processes spawned from Node.js
- File changes from unexpected overwrites
- Regex bypass attempts in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1|tools/curl]]
- [[Related Tool 2|tools/Node.js]]

## References

- Official documentation: https://www.npmjs.com/package/curling
- Related resources: HackerOne report #973386
