---
data: 'echo -n "testtrailer: " > 8190_EXCLUDE_COLON_SP_CR_LF.txt'
tags:
  - payload
type: command
executor: bash
platforms:
  - Linux
id: dc4ef019-07fa-4999-a0a5-e6c6d3fc589c
created_at: '2025-12-13T09:01:22.344Z'
updated_at: '2025-12-13T09:01:22.344Z'
verified: false
validated: true
submitted: true
---
# Echo Create File

## Command

```bash
echo -n "testtrailer: " > 8190_EXCLUDE_COLON_SP_CR_LF.txt
```

## Description

Writes 'testtrailer: ' to a file without adding a newline.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Do not output trailing newline | Yes |

## Examples

### Basic Usage

```bash
echo -n "testtrailer: " > 8190_EXCLUDE_COLON_SP_CR_LF.txt
```

## Expected Output

File created with specified content.

## Related

- [[procedures/Craft-Oversized-Trailer-Payload]]
