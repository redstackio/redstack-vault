---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
name: hexo-generate
type: command
executor: bash
data: hexo generate
output: >-
  Static HTML files created in the public folder, including the affected post
  with embedded XSS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.017Z'
platforms:
  - Node.js
tags:
  - hexo
  - build
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

Generates static files from Hexo source into the public directory, processing posts and themes to create deployable HTML. Essential for incorporating stored XSS payloads into the final site output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o, --output` | Specify output directory | No |

## Examples

### Basic Usage

```bash
hexo generate
```

### Advanced Usage

```bash
hexo generate --output ./dist
```

## Expected Output

Logs: INFO X posts generated, files written to public/ with unescaped XSS in post HTML.

## Related

- [[commands/hexo-clean]]
- [[procedures/Save-Post-Rebuild-Site-and-Verify-Persistent-XSS]]
