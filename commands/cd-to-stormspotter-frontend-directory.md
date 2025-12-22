---
id: 99a8d730-e8f0-4f4f-ba1e-45d78a7153a2
type: command
executor: bash
data: cd $_FRONTEND_PATH
output: null
created_at: '2023-04-06T03:56:14.585395+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - setup
  - directory
verified: true
validated: true
---

# cd-to-stormspotter-frontend-directory

## Command

```bash
cd $_FRONTEND_PATH
```

## Description

Navigates to the StormSpotter frontend directory for serving the UI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FRONTEND_PATH | Path to frontend/dist/spa | Yes |

## Examples

### Basic Usage

```bash
cd C:\Tools\stormspotter\frontend\dist\spa\
```

## Expected Output

Prompt changes to the directory.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azure-StormSpotter]]
