---
data: dir
tags:
  - recon
  - file-system
type: command
output: Directory listing of files and folders
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.442Z'
id: 9f619b28-5f59-4c37-99f7-dedf2510e4bd
verified: false
validated: true
submitted: true
---
# windows-dir

## Command

```cmd
dir
```

## Description

The 'dir' command lists the contents of the current directory on Windows, including files, folders, sizes, and dates. Used here via the ASP shell to demonstrate RCE by showing server file structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Lists current directory | No |

## Examples

### Basic Usage

```cmd
dir
```

### With Path

```cmd
dir C:\Windows
```

## Expected Output

Directory listing including volume info, file names, sizes, and last modified dates, e.g., ' Volume in drive C is OS ... Directory of C:\\savefiles ... poc.asp ...'

## Related

- [[commands/windows-cmd-c]]
