---
data: node portScanner.js test1 BJe2Pi2AgB
tags:
  - ssrf
  - scan
type: command
executor: bash
platforms:
  - Linux
  - Node.js
id: 8057a68b-ed37-4449-8df8-ae270c39065b
created_at: '2025-12-14T17:23:24.936Z'
updated_at: '2025-12-14T17:23:24.936Z'
verified: false
validated: true
submitted: true
---
# node-portscanner-jsreport

## Command

```bash
node portScanner.js test1 BJe2Pi2AgB
```

## Description

Executes a custom Node.js script to perform SSRF-based port scanning on the jsreport instance, discovering the script-manager port by analyzing rendering errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `test1` | Template name for API requests | Yes |
| `BJe2Pi2AgB` | Template shortid | Yes |

## Examples

### Basic Usage

```bash
node portScanner.js test1 BJe2Pi2AgB
```

### Advanced Usage

Modify script for custom ranges:

```bash
node portScanner.js --start 1024 --end 2000 test1 ID
```

## Expected Output

Console log: "Discovered script-manager port: 12354" based on error patterns.

## Related

- [[procedures/discover-script-manager-port-via-ssrf]]
