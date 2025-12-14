---
data: dir
tags:
  - recon
  - directory-listing
type: command
output: Directory listing output
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.313Z'
id: ac44ea93-07b3-48dc-84de-226e7d9b4cd3
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

Lists the contents of the current directory on a Windows server, used here to demonstrate RCE via an uploaded ASP shell by verifying file presence and server environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; lists current directory | No |

## Examples

### Basic Usage

```cmd
dir
```

### Advanced Usage

```cmd
dir /s
```

## Expected Output

Directory listing including file names, sizes, and dates, e.g., ' Volume in drive C is ... Directory of C:\savefiles ... poc.asp ...'

## Related

- [[commands/windows-cmd-c]]
- [[procedures/Execute-Commands-via-Uploaded-ASPShell]]
