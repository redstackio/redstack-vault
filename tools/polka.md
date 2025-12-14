---
id: tool-008
url: 'https://github.com/lukeed/polka'
tags:
  - web-server
type: tool
verified: false
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.435Z'
validated: true
submitted: true
---
---

# polka

**Status**: Unverified

## Overview

Polka is a lightweight web server used in Sapper production mode, applying extra decodeURIComponent that requires double encoding for path traversal exploits.

## Description

In Sapper, Polka handles requests, introducing an additional decoding layer that alters exploitation from single to double encoding for '../' sequences.

## Features

- Feature 1: Fast HTTP server
- Feature 2: Middleware support
- Feature 3: Minimal footprint

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm i polka
```

## Basic Usage

```bash
node server.js  # With Polka imported
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Config via code |

## Examples

### Example 1: Basic Usage

```bash
# In Sapper build
node __sapper__build
```

### Example 2: Advanced Usage

```bash
# Custom Polka server
const polka = require('polka')();
polka.listen(3000);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Polka headers in responses
- Decoding anomalies in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: express]]

## References

- Official documentation: https://github.com/lukeed/polka

---
