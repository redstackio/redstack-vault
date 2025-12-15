---
data: 'dir /ad "C:\Program Files"'
tags:
  - directory
  - list
type: command
output: Directory listing
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.141Z'
id: a463545e-6562-416d-9123-e5783deeeb8e
verified: false
validated: true
submitted: true
---
# dir-path-segments

## Command

```cmd
dir /ad "C:\Program Files"
```

## Description

Lists directories in a path segment to assess writability for hijack exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ad | Directories only | Yes |

## Examples

### Basic Usage

```cmd
dir /ad "C:\Program Files"
```

## Expected Output

Directory contents, indicating potential hijack points.

## Related

- [[Related Procedure: Identify-Unquoted-Path-in-Service-ImagePath]]
