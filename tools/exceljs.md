---
url: 'https://www.npmjs.com/package/exceljs'
tags:
  - xlsx-parser
  - vulnerable
  - xss
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.797Z'
configuration: 'Version 1.4.6 (reproduced in 1.5.1, patched in 1.6.0 with .html property)'
id: bcb66ef9-6e4d-4742-aa1b-a6b67e61747a
validated: true
submitted: true
---
# exceljs

**Status**: Unverified

## Overview

exceljs is a Node.js module for reading, manipulating, and writing Excel XLSX files. It's vulnerable to stored XSS in versions before 1.6.0 due to unescaped cell values when rendered in HTML.

## Description

The library parses XLSX without validating content, allowing HTML/JS in cells to be inserted directly (e.g., via getCell().value). Used in web apps for spreadsheet display, it enables attacks where malicious files execute code on viewing.

## Features

- Feature 1: Read/write XLSX with cell styling and formulas
- Feature 2: Worksheet iteration and data extraction
- Feature 3: Streaming for large files (vulnerable versions lack escaping)

## Installation

### Requirements

- Node.js 8+

### Install Commands

```bash
npm i exceljs@1.4.6
```

## Basic Usage

```bash
const ExcelJS = require('exceljs');
const wb = new ExcelJS.Workbook();
wb.xlsx.readFile('file.xlsx');
```

### Common Options

| Option | Description |
|--------|-------------|
| `getCell(address)` | Retrieve cell value (unescaped in vuln versions) |
| `eachRow(callback)` | Iterate rows for HTML building |

## Examples

### Example 1: Basic Usage

```bash
# In script: Parse and log cell
worksheet.getCell('A1').value
```

### Example 2: Advanced Usage

```javascript
worksheet.eachRow((row) => {
  row.eachCell((cell) => console.log(cell.value));
});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Dependency scans showing exceljs <1.6.0
- Detection method 2: Code reviews for direct cell.value in HTML templates

## Related Procedures


## Related Tools

- [[tools/Node-js]]
- [[tools/LibreOffice]]

## References

- Official documentation: https://github.com/exceljs/exceljs
- Vulnerability report: https://hackerone.com/reports/356809
