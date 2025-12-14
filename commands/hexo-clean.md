---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
name: hexo-clean
type: command
executor: bash
data: hexo clean
output: Generated files in public directory and db.json cache cleared
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.020Z'
platforms:
  - Node.js
tags:
  - hexo
  - cleanup
verified: false
validated: true
submitted: true
---

# hexo-clean

## Command

```bash
hexo clean
```

## Description

Removes all generated files and cache from the Hexo project to ensure a clean rebuild, preventing artifacts from prior builds during vulnerability testing like XSS persistence checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters | N/A |

## Examples

### Basic Usage

```bash
hexo clean
```

### Advanced Usage

Not applicable; single-purpose command.

## Expected Output

Console message: Database has been cleaned. Public folder and .cache/db.json removed.

## Related

- [[commands/hexo-generate]]
- [[procedures/Save-Post-Rebuild-Site-and-Verify-Persistent-XSS]]
