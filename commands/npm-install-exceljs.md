---
data: npm i exceljs
tags:
  - installation
  - npm
  - dependency
type: command
output: Installation logs and confirmation of exceljs version 1.4.6
executor: bash
platforms:
  - Node.js
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.820Z'
id: 526b4b7d-ef7e-4dd0-bd10-27d3648784c4
verified: false
validated: true
submitted: true
---
# npm-install-exceljs

## Command

```bash
npm i exceljs
```

## Description

Installs the exceljs package from the npm registry, specifically version 1.4.6 which is vulnerable to stored XSS when parsing unescaped cell values from XLSX files. Use this in Node.js projects to add spreadsheet manipulation capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install flag (short for --save) | Yes |
| `exceljs` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i exceljs
```

### Advanced Usage

```bash
npm i exceljs@1.4.6 --save-dev
```

## Expected Output

npm WARN deprecated ... (warnings if any)
+ exceljs@1.4.6
added 1 package in X ms

## Related

- [[Related Procedure|procedures/Install-Vulnerable-exceljs-Module]]
