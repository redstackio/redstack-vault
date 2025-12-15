---
data: cat public/books/1.html
tags:
  - inspection
type: command
output: Escaped HTML content with payload
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.391Z'
id: 72f577af-02fd-4988-bb2d-90200987caab
verified: false
validated: true
submitted: true
---
# cat-cache-file

## Command

```bash
cat public/books/1.html
```

## Description

Displays the cached HTML file contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| public/books/1.html | File path | Yes |

## Examples

### Basic Usage

```bash
cat public/books/1.html
```

## Expected Output

HTML with escaped ERB.

## Related

- [[commands/ls-public-dir]]
