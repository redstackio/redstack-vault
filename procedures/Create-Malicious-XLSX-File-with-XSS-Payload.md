---
tags:
  - xss
  - payload-creation
  - xlsx
type: procedure
tools:
  - '[[tools/LibreOffice]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.851Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b36643c3-743b-46c0-bc46-c7e3428ea8d2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-XLSX-File-with-XSS-Payload

## Summary

This procedure crafts a malicious XLSX file using LibreOffice by embedding an HTML/JavaScript payload in a cell, which will later be parsed without escaping by exceljs, leading to stored XSS execution.

## Description

Attackers can upload or share XLSX files containing payloads like `<script>alert('xss!')</script>` in cells. When processed by vulnerable exceljs and rendered in HTML, the script executes in the viewer's browser context. This targets web applications that display spreadsheet data. Prerequisites: LibreOffice installed. Expected outcome: A valid XLSX file with hidden malicious content that appears benign in office tools but triggers XSS in web views.

## Requirements

1. LibreOffice Calc (version 5.1.6.2 or compatible)
2. Basic knowledge of spreadsheet editing
3. File system access to save XLSX files

## Defense

Defensive measures and detection strategies:

- Sanitize all file uploads: Scan for embedded scripts in office documents using tools like ClamAV or custom parsers
- Use secure parsing libraries that escape HTML (e.g., updated exceljs with .html property)
- Implement content security policies (CSP) to block inline scripts on web pages displaying parsed content

## Objectives

1. Embed XSS payload in XLSX cell without detection in office viewers
2. Ensure payload survives XLSX format and parsing
3. Prepare file for upload/exploitation in vulnerable web app

## Instructions

### Step 1: Create and Populate Spreadsheet

**Context**: Open LibreOffice and insert the payload along with benign data to mimic legitimate files.

**Instructions**: Launch LibreOffice Calc, create a new spreadsheet. In cell A1, type `<script>alert(`xss!`)</script>`. In A2, enter 'test'; B1: 'another'; A3: '1'; B3: '2'; C3: '3'. Save as testsheet.xlsx.

> The payload will display as text in LibreOffice but execute when unescaped in HTML. Expected output: File saved successfully, payload intact upon reopening.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/LibreOffice]]

## Tags

- xss
- payload-creation
- xlsx
