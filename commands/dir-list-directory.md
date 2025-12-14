---
data: dir
tags:
  - verification
  - windows
type: command
output: null
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.640Z'
id: ec85d9a4-312c-459e-af8c-8683d3e4870f
verified: false
validated: true
submitted: true
---
# dir-list-directory

## Command

```bash
dir
```

## Description

Lists files and directories in the current working directory on Windows, used to verify state before and after exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Basic listing | No |

## Examples

### Basic Usage

```bash
dir
```

### Advanced Usage

```bash
dir /b
```

## Expected Output

Formatted list of files, e.g., "Volume in drive C... Directory of C:\project\ ... 10/01/2023  12:00 PM    <DIR>          . ... No HACKED.txt initially; present post-exploit."

## Related

- [[commands/type-view-file]]
- [[procedures/Verify-Initial-Directory-State]]
