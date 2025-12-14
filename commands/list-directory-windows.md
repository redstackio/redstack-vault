---
id: cmd-002
data: dir
tags:
  - windows
  - directory-listing
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.572Z'
verified: false
validated: true
submitted: true
---
# list-directory-windows

## Command

```bash
dir
```

## Description

Lists files and directories in the current working directory on Windows, used to verify the presence or absence of the HACKED.txt file in the treekill RCE exploitation workflow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

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

Formatted list of files, e.g., "Volume in drive C... Directory of C:\path\n\n10/01/2023  12:00 PM    <DIR>          .
10/01/2023  12:00 PM    <DIR>          ..
..." Pre-exploit: no HACKED.txt; post: includes "HACKED.txt".

## Related

- [[Related Procedure|procedures/Check-Directory-for-HACKED-File]]
