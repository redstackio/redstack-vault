---
data: 'curl "http://target:3000/file?path=test.txt"'
tags:
  - testing
type: command
output: null
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.783Z'
id: 7f9e1f42-5d81-4c49-bd39-0cbbd4377e4a
verified: false
validated: true
submitted: true
---
# curl-basic-test

## Command

```bash
curl "http://target:3000/file?path=test.txt"
```

## Description

Tests a basic file request to a Node.js server to verify path handling before attempting traversal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Endpoint with benign path | Yes |

## Examples

### Basic Usage

```bash
curl "http://localhost:3000/file?path=test.txt"
```

## Expected Output

Returns contents of intended_dir/test.txt or 404.

## Related

- [[Related Procedure: Setup-Vulnerable-Node.js-Path-Join-App]]
