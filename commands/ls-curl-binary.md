---
id: cmd-017
data: ls -la src/curl
tags:
  - verify
  - file
type: command
output: File listing with timestamp
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.002Z'
verified: false
validated: true
submitted: true
---
# ls-curl-binary

## Command

```bash
ls -la src/curl
```

## Description

Lists the curl executable details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-la` | Long all | Yes |

## Examples

### Basic Usage

```bash
ls -la src/curl
```

## Expected Output

-rwxr-xr-x ... src/curl

## Related

- [[commands/curl-version-check]]
