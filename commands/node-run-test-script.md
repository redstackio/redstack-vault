---
data: node test.js
tags:
  - execution
  - test
type: command
output: \\\\fileserver\\public\\private\\passwords.txt
executor: bash
platforms:
  - Windows
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.239Z'
id: 49a5837f-ecdc-4e6c-86dc-46aaefd13f8c
verified: false
validated: true
submitted: true
---
# node-run-test-script

## Command

```bash
node test.js
```

## Description

Executes a Node.js script file to test the UNC path traversal vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| test.js | Path to the JavaScript test file | Yes |

## Examples

### Basic Usage

```bash
node test.js
```

### Advanced Usage

```bash
node --inspect test.js
```

## Expected Output

Traversed path in console, e.g., escaped to private directory.

## Related

- [[commands/node-path-join-unc-test]]
