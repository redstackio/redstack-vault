---
data: cat README.md
tags:
  - inspection
type: command
output: Cached HTML content in README.md
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.357Z'
id: 682cf518-c2b9-49d2-bbdc-7d6fd15ab220
verified: false
validated: true
submitted: true
---
# cat-readme-file

## Command

```bash
cat README.md
```

## Description

Displays overwritten README.md to confirm exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| README.md | File path | Yes |

## Examples

### Basic Usage

```bash
cat README.md
```

## Expected Output

Book name in HTML.

## Related

- [[commands/curl-traversal-overwrite]]
