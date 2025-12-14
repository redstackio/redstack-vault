---
data: hexo clean
tags:
  - cleanup
  - hexo
type: command
output: Generated files in public folder deleted
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.698Z'
id: c607f208-9aaf-4125-a53a-db0e177b9827
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

Removes all generated files and cache from the public directory to ensure a clean rebuild, preventing stale content issues after post updates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
hexo clean
```

### Advanced Usage

No additional options typically needed.

## Expected Output

INFO  Cleaned up.
Files in ./public deleted.

## Related

- [[commands/hexo-generate]]
- [[procedures/Save-and-Publish-Post-to-Trigger-Stored-XSS]]
