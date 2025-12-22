---
tags:
  - xss
  - node-js
  - parsing
type: procedure
tools:
  - '[[tools/Node-js]]'
  - '[[tools/exceljs]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.845Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 863d3c03-3549-4541-9abd-83b1e4e36828
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Develop-Node-js-App-to-Parse-and-Serve-XLSX-as-HTML

## Summary

This procedure creates a Node.js application that uses the vulnerable exceljs module to read an XLSX file, insert cell values directly into an HTML table without escaping, and serve it over HTTP, enabling XSS execution.

## Description

The app simulates a web application processing uploaded spreadsheets. It reads the XLSX worksheet, iterates over cells using template literals to build HTML, and hosts it on port 8080. Due to no validation in exceljs.getCell().value, payloads are rendered executable. Prerequisites: exceljs installed, testsheet.xlsx present. Expected outcome: A running server that outputs vulnerable HTML.

## Requirements

1. Node.js (version 8.11.1) and exceljs (1.4.6) installed
2. Malicious XLSX file in the project directory
3. Basic JavaScript knowledge for app development

## Defense

Defensive measures and detection strategies:

- Escape all user-controlled data before HTML insertion (e.g., use libraries like escape-html)
- Validate and sanitize XLSX content during parsing; reject files with script tags
- Audit code for direct template literal usage with untrusted inputs; implement OWASP guidelines for XSS prevention

## Objectives

1. Parse XLSX and generate unescaped HTML table
2. Expose the content via a local HTTP server
3. Demonstrate vulnerability in spreadsheet-displaying web apps

## Instructions

### Step 1: Write the Application Script

**Context**: Develop app.js to load, parse, and serve the XLSX content.

**Instructions**: Create app.js with code to require exceljs and http, read testsheet.xlsx, build HTML table using ${cell.value}, and start server on 8080.

```javascript
const ExcelJS = require('exceljs');
const http = require('http');

const workbook = new ExcelJS.Workbook();
(async () => {
  await workbook.xlsx.readFile('testsheet.xlsx');
  const worksheet = workbook.getWorksheet(1);
  let html = '<table border="1">';
  worksheet.eachRow((row, rowNumber) => {
    html += '<tr>';
    row.eachCell({ includeEmpty: true }, (cell) => {
      html += `<td>${cell.value}</td>`;
    });
    html += '</tr>';
  });
  html += '</table>';

  http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(html);
  }).listen(8080);
  console.log('server is listening on 8080');
})();
```

> Expected output: Script runs without errors; HTML includes unescaped payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Node-js]]
- [[tools/exceljs]]

## Tags

- xss
- node-js
- parsing
