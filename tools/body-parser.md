---
url: null
tags:
  - middleware
type: tool
platforms:
  - Web
description: Middleware for Express to parse request bodies.
id: 7448d535-54a2-4027-b7bc-8d329195fa3b
created_at: '2025-12-13T09:01:22.050Z'
updated_at: '2025-12-13T09:01:22.050Z'
verified: false
validated: true
submitted: true
---
# body-parser

**Status**: Unverified

## Overview

body-parser is an Express middleware that parses JSON, URL-encoded, and other request bodies.

## Description

Used in app.use(bodyParser()) to handle POST requests in the vulnerable setup.

## Features

- Parse JSON
- Parse URL-encoded
- Handle multipart

## Installation

### Requirements

- Express

### Install Commands

```bash
npm install body-parser
```

## Basic Usage

```javascript
app.use(bodyParser.json())
```

### Common Options

| Option | Description |
|--------|-------------|
| `json` | Parse JSON bodies |

## Examples

### Example 1: Basic Usage

```javascript
app.use(bodyParser())
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques



### Tactics



## Detection

Indicators and methods for detecting this tool's usage:

- Check Express configs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Express]]

## References

- body-parser docs
