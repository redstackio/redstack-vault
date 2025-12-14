---
data: hexo generate
tags:
  - generate
  - hexo
type: command
output: Static HTML files created in public folder
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.695Z'
id: badf0aaf-28e4-4fb7-be5d-3964d00f45c6
verified: false
validated: true
submitted: true
---
# hexo-generate

## Command

```bash
hexo generate
```

## Description

Generates static files from the blog's source Markdown and templates into the public directory, incorporating any new or updated posts like those with XSS payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w` | Watch mode for continuous generation | No |

## Examples

### Basic Usage

```bash
hexo generate
```

### Advanced Usage

```bash
hexo generate -w
```

## Expected Output

INFO  Generated files in ./public

## Related

- [[commands/hexo-clean]]
- [[procedures/Save-and-Publish-Post-to-Trigger-Stored-XSS]]
